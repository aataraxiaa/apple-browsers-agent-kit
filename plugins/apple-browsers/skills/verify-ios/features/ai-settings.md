# AI Features settings

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `ai-chat-settings` — `.maestro/release_tests/ai-chat-settings.yaml`.

- `ai-settings-search-assist` changes Search Assist frequency through its native picker.
- `ai-settings-hide-images` switches hiding generated images on/off.
- `ai-settings-disable-all` disables all AI options, greys its action and changes the footer.
- `ai-settings-input-preference` selects Search Only or Search & Duck.ai and conditionally exposes default input mode.

## How to get to it (user POV)

Browsing Menu → Settings → AI Features. Scroll to the exact stable row identifier before choosing it, then return through Settings and Done.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### ai-chat-settings

Source: `.maestro/release_tests/ai-chat-settings.yaml`. Tags: `["iphone", "release"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Tap label/text `"Browsing Menu"`.
3. Tap label/text `"Settings"`.
4. Scroll toward `"DOWN"` until label/text `"AI Features"` is fully visible. Refresh the snapshot.
5. Tap label/text `"AI Features"`.
6. Scroll toward `"DOWN"` until identifier `"Settings.AIFeatures.DuckAISettings"` is fully visible; center it before tapping. Refresh the snapshot.
7. Require visible identifier `"Settings.AIFeatures.DuckAISettings"`.
8. Require visible label/text `"Duck.ai Settings"`.
9. Scroll toward `"UP"` until identifier `"Settings.AIFeatures.EnableToggle"` is fully visible. Refresh the snapshot.
10. Tap identifier `"Settings.AIFeatures.EnableToggle"`.
11. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
12. Require absent identifier `"Settings.AIFeatures.DuckAISettings"`.
13. Require absent label/text `"Duck.ai Settings"`.
14. Tap identifier `"Settings.AIFeatures.EnableToggle"`.
15. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
16. Scroll toward `"DOWN"` until identifier `"Settings.AIFeatures.DuckAISettings"` is fully visible; center it before tapping. Refresh the snapshot.
17. Require visible identifier `"Settings.AIFeatures.DuckAISettings"`.
18. Tap identifier `"Settings.AIFeatures.DuckAISettings"`.
19. Require absent label/text `"AI Features"`.
20. Require visible label/text `".*duck\\.ai.*"`.

### Native settings beyond the YAML

Source: `SettingsAIFeaturesView.swift`, `SettingsAIExperimentalPickerView.swift`. These are source-derived scenarios, not observed behavior.

1. Capture the original selection. Open `Settings.AIFeatures.SearchAssistPicker`; the source offers never, onDemand, sometimes and often through localized labels. Select the label in the fresh snapshot, reopen and assert the same selection. Return it to the original value. Do not invent English labels from enum cases.
2. Open `Settings.AIFeatures.HideAIGeneratedImagesPicker`, select the other On/Off option visible in the snapshot, return/reopen and assert persistence, then restore. This local setting check does not prove filtered image search results.
3. On disposable settings state choose `Settings.AIFeatures.DisableAllAIOptions`. Require `Settings.AIFeatures.EnableToggle` off, the Duck.ai section gone, the disable-all button disabled, and the changed no-AI footer. Read current localized strings before matching them. Re-enable individual options only if restoring an observed original state.
4. With Duck.ai enabled, select `Settings.AIFeatures.Picker.SearchAndDuckAI`, return to the browser and assert Search/Duck.ai toggle presence. Select `Settings.AIFeatures.Picker.SearchOnly`, return and assert toggle absence. Default omnibar mode appears only when search-input preference and `isDefaultOmnibarModeEnabled` both hold. Its source choices are search, duckAI, lastUsed; resolve localized labels from the snapshot.
5. Automatic page content control exists only when contextual Duck.ai is enabled; Manage Shortcuts and Duck.ai Settings are inside the enabled Duck.ai section. The other worker owns shortcut scenario prose; use its dedicated shortcut map for individual entry points.

## Gotchas

Disabling Duck.ai collapses the Duck.ai section including Settings.AIFeatures.DuckAISettings. Enabling restores it; choosing Duck.ai Settings dismisses Settings and opens duck.ai. Web content and consent remain network-dependent.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
