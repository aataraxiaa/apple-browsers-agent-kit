#!/usr/bin/env python3
import json
from pathlib import Path
import re
import shlex
import sys
import importlib.util
import subprocess

spec = importlib.util.spec_from_file_location("apple_resources", Path(__file__).resolve().parents[1] / "scripts/resources.py")
resources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resources)

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = {"mobilebuild", "MobileBuildMCP", "mobilebuildmcp", "XcodeBuildMCP", "xcodebuildmcp",
             "plugin_apple-browsers_mobilebuild", "plugin_apple-browsers_XcodeBuildMCP"}
SIMULATOR_TOOLS = {
    "debug_attach_sim", "boot_sim", "erase_sims", "set_sim_location", "reset_sim_location",
    "set_sim_appearance", "sim_statusbar", "toggle_software_keyboard",
    "toggle_connect_hardware_keyboard", "build_sim", "build_run_sim", "test_sim",
    "get_sim_app_path", "install_app_sim", "launch_app_sim", "stop_app_sim",
    "record_sim_video", "screenshot", "snapshot_ui", "wait_for_ui", "batch",
    "tap", "touch", "long_press", "swipe", "drag", "gesture", "button",
    "key_press", "key_sequence", "type_text",
}
DEBUG_SESSION_TOOLS = {
    "debug_breakpoint_add", "debug_breakpoint_remove", "debug_continue", "debug_detach",
    "debug_lldb_command", "debug_stack", "debug_variables",
}
DEFAULTS_MUTATIONS = {
    "session_set_defaults", "session_clear_defaults", "session_use_defaults_profile",
    "sync_xcode_defaults",
}
ALTERNATE_TOOLS = {
    "xcode": {"BuildProject", "RunAllTests", "RunSomeTests", "RenderPreview", "ExecuteSnippet"},
    "maestro": {"launch_app", "stop_app", "tap_on", "input_text", "erase_text",
                "swipe", "press_key", "take_screenshot", "run_flow", "run_flow_files"},
    "ios_simulator": {"launch_app", "install_app", "tap", "swipe", "type_text",
                      "screenshot", "ui_tap", "ui_swipe", "ui_type_text"},
}
SEPARATORS = {";", "&&", "||", "|", "(", ")", "&", "\n"}
UUID = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\Z")


def simulator_id(value):
    return isinstance(value, str) and UUID.fullmatch(value) is not None


def deny(reason):
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
            "permissionDecision": "deny", "permissionDecisionReason": reason}}


def checkout(path):
    if not path:
        return False
    for parent in (Path(path).resolve(), *Path(path).resolve().parents):
        if (parent / "DuckDuckGo.xcworkspace").is_dir() and (parent / "iOS/DuckDuckGo-iOS.xcodeproj").is_dir():
            return True
    return False


def shell_tokens(command):
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|()\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    return list(lexer)


def macos_build(arguments):
    for index, token in enumerate(arguments[:-1]):
        if token == "-scheme" and arguments[index + 1].startswith("macOS "):
            return not any("iphonesimulator" in arg.lower() or "ios simulator" in arg.lower() for arg in arguments)
    return False


def clipboard(arguments):
    return (len(arguments) >= 2 and arguments[0] in {"pbcopy", "pbpaste"}
            and simulator_id(arguments[1])
            and (len(arguments) == 2 or arguments[2].startswith(("<", ">"))))


def bypass(command):
    try:
        tokens = shell_tokens(command)
    except ValueError:
        return False
    start = True
    executable = None
    for index, token in enumerate(tokens):
        if token in SEPARATORS or token and set(token) <= {"\n", ";", "&", "|", "(", ")"}:
            start = True
            executable = None
            continue
        end = next((i for i in range(index + 1, len(tokens))
                    if tokens[i] in SEPARATORS), len(tokens))
        arguments = tokens[index + 1:end]
        if start:
            if "=" in token and not token.startswith("/"):
                continue
            name = Path(token).name
            if name in ("env", "command", "exec", "sudo"):
                continue
            executable = name
            start = False
            if name == "xcodebuild" and not macos_build(arguments):
                return True
            if name == "simctl" and not clipboard(arguments):
                return True
            if name in ("maestro", "setup_ui_tests.sh", "run_ui_tests.sh", "clean_simulators.sh"):
                return True
        elif executable == "xcrun":
            if token == "simctl" and not clipboard(arguments):
                return True
            if token == "xcodebuild" and not macos_build(arguments):
                return True
    return False


