# TLS warning explanations and navigation

Show specific certificate failure reasons and verify leaving or explicitly accepting the expired-certificate warning. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 10 expired certificate
- 13 ssl wrong host certificate
- 14 ssl self signed certificate
- 15 ssl untrusted root certificate

## How to get to it (user POV)

Navigate through `searchEntry` to expired.badssl.com, wrong.host.badssl.com, self-signed.badssl.com or untrusted-root.badssl.com as listed below.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Check `Warning: This site may be insecure` plus `Globe-24`; open Advanced and find the source-specific reason. In the expired-certificate case first visit the safe ad test page, then Leave This Site must return there; Forward restores warning and Back restores safe page. Explicitly choose Advanced → Accept Risk and Visit Site only for this disposable test fixture; wait for `privacy-icon-shield.button` and expired.badssl.com, then repeat back/forward.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**10 expired certificate** — `.maestro/privacy_tests/10_expired_certificate.yaml` (`.maestro/privacy_tests/10_expired_certificate.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- eraseText`
  - L19: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L20: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L24: `- tapOn:; id: "searchEntry"`
  - L26: `- eraseText`
  - L27: `- inputText: "https://expired.badssl.com"`
  - L28: `- pressKey: Enter`
  - L29: `- assertVisible: "Warning: This site may be insecure"`
  - L30: `- assertVisible:; id: "Globe-24"`
  - L32: `- tapOn: "Leave This Site"`
  - L33: `- assertNotVisible: "Warning: This site may be insecure"`
  - L34: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L36: `- tapOn: "Browse Forward"`
  - L37: `- assertVisible: "Warning: This site may be insecure"`
  - L38: `- tapOn: "Browse Back"`
  - L39: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L40: `- assertNotVisible: "Warning: This site may be insecure"`
  - L44: `- tapOn: "Browse Forward"`
  - L45: `- assertVisible: "Warning: This site may be insecure"`
  - L46: `- assertVisible:; id: "Globe-24"`
  - L48: `- tapOn: "Advanced"`
  - L49: `- scrollUntilVisible:; element:; text: ".*is expired.*"; direction: DOWN`
  - L53: `- scrollUntilVisible:; element:; text: "Accept Risk and Visit Site"; direction: DOWN`
  - L57: `- tapOn: "Accept Risk and Visit Site"`
  - L59: `- extendedWaitUntil:; visible:; id: "privacy-icon-shield.button"; timeout: 20000`
  - L63: `- assertVisible: "expired.badssl.com"`
  - L65: `- tapOn: "Browse Back"`
  - L66: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L67: `- tapOn: "Browse Forward"`
  - L68: `- extendedWaitUntil:; visible:; id: "privacy-icon-shield.button"; timeout: 20000`
  - L72: `- assertVisible: "expired.badssl.com"`

**13 ssl wrong host certificate** — `.maestro/privacy_tests/13_ssl_wrong_host_certificate.yaml` (`.maestro/privacy_tests/13_ssl_wrong_host_certificate.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://wrong.host.badssl.com"`
  - L19: `- pressKey: Enter`
  - L22: `- assertVisible: "Warning: This site may be insecure"`
  - L23: `- assertVisible:; id: "Globe-24"`
  - L25: `- tapOn: "Advanced"`
  - L26: `- scrollUntilVisible:; element:; text: ".*does not match.*"; direction: DOWN`

**14 ssl self signed certificate** — `.maestro/privacy_tests/14_ssl_self_signed_certificate.yaml` (`.maestro/privacy_tests/14_ssl_self_signed_certificate.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://self-signed.badssl.com"`
  - L19: `- pressKey: Enter`
  - L22: `- assertVisible: "Warning: This site may be insecure"`
  - L23: `- assertVisible:; id: "Globe-24"`
  - L25: `- tapOn: "Advanced"`
  - L26: `- scrollUntilVisible:; element:; text: ".*not trusted by your device.*"; direction: DOWN`

**15 ssl untrusted root certificate** — `.maestro/privacy_tests/15_ssl_untrusted_root_certificate.yaml` (`.maestro/privacy_tests/15_ssl_untrusted_root_certificate.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L12: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://untrusted-root.badssl.com"`
  - L19: `- pressKey: Enter`
  - L22: `- assertVisible: "Warning: This site may be insecure"`
  - L23: `- assertVisible:; id: "Globe-24"`
  - L25: `- tapOn: "Advanced"`
  - L26: `- scrollUntilVisible:; element:; text: ".*not trusted by your device.*"; direction: DOWN`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

An expired-certificate scenario needs real back history. Network load after acceptance may take 20 seconds. Warning text alone does not prove certificate-specific messaging. Never run these scenarios against arbitrary user sites or persist an acceptance in a personal simulator.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
