# Passwords and Autofill

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `password-authentication` — `.maestro/release_tests/password-authentication.yaml`.
- `password-autofill` — `.maestro/release_tests/password-autofill.yaml`.
- `password-management` — `.maestro/release_tests/password-management.yaml`.

## How to get to it (user POV)

Browsing Menu → Settings → Passwords & Autofill → Passwords. Use disposable sample entries; inspect current passcode/auth state before following fixture assumptions.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### password-authentication

Source: `.maestro/release_tests/password-authentication.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Tap label/text `"Browsing Menu"`.
3. Tap label/text `"Settings"`.
4. Scroll toward `"DOWN"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
5. Tap label/text `"Passwords & Autofill"`.
6. Tap label/text `"Passwords"`.
7. Tap label/text `"Add 24"`.
8. Tap identifier `"Field_PasswordName"`.
9. Enter `"Example"` into the currently focused field using its refreshed elementRef.
10. Use the exposed provider key action for `"Enter"`; inspect its schema first.
11. Tap label/text `"Save"`.
12. Tap label/text `"Passwords"`.
13. Tap label/text `"Passwords & Autofill"`.
14. Tap label/text `"Settings"`.
15. Tap label/text `"Done"`.
16. Tap label/text `"Browsing Menu"`.
17. Tap label/text `"Settings"`.
18. Scroll toward `"DOWN"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
19. Tap label/text `"Passwords & Autofill"`.
20. Tap label/text `"Passwords"`.
21. Require visible label/text `"Unlock device to access passwords"`.
22. Use the exposed provider key action for `"Enter"`; inspect its schema first.
23. Require visible label/text `"Unlock device to access passwords"`.
24. Enter `"Anything"` into the currently focused field using its refreshed elementRef.
25. Use the exposed provider key action for `"Enter"`; inspect its schema first.
26. Require visible label/text `"Passwords"`.
27. Tap label/text `"Passwords & Autofill"`.
28. Tap label/text `"Settings"`.
29. Tap label/text `"Done"`.
30. Use the exposed provider key action for `"HOME"`; inspect its schema first.
31. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
32. Tap label/text `"DuckDuckGO"`.
33. Tap label/text `"Browsing Menu"`.
34. Tap label/text `"Settings"`.
35. Scroll toward `"DOWN"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
36. Tap label/text `"Passwords & Autofill"`.
37. Tap label/text `"Passwords"`.
38. Require visible label/text `"Unlock device to access passwords"`.
39. Enter `"Anything"` into the currently focused field using its refreshed elementRef.
40. Use the exposed provider key action for `"Enter"`; inspect its schema first.
41. Require visible label/text `"Passwords"`.
42. Use the exposed provider key action for `"HOME"`; inspect its schema first.
43. Wait for the destination UI to settle; do not reuse elementRefs from before navigation.
44. Tap label/text `"DuckDuckGO"`.
45. Require visible label/text `"Unlock device to access passwords"`.
46. Enter `"Anything"` into the currently focused field using its refreshed elementRef.
47. Use the exposed provider key action for `"Enter"`; inspect its schema first.
48. Require visible label/text `"Passwords"`.
49. Tap label/text `"Passwords & Autofill"`.
50. Tap label/text `"Settings"`.
51. Tap label/text `"Done"`.

### password-autofill

