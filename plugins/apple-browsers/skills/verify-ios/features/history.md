# Navigation history and capture boundaries

Verify visible Back/Forward history and distinguish it from internal history capture and Duck.ai chat history. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- Verify visible Back/Forward history and distinguish it from internal history capture and Duck.ai chat history.

## How to get to it (user POV)

Navigate two ordinary pages in a tab, then use Browse Back and Browse Forward. There is no verified user-facing browsing History menu entry in the inspected iOS BrowsingMenuBuilder.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier.

Use the restoration, privacy-navigation and expired-certificate routes to assert title/origin and back/forward outcomes. Restart while preserving data and repeat on the restored tab. Read History/HistoryCapture.swift when investigating capture behavior; it is internal source evidence, not a UI selector. Do not route the user to AIChatHistoryViewController for browsing history.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

Source: `iOS/DuckDuckGo/History/HistoryCapture.swift:50-71` adds a visit on web-view commit, skips title updates for fire tabs, and only commits nonempty title changes for the same current URL. Its `urlOrDuckDuckGoCleanQuery` cleans search parameters. These facts guide investigation; a UI Back/Forward proof does not establish internal stored-visit behavior. Source menu boundary: `iOS/DuckDuckGo/BrowsingMenu/SheetPresentationMenu/BrowsingMenuBuilder.swift:97-103,194-200`.

## Gotchas

No standalone browsing-history Maestro flow was found. HistoryCapture exists but the inspected menu exposes Bookmarks and Downloads, with no History action. A browse-history list, search, and delete UI are unresolved coverage, not executable steps; add them only after locating a real current entry path. Never infer a menu label from a class name.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
