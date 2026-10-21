# Contextual Duck.ai and page attachment

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `test_contextual_immediate_uti_manual_context_clears_after_navigation` — `.maestro/unified_toggle_input/test_contextual_immediate_uti_manual_context_clears_after_navigation.yaml`.
- `test_contextual_immediate_uti_manual_context_clears_after_post_submit_navigation` — `.maestro/unified_toggle_input/test_contextual_immediate_uti_manual_context_clears_after_post_submit_navigation.yaml`.
- `test_contextual_immediate_uti_pre_submit_context` — `.maestro/unified_toggle_input/test_contextual_immediate_uti_pre_submit_context.yaml`.
- `test_contextual_immediate_uti_pre_submit_toolbar` — `.maestro/unified_toggle_input/test_contextual_immediate_uti_pre_submit_toolbar.yaml`.
- `test_contextual_web_uti_auto_attach_regression` — `.maestro/unified_toggle_input/test_contextual_web_uti_auto_attach_regression.yaml`.
- `test_contextual_web_uti_manual_attach_regression` — `.maestro/unified_toggle_input/test_contextual_web_uti_manual_attach_regression.yaml`.

## How to get to it (user POV)

Visit the referenced web page via `searchEntry`. Open the omnibar Duck.ai menu and choose `Ask About Page`; distinguish the floating pre-submit input from `AIChat.ContextualSheet`. Reopen an existing chat directly with the same omnibar button.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### test_contextual_immediate_uti_manual_context_clears_after_navigation

Source: `.maestro/unified_toggle_input/test_contextual_immediate_uti_manual_context_clears_after_navigation.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "true", "ff.aiChatAutoAttachContextByDefault": "false"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
10. Tap identifier `"AIChat.ContextChip.RemoveButton"`.
11. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
12. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
13. Tap label/text `"Attach"`.
14. Require visible label/text `"Ask About Page"`.
15. Tap label/text `"Ask About Page"`.
16. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
17. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
18. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
19. Tap identifier `"searchEntry"`.
20. Enter `"https://privacy-test-pages.site/security/address-bar-spoofing/index.html"` into the currently focused field using its refreshed elementRef.
21. Use the exposed provider key action for `"Enter"`; inspect its schema first.
22. Require visible label/text `".*Address Bar Spoofing.*"`.
23. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
24. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
25. Require absent identifier `"AIChat.ContextChip.Placeholder"`.

### test_contextual_immediate_uti_manual_context_clears_after_post_submit_navigation

Source: `.maestro/unified_toggle_input/test_contextual_immediate_uti_manual_context_clears_after_post_submit_navigation.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`, `.maestro/shared/expand_contextual_uti.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "true", "ff.aiChatAutoAttachContextByDefault": "false"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
10. Tap identifier `"searchEntry"`.
11. Enter `"First contextual UTI prompt"` into the currently focused field using its refreshed elementRef.
12. Tap identifier `"AIChat.Toolbar.Button.Submit"`.
13. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
14. Wait until visible identifier `"AIChat.ContextualSheet"` (source deadline 15000 ms); retain resulting snapshot.
15. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
16. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
17. Tap identifier `"searchEntry"`.
18. Enter `"https://privacy-test-pages.site/security/address-bar-spoofing/index.html"` into the currently focused field using its refreshed elementRef.
19. Use the exposed provider key action for `"Enter"`; inspect its schema first.
20. Require visible label/text `".*Address Bar Spoofing.*"`.
21. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
22. Require visible identifier `"AIChat.ContextualSheet"`.
23. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
24. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
25. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
26. Tap label/text `"Attach"`.
27. Require visible label/text `"Ask About Page"`.

### test_contextual_immediate_uti_pre_submit_context

Source: `.maestro/unified_toggle_input/test_contextual_immediate_uti_pre_submit_context.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`, `.maestro/shared/expand_contextual_uti.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "true", "ff.aiChatAutoAttachContextByDefault": "true", "ff.contextualSuggestedPrompts": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Require visible identifier `"summarize-page"`.
10. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
11. Tap identifier `"AIChat.ContextChip.RemoveButton"`.
12. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
13. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
14. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
15. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
16. Tap identifier `"searchEntry"`.
17. Enter `"https://privacy-test-pages.site/security/address-bar-spoofing/index.html"` into the currently focused field using its refreshed elementRef.
18. Use the exposed provider key action for `"Enter"`; inspect its schema first.
19. Require visible label/text `".*Address Bar Spoofing.*"`.
20. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
21. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
22. Tap identifier `"searchEntry"`.
23. Enter `"First contextual UTI prompt"` into the currently focused field using its refreshed elementRef.
24. Tap identifier `"AIChat.Toolbar.Button.Submit"`.
25. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
26. Wait until visible identifier `"AIChat.ContextualSheet"` (source deadline 15000 ms); retain resulting snapshot.
27. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
28. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
29. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
30. Require visible identifier `"AIChat.ContextualSheet"`.
31. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
32. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
33. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
34. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
35. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
36. Tap identifier `"searchEntry"`.
37. Enter `"https://example.com"` into the currently focused field using its refreshed elementRef.
38. Use the exposed provider key action for `"Enter"`; inspect its schema first.
39. Require visible label/text `".*Example Domain.*"`.
40. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
41. Require visible identifier `"AIChat.ContextualSheet"`.
42. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
43. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.

### test_contextual_immediate_uti_pre_submit_toolbar

Source: `.maestro/unified_toggle_input/test_contextual_immediate_uti_pre_submit_toolbar.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "true", "ff.aiChatAutoAttachContextByDefault": "false"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Require visible identifier `"AIChat.Toolbar.Button.ModelChip"`.
10. Require visible label/text `"Attach"`.
11. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
12. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
13. Tap identifier `"AIChat.ContextChip.RemoveButton"`.
14. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
15. Tap label/text `"Attach"`.
16. Require visible label/text `"Add Image"`.
17. Require visible label/text `"Add File"`.
18. Require visible label/text `"Ask About Page"`.
19. Tap label/text `"Ask About Page"`.
20. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
21. Require absent identifier `"AIChat.ContextChip.Placeholder"`.

