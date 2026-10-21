# First-run and contextual onboarding

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `01_onboarding_contextual` — `.maestro/onboarding_tests/01_onboarding_contextual.yaml`.
- `02_onboarding_add_to_dock_intro` — `.maestro/onboarding_tests/02_onboarding_add_to_dock_intro.yaml`.
- `03_onboarding_add_to_dock_contextual` — `.maestro/onboarding_tests/03_onboarding_add_to_dock_contextual.yaml`.
- `onboarding` (helper/configuration) — `.maestro/onboarding_tests/shared/onboarding.yaml`.

## How to get to it (user POV)

Start a separately designated disposable fresh installation with onboarding incomplete, and use the variant named by the chosen scenario. Follow linear intro screens before NTP search/site suggestions and contextual education.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### 01_onboarding_contextual

Source: `.maestro/onboarding_tests/01_onboarding_contextual.yaml`. Tags: `["iphone", "onboarding"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/onboarding_tests/shared/onboarding.yaml`, `.maestro/shared/use_firebutton.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml` with parameters `{"ONBOARDING_COMPLETED": "false", "APP_VARIANT": "mh"}`.
2. Follow visible behavior from `.maestro/onboarding_tests/shared/onboarding.yaml`.
3. Require visible label/text `"Ready to get started?\nTry a search!"`.
4. Require visible label/text `"Surprise Me!"`.
5. Tap label/text `"Surprise Me!"`.
6. Require visible label/text `"That’s DuckDuckGo Search. Private. Fast. Fewer ads."`.
7. Require visible label/text `"Got It!"`.
8. Tap label/text `"Got It!"`.
9. Require visible label/text `"Next, try visiting a site!"`.
10. Require visible label/text `"Surprise Me!"`.
11. Tap label/text `"Surprise Me!"`.
12. Require visible label/text `"Got It!"`.
13. Tap identifier `"privacy-icon-shield.button"`.
14. Require visible text `"View Tracker Companies"`.
15. Require visible text `"Done"`.
16. Tap label/text `"Done"`.
17. Require visible label/text `"Got It!"`.
18. Tap label/text `"Got It!"`.
19. Require visible label/text `"Instantly clear your browsing activity with the Fire Button.\n\nGive it a try! 🔥"`.
20. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
21. Require visible label/text `"You’ve got this!"`.
22. Require visible label/text `"High five!"`.
23. Tap label/text `"High five!"`.

### 02_onboarding_add_to_dock_intro

Source: `.maestro/onboarding_tests/02_onboarding_add_to_dock_intro.yaml`. Tags: `["iphone", "onboarding"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/onboarding_tests/shared/onboarding.yaml`, `.maestro/shared/use_firebutton.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml` with parameters `{"ONBOARDING_COMPLETED": "false", "APP_VARIANT": "mk"}`.
2. Follow visible behavior from `.maestro/onboarding_tests/shared/onboarding.yaml`.
3. Require visible label/text `"Ready to get started?\nTry a search!"`.
4. Require visible label/text `"Surprise Me!"`.
5. Tap label/text `"Surprise Me!"`.
6. Require visible label/text `"That’s DuckDuckGo Search. Private. Fast. Fewer ads."`.
7. Require visible label/text `"Got It!"`.
8. Tap label/text `"Got It!"`.
9. Require visible label/text `"Next, try visiting a site!"`.
10. Require visible label/text `"Surprise Me!"`.
11. Tap label/text `"Surprise Me!"`.
12. Require visible label/text `"Got It!"`.
13. Tap identifier `"privacy-icon-shield.button"`.
14. Require visible text `"View Tracker Companies"`.
15. Require visible text `"Done"`.
16. Tap label/text `"Done"`.
17. Require visible label/text `"Got It!"`.
18. Tap label/text `"Got It!"`.
19. Require visible label/text `"Instantly clear your browsing activity with the Fire Button.\n\nGive it a try! 🔥"`.
20. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
21. Require visible label/text `"You’ve got this!"`.
22. Require visible label/text `"High five!"`.
23. Tap label/text `"High five!"`.

### 03_onboarding_add_to_dock_contextual

Source: `.maestro/onboarding_tests/03_onboarding_add_to_dock_contextual.yaml`. Tags: `["iphone", "onboarding"]`.

Dependencies: `.maestro/shared/setup.yaml`, `.maestro/onboarding_tests/shared/onboarding.yaml`, `.maestro/shared/use_firebutton.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml` with parameters `{"ONBOARDING_COMPLETED": "false", "APP_VARIANT": "mo"}`.
2. Follow visible behavior from `.maestro/onboarding_tests/shared/onboarding.yaml`.
3. Require visible label/text `"Ready to get started?\nTry a search!"`.
4. Require visible label/text `"Surprise Me!"`.
5. Tap label/text `"Surprise Me!"`.
6. Require visible label/text `"That’s DuckDuckGo Search. Private. Fast. Fewer ads."`.
7. Require visible label/text `"Got It!"`.
8. Tap label/text `"Got It!"`.
9. Require visible label/text `"Next, try visiting a site!"`.
10. Require visible label/text `"Surprise Me!"`.
11. Tap label/text `"Surprise Me!"`.
12. Require visible label/text `"Got It!"`.
13. Tap identifier `"privacy-icon-shield.button"`.
14. Require visible text `"View Tracker Companies"`.
15. Require visible text `"Done"`.
16. Tap label/text `"Done"`.
17. Require visible label/text `"Got It!"`.
18. Tap label/text `"Got It!"`.
19. Require visible label/text `"Instantly clear your browsing activity with the Fire Button.\n\nGive it a try! 🔥"`.
20. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
21. Require visible label/text `"Add me to your Dock!"`.
22. Require visible label/text `"Show Me How"`.
23. Tap label/text `"Start Browsing"`.

### onboarding

Source: `.maestro/onboarding_tests/shared/onboarding.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Require visible text `"Let’s Do It!"`, index `0`.
2. Tap text `"Let’s Do It!"`, index `0`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
3. Tap text `"Skip"`.
4. Conditional branch `{"visible": "Add me to your Dock!"}`: Require visible label/text `"Show Me How"`. Tap label/text `"Skip"`.
5. Require visible label/text `"Which color looks best on me?"`.
6. Require visible label/text `"Next"`.
7. Tap label/text `"Next"`.
8. Require visible label/text `"Where should I put your address bar?"`.
9. Require visible label/text `"Next"`.
10. Tap label/text `"Next"`.

## Gotchas

The three contextual variants are mh, mk, mo. The mo variant ends at Add me to your Dock! and Start Browsing. Other variants finish You’ve got this! / High five!. Fire action clears browsing state and is allowed only on disposable fixtures. Source flows depend on current education copy; current onboarding source may expose additional steps, so treat a mismatch as map drift.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
