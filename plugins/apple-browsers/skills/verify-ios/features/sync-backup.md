# Sync and Backup

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `01_create_account` — `.maestro/sync_tests/01_create_account.yaml`.
- `02_login_account` — `.maestro/sync_tests/02_login_account.yaml`.
- `03_recover_account` — `.maestro/sync_tests/03_recover_account.yaml`.
- `04_sync_data_setup` — `.maestro/sync_tests/04_sync_data_setup.yaml`.
- `05_sync_data_check` — `.maestro/sync_tests/05_sync_data_check.yaml`.
- `06_delete_account` — `.maestro/sync_tests/06_delete_account.yaml`.

## How to get to it (user POV)

Browsing Menu → Settings → Sync & Backup. Inspect the logged-out surface before any account mutation. Account creation starts with SyncToggle then Sync This Device Only; recovery/login use I Have a Recovery Code or Sync With Another Device and Enter Code.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### 01_create_account

Source: `.maestro/sync_tests/01_create_account.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_create.yaml`, `.maestro/shared/sync_delete.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
5. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
6. Follow visible behavior from `.maestro/shared/sync_create.yaml`.
7. Require visible label/text `"Sync & Backup"`.
8. Follow visible behavior from `.maestro/shared/sync_delete.yaml`.

### 02_login_account

Source: `.maestro/sync_tests/02_login_account.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/copy_recovery_code_from_settings.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_login.yaml`, `.maestro/shared/sync_logout.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/copy_recovery_code_from_settings.yaml` with parameters `{"CODE": "${CODE}"}`.
5. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
6. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
7. Require visible label/text `"Sync & Backup"`.
8. Tap label/text `"Sync & Backup"`.
9. Follow visible behavior from `.maestro/shared/sync_login.yaml`.
10. Require visible label/text `"Sync & Backup"`.
11. Follow visible behavior from `.maestro/shared/sync_logout.yaml`.

### 03_recover_account

Source: `.maestro/sync_tests/03_recover_account.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_create.yaml`, `.maestro/shared/sync_logout.yaml`, `.maestro/shared/sync_recover_data.yaml`, `.maestro/shared/sync_delete.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
5. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
6. Follow visible behavior from `.maestro/shared/sync_create.yaml`.
7. Follow visible behavior from `.maestro/shared/sync_logout.yaml`.
8. Follow visible behavior from `.maestro/shared/sync_recover_data.yaml`.
9. Follow visible behavior from `.maestro/shared/sync_delete.yaml`.

### 04_sync_data_setup

