# Shared navigation and fixture helpers

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `config` (helper/configuration) — `.maestro/config.yaml`.
- `add_bookmarks_and_favorites` (helper/configuration) — `.maestro/shared/add_bookmarks_and_favorites.yaml`.
- `add_credit_card_from_settings` (helper/configuration) — `.maestro/shared/add_credit_card_from_settings.yaml`.
- `add_login_from_settings` (helper/configuration) — `.maestro/shared/add_login_from_settings.yaml`.
- `check_number_of_tabs` (helper/configuration) — `.maestro/shared/check_number_of_tabs.yaml`.
- `copy_recovery_code` (helper/configuration) — `.maestro/shared/copy_recovery_code.yaml`.
- `copy_recovery_code_from_settings` (helper/configuration) — `.maestro/shared/copy_recovery_code_from_settings.yaml`.
- `delay` (helper/configuration) — `.maestro/shared/delay.yaml`.
- `dismiss_address_bar_editing` (helper/configuration) — `.maestro/shared/dismiss_address_bar_editing.yaml`.
- `dismiss_chat_open_modals` (helper/configuration) — `.maestro/shared/dismiss_chat_open_modals.yaml`.
- `duckai_chrome_shortcut_setup` (helper/configuration) — `.maestro/shared/duckai_chrome_shortcut_setup.yaml`.
- `expand_contextual_uti` (helper/configuration) — `.maestro/shared/expand_contextual_uti.yaml`.
- `hide_daxdialogs` (helper/configuration) — `.maestro/shared/hide_daxdialogs.yaml`.
- `open_ai_features_settings` (helper/configuration) — `.maestro/shared/open_ai_features_settings.yaml`.
- `open_browsing_menu_item` (helper/configuration) — `.maestro/shared/open_browsing_menu_item.yaml`.
- `open_chat_tab` (helper/configuration) — `.maestro/shared/open_chat_tab.yaml`.
- `open_contextual_duckai_from_address_bar` (helper/configuration) — `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`.
- `open_debug_menu` (helper/configuration) — `.maestro/shared/open_debug_menu.yaml`.
- `open_manage_duckai_shortcuts` (helper/configuration) — `.maestro/shared/open_manage_duckai_shortcuts.yaml`.
- `pull_to_refresh` (helper/configuration) — `.maestro/shared/pull_to_refresh.yaml`.
- `remove_local_bookmarks` (helper/configuration) — `.maestro/shared/remove_local_bookmarks.yaml`.
- `remove_local_credit_cards` (helper/configuration) — `.maestro/shared/remove_local_credit_cards.yaml`.
- `remove_local_logins` (helper/configuration) — `.maestro/shared/remove_local_logins.yaml`.
- `seed_duckai_usage_warning` (helper/configuration) — `.maestro/shared/seed_duckai_usage_warning.yaml`.
- `set_internal_user_from_settings` (helper/configuration) — `.maestro/shared/set_internal_user_from_settings.yaml`.
- `set_search_and_duckai` (helper/configuration) — `.maestro/shared/set_search_and_duckai.yaml`.
- `set_search_only` (helper/configuration) — `.maestro/shared/set_search_only.yaml`.
- `set_sync_dev_environment` (helper/configuration) — `.maestro/shared/set_sync_dev_environment.yaml`.
- `setup` (helper/configuration) — `.maestro/shared/setup.yaml`.
- `sync_create` (helper/configuration) — `.maestro/shared/sync_create.yaml`.
- `sync_delete` (helper/configuration) — `.maestro/shared/sync_delete.yaml`.
- `sync_login` (helper/configuration) — `.maestro/shared/sync_login.yaml`.
- `sync_logout` (helper/configuration) — `.maestro/shared/sync_logout.yaml`.
- `sync_recover_data` (helper/configuration) — `.maestro/shared/sync_recover_data.yaml`.
- `sync_setup` (helper/configuration) — `.maestro/shared/sync_setup.yaml`.
- `sync_verify_bookmarks` (helper/configuration) — `.maestro/shared/sync_verify_bookmarks.yaml`.
- `sync_verify_credit_cards` (helper/configuration) — `.maestro/shared/sync_verify_credit_cards.yaml`.
- `sync_verify_logins` (helper/configuration) — `.maestro/shared/sync_verify_logins.yaml`.
- `sync_verify_unified_favorites` (helper/configuration) — `.maestro/shared/sync_verify_unified_favorites.yaml`.
- `use_firebutton` (helper/configuration) — `.maestro/shared/use_firebutton.yaml`.

