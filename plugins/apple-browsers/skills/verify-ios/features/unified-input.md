# Search and Duck.ai input modes

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `test_enter_chat_from_web` — `.maestro/unified_toggle_input/test_enter_chat_from_web.yaml`.
- `test_search_only_website_active_ai_shortcut_prompt` — `.maestro/unified_toggle_input/test_search_only_website_active_ai_shortcut_prompt.yaml`.
- `test_unified_input_search` — `.maestro/unified_toggle_input/test_unified_input_search.yaml`.
- `test_unified_input_send_prompt` — `.maestro/unified_toggle_input/test_unified_input_send_prompt.yaml`.
- `test_unified_input_toolbar_buttons` — `.maestro/unified_toggle_input/test_unified_input_toolbar_buttons.yaml`.
- `test_unified_toggle_input` — `.maestro/unified_toggle_input/test_unified_toggle_input.yaml`.
- `test_uti_multiline_contextual` — `.maestro/unified_toggle_input/test_uti_multiline_contextual.yaml`.
- `test_uti_multiline_duck_ai_mode` — `.maestro/unified_toggle_input/test_uti_multiline_duck_ai_mode.yaml`.
- `test_uti_multiline_duck_ai_tab` — `.maestro/unified_toggle_input/test_uti_multiline_duck_ai_tab.yaml`.
- `test_uti_single_line_no_toggle` — `.maestro/unified_toggle_input/test_uti_single_line_no_toggle.yaml`.
- `test_uti_single_line_search_mode` — `.maestro/unified_toggle_input/test_uti_single_line_search_mode.yaml`.

## How to get to it (user POV)

Browsing Menu → Settings → AI Features. Scroll `Settings.AIFeatures.Picker.SearchAndDuckAI` fully inside the sheet, select it, return via Settings → Done; focus `searchEntry`. Select `AddressBar.Button.Search` or `AddressBar.Button.DuckAI`. Search Only is the alternative picker `Settings.AIFeatures.Picker.SearchOnly`.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### test_enter_chat_from_web

Source: `.maestro/unified_toggle_input/test_enter_chat_from_web.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Tap label/text `"Browsing Menu"`.
8. Require visible label/text `"Duck.ai"`.
9. Tap label/text `"Duck.ai"`.
10. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
11. Require visible label/text `"Close tab"`.
12. Require visible label/text `"Free Plan"`.
13. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_search_only_website_active_ai_shortcut_prompt

Source: `.maestro/unified_toggle_input/test_search_only_website_active_ai_shortcut_prompt.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_only.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true", "ff.contextualDuckAIMode": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_only.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require absent identifier `"AddressBar.Button.Search"`.
6. Require absent identifier `"AddressBar.Button.DuckAI"`.
7. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
8. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
9. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
10. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
11. Require visible label/text `"Close tab"`.
12. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
13. Tap label/text `"Close tab"`.
14. Require visible identifier `"searchEntry"`.
15. Tap identifier `"searchEntry"`.
16. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
17. Use the exposed provider key action for `"Enter"`; inspect its schema first.
18. Require visible label/text `".*Privacy Test Pages.*"`.
19. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
20. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
21. Require absent identifier `"AIChat.ContextualSheet"`.
22. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
23. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
24. Tap identifier `"searchEntry"`.
25. Require absent identifier `"AddressBar.Button.Search"`.
26. Require absent identifier `"AddressBar.Button.DuckAI"`.
27. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
28. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
29. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
30. Require visible label/text `"Close tab"`.
31. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
32. Require absent identifier `"AIChat.ContextualSheet"`.
33. Require absent label/text `".*privacy-test-pages.*"`.
34. Tap label/text `"Close tab"`.
35. Require visible label/text `".*Privacy Test Pages.*"`.
36. Tap identifier `"searchEntry"`.
37. Source timing/gesture shorthand `"eraseText"`; inspect destination state and supported provider tool.
38. Enter `"https://example.com"` into the currently focused field using its refreshed elementRef.
39. Require visible label/text `"https://example.com"`.
40. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
41. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
42. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
43. Require visible label/text `"Close tab"`.
44. Require absent identifier `"AIChat.ContextualSheet"`.
45. Require visible label/text `".*example.com.*"`.
46. Tap label/text `"Close tab"`.
47. Require visible label/text `".*Privacy Test Pages.*"`.
48. Tap identifier `"searchEntry"`.
49. Source timing/gesture shorthand `"eraseText"`; inspect destination state and supported provider tool.
50. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
51. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
52. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
53. Require visible label/text `"Close tab"`.
54. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
55. Require absent identifier `"AIChat.ContextualSheet"`.
56. Tap label/text `"Close tab"`.
57. Require visible label/text `".*Privacy Test Pages.*"`.
58. Tap identifier `"searchEntry"`.
59. Source timing/gesture shorthand `"eraseText"`; inspect destination state and supported provider tool.
60. Enter `"What is a duck?"` into the currently focused field using its refreshed elementRef.
61. Require visible label/text `"What is a duck?"`.
62. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
63. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
64. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
65. Require visible label/text `"Close tab"`.
66. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
67. Require absent identifier `"AIChat.ContextualSheet"`.
68. Require visible label/text `"What is a duck?"`.