Source: `.maestro/sync_tests/04_sync_data_setup.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/add_bookmarks_and_favorites.yaml`, `.maestro/shared/use_firebutton.yaml`, `.maestro/shared/add_login_from_settings.yaml`, `.maestro/shared/add_credit_card_from_settings.yaml`, `.maestro/shared/copy_recovery_code_from_settings.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_login.yaml`, `.maestro/shared/sync_logout.yaml`, `.maestro/shared/remove_local_bookmarks.yaml`, `.maestro/shared/remove_local_logins.yaml`, `.maestro/shared/remove_local_credit_cards.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Follow visible behavior from `.maestro/shared/add_bookmarks_and_favorites.yaml`.
3. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
4. Conditional branch `{"visible": "Back"}`: Tap label/text `"Back"`.
5. Conditional branch `{"visible": {"text": "Cancel"}}`: Tap label/text `"Cancel"`.
6. Tap label/text `"Browsing menu"`.
7. Tap label/text `"Settings"`.
8. Follow visible behavior from `.maestro/shared/add_login_from_settings.yaml`.
9. Tap label/text `"Browsing menu"`.
10. Tap label/text `"Settings"`.
11. Follow visible behavior from `.maestro/shared/add_credit_card_from_settings.yaml`.
12. Tap label/text `"Browsing menu"`.
13. Tap label/text `"Settings"`.
14. Follow visible behavior from `.maestro/shared/copy_recovery_code_from_settings.yaml` with parameters `{"CODE": "${CODE}"}`.
15. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
16. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
17. Require visible label/text `"Sync & Backup"`.
18. Tap label/text `"Sync & Backup"`.
19. Follow visible behavior from `.maestro/shared/sync_login.yaml`.
20. Require visible label/text `"Sync & Backup"`.
21. Follow visible behavior from `.maestro/shared/sync_logout.yaml`.
22. Tap label/text `"Settings"`.
23. Tap label/text `"Done"`.
24. Follow visible behavior from `.maestro/shared/remove_local_bookmarks.yaml`.
25. Follow visible behavior from `.maestro/shared/remove_local_logins.yaml`.
26. Follow visible behavior from `.maestro/shared/remove_local_credit_cards.yaml`.
27. Require visible identifier `"searchEntry"`.

### 05_sync_data_check

Source: `.maestro/sync_tests/05_sync_data_check.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/copy_recovery_code_from_settings.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_login.yaml`, `.maestro/shared/sync_verify_bookmarks.yaml`, `.maestro/shared/sync_verify_unified_favorites.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`, `.maestro/shared/sync_verify_logins.yaml`, `.maestro/shared/sync_verify_credit_cards.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/copy_recovery_code_from_settings.yaml` with parameters `{"CODE": "${CODE}"}`.
5. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
6. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
7. Require visible label/text `"Sync & Backup"`.
8. Tap label/text `"Sync & Backup"`.
9. Follow visible behavior from `.maestro/shared/sync_login.yaml`.
10. Require visible label/text `"Sync & Backup"`.
11. Tap label/text `"Settings"`.
12. Follow visible behavior from `.maestro/shared/sync_verify_bookmarks.yaml`.
13. Tap label/text `"Done"`.
14. Tap label/text `"Browsing menu"`.
15. Tap label/text `"Settings"`.
16. Follow visible behavior from `.maestro/shared/sync_verify_unified_favorites.yaml`.
17. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
18. Tap label/text `"Browsing menu"`.
19. Tap label/text `"Settings"`.
20. Follow visible behavior from `.maestro/shared/sync_verify_logins.yaml`.
21. Tap label/text `"Done"`.
22. Tap label/text `"Browsing menu"`.
23. Tap label/text `"Settings"`.
24. Follow visible behavior from `.maestro/shared/sync_verify_credit_cards.yaml`.

### 06_delete_account

Source: `.maestro/sync_tests/06_delete_account.yaml`. Tags: `["iphone", "sync"]`.

Dependencies: `.maestro/shared/sync_setup.yaml`, `.maestro/shared/set_internal_user_from_settings.yaml`, `.maestro/shared/set_sync_dev_environment.yaml`, `.maestro/shared/sync_create.yaml`, `.maestro/shared/sync_delete.yaml`.

1. Follow visible behavior from `.maestro/shared/sync_setup.yaml`.
2. Tap label/text `"Browsing menu"`.
3. Tap label/text `"Settings"`.
4. Follow visible behavior from `.maestro/shared/set_internal_user_from_settings.yaml`.
5. Follow visible behavior from `.maestro/shared/set_sync_dev_environment.yaml`.
6. Follow visible behavior from `.maestro/shared/sync_create.yaml`.
7. Follow visible behavior from `.maestro/shared/sync_delete.yaml`.
8. Require visible label/text `"Sync With Another Device"`.
9. Tap label/text `"Sync With Another Device"`.
10. Conditional branch `{"visible": "Unlock device to set up Sync & Backup"}`: Enter `"0000"` into the currently focused field using its refreshed elementRef. Use the exposed provider key action for `"Enter"`; inspect its schema first.
11. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
12. Wait until visible label/text `"Enter Code"` (source deadline 30000 ms); retain resulting snapshot.
13. Tap label/text `"Enter Code"`.
14. Conditional branch `{"visible": "Allows you to upload photographs and videos"}`: Tap label/text `"Allow"`.
15. Tap label/text `"Paste Sync Code"`.
16. Require visible label/text `"Sync failed."`.
17. Require visible label/text `"Please try again."`.
18. Tap label/text `"Got It"`.

## Gotchas

Do not execute these backend-mutating recipes against a real account. They need explicitly disposable account data and known credentials/passcode. The shared helper named set_sync_dev_environment selects Production in this checkout, so its name does not prove an isolated backend. Data check 05 depends on completed 04 setup and a persisted remote account. Deletion uses TurnOffAndDeleteServerDataButton then Permanently Delete; map only unless a disposable test account is explicitly authorized. Never capture recovery codes in evidence.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
