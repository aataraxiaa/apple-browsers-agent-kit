# iPad Duck.ai input controls

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `ipad_duckai_bar_controls` — `.maestro/ipad_duckai/ipad_duckai_bar_controls.yaml`.

## How to get to it (user POV)

On a designated iPad, Browsing Menu → Settings → AI Features. Center the Search & Duck.ai picker inside the form sheet before tapping. Settings → Done, focus searchEntry and select Browser.OmniBar.Button.ModeToggle.AIChat.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### ipad_duckai_bar_controls

Source: `.maestro/ipad_duckai/ipad_duckai_bar_controls.yaml`. Tags: `["ipad", "ipad_duckai"]`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Tap identifier `"Browser.OmniBar.Button.BrowsingMenu"`.
3. Tap label/text `"Settings"`.
4. Scroll toward `"DOWN"` until text `"AI Features"` is fully visible. Refresh the snapshot.
5. Tap label/text `"AI Features"`.
6. Scroll toward `"DOWN"` until identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"` is fully visible; center it before tapping. Refresh the snapshot.
7. Tap identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
8. Tap label/text `"Settings"`.
9. Tap label/text `"Done"`.
10. Tap identifier `"searchEntry"`.
11. Require visible identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
12. Require visible identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.
13. Require absent identifier `"AIChat.Omnibar.iPad.ModelPicker"`.
14. Require absent identifier `"AIChat.Omnibar.iPad.ReasoningPicker"`.
15. Require absent identifier `"AIChat.Omnibar.iPad.ToolPicker"`.
16. Require absent identifier `"AIChat.Omnibar.iPad.Attach"`.
17. Tap identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.
18. Wait until visible identifier `"AIChat.Omnibar.iPad.ModelPicker"` (source deadline 20000 ms); retain resulting snapshot.
19. Require visible identifier `"AIChat.Omnibar.iPad.ReasoningPicker"`.
20. Require visible identifier `"AIChat.Omnibar.iPad.ToolPicker"`.
21. Require visible identifier `"AIChat.Omnibar.iPad.Attach"`.

## Gotchas

The iPad toggle identifiers differ from iPhone. Four controls are hidden in Search mode; model list arrives from Duck.ai network with no bundled default. Reasoning, Tools and Attach additionally depend on default-model capabilities. No chat submission is needed for this scenario.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
