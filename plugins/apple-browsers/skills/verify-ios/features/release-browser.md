# Release browsing, tabs and lifecycle

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `backbutton-close-tab` — `.maestro/release_tests/backbutton-close-tab.yaml`.
- `backgrounding` — `.maestro/release_tests/backgrounding.yaml`.
- `browsing` — `.maestro/release_tests/browsing.yaml`.
- `refresh` — `.maestro/release_tests/refresh.yaml`.
- `tab-switcher-selection` — `.maestro/release_tests/tab-switcher-selection.yaml`.
- `tabs` — `.maestro/release_tests/tabs.yaml`.
- `tabswitcher` — `.maestro/release_tests/tabswitcher.yaml`.
- `widgets` — `.maestro/release_tests/widgets.yaml`.

## How to get to it (user POV)

Begin on the browser NTP, enter the scenario URL into searchEntry, and use visible browser controls or tab switcher. Follow each source recipe for tab counts, Back, refresh, background/resume and persisted state.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### backbutton-close-tab

Source: `.maestro/release_tests/backbutton-close-tab.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Require visible label/text `"Tab Switcher"`.
8. Tap label/text `"Tab Switcher"`.
9. Require visible label/text `".*Privacy Test Pages.*"`.
10. Require visible label/text `"New Tab"`.
11. Tap label/text `"New Tab"`.
12. Require visible identifier `"searchEntry"`.
13. Tap identifier `"searchEntry"`.
14. Enter `"https://www.search-company.site"` into the currently focused field using its refreshed elementRef.
15. Use the exposed provider key action for `"Enter"`; inspect its schema first.
16. Require visible label/text `"Search engine"`.
17. Require visible label/text `"Tab Switcher"`.
18. Tap label/text `"Tab Switcher"`.
19. Require visible label/text `".*Privacy Test Pages.*"`.
20. Require visible label/text `".*Ad Click Flow.*"`.
21. Require visible label/text `"2 Private Tabs"`.
22. Tap label/text `"Open \"Privacy Test Pages - Home\" at privacy-test-pages.site"`.
23. Require absent label/text `".*Ad Click Flow.*"`.
24. Require visible label/text `".*Privacy Test Pages.*"`.
25. Read dependency `"../shared/pull_to_refresh.yaml"`.
26. Long-press label/text `"• 1 major tracker loaded via script"`.
27. Tap label/text `"Open In New Tab"`.
28. Tap label/text `"Browse Back"`.
29. Require visible label/text `".*Privacy Test Pages.*"`.

### backgrounding

Source: `.maestro/release_tests/backgrounding.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/shared/dismiss_address_bar_editing.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Use the exposed provider key action for `"Home"`; inspect its schema first.
8. Gesture intent `{"start": "50%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
9. Gesture intent `{"start": "10%, 50%", "end": "50%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
10. Tap label/text `"DuckDuckGo"`.
11. Require visible label/text `"Privacy Test Pages"`.
12. Require visible label/text `"Browsing menu"`.
13. Tap label/text `"Browsing menu"`.
14. Require visible label/text `"Add Bookmark"`.
15. Tap label/text `"Add Bookmark"`.
16. Tap label/text `"Privacy Icon"`.
17. Require visible label/text `"Protections are ON for this site"`.
18. Tap label/text `"Done"`.
19. Require visible label/text `"Tab Switcher"`.
20. Tap label/text `"Tab Switcher"`.
21. Tap label/text `"New Tab"`.
22. Use the exposed provider key action for `"Home"`; inspect its schema first.
23. Gesture intent `{"start": "50%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
24. Gesture intent `{"start": "10%, 50%", "end": "50%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
25. Tap label/text `"DuckDuckGo"`.
26. Follow visible behavior from `.maestro/shared/dismiss_address_bar_editing.yaml`.
27. Tap label/text `"Browsing menu"`.
28. Tap label/text `"Settings"`.
29. Require visible identifier `"Settings.ListItem.Field_DefaultBrowser"`.
30. Tap label/text `"Done"`.
31. Require visible label/text `"Bookmarks"`.
32. Tap label/text `"Bookmarks"`.
33. Require visible label/text `"Privacy Test Pages - Home"`.
34. Tap label/text `"Done"`.
35. Require visible label/text `"Tab Switcher"`.
36. Tap label/text `"Tab Switcher"`.

### browsing

Source: `.maestro/release_tests/browsing.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.

### refresh

Source: `.maestro/release_tests/refresh.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require absent label/text `"Refresh Page"`.
3. Require visible identifier `"searchEntry"`.
4. Tap identifier `"searchEntry"`.
5. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
6. Use the exposed provider key action for `"Enter"`; inspect its schema first.
7. Require visible label/text `".*Privacy Test Pages.*"`.
8. Require visible label/text `"Refresh Page"`.
9. Tap label/text `"Refresh Page"`.

### tab-switcher-selection

Source: `.maestro/release_tests/tab-switcher-selection.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Read dependency `"../shared/pull_to_refresh.yaml"`.
8. Require visible label/text `"Tab Switcher"`.
9. Tap label/text `"Tab Switcher"`.
10. Tap label/text `"New Tab"`.
11. Require visible identifier `"searchEntry"`.
12. Tap identifier `"searchEntry"`.
13. Enter `"https://www.search-company.site"` into the currently focused field using its refreshed elementRef.
14. Use the exposed provider key action for `"Enter"`; inspect its schema first.
15. Require visible label/text `".*Search engine.*"`.
16. Read dependency `"../shared/pull_to_refresh.yaml"`.
17. Require visible label/text `"Tab Switcher"`.
18. Tap label/text `"Tab Switcher"`.
19. Require visible label/text `"2 Private Tabs"`.
20. Tap label/text `"Edit"`.
21. Tap label/text `"Select Tabs"`.
22. Require visible label/text `"2 Private Tabs"`.
23. Require visible label/text `"Select All"`.
24. Tap label/text `"Select All"`.
25. Require visible label/text `"2 Selected"`.
26. Require visible label/text `"Deselect All"`.
27. Tap label/text `"Deselect All"`.
28. Require visible label/text `"2 Private Tabs"`.
29. Require visible label/text `"Select All"`.
30. Tap label/text `".*Privacy Test Pages.*"`.
31. Require visible label/text `"1 Selected"`.
32. Tap label/text `"More Menu"`.
33. Tap label/text `"Close Tab"`.
34. Require visible label/text `"Close Tab?"`.
35. Tap label/text `"Close Tab"`.
36. Require visible label/text `"1 Private Tab"`.
37. Tap label/text `"Done"`.
38. Long-press label/text `"Open \"Ad Click Flow\" at www.search-company.site"`.
39. Require visible label/text `"Select Tab"`.
40. Tap label/text `"Select Tab"`.
41. Require visible label/text `"1 Selected"`.
42. Tap label/text `"Done"`.

### tabs

Source: `.maestro/release_tests/tabs.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Require visible label/text `"Tab Switcher"`.
8. Tap label/text `"Tab Switcher"`.
9. Require visible label/text `".*Privacy Test Pages.*"`.
10. Require visible label/text `"New Tab"`.
11. Tap label/text `"New Tab"`.
12. Require visible identifier `"searchEntry"`.
13. Tap identifier `"searchEntry"`.
14. Enter `"https://www.search-company.site"` into the currently focused field using its refreshed elementRef.
15. Use the exposed provider key action for `"Enter"`; inspect its schema first.
16. Require visible label/text `"Search engine"`.
17. Require visible label/text `"Tab Switcher"`.
18. Tap label/text `"Tab Switcher"`.
19. Require visible label/text `".*Privacy Test Pages.*"`.
20. Require visible label/text `".*Ad Click Flow.*"`.
21. Require visible label/text `"2 Private Tabs"`.
22. Tap label/text `"Open \"Privacy Test Pages - Home\" at privacy-test-pages.site"`.
23. Require absent label/text `".*Ad Click Flow.*"`.
24. Require visible label/text `".*Privacy Test Pages.*"`.
25. Read dependency `"../shared/pull_to_refresh.yaml"`.
26. Require visible identifier `"searchEntry"`.
27. Tap identifier `"searchEntry"`.
28. Enter `"ad click"` into the currently focused field using its refreshed elementRef.
29. Require visible label/text `"Switch to Tab.*search-company.site"`.
30. Tap label/text `"Switch to Tab.*search-company.site"`.
31. Require visible label/text `".*Ad Click Flow.*"`.
32. Tap identifier `"searchEntry"`.
33. Enter `"privacy"` into the currently focused field using its refreshed elementRef.
34. Require visible label/text `"Switch to Tab.*privacy-test-pages.site"`.
35. Tap label/text `"Switch to Tab.*privacy-test-pages.site"`.
36. Require visible label/text `".*Privacy Test Pages.*"`.
37. Read dependency `"../shared/pull_to_refresh.yaml"`.
38. Require visible label/text `"Tab Switcher"`.
39. Tap label/text `"Tab Switcher"`.
40. Require visible label/text `".*Privacy Test Pages.*"`.
41. Require visible label/text `".*Ad Click Flow.*"`.
42. Require visible label/text `"2 Private Tabs"`.
43. Require visible label/text `"Close \"Ad Click Flow\" at www.search-company.site"`.
44. Tap label/text `"Close \"Ad Click Flow\" at www.search-company.site"`.
45. Require absent label/text `".*Ad Click Flow.*"`.
46. Require visible label/text `"1 Private Tab"`.
47. Tap label/text `"Done"`.
48. Read dependency `"../shared/pull_to_refresh.yaml"`.
49. Require visible label/text `"Tab Switcher"`.
50. Tap label/text `"Tab Switcher"`.
51. Require visible label/text `".*Privacy Test Pages.*"`.
52. Require visible label/text `"New Tab"`.
53. Tap label/text `"New Tab"`.
54. Require visible identifier `"searchEntry"`.
55. Tap identifier `"searchEntry"`.
56. Enter `"privacy"` into the currently focused field using its refreshed elementRef.
57. Require visible label/text `"Switch to Tab.*privacy-test-pages.site"`.
58. Tap label/text `"Switch to Tab.*privacy-test-pages.site"`.
59. Require visible label/text `".*Privacy Test Pages.*"`.
60. Read dependency `"../shared/pull_to_refresh.yaml"`.
61. Require visible label/text `"Tab Switcher"`.
62. Tap label/text `"Tab Switcher"`.
63. Require visible label/text `"1 Private Tab"`.

### tabswitcher

Source: `.maestro/release_tests/tabswitcher.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/shared/open_browsing_menu_item.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Require visible label/text `"Tab Switcher"`.
8. Tap label/text `"Tab Switcher"`.
9. Require visible label/text `".*Privacy Test Pages.*"`.
10. Require visible label/text `"New Tab"`.
11. Tap label/text `"New Tab"`.
12. Require visible identifier `"searchEntry"`.
13. Tap identifier `"searchEntry"`.
14. Enter `"https://www.search-company.site"` into the currently focused field using its refreshed elementRef.
15. Use the exposed provider key action for `"Enter"`; inspect its schema first.
16. Require visible label/text `"Search engine"`.
17. Require visible label/text `"Tab Switcher"`.
18. Tap label/text `"Tab Switcher"`.
19. Tap label/text `"Edit"`.
20. Tap label/text `"Select Tabs"`.
21. Tap label/text `"More Menu"`.
22. Tap label/text `"Bookmark All Tabs"`.
23. Require visible label/text `"Bookmark 2 tabs?"`.
24. Tap label/text `"Bookmark"`.
25. Tap label/text `"Done"`.
26. Tap label/text `"Switch to list view"`.
27. Tap label/text `"Switch to grid view"`.
28. Tap label/text `"Done"`.
29. Follow visible behavior from `.maestro/shared/open_browsing_menu_item.yaml` with parameters `{"ITEM": "Bookmarks"}`.
30. Require visible label/text `"Privacy Test Pages - Home"`.
31. Require visible label/text `"Ad Click Flow"`.

### widgets

Source: `.maestro/release_tests/widgets.yaml`. Tags: `[]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://privacy-test-pages.site/"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible label/text `".*Privacy Test Pages.*"`.
7. Use the exposed provider key action for `"HOME"`; inspect its schema first.
8. Gesture intent `{"start": "5%, 70%", "end": "95%, 70%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
9. Long-press point `"50%,50%"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
10. Tap label/text `"Edit"`.
11. Tap label/text `"Add Widget"`.
12. Tap label/text `"Search Widgets"`.
13. Enter `"DuckDuckGo"` into the currently focused field using its refreshed elementRef.
14. Tap point `"30%,30%"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
15. Tap label/text `" Add Widget"`.
16. Tap label/text `"Done"`.
17. Tap label/text `"DuckDuckGo"`.
18. Enter `"example.com"` into the currently focused field using its refreshed elementRef.
19. Use the exposed provider key action for `"Enter"`; inspect its schema first.
20. Require visible label/text `"Example Domain"`.
21. Require visible label/text `"Tab Switcher"`.
22. Tap label/text `"Tab Switcher"`.
23. Require visible label/text `"Open \"Privacy Test Pages - Home\" at privacy-test-pages.site"`.
24. Use the exposed provider key action for `"HOME"`; inspect its schema first.
25. Long-press point `"50%,50%"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
26. Tap label/text `"Edit"`.
27. Tap label/text `"Add Widget"`.
28. Tap label/text `"Search Widgets"`.
29. Enter `"DuckDuckGo"` into the currently focused field using its refreshed elementRef.
30. Tap point `"30%,30%"`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
31. Require visible label/text `"Search"`.
32. Gesture intent `{"start": "90%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
33. Require visible label/text `"Search Passwords"`.
34. Gesture intent `{"start": "90%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
35. Require visible label/text `"Search and Favorites"`.
36. Gesture intent `{"start": "90%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
37. Require visible label/text `"Search and Favorites"`.
38. Gesture intent `{"start": "90%, 50%", "end": "10%, 50%"}`; use only an exposed supported provider action and current snapshot targets; coordinate hints are not stable selectors.
39. Require visible label/text `"VPN"`.

## Gotchas

Remote sites may change. System HOME, widget gestures and coordinate-only selectors are intent references: inspect exposed MobileBuildMCP tools and current elementRefs; report unsupported controls rather than substitute shell automation. A wildcard .* oracle is too weak to prove the destination.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