## How to get to it (user POV)

These are dependencies, not standalone user features. Begin from the parent scenario’s declared screen. Navigation helpers target AI Features, debug settings, contextual chat, browser menu or data-entry settings.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### config

Source: `.maestro/config.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Configuration only: `[{"appStartup": {"enabled": false}, "appSize": {"enabled": false}, "flows": ["**"]}]`. No user behavior to verify.

### add_bookmarks_and_favorites

Source: `.maestro/shared/add_bookmarks_and_favorites.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap identifier `"searchEntry"`.
2. Enter `"www.duckduckgo.com"` into the currently focused field using its refreshed elementRef.
3. Use the exposed provider key action for `"Enter"`; inspect its schema first.
4. Tap label/text `"Browsing Menu"`.
5. Tap label/text `"Add Favorite"`.
6. Tap identifier `"searchEntry"`.
7. Enter `"www.spreadprivacy.com"` into the currently focused field using its refreshed elementRef.
8. Use the exposed provider key action for `"Enter"`; inspect its schema first.
9. Tap label/text `"Browsing Menu"`.
10. Tap label/text `"Add Bookmark"`.

### add_credit_card_from_settings

Source: `.maestro/shared/add_credit_card_from_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
2. Tap label/text `"Passwords & Autofill"`.
3. Tap label/text `"Credit Cards"`.
4. Require visible label/text `"Add Card"`.
5. Tap label/text `"Add Card"`.
6. Tap identifier `"Field_CardNumber"`, index `1`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
7. Enter `378282246310005` into the currently focused field using its refreshed elementRef.
8. Tap identifier `"Field_SecurityCode"`.
9. Enter `123` into the currently focused field using its refreshed elementRef.
10. Tap identifier `"Field_CardName"`.
11. Enter `"Maestro Test"` into the currently focused field using its refreshed elementRef.
12. Tap identifier `"Field_CardNickname"`.
13. Enter `"Maestro Test Card"` into the currently focused field using its refreshed elementRef.
14. Tap label/text `"Save"`.
15. Tap label/text `"Passwords & Autofill"`.
16. Tap label/text `"Settings"`.
17. Tap label/text `"Done"`.

### add_login_from_settings

Source: `.maestro/shared/add_login_from_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
2. Tap label/text `"Passwords & Autofill"`.
3. Tap label/text `"Passwords"`.
4. Tap label/text `"Add 24"`.
5. Tap identifier `"Field_PasswordName"`.
6. Enter `"My Personal Website"` into the currently focused field using its refreshed elementRef.
7. Tap identifier `"Field_Username"`.
8. Enter `"me@mypersonalwebsite.com"` into the currently focused field using its refreshed elementRef.
9. Tap identifier `"Field_Address"`.
10. Enter `"mypersonalwebsite.com"` into the currently focused field using its refreshed elementRef.
11. Tap label/text `"Save"`.
12. Tap label/text `"Passwords"`.
13. Tap label/text `"Passwords & Autofill"`.
14. Tap label/text `"Settings"`.
15. Tap label/text `"Done"`.

### check_number_of_tabs

Source: `.maestro/shared/check_number_of_tabs.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Read dependency `"../shared/pull_to_refresh.yaml"`.
2. Require visible label/text `"Tab Switcher"`.
3. Tap label/text `"Tab Switcher"`.
4. Require visible label/text `"${TITLE}"`.
5. Tap label/text `"Done"`.

### copy_recovery_code

Source: `.maestro/shared/copy_recovery_code.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Sync Info"`.
2. Tap label/text `"Paste and Copy Recovery Code"`.
3. Enter `"${CODE}"` into the currently focused field using its refreshed elementRef.
4. Tap label/text `"Copy"`.
5. Tap label/text `"Debug"`.

### copy_recovery_code_from_settings

Source: `.maestro/shared/copy_recovery_code_from_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/shared/open_debug_menu.yaml`.

