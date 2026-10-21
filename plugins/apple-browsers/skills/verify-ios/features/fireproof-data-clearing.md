# Fire Button, fireproofing and preserved search settings

Burn tabs and data while preserving allowed site cookies and DuckDuckGo preferences, then remove protection and prove deletion. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 01 fire proofing
- 02 duckduckgo settings
- 02 fire proofing etldplus1

## How to get to it (user POV)

Browsing menu → Fireproof This Site → Fireproof; Fire Button identifier `Browser.Toolbar.Button.Fire` → `alert.forget-data.confirm`; remove via Browsing menu → Remove Fireproofing.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

On setcookie.net set TestName=TestValue, fireproof, burn twice, reload and verify cookie survived. Remove fireproofing, burn, reload and assert Received no cookies. For eTLD+1 on www.first-party.site/fireproofing/ set parent and host-only cookies. Fireproof, burn, revisit same host (both retained) then hsts.first-party.site (parent retained; host-only is host-scoped). Remove fireproofing, burn and verify No cookies found. on both hosts. In the search-settings variant set Safe search Off, burn twice, search again and assert Safe search: off.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**01 fire proofing** — `.maestro/data_clearing_tests/01_fire_proofing.yaml` (`.maestro/data_clearing_tests/01_fire_proofing.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/data_clearing_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://setcookie.net"`
  - L18: `- pressKey: Enter`
  - L19: `- runFlow:; file: ../shared/hide_daxdialogs.yaml`
  - L23: `- assertVisible: "Cookie Test"`
  - L24: `- tapOn: "Cookie name"`
  - L25: `- inputText: "TestName"`
  - L26: `- tapOn: "Cookie value"`
  - L27: `- inputText: "TestValue"`
  - L28: `- tapOn: "Done"`
  - L29: `- scrollUntilVisible:; element:; text: "Submit"`
  - L32: `- tapOn: "Submit"`
  - L35: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Fireproof This Site"`
  - L39: `- tapOn: "Fireproof"`
  - L40: `- assertVisible: "setcookie.net is now Fireproof"`
  - L43: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L46: `- runFlow:; file: ../shared/dismiss_address_bar_editing.yaml`
  - L48: `- assertVisible:; id: "searchEntry"`
  - L50: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L54: `- tapOn:; id: "searchEntry"`
  - L56: `- inputText: "https://setcookie.net"`
  - L57: `- pressKey: Enter`
  - L58: `- assertVisible: "TestName = TestValue"`
  - L61: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Remove Fireproofing"`
  - L67: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L71: `- tapOn:; id: "searchEntry"`
  - L73: `- inputText: "https://setcookie.net"`
  - L74: `- pressKey: Enter`
  - L75: `- assertVisible: "Cookie Test"`
  - L76: `- assertVisible: "Received no cookies."`

**02 duckduckgo settings** — `.maestro/data_clearing_tests/02_duckduckgo_settings.yaml` (`.maestro/data_clearing_tests/02_duckduckgo_settings.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/data_clearing_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "privacy blogs"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "Safe search"`
  - L22: `- waitForAnimationToEnd`
  - L23: `- tapOn: "Safe search"`
  - L24: `- assertVisible: "Off"`
  - L25: `- waitForAnimationToEnd`
  - L26: `- tapOn: "Off"`
  - L29: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L31: `- assertVisible:; id: "searchEntry"`
  - L34: `- runFlow:; file: ../shared/dismiss_address_bar_editing.yaml`
  - L36: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L40: `- tapOn:; id: "searchEntry"`
  - L42: `- inputText: "creepy trackers"`
  - L43: `- pressKey: Enter`
  - L44: `- assertVisible: "Safe search: off"`

**02 fire proofing etldplus1** — `.maestro/data_clearing_tests/02_fire_proofing_etldplus1.yaml` (`.maestro/data_clearing_tests/02_fire_proofing_etldplus1.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/data_clearing_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.first-party.site/fireproofing/"`
  - L18: `- pressKey: Enter`
  - L19: `- runFlow:; file: ../shared/hide_daxdialogs.yaml`
  - L23: `- assertVisible: "Fireproofing Cookie Test"`
  - L24: `- tapOn: "Set Parent Cookie"`
  - L25: `- assertVisible: ".*ddg_fireproof_test=fireproofed.*"`
  - L26: `- tapOn: "Set Host-Only Cookie"`
  - L27: `- assertVisible: ".*ddg_fireproof_host_test=fireproofed.*"`
  - L30: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Fireproof This Site"`
  - L34: `- tapOn: "Fireproof"`
  - L35: `- assertVisible: "first-party\\.site is now Fireproof"`
  - L38: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L43: `- tapOn:; id: "searchEntry"`
  - L45: `- inputText: "https://www.first-party.site/fireproofing/"`
  - L46: `- pressKey: Enter`
  - L47: `- assertVisible: "Fireproofing Cookie Test"`
  - L48: `- assertVisible: ".*ddg_fireproof_test=fireproofed.*"`
  - L49: `- assertVisible: ".*ddg_fireproof_host_test=fireproofed.*"`
  - L54: `- tapOn:; id: "searchEntry"`
  - L56: `- inputText: "https://hsts.first-party.site/fireproofing/"`
  - L57: `- pressKey: Enter`
  - L58: `- assertVisible: "Fireproofing Cookie Test"`
  - L59: `- assertVisible: ".*ddg_fireproof_test=fireproofed.*"`
  - L62: `- runFlow:; file: ../shared/open_browsing_menu_item.yaml; env:; ITEM: "Remove Fireproofing"`
  - L68: `- runFlow:; file: ../shared/use_firebutton.yaml`
  - L72: `- tapOn:; id: "searchEntry"`
  - L74: `- inputText: "https://www.first-party.site/fireproofing/"`
  - L75: `- pressKey: Enter`
  - L76: `- assertVisible: "Fireproofing Cookie Test"`
  - L77: `- assertVisible: "No cookies found\\."`
  - L80: `- tapOn:; id: "searchEntry"`
  - L82: `- inputText: "https://hsts.first-party.site/fireproofing/"`
  - L83: `- pressKey: Enter`
  - L84: `- assertVisible: "Fireproofing Cookie Test"`
  - L85: `- assertVisible: "No cookies found\\."`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Run exclusively in the designated disposable app state: Fire Button deletes browsing data. Dismiss focused address editing via actual Cancel/Back before the second burn. Host-only absence on sibling domains is cookie scoping, not data loss. Settings persistence and website cookie persistence are separate assertions.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