Source: `.maestro/release_tests/password-autofill.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/shared/open_browsing_menu_item.yaml`, `.maestro/shared/delay.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site/autofill/autoprompt/0-standard-signup-form.html"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `"Password generation during signup"`.
7. Tap text `"Email"`.
8. Enter `"test@example.com"` into the currently focused field using its refreshed elementRef.
9. Tap text `"Password"`.
10. Require visible label/text `"Use a strong password from DuckDuckGo?"`.
11. Tap text `"Use Strong Password"`.
12. Tap text `"Sign up"`.
13. Require visible label/text `"Success"`.
14. Follow visible behavior from `.maestro/shared/open_browsing_menu_item.yaml` with parameters `{"ITEM": "Passwords"}`.
15. Require visible label/text `"Unlock device to access passwords"`.
16. Enter `"passcode"` into the currently focused field using its refreshed elementRef.
17. Use the exposed provider key action for `"Enter"`; inspect its schema first.
18. Require visible label/text `"Passwords"`.
19. Require visible label/text `"privacy-test-pages.site"`.
20. Require visible label/text `"test@example.com"`.
21. Tap label/text `"Close"`.
22. Require visible identifier `"searchEntry"`.
23. Tap identifier `"searchEntry"`.
24. Follow visible behavior from `.maestro/shared/delay.yaml`.
25. Enter `"https://privacy-test-pages.site/autofill/autoprompt/1-standard-login-form.html"` into the currently focused field using its refreshed elementRef.
26. Use the exposed provider key action for `"Enter"`; inspect its schema first.
27. Require visible label/text `"Use a saved password?"`.
28. Require visible label/text `"test@example.com"`.
29. Tap label/text `"test@example.com"`.
30. Require visible label/text `"Unlock device to use saved password"`.
31. Enter `"passcode"` into the currently focused field using its refreshed elementRef.
32. Use the exposed provider key action for `"Enter"`; inspect its schema first.
33. Require visible label/text `"Submitted!"`.
34. Tap identifier `"searchEntry"`.
35. Enter `"https://privacy-test-pages.site/autofill/autoprompt/3-multistep-form.html"` into the currently focused field using its refreshed elementRef.
36. Use the exposed provider key action for `"Enter"`; inspect its schema first.
37. Follow visible behavior from `.maestro/shared/delay.yaml`.
38. Require visible label/text `"Use a saved password?"`.
39. Require visible label/text `"test@example.com"`.
40. Tap label/text `"test@example.com"`.
41. Require visible label/text `"Unlock device to use saved password"`.
42. Enter `"passcode"` into the currently focused field using its refreshed elementRef.
43. Use the exposed provider key action for `"Enter"`; inspect its schema first.
44. Require visible label/text `"Password"`.
45. Tap label/text `"Password"`.
46. Require visible label/text `"Use a saved password?"`.
47. Require visible label/text `"test@example.com"`.
48. Tap label/text `"test@example.com"`.
49. Require visible label/text `"Submitted!"`.

### password-management

Source: `.maestro/release_tests/password-management.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Tap label/text `"Browsing Menu"`.
3. Tap label/text `"Settings"`.
4. Scroll toward `"DOWN"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
5. Tap label/text `"Passwords & Autofill"`.
6. Tap label/text `"Passwords"`.
7. Tap label/text `"Add 24"`.
8. Tap identifier `"Field_PasswordName"`.
9. Enter `"Netflix"` into the currently focused field using its refreshed elementRef.
10. Use the exposed provider key action for `"Enter"`; inspect its schema first.
11. Tap identifier `"Field_Username"`.
12. Enter `"test2@example.com"` into the currently focused field using its refreshed elementRef.
13. Use the exposed provider key action for `"Enter"`; inspect its schema first.
14. Tap identifier `"Field_Password"`.
15. Enter `"secure!password"` into the currently focused field using its refreshed elementRef.
16. Use the exposed provider key action for `"Enter"`; inspect its schema first.
17. Tap identifier `"Field_Address"`.
18. Enter `"netflix.com"` into the currently focused field using its refreshed elementRef.
19. Use the exposed provider key action for `"Enter"`; inspect its schema first.
20. Tap identifier `"Field_Notes"`.
21. Enter `"A subscription based streaming site."` into the currently focused field using its refreshed elementRef.
22. Tap label/text `"Save"`.
23. Tap label/text `"Passwords"`.
24. Tap label/text `"Passwords & Autofill"`.
25. Tap label/text `"Settings"`.
26. Tap label/text `"Done"`.
27. Tap label/text `"Browsing Menu"`.
28. Tap label/text `"Settings"`.
29. Scroll toward `"DOWN"` until label/text `"Passwords & Autofill"` is fully visible. Refresh the snapshot.
30. Tap label/text `"Passwords & Autofill"`.
31. Tap label/text `"Passwords"`.
32. Require visible label/text `"Unlock device to access passwords"`.
33. Enter `"passcode"` into the currently focused field using its refreshed elementRef.
34. Use the exposed provider key action for `"Enter"`; inspect its schema first.
35. Require visible label/text `"Passwords"`.
36. Require visible label/text `"Netflix"`.
37. Require visible label/text `"test2@example.com"`.
38. Tap label/text `"test2@example.com"`.
39. Require visible label/text `"Delete Password"`.
40. Require visible label/text `"Netflix"`.
41. Require visible label/text `"test2@example.com"`.
42. Require visible label/text `"A subscription based streaming site."`.
43. Require visible label/text `"•••••••••••••••"`.
44. Tap label/text `"Show Password"`.
45. Require visible label/text `"secure!password"`.
46. Tap label/text `"Hide Password"`.
47. Require visible label/text `"•••••••••••••••"`.
48. Tap label/text `"Edit"`.
49. Tap identifier `"Field_PasswordName"`.
50. Tap identifier `"Field_PasswordName"`.
51. Tap label/text `"Select All"`.
52. Enter `"Netflix Streaming"` into the currently focused field using its refreshed elementRef.
53. Use the exposed provider key action for `"Enter"`; inspect its schema first.
54. Tap identifier `"Field_Username"`.
55. Tap identifier `"Field_Username"`.
56. Tap label/text `"Select All"`.
57. Enter `"test3@example.com"` into the currently focused field using its refreshed elementRef.
58. Use the exposed provider key action for `"Enter"`; inspect its schema first.
59. Tap identifier `"Field_Password"`.
60. Tap identifier `"Field_Password"`.
61. Tap label/text `"Select All"`.
62. Enter `"secure?password"` into the currently focused field using its refreshed elementRef.
63. Use the exposed provider key action for `"Enter"`; inspect its schema first.
64. Tap identifier `"Field_Address"`.
65. Tap identifier `"Field_Address"`.
66. Tap label/text `"Select All"`.
67. Enter `"netflix.com/login"` into the currently focused field using its refreshed elementRef.
68. Use the exposed provider key action for `"Enter"`; inspect its schema first.
69. Tap identifier `"Field_Notes"`.
70. Long-press identifier `"Field_Notes"`.
71. Tap label/text `"Select All"`.
72. Enter `"A subscription site."` into the currently focused field using its refreshed elementRef.
73. Tap label/text `"Save"`.
74. Tap label/text `"Passwords"`.
75. Require visible label/text `"Passwords"`.
76. Require visible label/text `"Netflix Streaming"`.
77. Require visible label/text `"test3@example.com"`.
78. Tap label/text `"Search passwords"`.
79. Enter `"ZZZ"` into the currently focused field using its refreshed elementRef.
80. Require visible label/text `"No Results"`.
81. Require absent label/text `"Netflix Streaming"`.
82. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
83. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
84. Use the exposed provider key action for `"Backspace"`; inspect its schema first.
85. Enter `"Net"` into the currently focused field using its refreshed elementRef.
86. Require visible label/text `"N"`.
87. Require visible label/text `"Netflix Streaming"`.
88. Tap label/text `"Cancel"`.
89. Tap label/text `"test3@example.com"`.
90. Require visible label/text `"Delete Password"`.
91. Require visible label/text `"Netflix Streaming"`.
92. Require visible label/text `"test3@example.com"`.
93. Require visible label/text `"A subscription site."`.
94. Require visible label/text `"•••••••••••••••"`.
95. Tap label/text `"Show Password"`.
96. Require visible label/text `"secure?password"`.
97. Tap label/text `"Delete Password"`.
98. Require visible label/text `"Are you sure you want to delete this password?"`.
99. Tap label/text `"Delete Password"`.
100. Require visible label/text `"Passwords"`.
101. Require absent label/text `"Netflix"`.

## Gotchas

Authentication, system permission/autofill UI and simulator passcode differ by runtime. Literal Anything or 0000 in source tests are fixture assumptions, never real credentials. Do not bypass auth, alter real passwords, or assume a backend login was verified.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