### test_unified_input_search

Source: `.maestro/unified_toggle_input/test_unified_input_search.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.DuckAI"`.
6. Tap identifier `"AddressBar.Button.Search"`.
7. Require absent identifier `"AIChat.Toolbar.Button.ModelChip"`.
8. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
9. Use the exposed provider key action for `"Enter"`; inspect its schema first.
10. Require visible label/text `".*Privacy Test Pages.*"`.
11. Require absent identifier `"AddressBar.Button.DuckAI"`.
12. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.

### test_unified_input_send_prompt

Source: `.maestro/unified_toggle_input/test_unified_input_send_prompt.yaml`. Tags: `["iphone", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.DuckAI"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
8. Enter `"What is a duck?"` into the currently focused field using its refreshed elementRef.
9. Require visible label/text `"What is a duck?"`.
10. Tap label/text `"Submit"`.
11. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
12. Require visible label/text `"Close tab"`.
13. Require visible label/text `"What is a duck?"`.

### test_unified_input_toolbar_buttons

Source: `.maestro/unified_toggle_input/test_unified_input_toolbar_buttons.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.DuckAI"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
8. Require visible identifier `"AIChat.Toolbar.Button.Reasoning"`.
9. Require visible label/text `"Tools"`.
10. Require visible label/text `"Attach"`.

### test_unified_toggle_input

Source: `.maestro/unified_toggle_input/test_unified_toggle_input.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.DuckAI"`.
6. Require visible identifier `"AddressBar.Button.Search"`.
7. Tap identifier `"AddressBar.Button.DuckAI"`.
8. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
9. Tap identifier `"AddressBar.Button.Search"`.
10. Require absent identifier `"AIChat.Toolbar.Button.ModelChip"`.
11. Enter `"What is a tokamak?"` into the currently focused field using its refreshed elementRef.
12. Require visible label/text `"What is a tokamak?"`.
13. Tap identifier `"AddressBar.Button.DuckAI"`.
14. Require visible label/text `"What is a tokamak?"`.
15. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_uti_multiline_contextual

Source: `.maestro/unified_toggle_input/test_uti_multiline_contextual.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Tap label/text `"Browsing Menu"`.
8. Tap label/text `"Duck.ai"`.
9. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
10. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
11. Require absent identifier `"AddressBar.Button.Search"`.
12. Require absent identifier `"AddressBar.Button.DuckAI"`.
13. Tap identifier `"searchEntry"`.
14. Enter `"https://en.wikipedia.org/wiki/Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"` into the currently focused field using its refreshed elementRef.
15. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_uti_multiline_duck_ai_mode

Source: `.maestro/unified_toggle_input/test_uti_multiline_duck_ai_mode.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.DuckAI"`.
6. Tap identifier `"AddressBar.Button.DuckAI"`.
7. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
8. Enter `"https://en.wikipedia.org/wiki/Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"` into the currently focused field using its refreshed elementRef.
9. Require visible identifier `"searchEntry"`.
10. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
11. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.

### test_uti_multiline_duck_ai_tab

Source: `.maestro/unified_toggle_input/test_uti_multiline_duck_ai_tab.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://en.wikipedia.org/wiki/Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"` into the currently focused field using its refreshed elementRef.
5. Require absent identifier `"AddressBar.Button.Search"`.
6. Require absent identifier `"AddressBar.Button.DuckAI"`.
7. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_uti_single_line_no_toggle

Source: `.maestro/unified_toggle_input/test_uti_single_line_no_toggle.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_only.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_only.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require absent identifier `"AddressBar.Button.Search"`.
6. Require absent identifier `"AddressBar.Button.DuckAI"`.
7. Enter `"https://en.wikipedia.org/wiki/Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"` into the currently focused field using its refreshed elementRef.
8. Require visible identifier `"searchEntry"`.
9. Require absent identifier `"AIChat.Toolbar.Button.ModelChip"`.
10. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.

### test_uti_single_line_search_mode

Source: `.maestro/unified_toggle_input/test_uti_single_line_search_mode.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/set_search_and_duckai.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Follow visible behavior from `.maestro/shared/set_search_and_duckai.yaml`.
4. Tap identifier `"searchEntry"`.
5. Require visible identifier `"AddressBar.Button.Search"`.
6. Require visible identifier `"AddressBar.Button.DuckAI"`.
7. Tap identifier `"AddressBar.Button.Search"`.
8. Enter `"https://en.wikipedia.org/wiki/Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"` into the currently focused field using its refreshed elementRef.
9. Require absent identifier `"AIChat.Toolbar.Button.ModelChip"`.
10. Require visible identifier `"searchEntry"`.
11. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.

## Gotchas

Set the search/AI preference through Settings; the flow warns direct launch injection crashes. ModelChip presence establishes AI mode, not composer geometry. Long-text flows only assert field/chip presence; capture layout to prove actual multiline expansion. Inspect current dismissal affordance: Back chevron for unified input versus Cancel/Dismiss for classic.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
