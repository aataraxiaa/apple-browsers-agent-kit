# Calendar and contact link previews

Import a single calendar event or contact and handle malformed, unsupported and multi-item downloads. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- ics calendar links happy path
- ics calendar links multi event fallback
- ics calendar links parse failure fallback
- ics calendar links unrecognized timezone fallback
- vcf contact links happy path
- vcf contact links multiple contacts
- vcf contact links parse failure

## How to get to it (user POV)

Load the exact fixture URL below through `searchEntry`. Single .ics opens `New Event`; a supported .vcf opens the native card with `contactPreviewCancelButton`.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

For single calendar show New Event and ensure neither fallback error toast is present. Multi-event, invalid-calendar and unknown-timezone fixtures must reach the QuickLook Done identifier `QLOverlayDoneButtonAccessibilityIdentifier` according to their source assertion. Single and multi-contact fixtures must show `contactPreviewCancelButton`; multi-contact must not show QuickLook. Cancel each system sheet through its current snapshot ref; do not save to the simulator calendar or contacts merely to prove preview routing.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**ics calendar links happy path** — `.maestro/browser_features/ics_calendar_links_happy_path.yaml` (`.maestro/browser_features/ics_calendar_links_happy_path.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/calendar-single.ics"`
  - L19: `- pressKey: Enter`
  - L23: `- extendedWaitUntil:; visible: "New Event"; timeout: 10000`
  - L28: `- assertNotVisible: "Multiple events aren't supported. Try opening the downloaded file instead."`
  - L29: `- assertNotVisible: "This file can't be processed. Try opening the downloaded file instead."`

**ics calendar links multi event fallback** — `.maestro/browser_features/ics_calendar_links_multi_event_fallback.yaml` (`.maestro/browser_features/ics_calendar_links_multi_event_fallback.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L10: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://privacy-test-pages.site/features/download/calendar-multi.ics"`
  - L18: `- pressKey: Enter`
  - L20: `- extendedWaitUntil:; visible:; id: "QLOverlayDoneButtonAccessibilityIdentifier"; timeout: 10000`

**ics calendar links parse failure fallback** — `.maestro/browser_features/ics_calendar_links_parse_failure_fallback.yaml` (`.maestro/browser_features/ics_calendar_links_parse_failure_fallback.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/calendar-malformed.ics"`
  - L19: `- pressKey: Enter`
  - L21: `- extendedWaitUntil:; visible: "This file can't be processed. Try opening the downloaded file instead."; timeout: 15000`
  - L26: `- assertNotVisible:; id: "QLOverlayDoneButtonAccessibilityIdentifier"`

**ics calendar links unrecognized timezone fallback** — `.maestro/browser_features/ics_calendar_links_unrecognized_timezone_fallback.yaml` (`.maestro/browser_features/ics_calendar_links_unrecognized_timezone_fallback.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/calendar-unrecognized-timezone.ics"`
  - L19: `- pressKey: Enter`
  - L21: `- extendedWaitUntil:; visible:; id: "QLOverlayDoneButtonAccessibilityIdentifier"; timeout: 10000`

**vcf contact links happy path** — `.maestro/browser_features/vcf_contact_links_happy_path.yaml` (`.maestro/browser_features/vcf_contact_links_happy_path.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/contact-full.vcf"`
  - L19: `- pressKey: Enter`
  - L27: `- extendedWaitUntil:; visible:; id: "contactPreviewCancelButton"; timeout: 10000`
  - L33: `- assertNotVisible: "Unable to add contact. Try opening the contact file from Downloads instead."`

**vcf contact links multiple contacts** — `.maestro/browser_features/vcf_contact_links_multiple_contacts.yaml` (`.maestro/browser_features/vcf_contact_links_multiple_contacts.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/contact-multiple.vcf"`
  - L19: `- pressKey: Enter`
  - L27: `- extendedWaitUntil:; visible:; id: "contactPreviewCancelButton"; timeout: 10000`
  - L34: `- assertNotVisible:; id: "QLOverlayDoneButtonAccessibilityIdentifier"`

**vcf contact links parse failure** — `.maestro/browser_features/vcf_contact_links_parse_failure.yaml` (`.maestro/browser_features/vcf_contact_links_parse_failure.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow:; file: ../shared/setup.yaml`
  - L14: `- assertVisible:; id: "searchEntry"`
  - L16: `- tapOn:; id: "searchEntry"`
  - L18: `- inputText: "https://privacy-test-pages.site/features/download/contact-malformed.vcf"`
  - L19: `- pressKey: Enter`
  - L21: `- extendedWaitUntil:; visible: "Unable to add contact. Try opening the contact file from Downloads instead."; timeout: 15000`
  - L26: `- assertNotVisible:; id: "QLOverlayDoneButtonAccessibilityIdentifier"`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Requires iOS 17+ for calendar happy path. iOS 26 replaced Cancel/Add text with icons; New Event is the stable title. Multi-contact .vcf intentionally truncates to first contact, unlike multi-event .ics fallback. System Contacts content may not be exposed fully: card presence proves routing, not every parsed field. Fallback comments mention toasts but some flows only assert QuickLook; record this limitation.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
