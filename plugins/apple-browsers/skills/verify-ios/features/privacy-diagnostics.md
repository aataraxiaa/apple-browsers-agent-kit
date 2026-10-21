# Content-scope experiments and fingerprinting

Exercise the debug privacy configuration override and externally visible fingerprinting values. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 11 content scope experiments setup
- 12 fingerprinting protection

## How to get to it (user POV)

Settings → Debug → Configuration URLs → Privacy Config; the source flow installs conditional-matching-experiments.json. Fingerprinting uses the Bookmarks editing UI to create a javascript bookmarklet, then loads the fingerprinting test fixture.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

For experiments replace the config URL through its UI, choose Override and visit the matching HTML fixture; assert `pass, application status`. The historical `0` indexed debug tap is ambiguous: identify its semantic target from a live snapshot/source before acting. For fingerprinting create/edit the bookmark with the exact source bookmarklet, burn the tabs, load `/privacy-protections/fingerprinting/?run`, wait for `⚠️ Please note that:`, invoke the bookmark from Bookmarks, and assert `TEST PASSED`. Remove that bookmark through Edit → chevron → Delete → Delete, confirming `No bookmarks added yet`.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**11 content scope experiments setup** — `.maestro/privacy_tests/11_content_scope_experiments_setup.yaml` (`.maestro/privacy_tests/11_content_scope_experiments_setup.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- tapOn: Browsing menu`
  - L15: `- tapOn: Settings`
  - L16: `- runFlow:; file: ../shared/open_debug_menu.yaml`
  - L20: `- tapOn:; text: "0"; index: 0`
  - L25: `- scrollUntilVisible:; element: "Configuration URLs"`
  - L27: `- tapOn: "Configuration URLs"`
  - L28: `- tapOn: "Privacy Config"`
  - L29: `- inputText: "https://privacy-test-pages.site/content-scope-scripts/infra/config/conditional-matching-experiments.json"`
  - L30: `- tapOn: "Override"`
  - L31: `- tapOn: "Debug"`
  - L32: `- tapOn: "Settings"`
  - L33: `- tapOn: "Done"`
  - L36: `- tapOn:; id: "searchEntry"`
  - L38: `- inputText: "https://privacy-test-pages.site/content-scope-scripts/infra/pages/conditional-matching-experiments.html"`
  - L39: `- pressKey: Enter`
  - L42: `- assertVisible: "pass, application status"`

**12 fingerprinting protection** — `.maestro/privacy_tests/12_fingerprinting_protection.yaml` (`.maestro/privacy_tests/12_fingerprinting_protection.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://duckduckgo.com"`
  - L17: `- pressKey: Enter`
  - L19: `- assertVisible: ".*DuckDuckGo.*"`
  - L22: `- assertVisible: "Browsing menu"`
  - L23: `- tapOn: "Browsing menu"`
  - L24: `- assertVisible: "Add Bookmark"`
  - L25: `- tapOn: "Add Bookmark"`
  - L28: `- assertVisible: "Browsing menu"`
  - L29: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Bookmarks"`
  - L33: `- assertVisible: "DuckDuckGo - Protection. Privacy. Peace of mind."`
  - L36: `- tapOn: "Edit"`
  - L37: `- assertVisible: "chevron"`
  - L38: `- tapOn: "chevron"`
  - L39: `- assertVisible: "Clear text"`
  - L40: `- tapOn: "Clear text"`
  - L41: `- inputText: "javascript:(function(){const values = {'screen.availTop': 0,'screen.availLeft': 0,'screen.availWidth': screen.width,'screen.availHeight': screen.height,'screen.colorDepth': 24,'screen.pixelDepth': 24,'window.screenY': 0,'window.screenLeft': 0,'navigator.doNotTrack': undefined};var passed = true;var reason = null;for (const test of results.results) {if (values[test.id] !== undefined) {if (values[test.id] !== test.value) {console.log(test.id, values[test.id]);reason = test.id;passed = false;break;}}}var elem = document.createElement('p');elem.innerHTML = (passed) ? 'TEST PASSED' : 'TEST FAILED: ' + reason;document.body.insertBefore(elem, document.body.childNodes[0]);}());"`
  - L42: `- tapOn: "Save"`
  - L43: `- tapOn: "Done"`
  - L44: `- tapOn: "Done"`
  - L47: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L51: `- assertVisible:; id: "searchEntry"`
  - L53: `- tapOn:; id: "searchEntry"`
  - L55: `- inputText: "https://privacy-test-pages.site/privacy-protections/fingerprinting/?run"`
  - L56: `- pressKey: Enter`
  - L59: `- extendedWaitUntil:; visible: "⚠️ Please note that:"; timeout: 10000`
  - L64: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Bookmarks"`
  - L68: `- tapOn: "DuckDuckGo - Protection. Privacy. Peace of mind."`
  - L71: `- extendedWaitUntil:; visible: "TEST PASSED"; timeout: 10000`
  - L76: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Bookmarks"`
  - L80: `- tapOn: "Edit"`
  - L81: `- tapOn: "chevron"`
  - L82: `- hideKeyboard`
  - L83: `- tapOn: "Delete"`
  - L84: `- assertVisible: "Delete?"`
  - L85: `- tapOn: "Delete"`
  - L86: `- assertVisible: "No bookmarks added yet"`
  - L87: `- tapOn: "Done"`
  - L88: `- tapOn: "Done"`
  - L91: `- runFlow:; file: ../shared/use_firebutton.yaml`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Debug/internal surfaces may require internal-user setup. Do not infer the meaning of an indexed `0` control. Copy the bookmarklet verbatim from the source; it tests screen dimensions/depth and other navigator properties. The source override persists: restore it after capture. A bookmarklet is the existing user-facing oracle, not a license to inject arbitrary scripts through another driver.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