1. Follow visible behavior from `.maestro/shared/open_debug_menu.yaml`.
2. Scroll toward `"DOWN"` until label/text `"Sync"` is fully visible; center it before tapping. Refresh the snapshot.
3. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
4. Tap label/text `"Sync"`.
5. Wait until visible label/text `"Paste and Copy Recovery Code"` (source deadline 10000 ms); retain resulting snapshot.
6. Tap label/text `"Paste and Copy Recovery Code"`.
7. Enter `"${CODE}"` into the currently focused field using its refreshed elementRef.
8. Tap label/text `"Copy"`.
9. Tap label/text `"Debug"`.
10. Tap label/text `"Settings"`.

### delay

Source: `.maestro/shared/delay.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Conditional branch `{"visible": {"text": "This is just a text that will be never matched so this invocation will cause 5s delay", "index": 0}}`: Source timing/gesture shorthand `"stopApp"`; inspect destination state and supported provider tool.

### dismiss_address_bar_editing

Source: `.maestro/shared/dismiss_address_bar_editing.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Conditional branch `{"visible": "Cancel"}`: Tap label/text `"Cancel"`.
2. Conditional branch `{"visible": "Back"}`: Tap label/text `"Back"`.

### dismiss_chat_open_modals

Source: `.maestro/shared/dismiss_chat_open_modals.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Conditional branch `{"visible": "Agree and Continue"}`: Tap label/text `"Agree and Continue"`.
2. Conditional branch `{"visible": "×"}`: Tap label/text `"×"`.
3. Conditional branch `{"visible": "×"}`: Tap label/text `"×"`.

### duckai_chrome_shortcut_setup

Source: `.maestro/shared/duckai_chrome_shortcut_setup.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true", "ff.aiChatChromeShortcutIPad": "true", "ff.aiChatChromeMenuButtonIPad": "true", "ff.contextualDuckAIMode": "true", "ff.aiChatAddressBarRecentChats": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Read dependency `"./hide_daxdialogs.yaml"`.

### expand_contextual_uti

Source: `.maestro/shared/expand_contextual_uti.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap identifier `"searchEntry"`.
2. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.

### hide_daxdialogs

Source: `.maestro/shared/hide_daxdialogs.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Conditional branch `{"visible": {"id": "DaxIcon"}}`: Tap label/text `"Hide"`. Tap label/text `"Hide Tips Forever"`.

### open_ai_features_settings

Source: `.maestro/shared/open_ai_features_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap identifier `"Browser.OmniBar.Button.BrowsingMenu"`.
2. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
3. Tap label/text `"Settings"`.
4. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
5. Scroll toward `"DOWN"` until text `"AI Features"` is fully visible; center it before tapping. Refresh the snapshot.
6. Tap label/text `"AI Features"`.
7. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### open_browsing_menu_item

Source: `.maestro/shared/open_browsing_menu_item.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing menu"`.
2. Scroll toward `"default"` until label/text `"${ITEM}"` is fully visible; center it before tapping. Refresh the snapshot.
3. Tap label/text `"${ITEM}"`.

### open_chat_tab

Source: `.maestro/shared/open_chat_tab.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/shared/dismiss_chat_open_modals.yaml`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "ff.browsingMenuSheetEnabledByDefault": "true"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
3. Conditional branch `{"visible": "New Chat"}`: Tap label/text `"New Chat"`.
4. Follow visible behavior from `.maestro/shared/dismiss_chat_open_modals.yaml`.
5. Require visible label/text `"Close tab"`.

### open_contextual_duckai_from_address_bar

Source: `.maestro/shared/open_contextual_duckai_from_address_bar.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap identifier `"Browser.OmniBar.Button.AIChat"`.
2. Require visible label/text `"New Chat"`.
3. Require visible label/text `"Ask About Page"`.
4. Tap label/text `"Ask About Page"`.
5. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.

### open_debug_menu

Source: `.maestro/shared/open_debug_menu.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"All debug options"` is fully visible; center it before tapping. Refresh the snapshot.
2. Require visible label/text `"All debug options"`.
3. Tap label/text `"All debug options"`.

### open_manage_duckai_shortcuts

Source: `.maestro/shared/open_manage_duckai_shortcuts.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Read dependency `"./open_ai_features_settings.yaml"`.
2. Scroll toward `"DOWN"` until text `"Manage Duck.ai Shortcuts"` is fully visible; center it before tapping. Refresh the snapshot.
3. Tap label/text `"Manage Duck.ai Shortcuts"`.
4. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### pull_to_refresh

