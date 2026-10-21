# Duck.ai usage warnings

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `test_uti_duckai_warnings_approaching` — `.maestro/unified_toggle_input/test_uti_duckai_warnings_approaching.yaml`.
- `test_uti_duckai_warnings_disabled` — `.maestro/unified_toggle_input/test_uti_duckai_warnings_disabled.yaml`.
- `test_uti_duckai_warnings_limit_reached` — `.maestro/unified_toggle_input/test_uti_duckai_warnings_limit_reached.yaml`.

## How to get to it (user POV)

Use the internal Debug menu to seed the exact preset in the dependency recipe, then focus NTP input and select Duck.ai. Return to Search to exercise warning suppression.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### test_uti_duckai_warnings_approaching

Source: `.maestro/unified_toggle_input/test_uti_duckai_warnings_approaching.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`, `.maestro/shared/seed_duckai_usage_warning.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "true", "ff.utiDuckAIWarnings": "true", "ff.aiChatNativeStorage": "true", "ff.duckAINativeTermsOfService": "false", "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Follow visible behavior from `.maestro/shared/seed_duckai_usage_warning.yaml` with parameters `{"PRESET": "Approaching weekly limit (90%)"}`.
5. Tap identifier `"searchEntry"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
8. Require visible identifier `"AIChat.Footer.Card.usageWarning"`.
9. Require visible identifier `"AIChat.Footer.Label.Title"`, text `"90% of weekly limit"`.
10. Require visible identifier `"AIChat.Footer.Label.Subtitle"`.
11. Require visible identifier `"AIChat.Footer.Icon.UsageRing"`.
12. Require absent identifier `"AIChat.Footer.Icon.Alert"`.
13. Require visible identifier `"AIChat.Footer.Button.Dismiss"`.
14. Tap identifier `"AddressBar.Button.Search"`.
15. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
16. Require absent identifier `"AIChat.Footer.Card.usageWarning"`.
17. Tap identifier `"AddressBar.Button.DuckAI"`.
18. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
19. Require visible identifier `"AIChat.Footer.Card.usageWarning"`.
20. Tap identifier `"AIChat.Footer.Button.Dismiss"`.
21. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
22. Require absent identifier `"AIChat.Footer.Card.usageWarning"`.
23. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
24. Tap identifier `"searchEntry"`.
25. Tap identifier `"AddressBar.Button.DuckAI"`.
26. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
27. Require absent identifier `"AIChat.Footer.Card.usageWarning"`.

### test_uti_duckai_warnings_disabled

Source: `.maestro/unified_toggle_input/test_uti_duckai_warnings_disabled.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`, `.maestro/shared/seed_duckai_usage_warning.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "true", "ff.utiDuckAIWarnings": "false", "ff.aiChatNativeStorage": "true", "ff.duckAINativeTermsOfService": "false", "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Follow visible behavior from `.maestro/shared/seed_duckai_usage_warning.yaml` with parameters `{"PRESET": "Weekly limit reached"}`.
5. Tap identifier `"searchEntry"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
8. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
9. Require absent identifier `"AIChat.Footer.Card.outOfUsage"`.

### test_uti_duckai_warnings_limit_reached

Source: `.maestro/unified_toggle_input/test_uti_duckai_warnings_limit_reached.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`, `.maestro/shared/seed_duckai_usage_warning.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "true", "ff.utiDuckAIWarnings": "true", "ff.aiChatNativeStorage": "true", "ff.duckAINativeTermsOfService": "false", "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Follow visible behavior from `.maestro/shared/seed_duckai_usage_warning.yaml` with parameters `{"PRESET": "Weekly limit reached"}`.
5. Tap identifier `"searchEntry"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
8. Require visible identifier `"AIChat.Footer.Card.outOfUsage"`.
9. Require visible identifier `"AIChat.Footer.Label.Title"`, text `"Weekly usage limit reached"`.
10. Require visible identifier `"AIChat.Footer.Icon.Alert"`.
11. Require absent identifier `"AIChat.Footer.Icon.UsageRing"`.
12. Require absent identifier `"AIChat.Footer.Button.Dismiss"`.
13. Require absent identifier `"AIChat.Footer.Button.Primary"`.
14. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
15. Follow visible behavior from `.maestro/shared/seed_duckai_usage_warning.yaml` with parameters `{"PRESET": "Daily limit reached"}`.
16. Tap identifier `"searchEntry"`.
17. Tap identifier `"AddressBar.Button.DuckAI"`.
18. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
19. Require visible identifier `"AIChat.Footer.Card.outOfUsage"`.
20. Require visible identifier `"AIChat.Footer.Label.Title"`, text `"Daily limit reached"`.
21. Require visible identifier `"AIChat.Footer.Icon.Alert"`.
22. Require absent identifier `"AIChat.Footer.Button.Dismiss"`.
23. Require visible identifier `"AIChat.Footer.Button.Primary"`.

## Gotchas

Requires isInternalUser true and aiChatNativeStorage true; pin utiDuckAIWarnings true/false and duckAINativeTermsOfService false so consent does not occupy the footer. Seeds are local debug state, not real account quota proof. Weekly blocked has no primary CTA; free daily blocked may show Try Subscription for Free or Subscribe, so assert the stable CTA identifier without purchasing.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
