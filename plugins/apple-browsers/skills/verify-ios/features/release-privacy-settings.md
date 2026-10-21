# App lock, autoclear and release privacy

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `application-lock` — `.maestro/release_tests/application-lock.yaml`.
- `autoclear` — `.maestro/release_tests/autoclear.yaml`.
- `content-blocking` — `.maestro/release_tests/content-blocking.yaml`.
- `emailprotection` — `.maestro/release_tests/emailprotection.yaml`.
- `firebutton` — `.maestro/release_tests/firebutton.yaml`.
- `local-storage` — `.maestro/release_tests/local-storage.yaml`.

## How to get to it (user POV)

Reach Settings from Browsing Menu for lock/autoclear; use privacy dashboard, Fire Button, or fixture-specific email/local-storage controls as named below.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### application-lock

Source: `.maestro/release_tests/application-lock.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Tap label/text `"Browsing Menu"`.
3. Wait until visible label/text `"Settings"` (source deadline 10000 ms); retain resulting snapshot.
4. Tap label/text `"Settings"`.
5. Scroll toward `"DOWN"` until label/text `"General"` is fully visible. Refresh the snapshot.
6. Tap label/text `"General"`.
7. Tap text `"0"`, index `"0"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
8. Source timing/gesture shorthand `"stopApp"`; inspect destination state and supported provider tool.
9. Launch intent `{"arguments": {"isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
10. Require visible label/text `"Unlock DuckDuckGo."`.
11. Enter `"password"` into the currently focused field using its refreshed elementRef.
12. Use the exposed provider key action for `"Enter"`; inspect its schema first.
13. Require visible identifier `"searchEntry"`.
14. Tap identifier `"searchEntry"`.
15. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
16. Use the exposed provider key action for `"Enter"`; inspect its schema first.
17. Require visible label/text `".*Privacy Test Pages.*"`.
18. Tap label/text `"Browsing Menu"`.
19. Wait until visible label/text `"Settings"` (source deadline 10000 ms); retain resulting snapshot.
20. Tap label/text `"Settings"`.
21. Scroll toward `"DOWN"` until label/text `"General"` is fully visible. Refresh the snapshot.
22. Tap label/text `"General"`.
23. Tap text `"1"`, index `"0"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
24. Source timing/gesture shorthand `"stopApp"`; inspect destination state and supported provider tool.
25. Launch intent `{"arguments": {"isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
26. Require visible label/text `"Privacy Test Pages"`.

### autoclear

Source: `.maestro/release_tests/autoclear.yaml`. Tags: `["iphone", "release"]`.

1. Launch intent `{"appId": "com.duckduckgo.mobile.ios", "clearState": true, "clearKeychain": true, "arguments": {"isOnboardingCompleted": "${ONBOARDING_COMPLETED}", "autoclear-ui-test": true, "isRunningUITests": true, "isInternalUser": "${INTERNAL_USER_MODE}"}}`. Translate argument keys using the app parser; clearState/clearKeychain are historical fixture requirements, not permission to reset the device.
2. Tap label/text `"Browsing Menu"`.
3. Tap label/text `"Settings"`.
4. Require visible identifier `"Settings.ListItem.Field_DefaultBrowser"`.
5. Scroll toward `"default"` until text `"Data Clearing"` is fully visible; center it before tapping. Refresh the snapshot.
6. Require visible label/text `"Data Clearing"`.
7. Tap label/text `"Data Clearing"`.
8. Require visible label/text `"Off"`.
9. Require visible label/text `"Automatically Delete Data"`.
10. Tap label/text `"Automatically Delete Data"`.
11. Require visible identifier `"AutoclearEnabledToggle"`.
12. Tap identifier `"AutoclearEnabledToggle"`.
13. Require visible label/text `"App Exit, Inactive for 5 Minutes"`.
14. Tap label/text `"App Exit, Inactive for 5 Minutes"`.
15. Tap label/text `"Data Clearing"`.
16. Tap label/text `"Settings"`.
17. Tap label/text `"Done"`.
18. Require visible identifier `"searchEntry"`.
19. Tap identifier `"searchEntry"`.
20. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
21. Use the exposed provider key action for `"Enter"`; inspect its schema first.
22. Require visible label/text `"Storage Counter: undefined"`.
23. Require visible label/text `"Cookie Counter:"`.
24. Require absent label/text `"Cookie Counter: 1"`.
25. Require absent label/text `"Storage Counter: 1"`.
26. Require visible label/text `"Manual Increment"`.
27. Tap label/text `"Manual Increment"`.
28. Require visible label/text `"Cookie Counter: 1"`.
29. Require visible label/text `"Storage Counter: 1"`.
30. Tap label/text `"Tab Switcher"`.
31. Tap label/text `"New Tab"`.
32. Require visible identifier `"searchEntry"`.
33. Tap identifier `"searchEntry"`.
34. Enter `"https://example.com"` into the currently focused field using its refreshed elementRef.
35. Use the exposed provider key action for `"Enter"`; inspect its schema first.
36. Require visible label/text `".*Example Domain.*"`.
37. Use the exposed provider key action for `"Home"`; inspect its schema first.
38. Repeat source condition `{"times": 3}`: Gesture intent `{"start": "50%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors. Gesture intent `{"start": "10%, 50%", "end": "50%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
39. Tap label/text `"DuckDuckGo"`.
40. Require visible label/text `"Tab Switcher"`.
41. Require absent label/text `"https://example.com/"`.
42. Require visible label/text `"Search or enter address"`.
43. Tap label/text `"Tab Switcher"`.
44. Require absent label/text `"Example Domain"`.
45. Require visible label/text `"1 Private Tab"`.
46. Tap label/text `"Done"`.
47. Require visible identifier `"searchEntry"`.
48. Tap identifier `"searchEntry"`.
49. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
50. Use the exposed provider key action for `"Enter"`; inspect its schema first.
51. Require visible label/text `"Storage Counter: undefined"`.
52. Require visible label/text `"Cookie Counter:"`.

### content-blocking

Source: `.maestro/release_tests/content-blocking.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site/tracker-reporting/1major-via-script.html"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"1 major tracker loaded via script src"`.
7. Tap label/text `"Privacy Icon"`.
8. Require visible label/text `"Protections are ON for this site"`.
9. Require visible label/text `"We blocked Google Ads (Google) from loading tracking requests on this page."`.
10. Tap label/text `"View Tracker Companies"`.
11. Require visible label/text `"doubleclick.net"`.
12. Require visible label/text `"Back"`.
13. Tap label/text `"Back"`.
14. Require visible label/text `"Disable Protections"`.
15. Tap label/text `"Disable Protections"`.
16. Require visible label/text `"Site not working? Let us know."`.
17. Require visible label/text `"Don't Send"`.
18. Tap label/text `"Don't Send"`.
19. Wait until gone label/text `"Nonsense text that won't exist"` (source deadline 2000 ms); retain resulting snapshot.
20. Require visible label/text `"1 major tracker loaded via script src"`.
21. Tap label/text `"Privacy Icon"`.
22. Require visible label/text `"Protections are OFF for this site"`.
23. Tap label/text `"Done"`.
24. Tap label/text `"Browsing menu"`.
25. Scroll toward `"default"` until text `"Enable Privacy Protection"` is fully visible. Refresh the snapshot.
26. Tap label/text `"Enable Privacy Protection"`.
27. Require visible label/text `".*Privacy Protection enabled for.*"`.
28. Require visible label/text `"Undo"`.
29. Wait until gone label/text `"Undo"` (source deadline 8000 ms); retain resulting snapshot.
30. Tap label/text `"Privacy Icon"`.
31. Require visible label/text `"Protections are ON for this site"`.
32. Require visible label/text `"We blocked Google Ads (Google) from loading tracking requests on this page."`.
33. Tap label/text `"Done"`.
34. Tap label/text `"Browsing menu"`.
35. Scroll toward `"default"` until text `"Disable Privacy Protection"` is fully visible. Refresh the snapshot.
36. Tap label/text `"Disable Privacy Protection"`.
37. Require visible label/text `".*Privacy Protection disabled for.*"`.
38. Require visible label/text `"Undo"`.
39. Wait until gone label/text `"Undo"` (source deadline 8000 ms); retain resulting snapshot.
40. Tap label/text `"Privacy Icon"`.
41. Require visible label/text `"Protections are OFF for this site"`.
42. Require absent label/text `"We blocked Google Ads (Google) from loading tracking requests on this page."`.
43. Tap label/text `"Done"`.
44. Tap label/text `"Browsing menu"`.
45. Scroll toward `"default"` until text `"Enable Privacy Protection"` is fully visible. Refresh the snapshot.
46. Tap label/text `"Enable Privacy Protection"`.
47. Require visible label/text `".*Privacy Protection enabled for.*"`.
48. Tap label/text `"Undo"`.
49. Wait until gone label/text `"Undo"` (source deadline 8000 ms); retain resulting snapshot.
50. Tap label/text `"Privacy Icon"`.
51. Require visible label/text `"Protections are OFF for this site"`.
52. Require absent label/text `"We blocked Google Ads (Google) from loading tracking requests on this page."`.

### emailprotection

Source: `.maestro/release_tests/emailprotection.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Tap label/text `"Browsing Menu"`.
3. Tap label/text `"Settings"`.
4. Conditional branch `{"visible": "Email Protection"}`: Tap label/text `"Email Protection"`. Require visible label/text `"Enable Email Protection"`. Tap label/text `"Enable Email Protection"`.
5. Conditional branch `{"notVisible": "Email Protection"}`: Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool. Source timing/gesture shorthand `"scroll"`; inspect destination state and supported provider tool. Require visible label/text `"Email Protection"`. Tap label/text `"Email Protection"`.
6. Require visible label/text `"Email protection, simplified."`.
7. Require visible identifier `"searchEntry"`.
8. Tap identifier `"searchEntry"`.
9. Require visible label/text `"https://duckduckgo.com/email/"`.

### firebutton

Source: `.maestro/release_tests/firebutton.yaml`. Tags: `["iphone"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/shared/use_firebutton.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"Storage Counter: undefined"`.
7. Require visible label/text `"Cookie Counter:"`.
8. Require absent label/text `"Cookie Counter: 1"`.
9. Require absent label/text `"Storage Counter: 1"`.
10. Require visible label/text `"Manual Increment"`.
11. Tap label/text `"Manual Increment"`.
12. Require visible label/text `"Cookie Counter: 1"`.
13. Require visible label/text `"Storage Counter: 1"`.
14. Tap label/text `"Tab Switcher"`.
15. Tap label/text `"New Tab"`.
16. Require visible identifier `"searchEntry"`.
17. Tap identifier `"searchEntry"`.
18. Enter `"https://example.com"` into the currently focused field using its refreshed elementRef.
19. Use the exposed provider key action for `"Enter"`; inspect its schema first.
20. Require visible label/text `".*Example Domain.*"`.
21. Tap label/text `"Tab Switcher"`.
22. Tap label/text `"Close \"Example Domain\" at example.com"`.
23. Tap label/text `"New Tab"`.
24. Require visible identifier `"searchEntry"`.
25. Tap identifier `"searchEntry"`.
26. Enter `"ex"` into the currently focused field using its refreshed elementRef.
27. Require visible label/text `"example.com"`.
28. Require visible label/text `"Example Domain"`.
29. Tap label/text `"Example Domain"`.
30. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
31. Require absent label/text `"https://example.com/"`.
32. Require visible label/text `"Search or enter address"`.
33. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
34. Tap label/text `"Tab Switcher"`.
35. Require absent label/text `"Example Domain"`.
36. Require visible label/text `"1 Private Tab"`.
37. Tap label/text `"Done"`.
38. Require visible identifier `"searchEntry"`.
39. Tap identifier `"searchEntry"`.
40. Enter `"ex"` into the currently focused field using its refreshed elementRef.
41. Require absent label/text `"example.com"`.
42. Require absent label/text `"Example Domain"`.
43. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
44. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
45. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
46. Use the exposed provider key action for `"Enter"`; inspect its schema first.
47. Require visible label/text `"Storage Counter: undefined"`.
48. Require visible label/text `"Cookie Counter:"`.
49. Tap label/text `"Tab Switcher"`.
50. Require visible label/text `"1 Private Tab"`.
51. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
52. Require absent label/text `"https://privacy-test-pages.site/features/local-storage.html"`.
53. Require visible label/text `"Search or enter address"`.
54. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
55. Tap label/text `"Tab Switcher"`.
56. Require absent label/text `"Example Domain"`.
57. Require visible label/text `"1 Private Tab"`.
58. Tap label/text `"Done"`.
59. Require visible identifier `"searchEntry"`.
60. Tap identifier `"searchEntry"`.
61. Enter `"ex"` into the currently focused field using its refreshed elementRef.
62. Require absent label/text `"example.com"`.
63. Require absent label/text `"Example Domain"`.
64. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
65. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
66. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
67. Use the exposed provider key action for `"Enter"`; inspect its schema first.
68. Require visible label/text `"Storage Counter: undefined"`.
69. Require visible label/text `"Cookie Counter:"`.
70. Tap label/text `"Browsing Menu"`.
71. Tap label/text `"Settings"`.
72. Scroll toward `"default"` until label/text `"Data Clearing"` is fully visible. Refresh the snapshot.
73. Tap label/text `"Data Clearing"`.
74. Tap identifier `"Settings.DataClearing.Button.ForgetAll"`.
75. Tap identifier `"alert.forget-data.confirm"`.
76. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
77. Tap label/text `"Settings"`.
78. Tap label/text `"Done"`.
79. Require absent label/text `"https://privacy-test-pages.site/features/local-storage.html"`.
80. Require visible label/text `"Search or enter address"`.

### local-storage

Source: `.maestro/release_tests/local-storage.yaml`. Tags: `["iphone"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/shared/open_browsing_menu_item.yaml`, `.maestro/shared/use_firebutton.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"Storage Counter: undefined"`.
7. Require visible label/text `"Cookie Counter:"`.
8. Require absent label/text `"Cookie Counter: 1"`.
9. Require absent label/text `"Storage Counter: 1"`.
10. Require visible label/text `"Manual Increment"`.
11. Tap label/text `"Manual Increment"`.
12. Tap label/text `"Manual Increment"`.
13. Require visible label/text `"Cookie Counter: 2"`.
14. Require visible label/text `"Storage Counter: 2"`.
15. Follow visible behavior from `.maestro/shared/open_browsing_menu_item.yaml` with parameters `{"ITEM": "Fireproof This Site"}`.
16. Tap label/text `"Fireproof"`.
17. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
18. Require absent label/text `"https://privacy-test-pages.site/features/local-storage.html"`.
19. Require visible identifier `"searchEntry"`.
20. Tap identifier `"searchEntry"`.
21. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
22. Use the exposed provider key action for `"Enter"`; inspect its schema first.
23. Require visible label/text `"Storage Counter: 2"`.
24. Require visible label/text `"Cookie Counter: 2"`.
25. Follow visible behavior from `.maestro/shared/open_browsing_menu_item.yaml` with parameters `{"ITEM": "Remove Fireproofing"}`.
26. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
27. Require absent label/text `"https://privacy-test-pages.site/features/local-storage.html"`.
28. Require visible identifier `"searchEntry"`.
29. Tap identifier `"searchEntry"`.
30. Enter `"https://privacy-test-pages.site/features/local-storage.html"` into the currently focused field using its refreshed elementRef.
31. Use the exposed provider key action for `"Enter"`; inspect its schema first.
32. Require visible label/text `"Storage Counter: undefined"`.
33. Require visible label/text `"Cookie Counter:"`.

## Gotchas

Fire and autoclear delete local browsing data: only use isolated disposable fixtures. Email Protection and account service flows need an authorized disposable account; default to mapped-only. App lock requires simulator authentication setup; do not infer system integration from a visible toggle.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
