# Device identity and UI-test override diagnostics

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `ipad` — `.maestro/device_info/ipad.yaml`.
- `iphone` — `.maestro/device_info/iphone.yaml`.
- `ui_test_overrides` — `.maestro/ui_test_overrides/ui_test_overrides.yaml`.

## How to get to it (user POV)

Device identity: enter https://useragentstring.com/ through searchEntry on the correct simulator idiom. Override diagnostics: Browsing Menu → Settings → Debug → UI Test Overrides.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### ipad

Source: `.maestro/device_info/ipad.yaml`. Tags: `["ipad", "device_info"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://useragentstring.com/"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"Macintosh"`.
7. Tap identifier `"searchEntry"`.
8. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
9. Enter `"remote iOS developer jobs"` into the currently focused field using its refreshed elementRef.
10. Use the exposed provider key action for `"Enter"`; inspect its schema first.
11. Require visible label/text `".*"`.

### iphone

Source: `.maestro/device_info/iphone.yaml`. Tags: `["iphone", "device_info"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://useragentstring.com/"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"iPhone"`.
7. Tap identifier `"searchEntry"`.
8. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
9. Enter `"remote iOS developer jobs"` into the currently focused field using its refreshed elementRef.
10. Use the exposed provider key action for `"Enter"`; inspect its schema first.
11. Require visible label/text `".*"`.

### ui_test_overrides

Source: `.maestro/ui_test_overrides/ui_test_overrides.yaml`. Tags: `["iphone"]`.

Dependencies: `.maestro/shared/open_debug_menu.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "ff.uiTestFeatureFlag": "true", "experiment.uiTestExperiment": "treatment"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/open_debug_menu.yaml`.
5. Scroll toward `"DOWN"` until text `"UI Test Overrides"` is fully visible. Refresh the snapshot.
6. Tap label/text `"UI Test Overrides"`.
7. Require visible identifier `"ui-test-override-ff-value"`, text `"ENABLED"`.
8. Require visible identifier `"ui-test-override-experiment-value"`, text `"treatment"`.

## Gotchas

The device_info wildcard final assertion proves only some element exists; require observed destination/query for a useful search proof. UI test overrides are a diagnostic surface, not shipped user settings; inspect launch-argument parser and pin values as strings. Config rollout overrides support enabling only.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
