# Duck.ai chat tabs

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `ai-chat-ipad` — `.maestro/release_tests/ai-chat-ipad.yaml`.
- `ai-chat-iphone-ipad-flag` — `.maestro/release_tests/ai-chat-iphone-ipad-flag.yaml`.
- `ai-chat` — `.maestro/release_tests/ai-chat.yaml`.
- `test_ai_chat_tab_header` — `.maestro/unified_toggle_input/test_ai_chat_tab_header.yaml`.
- `test_chat_tab_model_picker` — `.maestro/unified_toggle_input/test_chat_tab_model_picker.yaml`.
- `test_chat_tab_new_button` — `.maestro/unified_toggle_input/test_chat_tab_new_button.yaml`.
- `test_chat_tab_new_chat` — `.maestro/unified_toggle_input/test_chat_tab_new_chat.yaml`.
- `test_chat_tab_send_prompt` — `.maestro/unified_toggle_input/test_chat_tab_send_prompt.yaml`.
- `test_chat_tab_stop_generating` — `.maestro/unified_toggle_input/test_chat_tab_stop_generating.yaml`.
- `test_chat_tab_toolbar_buttons` — `.maestro/unified_toggle_input/test_chat_tab_toolbar_buttons.yaml`.

## How to get to it (user POV)

Open the NTP omnibar Duck.ai button (`Browser.OmniBar.Button.AIChat`); choose `New Chat` if the menu appears, and dismiss consent or promo cards only when actually present. A chat tab has `Close tab`; recent chat history is reached by `Recent chats`.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### ai-chat-ipad

Source: `.maestro/release_tests/ai-chat-ipad.yaml`. Tags: `["ipad", "release"]`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}", "ff.iPadAIToggle": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Tap identifier `"Browser.OmniBar.Button.BrowsingMenu"`.
3. Tap label/text `"Settings"`.
4. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
5. Tap label/text `"AI Features"`.
6. Require visible label/text `"Duck.ai"`.
7. Require visible identifier `"Settings.AIFeatures.Picker.SearchOnly"`.
8. Require visible identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
9. Scroll toward `"DOWN"` until label/text `"Manage Duck.ai Shortcuts"` is fully visible. Refresh the snapshot.
10. Tap label/text `"Manage Duck.ai Shortcuts"`.
11. Require visible label/text `"Address Bar"`.
12. Tap label/text `"AI Features"`.
13. Tap identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
14. Tap label/text `"Settings"`.
15. Tap label/text `"Done"`.
16. Tap identifier `"searchEntry"`.
17. Require visible identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
18. Require visible identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.
19. Tap identifier `"Browser.OmniBar.Button.BrowsingMenu"`.
20. Tap label/text `"Settings"`.
21. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
22. Tap label/text `"AI Features"`.
23. Tap identifier `"Settings.AIFeatures.Picker.SearchOnly"`.
24. Tap label/text `"Settings"`.
25. Tap label/text `"Done"`.
26. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
27. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.

### ai-chat-iphone-ipad-flag

Source: `.maestro/release_tests/ai-chat-iphone-ipad-flag.yaml`. Tags: `["iphone", "release"]`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}", "ff.iPadAIToggle": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Require visible identifier `"searchEntry"`.
3. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
4. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
5. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.
6. Tap label/text `"Browsing Menu"`.
7. Tap label/text `"Settings"`.
8. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
9. Tap label/text `"AI Features"`.
10. Require visible label/text `"Duck.ai"`.
11. Require visible identifier `"Settings.AIFeatures.Picker.SearchOnly"`.
12. Require visible identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
13. Scroll toward `"DOWN"` until label/text `"Manage Duck.ai Shortcuts"` is fully visible. Refresh the snapshot.
14. Tap label/text `"Manage Duck.ai Shortcuts"`.
15. Require visible label/text `"Address Bar"`.
16. Tap label/text `"AI Features"`.
17. Tap identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
18. Tap label/text `"Settings"`.
19. Tap label/text `"Done"`.
20. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
21. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
22. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.
23. Tap label/text `"Browsing Menu"`.
24. Tap label/text `"Settings"`.
25. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
26. Tap label/text `"AI Features"`.
27. Tap identifier `"Settings.AIFeatures.Picker.SearchOnly"`.
28. Tap label/text `"Settings"`.
29. Tap label/text `"Done"`.
30. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
31. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.Search"`.
32. Require absent identifier `"Browser.OmniBar.Button.ModeToggle.AIChat"`.

### ai-chat