### test_contextual_web_uti_auto_attach_regression

Source: `.maestro/unified_toggle_input/test_contextual_web_uti_auto_attach_regression.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`, `.maestro/shared/expand_contextual_uti.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "false", "ff.aiChatAutoAttachContextByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Require visible identifier `"AIChat.Toolbar.Button.Submit"`.
10. Tap identifier `"searchEntry"`.
11. Enter `"First contextual prompt"` into the currently focused field using its refreshed elementRef.
12. Tap identifier `"AIChat.Toolbar.Button.Submit"`.
13. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
14. Wait until visible identifier `"AIChat.ContextualSheet"` (source deadline 15000 ms); retain resulting snapshot.
15. Wait until visible label/text `"First contextual prompt"` (source deadline 30000 ms); retain resulting snapshot.
16. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
17. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
18. Tap identifier `"searchEntry"`.
19. Enter `"https://privacy-test-pages.site/security/address-bar-spoofing/index.html"` into the currently focused field using its refreshed elementRef.
20. Use the exposed provider key action for `"Enter"`; inspect its schema first.
21. Require visible label/text `".*Address Bar Spoofing.*"`.
22. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
23. Require visible identifier `"AIChat.ContextualSheet"`.
24. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
25. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
26. Require absent label/text `"Attach Page Content"`.

### test_contextual_web_uti_manual_attach_regression

Source: `.maestro/unified_toggle_input/test_contextual_web_uti_manual_attach_regression.yaml`. Tags: `["iphone", "release", "unified_toggle_input"]`.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`, `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`, `.maestro/shared/expand_contextual_uti.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.contextualDuckAIMode": "true", "ff.aiChatContextualUnifiedToggleInput": "false", "ff.aiChatAutoAttachContextByDefault": "false"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Follow visible behavior from `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
8. Require absent identifier `"AIChat.ContextualSheet"`.
9. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
10. Tap identifier `"searchEntry"`.
11. Enter `"First contextual prompt"` into the currently focused field using its refreshed elementRef.
12. Tap identifier `"AIChat.Toolbar.Button.Submit"`.
13. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
14. Wait until visible identifier `"AIChat.ContextualSheet"` (source deadline 15000 ms); retain resulting snapshot.
15. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
16. Wait until visible label/text `"Attach"` (source deadline 30000 ms); retain resulting snapshot.
17. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
18. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
19. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
20. Tap identifier `"searchEntry"`.
21. Enter `"https://privacy-test-pages.site/security/address-bar-spoofing/index.html"` into the currently focused field using its refreshed elementRef.
22. Use the exposed provider key action for `"Enter"`; inspect its schema first.
23. Require visible label/text `".*Address Bar Spoofing.*"`.
24. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
25. Require visible identifier `"AIChat.ContextualSheet"`.
26. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
27. Require absent identifier `"AIChat.ContextChip.AttachedTitle"`.
28. Tap label/text `"Attach"`.
29. Require visible label/text `"Ask About Page"`.
30. Tap label/text `"Ask About Page"`.
31. Wait until visible identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
32. Tap identifier `"AIChat.ContextualSheet.CloseButton"`.
33. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
34. Tap identifier `"searchEntry"`.
35. Enter `"https://privacy-test-pages.site/privacy-protections/geolocation/"` into the currently focused field using its refreshed elementRef.
36. Use the exposed provider key action for `"Enter"`; inspect its schema first.
37. Require visible label/text `".*Geolocation.*"`.
38. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
39. Require visible identifier `"AIChat.ContextualSheet"`.
40. Follow visible behavior from `.maestro/shared/expand_contextual_uti.yaml`.
41. Wait until gone identifier `"AIChat.ContextChip.AttachedTitle"` (source deadline 10000 ms); retain resulting snapshot.
42. Require absent identifier `"AIChat.ContextChip.Placeholder"`.
43. Tap label/text `"Attach"`.
44. Require visible label/text `"Ask About Page"`.

## Gotchas

Pin contextualDuckAIMode, aiChatContextualUnifiedToggleInput, and aiChatAutoAttachContextByDefault per scenario. Automatic and manual attachment differ before and after first submission. Post-submit behavior requires live Duck.ai and consent; chip presence alone does not prove the correct page was attached.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