Source: `.maestro/shared/pull_to_refresh.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Gesture intent `{"start": "50%, 50%", "end": "50%, 90%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.

### remove_local_bookmarks

Source: `.maestro/shared/remove_local_bookmarks.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Bookmarks"`.
2. Tap label/text `"Edit"`.
3. Tap label/text `".*Spread Privacy.*"`.
4. Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool.
5. Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool.
6. Tap label/text `"Delete"`.
7. Tap label/text `"Delete"`.
8. Tap label/text `"Done"`.
9. Tap label/text `"Done"`.

### remove_local_credit_cards

Source: `.maestro/shared/remove_local_credit_cards.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing menu"`.
2. Tap label/text `"Settings"`.
3. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
4. Tap label/text `"Passwords & Autofill"`.
5. Tap label/text `"Credit Cards"`.
6. Tap label/text `"Passcode field"`.
7. Enter `"0000"` into the currently focused field using its refreshed elementRef.
8. Use the exposed provider key action for `"Enter"`; inspect its schema first.
9. Tap label/text `"Maestro Test Card"`.
10. Tap label/text `"Delete Card"`.
11. Tap label/text `"Delete Card"`.
12. Tap label/text `"Credit Cards"`.
13. Tap label/text `"Passwords & Autofill"`.
14. Tap label/text `"Settings"`.
15. Tap label/text `"Done"`.

### remove_local_logins

Source: `.maestro/shared/remove_local_logins.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing menu"`.
2. Tap label/text `"Settings"`.
3. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
4. Tap label/text `"Passwords & Autofill"`.
5. Tap label/text `"Passwords"`.
6. Tap label/text `"Passcode field"`.
7. Enter `"0000"` into the currently focused field using its refreshed elementRef.
8. Use the exposed provider key action for `"Enter"`; inspect its schema first.
9. Tap identifier `"Button_DismissImportPromo"`, optional `true`.
10. Tap label/text `"My Personal Website"`.
11. Tap label/text `"Delete Password"`.
12. Tap label/text `"Delete Password"`.
13. Tap label/text `"Passwords & Autofill"`.
14. Tap label/text `"Settings"`.
15. Tap label/text `"Done"`.

### seed_duckai_usage_warning

Source: `.maestro/shared/seed_duckai_usage_warning.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing Menu"`.
2. Tap label/text `"Settings"`.
3. Scroll toward `"DOWN"` until text `"All debug options"` is fully visible. Refresh the snapshot.
4. Retry source condition `{"maxRetries": 2}`: Conditional branch `{"visible": "All debug options"}`: Tap label/text `"All debug options"`. Wait until visible identifier `"Settings.Debug.InternalUser.identifier"` (source deadline 5000 ms); retain resulting snapshot.
5. Scroll toward `"DOWN"` until text `"AI Chat"` is fully visible. Refresh the snapshot.
6. Tap label/text `"AI Chat"`.
7. Scroll toward `"DOWN"` until text `"${PRESET}"` is fully visible. Refresh the snapshot.
8. Tap label/text `"${PRESET}"`.
9. Tap label/text `"Debug"`.
10. Tap label/text `"Settings"`.
11. Tap label/text `"Done"`.

### set_internal_user_from_settings

Source: `.maestro/shared/set_internal_user_from_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/shared/open_debug_menu.yaml`.

1. Follow visible behavior from `.maestro/shared/open_debug_menu.yaml`.
2. Scroll toward `"default"` until identifier `"Settings.Debug.InternalUser.identifier"` is fully visible. Refresh the snapshot.
3. Tap identifier `"Settings.Debug.InternalUser.identifier"`.
4. Tap label/text `"Settings"`.
5. Tap label/text `"Done"`.
6. Tap label/text `"Browsing menu"`.
7. Tap label/text `"Settings"`.

### set_search_and_duckai

Source: `.maestro/shared/set_search_and_duckai.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing Menu"`.
2. Tap label/text `"Settings"`.
3. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
4. Tap label/text `"AI Features"`.
5. Tap identifier `"Settings.AIFeatures.Picker.SearchAndDuckAI"`.
6. Tap label/text `"Settings"`.
7. Tap label/text `"Done"`.

### set_search_only

Source: `.maestro/shared/set_search_only.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Browsing Menu"`.
2. Tap label/text `"Settings"`.
3. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
4. Tap label/text `"AI Features"`.
5. Tap identifier `"Settings.AIFeatures.Picker.SearchOnly"`.
6. Tap label/text `"Settings"`.
7. Tap label/text `"Done"`.

### set_sync_dev_environment

Source: `.maestro/shared/set_sync_dev_environment.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/shared/open_debug_menu.yaml`.

1. Follow visible behavior from `.maestro/shared/open_debug_menu.yaml`.
2. Scroll toward `"DOWN"` until label/text `"Sync"` is fully visible; center it before tapping. Refresh the snapshot.
3. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
4. Tap label/text `"Sync"`.
5. Wait until visible label/text `"Sync now"` (source deadline 10000 ms); retain resulting snapshot.
6. Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool.
7. Scroll toward `"DOWN"` until label/text `"Production"` is fully visible. Refresh the snapshot.
8. Tap label/text `"Production"`.
9. Tap label/text `"Debug"`.
10. Tap label/text `"Settings"`.

### setup

Source: `.maestro/shared/setup.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}", "ff.floatingUIAugust2026": "false"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.

### sync_create

Source: `.maestro/shared/sync_create.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap label/text `"Sync & Backup"`.
2. Require visible label/text `"Sync & Backup"`.
3. Tap identifier `"SyncToggle"`.
4. Wait until visible label/text `"Sync This Device Only"` (source deadline 30000 ms); retain resulting snapshot.
5. Tap label/text `"Sync This Device Only"`.
6. Wait until visible label/text `"Unlock device to set up Sync & Backup"` (source deadline 30000 ms); retain resulting snapshot.
7. Enter `"0000"` into the currently focused field using its refreshed elementRef.
8. Use the exposed provider key action for `"Enter"`; inspect its schema first.
9. Wait until visible identifier `"SyncSuccessTitle"` (source deadline 60000 ms); retain resulting snapshot.
10. Tap identifier `"SyncSuccessCopyRecoveryCodeButton"`.
11. Conditional branch `{"visible": "Unlock device to set up Sync & Backup"}`: Enter `"0000"` into the currently focused field using its refreshed elementRef. Use the exposed provider key action for `"Enter"`; inspect its schema first.
12. Tap identifier `"SyncSuccessDoneButton"`.
13. Require visible label/text `"Sync & Backup"`.

### sync_delete

Source: `.maestro/shared/sync_delete.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Require visible label/text `"Sync & Backup"`.
2. Scroll toward `"DOWN"` until text `"Turn Off Sync & Backup"` is fully visible. Refresh the snapshot.
3. Tap label/text `"Turn Off Sync & Backup"`.
4. Conditional branch `{"visible": "Unlock device to set up Sync & Backup"}`: Enter `"0000"` into the currently focused field using its refreshed elementRef. Use the exposed provider key action for `"Enter"`; inspect its schema first.
5. Wait until visible identifier `"TurnOffAndDeleteServerDataButton"` (source deadline 30000 ms); retain resulting snapshot.
6. Tap identifier `"TurnOffAndDeleteServerDataButton"`.
7. Require visible label/text `"You Can’t Undo This Action."`.
8. Tap label/text `"Permanently Delete"`.
9. Wait until visible label/text `"I Have a Recovery Code"` (source deadline 30000 ms); retain resulting snapshot.

### sync_login

Source: `.maestro/shared/sync_login.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Require visible label/text `"Sync With Another Device"`.
2. Tap label/text `"Sync With Another Device"`.
3. Wait until visible label/text `"Unlock device to set up Sync & Backup"` (source deadline 30000 ms); retain resulting snapshot.
4. Enter `"0000"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
7. Wait until visible label/text `"Enter Code"` (source deadline 30000 ms); retain resulting snapshot.
8. Tap label/text `"Enter Code"`.
9. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
10. Tap label/text `"Paste Sync Code"`.
11. Wait until visible identifier `"SyncSuccessTitle"` (source deadline 60000 ms); retain resulting snapshot.
12. Tap identifier `"SyncSuccessDoneButton"`.

### sync_logout

Source: `.maestro/shared/sync_logout.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Require visible label/text `"Sync & Backup"`.
2. Tap label/text `"This Device"`.
3. Conditional branch `{"visible": "Unlock device to set up Sync & Backup"}`: Enter `"0000"` into the currently focused field using its refreshed elementRef. Use the exposed provider key action for `"Enter"`; inspect its schema first.
4. Wait until visible identifier `"SyncThisDeviceToggle"` (source deadline 30000 ms); retain resulting snapshot.
5. Tap identifier `"SyncThisDeviceToggle"`.
6. Require visible label/text `"Remove .* from Sync & Backup\\?"`.
7. Tap label/text `"Remove"`.
8. Wait until visible label/text `"I Have a Recovery Code"` (source deadline 30000 ms); retain resulting snapshot.

### sync_recover_data

Source: `.maestro/shared/sync_recover_data.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Require visible label/text `"I Have a Recovery Code"`.
2. Tap label/text `"I Have a Recovery Code"`.
3. Require visible label/text `"Recover your synced data"`.
4. Tap label/text `"Recover Synced Data"`.
5. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
6. Conditional branch `{"visible": "Unlock device to set up Sync & Backup"}`: Enter `"0000"` into the currently focused field using its refreshed elementRef. Use the exposed provider key action for `"Enter"`; inspect its schema first.
7. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
8. Wait until visible label/text `"Enter Code"` (source deadline 30000 ms); retain resulting snapshot.
9. Tap label/text `"Enter Code"`.
10. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
11. Tap label/text `"Paste Sync Code"`.
12. Wait until visible identifier `"SyncSuccessTitle"` (source deadline 60000 ms); retain resulting snapshot.
13. Tap identifier `"SyncSuccessDoneButton"`.

### sync_setup

Source: `.maestro/shared/sync_setup.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "currentAppVariant": "${APP_VARIANT}", "isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.

### sync_verify_bookmarks

Source: `.maestro/shared/sync_verify_bookmarks.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/shared/delay.yaml`.

1. Tap label/text `"Settings"`.
2. Tap label/text `"Done"`.
3. Follow visible behavior from `.maestro/shared/delay.yaml`.
4. Conditional branch `{"visible": {"text": "Download Missing Icons?"}}`: Tap label/text `"Not Now"`.
5. Tap label/text `"Bookmarks"`.
6. Conditional branch `{"visible": {"text": "Download Missing Icons?"}}`: Tap label/text `"Not Now"`.
7. Require visible label/text `".*Spread Privacy.*"`.
8. Require visible label/text `"Stack Overflow - Where Developers Learn, Share, & Build Careers"`.
9. Require visible label/text `"DuckDuckGo — Privacy, simplified."`.
10. Require visible label/text `"DuckDuckGo · GitHub"`.
11. Require visible label/text `"Wolfram|Alpha: Computational Intelligence"`.
12. Require visible label/text `"news"`.
13. Require visible label/text `"code"`.
14. Require visible label/text `"sports"`.
15. Tap label/text `"news"`.
16. Require visible label/text `"Breaking News, Latest News and Videos | CNN"`.
17. Require visible label/text `"News, sport and opinion from the Guardian's global edition | The Guardian"`.
18. Tap label/text `"Bookmarks"`.
19. Tap label/text `"code"`.
20. Require visible label/text `"GitHub - duckduckgo/Android: DuckDuckGo Android App"`.
21. Require visible label/text `"GitHub - duckduckgo/iOS: DuckDuckGo iOS Application"`.
22. Tap label/text `"Bookmarks"`.
23. Tap label/text `"sports"`.
24. Require visible label/text `"NFL.com | Official Site of the National Football League"`.
25. Require visible label/text `"AS.com - Diario online deportivo. Fútbol, motor y mucho más"`.
26. Tap label/text `"Bookmarks"`.

### sync_verify_credit_cards

Source: `.maestro/shared/sync_verify_credit_cards.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
2. Tap label/text `"Passwords & Autofill"`.
3. Tap label/text `"Credit Cards"`.
4. Tap label/text `"Passcode field"`.
5. Enter `"0000"` into the currently focused field using its refreshed elementRef.
6. Use the exposed provider key action for `"Enter"`; inspect its schema first.
7. Scroll toward `"default"` until label/text `"Credit card"` is fully visible. Refresh the snapshot.
8. Require visible label/text `"Credit card"`.
9. Tap label/text `"Credit card"`.
10. Require visible label/text `"5101 6737 0209 1308"`.
11. Tap label/text `"Credit Cards"`.
12. Scroll toward `"default"` until label/text `"Debit card"` is fully visible. Refresh the snapshot.
13. Require visible label/text `"Debit card"`.
14. Tap label/text `"Debit card"`.
15. Require visible label/text `"4242 4242 4242 4242"`.
16. Tap label/text `"Credit Cards"`.
17. Tap label/text `"Passwords & Autofill"`.
18. Tap label/text `"Settings"`.

### sync_verify_logins

Source: `.maestro/shared/sync_verify_logins.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
2. Tap label/text `"Passwords & Autofill"`.
3. Tap label/text `"Passwords"`.
4. Tap label/text `"Passcode field"`.
5. Enter `"0000"` into the currently focused field using its refreshed elementRef.
6. Use the exposed provider key action for `"Enter"`; inspect its schema first.
7. Tap identifier `"Button_DismissImportPromo"`, optional `true`.
8. Scroll toward `"default"` until label/text `"Dax Login"` is fully visible. Refresh the snapshot.
9. Require visible label/text `"Dax Login"`.
10. Tap label/text `"Dax Login"`.
11. Require visible label/text `"daxthetest"`.
12. Require visible label/text `"duckduckgo.com"`.
13. Tap label/text `"Passwords"`.
14. Scroll toward `"default"` until label/text `"Github"` is fully visible. Refresh the snapshot.
15. Require visible label/text `"Github"`.
16. Tap label/text `"Github"`.
17. Require visible label/text `"githubusername"`.
18. Require visible label/text `"github.com"`.
19. Tap label/text `"Passwords"`.
20. Scroll toward `"default"` until label/text `"StackOverflow"` is fully visible. Refresh the snapshot.
21. Require visible label/text `"StackOverflow"`.
22. Tap label/text `"StackOverflow"`.
23. Require visible label/text `"stacker"`.
24. Require visible label/text `"stackoverflow.com"`.
25. Tap label/text `"Passwords"`.
26. Scroll toward `"default"` until label/text `"My Personal Website"` is fully visible. Refresh the snapshot.
27. Require visible label/text `"My Personal Website"`.
28. Tap label/text `"My Personal Website"`.
29. Require visible label/text `"me@mypersonalwebsite.com"`.
30. Require visible label/text `"mypersonalwebsite.com"`.
31. Tap label/text `"Passwords"`.
32. Tap label/text `"Passwords & Autofill"`.
33. Tap label/text `"Settings"`.

### sync_verify_unified_favorites

Source: `.maestro/shared/sync_verify_unified_favorites.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Scroll toward `"default"` until label/text `"Sync & Backup"` is fully visible. Refresh the snapshot.
2. Tap label/text `"Sync & Backup"`.
3. Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool.
4. Require visible label/text `"Share Favorites Across Devices"`.
5. Conditional branch `{"visible": {"id": "UnifiedFavoritesToggle", "checked": false}}`: Tap identifier `"UnifiedFavoritesToggle"`.
6. Wait until visible identifier `"UnifiedFavoritesToggle"`, checked `true` (source deadline 10000 ms); retain resulting snapshot.
7. Tap label/text `"Settings"`.
8. Tap label/text `"Done"`.
9. Require visible label/text `"Tab Switcher"`.
10. Tap label/text `"Tab Switcher"`.
11. Require visible label/text `"New Tab"`.
12. Tap label/text `"New Tab"`.
13. Require visible label/text `"NFL.com | Official Site of the National Football League"`.
14. Require visible label/text `"DuckDuckGo · GitHub"`.
15. Require visible label/text `"Stack Overflow - Where Developers Learn, Share, & Build Careers"`.

### use_firebutton

Source: `.maestro/shared/use_firebutton.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Tap identifier `"Browser.Toolbar.Button.Fire"`.
2. Tap identifier `"alert.forget-data.confirm"`.
3. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

## Gotchas

Do not run YAML, shell scripts, evalScript or JavaScript fixtures as drivers. Translate visible UI intent through MobileBuildMCP. Constants and clipboard fixtures require reading their parent intent. Destructive cleanup and server-delete helpers are mapped only without explicit disposable-state authorization.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
