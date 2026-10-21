# iOS verification feature map

Resolve every `.maestro/` and `iOS/` source path against the caller's active Apple browsers checkout, never this plugin or its installed cache. This inventory was mapped at source commit `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; read the current referenced sources before driving. Source line numbers are navigation hints and can drift.

The [coverage manifest](coverage.json) accounts for all 199 YAML files in that checkout, including helpers and configuration. It does not imply 199 independently runnable tests or full product coverage. Every mapped scenario remains NOT RUN through MobileBuildMCP until a run records real evidence. Swift-sourced download, history, settings, and subscription notes extend the existing flow inventory; they are also unexecuted.

## Baseline and selection

Use [verify-ios](../SKILL.md) for launch, doctor, provider operations, evidence, and cleanup. Select the changed feature plus adjacent regressions. Read the chosen recipe and its helper dependencies, not this whole catalog. Require the scenario's device idiom, clean/disposable state where needed, exact launch flags, fixtures, and backend/account prerequisites. Do not turn setup helpers into independently passed user scenarios.

A historical regex or coordinate is a source hint, not a current elementRef. Inspect the real UI, resolve stable identifiers/labels, and assert the destination after each action. Do not fabricate a provider equivalent for clipboard, system sheets, widgets, or weak coordinate-only steps. Record blocked subpaths separately.

## Feature guides

- [Ad-click privacy classification](ad-click-detection.md)
- [Address bar spoof and redirect defense](address-bar-security.md)
- [Duck.ai chat tabs](ai-chat-tab.md)
- [AI Features settings](ai-settings.md)
- [Duck.ai usage warnings](ai-usage-warnings.md)
- [Bookmarks, favorites and folders](bookmarks-favorites.md)
- [Browser tabs, address entry and restoration](browser-navigation.md)
- [Calendar and contact link previews](calendar-contact-imports.md)
- [Contextual Duck.ai and page attachment](contextual-ai.md)
- [Device identity and UI-test override diagnostics](device-and-overrides.md)
- [Download list, preview and persistent files](downloads.md)
- [Duck Player Classic mode and entry routes](duckplayer-classic.md)
- [Fire Button, fireproofing and preserved search settings](fireproof-data-clearing.md)
- [Navigation history and capture boundaries](history.md)
- [iPad Duck.ai chrome shortcuts](ipad-duckai-shortcuts.md)
- [iPad Duck.ai input controls](ipad-duckai.md)
- [Native Duck Player](native-duckplayer.md)
- [First-run and contextual onboarding](onboarding.md)
- [Passwords and Autofill](passwords-autofill.md)
- [Tracker dashboard and ad attribution sessions](privacy-attribution.md)
- [Content-scope experiments and fingerprinting](privacy-diagnostics.md)
- [Release browsing, tabs and lifecycle](release-browser.md)
- [App lock, autoclear and release privacy](release-privacy-settings.md)
- [Shared navigation and fixture helpers](shared-helpers.md)
- [Subscription settings and setup re-entry](subscription-settings.md)
- [Sync and Backup](sync-backup.md)
- [TLS warning explanations and navigation](tls-warnings.md)
- [Search and Duck.ai input modes](unified-input.md)

## Results and maintenance

Record PASS, FAIL, BLOCKED, or NOT RUN per scenario and entry point with source identity and evidence. One successful smoke flow accepts the driver mechanics only; it does not accept every map entry. Review the manifest against the active checkout with `python3 scripts/check_coverage.py /absolute/path/to/apple-browsers` from this plugin's editable source. AStack's maintain-verification-skill updates this external source as the app changes.
