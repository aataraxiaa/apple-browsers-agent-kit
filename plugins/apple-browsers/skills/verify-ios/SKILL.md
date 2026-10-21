---
name: verify-ios
description: Verify DuckDuckGo apple-browsers iOS user flows through MobileBuildMCP on an assigned test simulator. Resolves a matching app with sibling build-ios. Use as AStack's iOS verification driver; excludes macOS and Android.
---

# Verify Apple browsers iOS

Read [the provider policy](../../policy.md), [feature index](features/README.md), and the selected checkout's `AGENTS.md` and `.maestro/AGENTS.md`. Choose the changed behavior and adjacent regressions. Read only their guides and current source references. Maestro YAML supplies scenario and setup information; never execute Maestro or its wrappers.

## Prepare and launch

1. Invoke [build-ios](../build-ios/SKILL.md) to resolve a matching completed `.app`. Reuse its validated product and receipt; rebuild only when the resolver cannot establish a match.
2. Confirm the assigned test simulator's exact UUID and idiom with `list_sims`. Keep that UUID explicit as `simulatorId` on every targeted MobileBuildMCP call, including boot, install, launch, UI, screenshots, and stop. Never change session defaults or profiles. Concurrent agents must use different leased simulators; builders in one worktree run sequentially with its canonical derived-data directory.
3. Call `boot_sim` and `install_app_sim` with the resolved app path. Check `isError` and `structuredContent.didError` before proceeding. Translate the scenario's launch map into an ordered `launchArgs` string array using the current `iOS/Core/LaunchOptionsHandler.swift`.
4. For ordinary post-onboarding legacy browser coverage, the source baseline is `["-isOnboardingCompleted","true","-isRunningUITests","true","-ff.floatingUIAugust2026","false"]`. Onboarding and new-chrome flows need their own baseline. Add the feature's source-grounded flag, rollout, cohort, and internal-user settings. Preserve strings and resolve environment placeholders before launch.
5. Establish required clean state before launching. Installation does not clear app state or keychain. Use supported provider operations on an authorized disposable target when a reset is needed. `-clearAllDefaults` also removes tab and webview state; internal-user state may persist even after passing false. A contaminated baseline fails the scenario's preconditions.
6. Call `launch_app_sim` with the explicit UUID, bundle ID, and prepared `launchArgs`. Use `snapshot_ui` to confirm the expected initial screen. If setup fails, use the provider's `doctor` when available and report the concrete blocker.

## Drive and assert

Use MobileBuildMCP for all build, install, launch, interaction, and app screenshot operations. Resolve current identifiers or labels through `snapshot_ui`, then pass its `elementRef` to `tap` or `type_text`. Keep refs with their simulator UUID and refresh after navigation; never carry refs between simulators. Source regexes and coordinates are lookup hints.

Pair actions with observable assertions through `wait_for_ui` and snapshots. Use the exposed conditions such as `exists`, `gone`, `enabled`, `focused`, `textContains`, and `settled`, with bounded timeouts. `textContains` needs `text`; `type_text` needs `elementRef` and `text`. Check the current schema for gestures, keyboard, batches, or debugger operations. Pass explicit `debugSessionId` on debugger calls that target a session.

Exercise the actual user path. Setup flags may select a cohort, but internal setters or debugger mutations cannot prove the behavior under test. Check persistence or side effects through another user-visible observation when relevant. Use disposable data and the task's authorization for account, payment, sharing, and deletion scenarios.

Simulator panel attach, detach, viewing, and panel screenshots are allowed. Capture app evidence through MobileBuildMCP `screenshot`. Only a user-authorized clipboard operation may use `simctl pbcopy` or `pbpaste`, always with the exact UUID. Do not fall back to other simulator-control tools.

## Evidence and finish

Save a concise run record outside the app checkout under `review-artifacts`: build receipt, assigned UUID, exact launch arguments, scenario names, expected and observed results, relevant snapshots, and screenshots. Use `screenshot` with `returnFormat:"path"` and preserve the returned file externally. Mark each scenario PASS, FAIL, BLOCKED, or NOT RUN; one passing path does not cover its whole feature family.

Stop only the app this run launched, using `stop_app_sim` with explicit UUID and bundle ID. Leave the simulator intact and remove only this run's scratch state. Confirm evidence exists and the app checkout has no changes caused by verification. Report results, evidence path, remaining state, and blockers. Maintain the feature map in this editable external plugin source.


## Local resource lifecycle

Use the bundled `scripts/resources.py` (relative to the plugin root). Before every build run `python3 "$PLUGIN_ROOT/scripts/resources.py" prepare "$CHECKOUT"`. The build hook also prepares and sets the canonical `derivedDataPath` on supported build calls. Resolve and reuse app products only inside that canonical cache; retain HEAD, local-edit and build-input receipt validation. Basename ownership collisions and symlinks require correction before building. Never choose an alternate cache.

Preparation reclaims caches only below 60 GiB free, protecting the current cache and live xcodebuild paths. It tries orphan caches first, then merged or positively remote-deleted branches, then least recently used caches. Errors and insufficient free space are reported and do not deny builds. Worktrees are never removed automatically.

Normalize provider simulator inventory to JSON objects with `uuid`, `os`, `idiom` and `state`. Acquire with `python3 "$PLUGIN_ROOT/scripts/resources.py" lease --inventory inventory.json --session "$SESSION_ID" --pid "$SESSION_PID" --os 18 --idiom phone` and save the returned token externally. Reuse the caller's stable session and PID identity. Prefer matching booted devices, then shutdown devices. Pass the returned UUID explicitly on every targeted MCP call. Release with `python3 "$PLUGIN_ROOT/scripts/resources.py" release --token token.json`. Never remove someone else's lease. Existing user simulators are never deleted. The authorized internal lifecycle helper permits only create/shutdown/delete. If no matching device is available, use `create --token identity.json --name NAME --device-type TYPE --runtime RUNTIME` with a stable session/PID identity JSON, save the returned lease token and refresh provider inventory. Before releasing a device created by this run, use `shutdown --token token.json`. Use `delete-stale --inventory inventory.json` to delete only proven plugin-created, shutdown devices unused for seven days with no lease and matching UUID/name provenance. Existing devices are never shut down or deleted. Never mutate provider defaults.

For explicit cleanup use `python3 "$PLUGIN_ROOT/scripts/resources.py" cleanup "$CHECKOUT"`. It refuses main checkout, dirty/untracked/ignored files, unpushed branches and live builds; removes the Git worktree without force, its cache and a proven merged/pushed local branch, then prunes. The bounded Stop hook reports local resource metadata and cached size estimates without network or recursive scans; it makes no continuation or permission decision. `python3 "$PLUGIN_ROOT/scripts/resources.py" report` prints that report explicitly.
