# Bookmarks, favorites and folders

Save, edit, organize and delete bookmarks and favorites, including Bookmark All Tabs. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- bookmarks-multi
- bookmarks
- favorites

## How to get to it (user POV)

Browsing menu → Add Bookmark / Add Favorite, then Browsing menu → Bookmarks; tab switcher Edit → Select Tabs → More Menu → Bookmark All Tabs is the bulk entry.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Create entries through the user menu, reopen from Bookmarks to prove destination, edit title/address/folder and reopen again. Follow the single/bookmark and favorite scenarios below for context-menu and delete assertions. Bulk: create five tabs, Bookmark All Tabs → Bookmark 5 tabs? → Bookmark. In Bookmarks create Examples via Add Folder → Save; edit/move four fixture entries using chevron → Examples → Save. Remove Examples → Delete must ask Delete Examples? and describe four items; confirm and check No bookmarks added yet.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**bookmarks-multi** — `.maestro/release_tests/bookmarks-multi.yaml` (`.maestro/release_tests/bookmarks-multi.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/release_tests`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: ".*Privacy Test Pages.*"`
  - L24: `- evalScript: ${output.counter = 0}`
  - L25: `- repeat:; while:; true: ${output.counter < 4}; commands:; - assertVisible:; id: "searchEntry"; - tapOn:; id: "searchEntry"; - inputText: ${ 'https://privacy-test-pages.site/' + output.counter }; - pressKey: Enter; - assertVisible: ${ 'Cannot GET /' + output.counter }; - tapOn: "Tab Switcher"; - tapOn: "New Tab"; - evalScript: ${output.counter += 1}`
  - L40: `- runFlow:; file: ../shared/dismiss_address_bar_editing.yaml`
  - L42: `- tapOn: "Tab Switcher"`
  - L43: `- tapOn: "Edit"`
  - L44: `- tapOn: "Select Tabs"`
  - L45: `- tapOn: "More Menu"`
  - L46: `- tapOn: "Bookmark All Tabs"`
  - L48: `- assertVisible: "Bookmark 5 tabs?"`
  - L49: `- tapOn: "Bookmark"`
  - L50: `- tapOn: "Done"`
  - L51: `- tapOn: "Done"`
  - L53: `- assertVisible: "Bookmarks"`
  - L54: `- tapOn: "Bookmarks"`
  - L56: `- tapOn: "Add Folder"`
  - L57: `- inputText: "Examples"`
  - L58: `- tapOn: "Save"`
  - L60: `- tapOn: "Edit"`
  - L62: `- evalScript: ${output.counter = 0}`
  - L63: `- repeat:; while:; true: ${output.counter < 4}; commands:; - tapOn: "chevron"; - tapOn: "Examples"; - tapOn: "Save"; - evalScript: ${output.counter += 1}`
  - L72: `- assertVisible: "Done"`
  - L73: `- tapOn: "Done"`
  - L74: `- assertNotVisible: "Example"`
  - L75: `- assertVisible: "Examples"`
  - L76: `- tapOn: "Edit"`
  - L77: `- assertVisible: "Remove Examples"`
  - L78: `- tapOn: "Remove Examples"`
  - L79: `- tapOn: "Delete"`
  - L80: `- assertVisible: "Delete Examples?"`
  - L81: `- assertVisible: "Are you sure you want to delete this folder and 4 items?"`
  - L82: `- tapOn: "Delete"`
  - L83: `- tapOn: "Done"`
  - L84: `- assertVisible: "No bookmarks added yet"`

**bookmarks** — `.maestro/release_tests/bookmarks.yaml` (`.maestro/release_tests/bookmarks.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/release_tests`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: ".*Privacy Test Pages.*"`
  - L24: `- assertVisible: "Browsing menu"`
  - L25: `- tapOn: "Browsing menu"`
  - L26: `- assertVisible: "Add Bookmark"`
  - L27: `- tapOn: "Add Bookmark"`
  - L30: `- tapOn: "Tab Switcher"`
  - L31: `- tapOn: "New Tab"`
  - L32: `- assertVisible:; id: "searchEntry"`
  - L34: `- tapOn:; id: "searchEntry"`
  - L36: `- inputText: "pri"`
  - L37: `- assertVisible: "Privacy Test Pages - Home"`
  - L38: `- assertVisible: "privacy-test-pages.site"`
  - L39: `- tapOn: "Privacy Test Pages - Home"`
  - L40: `- runFlow: ../shared/pull_to_refresh.yaml`
  - L43: `- assertVisible: "Browsing menu"`
  - L44: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Bookmarks"`
  - L48: `- assertVisible: "Privacy Test Pages - Home"`
  - L51: `- assertVisible: "Edit"`
  - L52: `- tapOn: "Edit"`
  - L53: `- tapOn: "chevron"`
  - L54: `- assertVisible: "Add Folder"`
  - L57: `- tapOn: "Add Folder"`
  - L58: `- assertVisible: "Add Folder"`
  - L59: `- assertVisible: "Save"`
  - L60: `- assertVisible: "Bookmarks"`
  - L61: `- assertVisible: "Title"`
  - L62: `- tapOn: "Title"`
  - L63: `- inputText: "Test Folder"`
  - L64: `- tapOn: "Save"`
  - L65: `- assertVisible: "Edit Bookmark"`
  - L66: `- assertVisible: "Add Folder"`
  - L67: `- assertVisible: "Test Folder"`
  - L68: `- tapOn: "Save"`
  - L69: `- tapOn: "Done"`
  - L70: `- assertNotVisible: "Remove Privacy Test Pages - Home"`
  - L71: `- assertVisible: "Test Folder"`
  - L72: `- tapOn: "Test Folder"`
  - L73: `- assertVisible: "Privacy Test Pages - Home"`
  - L76: `- assertVisible: "Edit"`
  - L77: `- tapOn: "Edit"`
  - L78: `- tapOn: "chevron"`
  - L79: `- assertVisible: "Add Folder"`
  - L81: `- tapOn: "Add Folder"`
  - L82: `- assertVisible: "Add Folder"`
  - L83: `- assertVisible: "Save"`
  - L84: `- assertVisible: "Bookmarks"`
  - L85: `- assertVisible: "Title"`
  - L86: `- tapOn: "Title"`
  - L87: `- inputText: "Test Folder 2"`
  - L88: `- tapOn: "Save"`
  - L89: `- assertVisible: "Edit Bookmark"`
  - L90: `- assertVisible: "Add Folder"`
  - L91: `- assertVisible: "Test Folder"`
  - L92: `- tapOn: "Save"`
  - L93: `- tapOn: "Done"`
  - L94: `- assertNotVisible: "Remove Privacy Test Pages - Home"`
  - L95: `- assertVisible: "Test Folder"`
  - L96: `- tapOn: "Test Folder"`
  - L97: `- assertVisible: "Test Folder 2"`
  - L98: `- tapOn: "Test Folder 2"`
  - L101: `- tapOn: "Edit"`
  - L102: `- tapOn: "chevron"`
  - L103: `- hideKeyboard`
  - L104: `- assertVisible: "Delete"`
  - L105: `- tapOn: "Delete"`
  - L106: `- assertVisible: "Delete?"`
  - L107: `- tapOn: "Delete"`
  - L110: `- assertNotVisible: "Privacy Test Pages - Home"`
  - L111: `- assertVisible: "Test Folder 2"`
  - L112: `- assertVisible: "Test Folder"`
  - L113: `- tapOn: "Test Folder"`
  - L114: `- assertNotVisible: "Privacy Test Pages - Home"`
  - L115: `- assertVisible: "Bookmarks"`
  - L116: `- tapOn: "Bookmarks"`
  - L119: `- tapOn: "Edit"`
  - L120: `- assertVisible: "Remove Test Folder"`
  - L121: `- tapOn: "Remove Test Folder"`
  - L122: `- assertVisible: "Delete"`
  - L123: `- tapOn: "Delete"`
  - L124: `- assertVisible: "Delete Test Folder?"`
  - L125: `- tapOn: "Delete"`
  - L126: `- assertVisible: "No bookmarks added yet"`
  - L127: `- tapOn: "Done"`
  - L128: `- tapOn: "Done"`

**favorites** — `.maestro/release_tests/favorites.yaml` (`.maestro/release_tests/favorites.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/release_tests`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: ".*Privacy Test Pages.*"`
  - L24: `- assertVisible: "Browsing menu"`
  - L25: `- tapOn: "Browsing menu"`
  - L26: `- assertVisible: "Add Favorite"`
  - L27: `- tapOn: "Add Favorite"`
  - L30: `- assertVisible: "Browsing menu"`
  - L31: `- tapOn: "Browsing menu"`
  - L32: `- assertVisible: "Remove Favorite"`
  - L33: `- tapOn: "Remove Favorite"`
  - L36: `- assertVisible: "Browsing menu"`
  - L37: `- tapOn: "Browsing menu"`
  - L38: `- assertVisible: "Add Favorite"`
  - L39: `- tapOn: "Add Favorite"`
  - L42: `- tapOn: "Tab Switcher"`
  - L43: `- tapOn: "New Tab"`
  - L44: `- assertVisible: "Privacy Test Pages - Home"`
  - L45: `- tapOn: "Privacy Test Pages - Home"`
  - L46: `- assertVisible: "privacy-test-pages.site"`
  - L47: `- tapOn:; id: "searchEntry"`
  - L49: `- inputText: "pri"`
  - L52: `- assertVisible:; id: "Autocomplete.Suggestions.ListItem.Favorite-pri.*"`
  - L54: `- runFlow:; file: ../shared/dismiss_address_bar_editing.yaml`
  - L58: `- assertVisible: "Browsing menu"`
  - L59: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Bookmarks"`
  - L63: `- assertVisible: "Privacy Test Pages - Home"`
  - L66: `- assertVisible: "Edit"`
  - L67: `- tapOn: "Edit"`
  - L68: `- assertVisible: "Privacy Test Pages - Home"`
  - L69: `- assertVisible: "Remove Privacy Test Pages - Home"`
  - L70: `- tapOn: "Remove Privacy Test Pages - Home"`
  - L71: `- assertVisible:; text: "Delete"; index: 0`
  - L74: `- tapOn:; text: "Delete"; index: 0`
  - L79: `- assertNotVisible: "Privacy Test Pages - Home"`
  - L80: `- assertVisible: "No bookmarks added yet"`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Use unique fixtures in a disposable profile. Empty-state assertions require removing every created fixture, including initial saved page. Indexed chevron controls require matching their associated row in the current snapshot. Shared sync_verify_bookmarks references are mapping aids; no account sync execution is authorized here.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
