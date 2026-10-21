# Apple browsers agent kit

Companion plugin for DuckDuckGo apple-browsers iOS. The plugin supplies separate [build-ios](plugins/apple-browsers/skills/build-ios/SKILL.md) and [verify-ios](plugins/apple-browsers/skills/verify-ios/SKILL.md) skills and bundles MobileBuildMCP. Verification uses the build skill to find a matching completed build or produce one. Source stays outside the app repository; native runtimes own installed caches.

## Acceptance status

This is a prerelease verification driver. Packaging, skill validation, source inventory, hook behavior tests, and native installation directly from the GitHub repository passed in both Codex and Claude Code. All 38 installed plugin files matched the source byte for byte, with no symlinks. The map covers 141 scenarios and 58 helpers/configuration files across 28 guides. None of those scenarios has been accepted through MobileBuildMCP yet: the authoring session cannot connect to macOS CoreSimulator. A successful live build, one mapped scenario, and cleanup are still required by AStack's create-verification-skill workflow. Do not interpret mapping completeness or tool discovery as app verification.

## Install from GitHub

The repository is public. GitHub authentication is not required to download it.

Codex:

```sh
codex plugin marketplace add https://github.com/aataraxiaa/apple-browsers-agent-kit.git
codex plugin add apple-browsers@apple-browsers-tools
```

Claude Code:

```sh
claude plugin marketplace add https://github.com/aataraxiaa/apple-browsers-agent-kit.git --scope user
claude plugin install apple-browsers@apple-browsers-tools --scope user
```

If you installed the earlier local development package, uninstall `apple-browsers@apple-browsers-local` and remove the `apple-browsers-local` marketplace using your runtime's native plugin commands before installing this package. This avoids duplicate skills, hooks, and MCP servers. No links or manual cache copies are needed.

For local development, substitute the repository's absolute path for the GitHub URL. Choose one source per marketplace.

Restart the runtime. Confirm registration with `codex plugin list` or `claude plugin list`. In Codex, review and trust the plugin hooks once through `/hooks`. Do not edit trust configuration automatically. Node.js and npx must be on PATH. The plugin's [.mcp.json](plugins/apple-browsers/.mcp.json) is the single package pin and server declaration; do not add a duplicate global server.

## Routing and limits

PreToolUse applies [the provider policy](plugins/apple-browsers/policy.md) to build and simulator actions inside Apple browsers checkouts. Read-only helpers receive no startup policy injection. Known alternate build and simulator tools and common direct xcodebuild or Maestro commands are denied. The Claude simulator viewing panel remains available. The only direct simctl exceptions are `pbcopy` and `pbpaste` with an explicit simulator UUID. Explicit macOS builds and source reads remain available.

The hook is a routing guard, not a security boundary. It parses common shell executable positions with shlex, including absolute executable paths and command separators. It does not interpret arbitrary scripts, shell functions, aliases, interpreter bodies, nested tool orchestration, write_stdin, or every possible alternate MCP name. Unknown syntax is not proof of compliance. Hooks must be enabled and trusted; skill instructions remain the policy for paths outside guard coverage.

The bundled server enables all 14 stable workflows in the pinned package: coverage, debugging, device, doctor, macos, project-discovery, project-scaffolding, session-management, simulator, simulator-management, swift-package, ui-automation, utilities, and xcode-ide. Debug mode is enabled because the doctor workflow requires it. Experimental workflow-discovery remains disabled. The build-ios and verify-ios skills remain scoped to Apple browsers iOS; broader server capabilities do not authorize unrelated device or project changes.

A real MCP initialize and tools/list with this configuration returned 80 tools. The conditional sync_xcode_defaults tool appears only when running inside Xcode with auto-sync disabled. The experimental manage_workflows tool remains absent by choice. Xcode IDE bridge tools are exposed outside Xcode agent mode, but successful bridge calls require an accessible Xcode MCP bridge and its permissions. Listing a tool does not establish simulator, device, debugger, or Xcode availability on the host.

The server exposes explicit target arguments with `MOBILEBUILDMCP_DISABLE_SESSION_DEFAULTS=true`. Each simulator call must include its assigned `simulatorId`; shared default and profile mutations are prohibited. Assign a different simulator to each driver and a different `derivedDataPath` to each concurrent builder. Debugger calls require an explicit `debugSessionId`. Xcode auto-sync stays disabled. Restart the server after updating so its tool schemas refresh.

The build skill reuses a completed app only when its source and build receipt match, including local edits. Verification installs that app on its assigned simulator. Compile-only builds do not authorize simulator interaction.

## Update and validate

Edit this source, increment both manifests and the marketplace entry together, and validate before refreshing installation:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
claude plugin validate .
claude plugin validate plugins/apple-browsers
codex plugin marketplace upgrade apple-browsers-tools
codex plugin add apple-browsers@apple-browsers-tools
claude plugin marketplace update apple-browsers-tools
claude plugin update apple-browsers@apple-browsers-tools --scope user
```

Do not edit native caches. Find editable source with the native marketplace list commands. Restart after updates and verify the returned installed version.

Packaging and hook tests do not prove native execution. For native acceptance, open an explicit Apple browsers checkout, confirm both skill names and the mobilebuild tool inventory, confirm simulatorId is exposed in the tool schemas, resolve a matching build or build the iOS Browser scheme, and drive one mapped scenario on a designated disposable simulator. Confirm a direct build-tool request is denied in both runtimes without executing it; a source read and a MobileBuildMCP call must remain permitted. Save source identity, tool results, snapshots, screenshots, and app-stop result outside Git. Record hook trust and provider failures separately from UI results. The driver remains runtime-unaccepted until those checks pass.

## Verification coverage and AStack

The verification entry point is `plugins/apple-browsers/skills/verify-ios/SKILL.md`. Its 28 feature guides and complete YAML inventory live in the adjacent `features/` directory. These are the companion skills built for this setup and adapted to MobileBuildMCP, using existing app test flows as behavior references. They are not a claim that those flows have been executed through the new provider.

The companion works independently through its skills and routing hooks. Automatic external-driver discovery in AStack requires its external-verification support, implemented in the local AStack 0.1.5 source. Its release and installed availability have not been verified; check that the installed poteto-mode skill links to verification-drivers.md. That AStack change is separate from this package; installing this companion does not upgrade AStack. With an older AStack, explicitly invoke `apple-browsers:verify-ios` and `apple-browsers:build-ios`.
