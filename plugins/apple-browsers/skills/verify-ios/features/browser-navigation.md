# Browser tabs, address entry and restoration

Open and switch private tabs, preserve a draft across refresh, and restore navigation history after restart. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- opening tabs
- search bar
- state restoration
- swipe tabs

## How to get to it (user POV)

Use `searchEntry` to load a URL; `Tab Switcher` → `New Tab` opens another. `Browse Back` and `Browse Forward` move through page history.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Open the new-window fixture and follow `Links Open in New Window` → `Opens in new window`; check `1 Private Tab` becomes `2 Private Tabs`. Close or back out and check the original page and count. On auto-refresh.html enter `abcd`, wait for refresh, append `efgh` and `ijkl`; the draft remains `abcdefghijkl`. For restoration build a DuckDuckGo → Terms of Service stack, go back, open example.com in another tab, stop and relaunch without clearing data; select the original tab by its current snapshot ref and verify Forward restores Terms of Service.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**opening tabs** — `.maestro/browser_features/opening_tabs.yaml` (`.maestro/browser_features/opening_tabs.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: ".*Privacy Test Pages.*"`
  - L22: `- tapOn: "Links Open in New Window"`
  - L25: `- runFlow:; file: ../shared/check_number_of_tabs.yaml; env:; TITLE: "1 Private Tab"`
  - L30: `- tapOn: "Opens in new window"`
  - L31: `- runFlow:; file: ../shared/check_number_of_tabs.yaml; env:; TITLE: "2 Private Tabs"`
  - L36: `- tapOn: "Close"`
  - L37: `- assertVisible: "A link that opens in a new window"`
  - L38: `- tapOn: "Opens in new window"`
  - L39: `- runFlow:; file: ../shared/check_number_of_tabs.yaml; env:; TITLE: "2 Private Tabs"`
  - L44: `- tapOn: "Browse Back"`
  - L45: `- assertVisible: "A link that opens in a new window"`
  - L47: `- runFlow:; file: ../shared/check_number_of_tabs.yaml; env:; TITLE: "1 Private Tab"`

**search bar** — `.maestro/browser_features/search_bar.yaml` (`.maestro/browser_features/search_bar.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/auto-refresh.html"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: "Website that refreshes every 3 seconds."`
  - L24: `- tapOn:; id: "searchEntry"`
  - L26: `- inputText: "abcd"`
  - L27: `- assertVisible: "abcd"`
  - L30: `- runFlow:; file: ../shared/delay.yaml`
  - L34: `- inputText: "efgh"`
  - L35: `- assertVisible: "abcdefgh"`
  - L38: `- runFlow:; file: ../shared/delay.yaml`
  - L41: `- inputText: "ijkl"`
  - L42: `- assertVisible: "abcdefghijkl"`

**state restoration** — `.maestro/browser_features/state_restoration.yaml` (`.maestro/browser_features/state_restoration.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://duckduckgo.com"`
  - L19: `- pressKey: Enter`
  - L22: `- assertVisible: 'DuckDuckGo.*'`
  - L23: `- scrollUntilVisible:; element: "Terms of Service"; timeout: 50000; speed: 100`
  - L27: `- tapOn:; text: 'Terms of Service'`
  - L29: `- assertVisible: "DuckDuckGo Terms of Service"`
  - L30: `- scrollUntilVisible:; element: "Privacy Policy"; timeout: 50000; speed: 100`
  - L35: `- tapOn:; point: 90%, 1%`
  - L37: `- tapOn: "Browse Back"`
  - L38: `- assertVisible: "DuckDuckGo.*"`
  - L41: `- tapOn: "Tab Switcher"`
  - L42: `- tapOn: "New Tab"`
  - L43: `- assertVisible:; id: "searchEntry"`
  - L45: `- tapOn:; id: "searchEntry"`
  - L47: `- inputText: "https://example.com"`
  - L48: `- pressKey: Enter`
  - L50: `- assertVisible: ".*Example Domain.*"`
  - L52: `- stopApp`
  - L53: `- launchApp:; arguments:; isRunningUITests: true`
  - L57: `- tapOn:; text: "Tab Switcher"; retryTapIfNoChange: true`
  - L60: `- tapOn:; point: 20%, 25%`
  - L64: `- assertVisible: "DuckDuckGo.*"`
  - L65: `- tapOn: "Browse Forward"`
  - L66: `- assertVisible: "DuckDuckGo Terms of Service"`

**swipe tabs** — `.maestro/browser_features/swipe_tabs.yaml` (`.maestro/browser_features/swipe_tabs.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://www.search-company.site"`
  - L19: `- pressKey: Enter`
  - L21: `- assertVisible: "Search engine"`
  - L24: `- tapOn: "Tab Switcher"`
  - L25: `- tapOn: "New Tab"`
  - L28: `- assertVisible:; id: "searchEntry"`
  - L30: `- tapOn:; id: "searchEntry"`
  - L32: `- inputText: "https://privacy-test-pages.site/features/favicon/"`
  - L33: `- pressKey: Enter`
  - L35: `- assertVisible: "Favicon Tests"`
  - L38: `- swipe:; start: 10%, 10%; end: 90%, 10%`
  - L42: `- assertVisible: "Search engine"`
  - L45: `- assertVisible:; id: "searchEntry"`
  - L47: `- tapOn:; id: "searchEntry"`
  - L49: `- inputText: "https://privacy-test-pages.site/features/download/"`
  - L50: `- pressKey: Enter`
  - L52: `- assertVisible: "Download PDF"`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Swipes and status-bar/tab-grid coordinate taps in the historical flow need a fresh snapshot-based alternative; never copy percentages. Relaunch must preserve app state. Network refresh and public page content are external dependencies.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
