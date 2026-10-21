# Address bar spoof and redirect defense

Keep displayed origin aligned with committed content during hostile navigation, downloads, application schemes and redirect chains. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 1 - AddressBarSpoof, basicauth
- 2 - AddressBarSpoof, aboutblank
- 3 - AddressBarSpoof, appschemes
- 4 - AddressBarSpoof, b64 html
- 5 - AddressBarSpoof, downloadpath
- 6 - AddressBarSpoof, formaction
- 7 - AddressBarSpoof, pagerewrite
- 8 - AddressBarSpoof, redirect filtering

## How to get to it (user POV)

Load each `/security/address-bar-spoofing/` fixture below through `searchEntry`, then choose the fixture’s `Start` or `run` control.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Read the rendered value of `searchEntry` from snapshots after each action. Basicauth Unicode 2028/2029/whitespace cases must not begin with google.com. about:blank rewrite must show Not DDG. content while the address reads about:blank. Application/unsupported schemes: Cancel external-app prompt; address stays privacy-test-pages.site and spoofed content must be absent where asserted. Base64 HTML and page rewrite keep privacy-test-pages.site. JS download cancellation and Save to Downloads both use about:blank. Form action lands at duckduckgo.com without Not DDG. For cross-origin redirect capture snapshots during the three-second delay (no first-party.site flash) and after commit, Back and Forward (privacy-test-pages origin).

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**1 - AddressBarSpoof, basicauth** — `.maestro/security_tests/1_-_AddressBarSpoof,_basicauth.yaml` (`.maestro/security_tests/1_-_AddressBarSpoof,_basicauth.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-basicauth-2028.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "run"`
  - L21: `- assertVisible: "Example Domain"`
  - L22: `- copyTextFrom:; id: "searchEntry"`
  - L24: `- assertTrue: ${maestro.copiedText.indexOf("google.com") != 0}`
  - L25: `- tapOn:; id: "searchEntry"`
  - L28: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-basicauth-2029.html"`
  - L29: `- pressKey: Enter`
  - L30: `- tapOn: "run"`
  - L31: `- assertVisible: "Example Domain"`
  - L32: `- copyTextFrom:; id: "searchEntry"`
  - L34: `- assertTrue: ${maestro.copiedText.indexOf("google.com") != 0}`
  - L35: `- tapOn:; id: "searchEntry"`
  - L38: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-basicauth-whitespace.html"`
  - L39: `- pressKey: Enter`
  - L40: `- tapOn: "run"`
  - L41: `- assertVisible: "Example Domain"`
  - L42: `- copyTextFrom:; id: "searchEntry"`
  - L44: `- assertTrue: ${maestro.copiedText.indexOf("google.com") != 0}`

**2 - AddressBarSpoof, aboutblank** — `.maestro/security_tests/2_-_AddressBarSpoof,_aboutblank.yaml` (`.maestro/security_tests/2_-_AddressBarSpoof,_aboutblank.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-about-blank-rewrite.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "Start"`
  - L22: `- extendedWaitUntil:; visible: "Not DDG."  # Spoofed content is visible; timeout: 10000`
  - L25: `- copyTextFrom:; id: "searchEntry"`
  - L27: `- assertTrue: ${maestro.copiedText == "about:blank"}`

**3 - AddressBarSpoof, appschemes** — `.maestro/security_tests/3_-_AddressBarSpoof,_appschemes.yaml` (`.maestro/security_tests/3_-_AddressBarSpoof,_appschemes.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-application-scheme.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "Start"`
  - L22: `- assertVisible: "Cancel"`
  - L23: `- tapOn: "Cancel"`
  - L24: `- copyTextFrom:; id: "searchEntry"`
  - L26: `- assertTrue: ${maestro.copiedText == "privacy-test-pages.site"}`
  - L27: `- assertNotVisible: "Not DDG." # HTML content shouldn't be spoofed.`
  - L28: `- tapOn:; id: "searchEntry"`
  - L31: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-unsupported-scheme.html"`
  - L32: `- pressKey: Enter`
  - L33: `- tapOn: "Start"`
  - L35: `- assertVisible: "Cancel"`
  - L36: `- tapOn: "Cancel"`
  - L37: `- copyTextFrom:; id: "searchEntry"`
  - L39: `- assertTrue: ${maestro.copiedText == "privacy-test-pages.site"}`

**4 - AddressBarSpoof, b64 html** — `.maestro/security_tests/4_-_AddressBarSpoof,_b64_html.yaml` (`.maestro/security_tests/4_-_AddressBarSpoof,_b64_html.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-open-b64-html.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "Start"`
  - L23: `- extendedWaitUntil:; visible:; id: "searchEntry"; text: "privacy-test-pages.site"; timeout: 10000`
  - L28: `- copyTextFrom:; id: "searchEntry"`
  - L30: `- assertTrue: ${maestro.copiedText == "privacy-test-pages.site"}`

**5 - AddressBarSpoof, downloadpath** — `.maestro/security_tests/5_-_AddressBarSpoof,_downloadpath.yaml` (`.maestro/security_tests/5_-_AddressBarSpoof,_downloadpath.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-js-download-url.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "Start"`
  - L22: `- runFlow:; when:; visible: "Cancel"; commands:; - tapOn: "Cancel"`
  - L27: `- copyTextFrom:; id: "searchEntry"`
  - L29: `- assertTrue: ${maestro.copiedText == "about:blank"} # Downloads should occur in empty origin.`
  - L30: `- tapOn:; id: "searchEntry"`
  - L32: `- pressKey: Backspace`
  - L33: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-js-download-url.html"`
  - L34: `- pressKey: Enter`
  - L35: `- tapOn: "Start"`
  - L37: `- runFlow:; when:; visible: "Save to Downloads"; commands:; - tapOn: "Save to Downloads"`
  - L42: `- copyTextFrom:; id: "searchEntry"`
  - L44: `- assertTrue: ${maestro.copiedText == "about:blank"} # Downloads should occur in empty origin.`
  - L46: `- tapOn:; id: "searchEntry"`
  - L48: `- pressKey: Backspace`
  - L49: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-js-download-url.html"`
  - L50: `- pressKey: Enter`

**6 - AddressBarSpoof, formaction** — `.maestro/security_tests/6_-_AddressBarSpoof,_formaction.yaml` (`.maestro/security_tests/6_-_AddressBarSpoof,_formaction.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-form-action.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "run"`
  - L22: `- extendedWaitUntil:; visible:; id: "searchEntry"; text: "duckduckgo.com"; timeout: 10000`
  - L27: `- copyTextFrom:; id: "searchEntry"`
  - L29: `- assertTrue: ${maestro.copiedText == "duckduckgo.com"}`
  - L30: `- assertNotVisible: "Not DDG."`

**7 - AddressBarSpoof, pagerewrite** — `.maestro/security_tests/7_-_AddressBarSpoof,_pagerewrite.yaml` (`.maestro/security_tests/7_-_AddressBarSpoof,_pagerewrite.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/spoof-js-page-rewrite.html"`
  - L17: `- pressKey: Enter`
  - L20: `- tapOn: "Start"`
  - L23: `- extendedWaitUntil:; visible:; id: "searchEntry"; text: "privacy-test-pages.site"; timeout: 10000`
  - L28: `- copyTextFrom:; id: "searchEntry"`
  - L30: `- assertTrue: ${maestro.copiedText == "privacy-test-pages.site"}`

**8 - AddressBarSpoof, redirect filtering** — `.maestro/security_tests/8_-_AddressBarSpoof,_redirect_filtering.yaml` (`.maestro/security_tests/8_-_AddressBarSpoof,_redirect_filtering.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/security_tests`; read each helper before driving.

  - L8: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L14: `- tapOn:; id: "searchEntry"`
  - L16: `- inputText: "https://privacy-test-pages.site/security/address-bar-spoofing/index.html"`
  - L17: `- pressKey: Enter`
  - L18: `- assertVisible: "Address Bar Spoofing Pages"`
  - L19: `- copyTextFrom:; id: "searchEntry"`
  - L21: `- assertTrue: ${maestro.copiedText.indexOf("privacy-test-pages") != -1}`
  - L26: `- tapOn: "Redirect Chain (cross-origin, 3s delay)"`
  - L27: `- copyTextFrom:; id: "searchEntry"`
  - L29: `- assertTrue: ${maestro.copiedText.indexOf("first-party") == -1}`
  - L31: `- runFlow:; file: ../shared/delay.yaml`
  - L33: `- copyTextFrom:; id: "searchEntry"`
  - L35: `- assertTrue: ${maestro.copiedText.indexOf("privacy-test-pages") != -1}`
  - L38: `- tapOn: "Browse Back"`
  - L39: `- assertVisible: "Address Bar Spoofing Pages"`
  - L40: `- copyTextFrom:; id: "searchEntry"`
  - L42: `- assertTrue: ${maestro.copiedText.indexOf("privacy-test-pages") != -1}`
  - L45: `- tapOn: "Browse Forward"`
  - L46: `- runFlow:; file: ../shared/delay.yaml`
  - L48: `- copyTextFrom:; id: "searchEntry"`
  - L50: `- assertTrue: ${maestro.copiedText.indexOf("privacy-test-pages") != -1}`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

A final screenshot cannot prove no transient origin flash. Capture the delay window; if snapshot timing cannot establish it, mark that assertion unverified. copyTextFrom and Maestro expressions are historical oracles: obtain current UI values through MobileBuildMCP snapshot data; do not claim a copied value that was not observed. Only cancel external-app prompts. Save-to-Downloads changes disposable storage; retain proof and remove the test file afterward.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
