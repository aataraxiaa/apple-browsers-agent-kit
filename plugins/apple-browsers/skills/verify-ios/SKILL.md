---
name: verify-ios
description: Verify DuckDuckGo apple-browsers iOS user flows through MobileBuildMCP on an assigned test simulator. Resolves a matching app with sibling build-ios. Use as AStack's iOS verification driver; excludes macOS and Android.
---

# Verify Apple browsers iOS

Read [the provider policy](../../policy.md), [feature index](features/README.md), and the selected checkout's `AGENTS.md` and `.maestro/AGENTS.md`. Choose the changed behavior and adjacent regressions. Read only their guides and current source references. Maestro YAML supplies scenario and setup information; never execute Maestro or its wrappers.

Before preparation, follow [simulator ownership and lifecycle](../../resources.md) to lease a matching device. Use its UUID throughout. The lease helper prefers booted devices, then shutdown devices; create an `agent-` device only when none can be leased.

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

Simulator panel attach, detach, viewing, and panel screenshots are allowed. Capture app evidence through MobileBuildMCP `screenshot`. Only a user-authorized clipboard operation may use `simctl pbcopy` or `pbpaste`, always with the exact UUID. The only other exception is the bundled lifecycle helper for create, shutdown, and delete.

## Evidence and finish

Save a concise run record outside the app checkout under `review-artifacts`: build receipt, assigned UUID, exact launch arguments, scenario names, expected and observed results, relevant snapshots, and screenshots. Use `screenshot` with `returnFormat:"path"` and preserve the returned file externally. Mark each scenario PASS, FAIL, BLOCKED, or NOT RUN; one passing path does not cover its whole feature family.

Stop only the app this run launched, using `stop_app_sim` with explicit UUID and bundle ID. For a simulator this run created, use the lifecycle helper to shut it down. Release the ownership token in all exit paths. Run creator-only seven-day collection with a fresh inventory. Leave reused simulators intact and remove only this run’s scratch state. Confirm evidence exists and the app checkout has no changes caused by verification. Report results, evidence path, remaining state, and blockers. Maintain the feature map in this editable external plugin source.
