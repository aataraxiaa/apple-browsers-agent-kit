# Download list, preview and persistent files

Save downloads, reopen their preview and remove test downloads using the real list UI. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- Save downloads, reopen their preview and remove test downloads using the real list UI.

## How to get to it (user POV)

Browsing menu → Downloads is built by BrowsingMenuBuilder.swift; Save to Downloads is the native download alert action. Calendar/contact link preview provides additional download entry routes.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier.

Use the JS-download fixture from address-bar-security or the calendar/contact fixtures; accept Save to Downloads only on the designated disposable app. Open Downloads, match the fixture filename from current snapshot and open its row. Verify the correct QuickLook/native preview; dismiss and reopen the list to prove persistence. Delete the fixture through the current row/list controls and verify its absence after reopening. Source `DownloadsList` supplies completion/ongoing section and deletion UI; capture observable filename/status transitions rather than only a toast.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.


Additional source-grounded list scenarios (no YAML counterpart):

- **Ongoing cancel.** Start a sufficiently slow fixture download; inspect its row. `DownloadsList.swift:165-168` routes an ongoing row cancellation to a confirmation alert. The copy in `UserText.swift:666-671` is `Cancel download?`, `Are you sure you want to cancel this download?`, `No`, and `Yes`. Choose No first and observe ongoing state; repeat and choose Yes, then observe the row is removed/stopped. Do not claim cancellation coverage if the fixture completes before the alert can be reached.
- **Completed preview and share.** `DownloadsList/View/Rows/CompleteDownloadRow.swift:54-118` renders the real filename and file size as a button; tapping prepares event/contact data, selects native event editor on iOS 17+, contact card when parsable, otherwise QuickLook. Its separate button has accessibility label `Share` (`UserText.actionShare`); tap it and assert the system share sheet, then cancel without sending to another app/person.
- **Edit and removal.** `DownloadsList.swift:111-159` uses SwiftUI EditButton and per-row `.onDelete`. Select Edit through the current snapshot, then the fixture row’s delete control; reopening confirms absence. The trash image in edit mode invokes delete-all without a confirmation in this view: only exercise it in an empty-or-fixture-only disposable list, and only if the current snapshot exposes a usable semantic elementRef. Source gives no accessibility label for that image; do not invent one.
- **Empty and dismissal.** With no entries, `UserText.swift:683` supplies `No files downloaded yet`. Confirm this exact empty text after fixture removal. In inactive edit mode the trailing Done button dismisses the list (`DownloadsList.swift:44-48`); capture the returned browser screen.

Source files: `iOS/DuckDuckGo/Downloads/DownloadsList/View/DownloadsList.swift`, `iOS/DuckDuckGo/Downloads/DownloadsList/View/Rows/CompleteDownloadRow.swift`, `iOS/DuckDuckGo/Downloads/DownloadsList/ViewModel/CompleteDownloadRowViewModel.swift`, `iOS/DuckDuckGo/Downloads/FilePreview/FilePreviewHelper.swift`, and `iOS/DuckDuckGo/UserInterface/UserText.swift` at the recorded HEAD.

## Gotchas

No dedicated download suite was found in the requested inventory. This is source-derived coverage, with no asserted accessibility identifier for list rows. Resolve the actual controls from snapshot labels; do not invent IDs. FilePreviewHelper.shouldPersistInDownloads deliberately keeps ICS/vCard files for retry. Preview success alone is not a completed-download/file-persistence assertion; if the provider cannot inspect disk, explicitly report that evidence gap.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