def handle(event):
    data = event.get("tool_input") or {}
    command = data.get("command", data.get("cmd", ""))
    paths = [event.get("cwd"), data.get("cwd"), data.get("workdir"), data.get("workspacePath"), data.get("projectPath")]
    try:
        tokens = shell_tokens(command)
        for index, token in enumerate(tokens[:-1]):
            if token in ("-workspace", "-project"):
                selected = Path(tokens[index + 1])
                base = data.get("workdir") or data.get("cwd") or event.get("cwd") or "."
                paths.append(str(selected if selected.is_absolute() else Path(base) / selected))
    except ValueError:
        pass
    if not any(checkout(path) for path in paths):
        return {}
    if event.get("hook_event_name") == "Stop":
        return {"systemMessage": "Apple browsers resource report: " + json.dumps(resources.report(Path(sys.argv[2]) if len(sys.argv) == 3 and sys.argv[1] == "--root" else resources.ROOT))}
    if event.get("hook_event_name") != "PreToolUse":
        return {}
    tool = event.get("tool_name", "")
    parts = tool.split("__")
    provider, operation = parts[1:] if len(parts) == 3 and parts[0] == "mcp" else (None, None)
    if provider in PROVIDERS:
        if operation in DEBUG_SESSION_TOOLS:
            session = data.get("debugSessionId")
            if not isinstance(session, str) or not session.strip():
                return deny("Pass your owned debugSessionId explicitly; the current debugger session is shared.")
        if operation in DEFAULTS_MUTATIONS:
            return deny("Pass explicit per-call parameters; do not mutate shared MobileBuildMCP defaults or profiles.")
        if operation in {"build_sim", "build_run_sim", "test_sim", "get_sim_app_path"}:
            if not simulator_id(data.get("simulatorId")):
                return deny("Pass your leased simulatorId explicitly.")
            explicit = data.get("workspacePath") or data.get("projectPath")
            base = Path(data.get("cwd") or data.get("workdir") or event.get("cwd") or ".")
            selected = (Path(explicit) if Path(explicit).is_absolute() else base / explicit) if explicit else next((Path(p).absolute() for p in paths if p and checkout(p)), None)
            selected = selected.absolute() if selected else None
            while selected and not (selected / "DuckDuckGo.xcworkspace").is_dir():
                selected = selected.parent
            try:
                cache = resources.canonical(selected)
                try:
                    completed = subprocess.run([sys.executable, str(ROOT / "scripts/resources.py"), "prepare", str(selected)],
                                               capture_output=True, text=True, timeout=2)
                    prepared = json.loads(completed.stdout) if completed.returncode == 0 else {"warning": completed.stderr.strip()}
                except (subprocess.TimeoutExpired, ValueError):
                    prepared = {"warning": "Resource preparation exceeded hook budget; run prepare explicitly and report free space."}
            except ValueError as error:
                return deny("Cannot establish canonical derived data ownership: " + str(error))
            return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "updatedInput":
                    dict(data, derivedDataPath=str(cache)), "additionalContext":
                    (ROOT / "policy.md").read_text() + "\nResource preparation: " + json.dumps(prepared)}}
        if operation in SIMULATOR_TOOLS:
            if not simulator_id(data.get("simulatorId")):
                return deny("Pass the agent's explicit simulator UUID as simulatorId on every simulator build or drive call.")
            return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                    "additionalContext": (ROOT / "policy.md").read_text()}}
    alternate = operation in ALTERNATE_TOOLS.get(provider, set())
    shell = tool in ("Bash", "exec_command", "functions.exec_command")
    if alternate or (shell and bypass(command)):
        return deny("Apple browsers iOS requires MobileBuildMCP. Use build-ios or verify-ios; report unsupported operations without a fallback.")
    return {}


if __name__ == "__main__":
    print(json.dumps(handle(json.load(sys.stdin))))