Source: `.maestro/release_tests/ai-chat.yaml`. Tags: `["iphone", "release"]`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.
3. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
4. Conditional branch `{"visible": "New Chat"}`: Tap label/text `"New Chat"`.
5. Conditional branch `{"visible": "Agree and Continue"}`: Tap label/text `"Agree and Continue"`.
6. Conditional branch `{"visible": "×"}`: Tap label/text `"×"`.
7. Conditional branch `{"visible": "×"}`: Tap label/text `"×"`.
8. Require visible label/text `"Free Plan"`.
9. Require visible label/text `"Upgrade"`.
10. Require visible label/text `"Close tab"`.
11. Require visible label/text `"Recent chats"`.
12. Require visible label/text `"New"`.
13. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
14. Tap label/text `"Close tab"`.
15. Require visible identifier `"searchEntry"`.
16. Tap identifier `"searchEntry"`.
17. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
18. Use the exposed provider key action for `"Enter"`; inspect its schema first.
19. Require visible label/text `".*Privacy Test Pages.*"`.
20. Tap label/text `"Browsing Menu"`.
21. Require visible label/text `"Duck.ai"`.
22. Tap label/text `"Duck.ai"`.
23. Require visible label/text `"Free Plan"`.
24. Require visible label/text `"Close tab"`.
25. Tap label/text `"Close tab"`.
26. Require visible label/text `".*Privacy Test Pages.*"`.
27. Tap label/text `"Tab Switcher"`.
28. Require visible identifier `"TabSwitcher.Button.DuckChat"`.
29. Tap identifier `"TabSwitcher.Button.DuckChat"`.
30. Require visible label/text `"Free Plan"`.
31. Require visible label/text `"Close tab"`.
32. Tap label/text `"Close tab"`.
33. Tap label/text `"Browsing Menu"`.
34. Tap label/text `"Settings"`.
35. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
36. Tap label/text `"AI Features"`.
37. Tap identifier `"Settings.AIFeatures.EnableToggle"`.
38. Tap label/text `"Settings"`.
39. Tap label/text `"Done"`.
40. Require absent identifier `"Browser.OmniBar.Button.AIChat"`.
41. Tap identifier `"searchEntry"`.
42. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
43. Use the exposed provider key action for `"Enter"`; inspect its schema first.
44. Require visible label/text `".*Privacy Test Pages.*"`.
45. Tap label/text `"Browsing Menu"`.
46. Require absent label/text `"Duck.ai"`.
47. Tap label/text `"Settings"`.
48. Tap label/text `"Done"`.
49. Tap label/text `"Tab Switcher"`.
50. Require absent identifier `"TabSwitcher.Button.DuckChat"`.

### test_ai_chat_tab_header

Source: `.maestro/unified_toggle_input/test_ai_chat_tab_header.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible label/text `"Free Plan"`.
3. Require visible label/text `"Upgrade"`.
4. Require visible label/text `"Close tab"`.
5. Require visible label/text `"Recent chats"`.
6. Require visible label/text `"New"`.
7. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
8. Require absent identifier `"AddressBar.Button.DuckAI"`.
9. Tap label/text `"Close tab"`.
10. Require visible identifier `"Browser.OmniBar.Button.AIChat"`.

### test_chat_tab_model_picker

Source: `.maestro/unified_toggle_input/test_chat_tab_model_picker.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_chat_tab_new_button

Source: `.maestro/unified_toggle_input/test_chat_tab_new_button.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible label/text `"Close tab"`.
3. Require visible label/text `"New"`.
4. Require visible label/text `"Recent chats"`.

### test_chat_tab_new_chat

Source: `.maestro/unified_toggle_input/test_chat_tab_new_chat.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Tap label/text `"Recent chats"`.
3. Require visible label/text `"Chats"`.
4. Require visible label/text `"No recent chats"`.
5. Require visible label/text `"Open Duck.ai"`.
6. Tap label/text `"Open Duck.ai"`.
7. Require visible label/text `"Close tab"`.
8. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.

### test_chat_tab_send_prompt

Source: `.maestro/unified_toggle_input/test_chat_tab_send_prompt.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"What is a duck?"` into the currently focused field using its refreshed elementRef.
5. Tap label/text `"Submit"`.
6. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
7. Require visible label/text `"What is a duck?"`.

### test_chat_tab_stop_generating

Source: `.maestro/unified_toggle_input/test_chat_tab_stop_generating.yaml`. Tags: `["iphone", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"Explain the life cycle of a duck in detail."` into the currently focused field using its refreshed elementRef.
5. Tap label/text `"Submit"`.
6. Conditional branch `{"visible": "Agree"}`: Tap label/text `"Agree"`.
7. Wait until visible label/text `"Stop generating"` (source deadline 15000 ms); retain resulting snapshot.
8. Tap label/text `"Stop generating"`.
9. Wait until gone label/text `"Stop generating"` (source deadline 10000 ms); retain resulting snapshot.
10. Require visible label/text `"Explain the life cycle of a duck in detail."`.

### test_chat_tab_toolbar_buttons

Source: `.maestro/unified_toggle_input/test_chat_tab_toolbar_buttons.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/open_chat_tab.yaml`.

1. Follow visible behavior from `.maestro/shared/open_chat_tab.yaml`.
2. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
3. Require visible identifier `"AIChat.Toolbar.Button.Reasoning"`.
4. Require visible label/text `"Tools"`.
5. Require visible label/text `"Attach"`.

## Gotchas

Model chip and New, Reasoning, Tools and Attach use native UIMenu controls. The YAML proves control presence only; inspect a new MobileBuildMCP snapshot after tapping before claiming menu contents. Live prompt send and generation-stop require network and consent; stop-generation has deliberately lost its release tag because it races the backend.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
