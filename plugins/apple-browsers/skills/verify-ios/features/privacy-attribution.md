# Tracker dashboard and ad attribution sessions

Distinguish blocked tracker requests from attribution exceptions while moving through checkout, tabs, refresh and browser restart. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 01 single-site single-tab session
- 02 single-site new tab session
- 03 single-site new-tab session variant two
- 04 single-site multi-tab session
- 05 multi-site single-tab session
- 06 multi-tab
- 07 browser restart mid-session
- 08 navigation with back forward
- 09 navigation with refresh

## How to get to it (user POV)

Open `https://www.search-company.site/#ad-id-5`, choose `[Ad 5] SERP Ad (heuristic)`, then use `privacy-icon-shield.button` → View Tracker Companies / View Non-Tracker Companies.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Check `ad-company.site` in blocked tracker companies and `convert.ad-company.site` in non-tracker companies with the ad-effectiveness explanation. Follow Publisher site → Buy now → Checkout → Pay → Order complete, opening the dashboard at each source checkpoint. Repeat the new-tab, same-site/multi-site, back/forward, refresh and restart variants separately; each variant changes which requests may qualify for the exception. Use each source file’s expected domains and explanatory copy rather than assuming all variants match the baseline.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**01 single-site single-tab session** — `.maestro/privacy_tests/01_single-site_single-tab_session.yaml` (`.maestro/privacy_tests/01_single-site_single-tab_session.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible: "Publisher site"`
  - L24: `- tapOn:; id: "privacy-icon-shield.button"`
  - L26: `- assertVisible:; text: "View Tracker Companies"`
  - L28: `- tapOn:; text: "View Tracker Companies"`
  - L30: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L32: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L34: `- assertVisible:; text: ".*Ad Company"`
  - L36: `- assertVisible:; text: "ad-company.site"`
  - L38: `- tapOn: "Back"`
  - L39: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L41: `- tapOn:; text: "View Non-Tracker Companies"`
  - L43: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L45: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L47: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L49: `- assertVisible:; text: "How our search ads impact our protections"`
  - L51: `- assertVisible:; text: ".*Ad Company"`
  - L53: `- assertVisible:; text: "convert.ad-company.site"`
  - L55: `- tapOn: "Back"`
  - L56: `- tapOn: "Done"`
  - L57: `- assertVisible:; text: "Buy now"`
  - L59: `- tapOn:; text: "Buy now"`
  - L61: `- tapOn:; text: "High five!"; optional: true`
  - L64: `- assertVisible:; text: "Checkout"`
  - L66: `- tapOn:; id: "privacy-icon-shield.button"`
  - L68: `- assertVisible:; text: "View Tracker Companies"`
  - L70: `- tapOn:; text: "View Tracker Companies"`
  - L72: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L74: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L76: `- assertVisible:; text: ".*Ad Company"`
  - L78: `- assertVisible:; text: "ad-company.site"`
  - L80: `- tapOn: "Back"`
  - L81: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L83: `- tapOn:; text: "View Non-Tracker Companies"`
  - L85: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L87: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L89: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L91: `- assertVisible:; text: "How our search ads impact our protections"`
  - L93: `- assertVisible:; text: ".*Ad Company"`
  - L95: `- assertVisible:; text: "convert.ad-company.site"`
  - L97: `- tapOn: "Back"`
  - L98: `- tapOn: "Done"`
  - L99: `- assertVisible:; text: "Pay"`
  - L101: `- tapOn: "Pay"`
  - L102: `- assertVisible:; text: ".*Order complete.*"`
  - L104: `- tapOn:; id: "privacy-icon-shield.button"`
  - L106: `- assertVisible:; text: "View Tracker Companies"`
  - L108: `- tapOn:; text: "View Tracker Companies"`
  - L110: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L112: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L114: `- assertVisible:; text: ".*Ad Company"`
  - L116: `- assertVisible:; text: "ad-company.site"`
  - L118: `- tapOn: "Back"`
  - L119: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L121: `- tapOn:; text: "View Non-Tracker Companies"`
  - L123: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L125: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L127: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L129: `- assertVisible:; text: "How our search ads impact our protections"`
  - L131: `- assertVisible:; text: ".*Ad Company"`
  - L133: `- assertVisible:; text: "convert.ad-company.site"`

**02 single-site new tab session** — `.maestro/privacy_tests/02_single-site_new_tab_session.yaml` (`.maestro/privacy_tests/02_single-site_new_tab_session.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- longPressOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Open in New Tab"`
  - L25: `- tapOn:; text: "Open in New Tab"`
  - L27: `- assertVisible:; text: "Publisher site"`
  - L29: `- tapOn:; id: "privacy-icon-shield.button"`
  - L31: `- assertVisible:; text: "View Tracker Companies"`
  - L33: `- tapOn:; text: "View Tracker Companies"`
  - L35: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L37: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L39: `- assertVisible:; text: ".*Ad Company"`
  - L41: `- assertVisible:; text: "ad-company.site"`
  - L43: `- tapOn: "Back"`
  - L44: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L46: `- tapOn:; text: "View Non-Tracker Companies"`
  - L48: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L50: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L52: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L54: `- assertVisible:; text: "How our search ads impact our protections"`
  - L56: `- assertVisible:; text: ".*Ad Company"`
  - L58: `- assertVisible:; text: "convert.ad-company.site"`
  - L60: `- tapOn: "Back"`
  - L61: `- tapOn: "Done"`
  - L62: `- assertVisible:; text: "Buy now"`
  - L64: `- tapOn:; text: "Buy now"`
  - L66: `- tapOn:; text: "High five!"; optional: true`
  - L69: `- assertVisible:; text: "Checkout"`
  - L71: `- tapOn:; id: "privacy-icon-shield.button"`
  - L73: `- assertVisible:; text: "View Tracker Companies"`
  - L75: `- tapOn:; text: "View Tracker Companies"`
  - L77: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L79: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L81: `- assertVisible:; text: ".*Ad Company"`
  - L83: `- assertVisible:; text: "ad-company.site"`
  - L85: `- tapOn: "Back"`
  - L86: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L88: `- tapOn:; text: "View Non-Tracker Companies"`
  - L90: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L92: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L94: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L96: `- assertVisible:; text: "How our search ads impact our protections"`
  - L98: `- assertVisible:; text: ".*Ad Company"`
  - L100: `- assertVisible:; text: "convert.ad-company.site"`
  - L102: `- tapOn: "Back"`
  - L103: `- tapOn: "Done"`
  - L104: `- assertVisible:; text: "Pay"`
  - L106: `- tapOn:; text: "Pay"`
  - L108: `- assertVisible:; text: ".*Order complete.*"`
  - L110: `- tapOn:; id: "privacy-icon-shield.button"`
  - L112: `- assertVisible:; text: "View Tracker Companies"`
  - L114: `- tapOn:; text: "View Tracker Companies"`
  - L116: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L118: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L120: `- assertVisible:; text: ".*Ad Company"`
  - L122: `- assertVisible:; text: "ad-company.site"`
  - L124: `- tapOn: "Back"`
  - L125: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L127: `- tapOn:; text: "View Non-Tracker Companies"`
  - L129: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L131: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L133: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L135: `- assertVisible:; text: "How our search ads impact our protections"`
  - L137: `- assertVisible:; text: ".*Ad Company"`
  - L139: `- assertVisible:; text: "convert.ad-company.site"`

**03 single-site new-tab session variant two** — `.maestro/privacy_tests/03_single-site_new-tab_session_variant_two.yaml` (`.maestro/privacy_tests/03_single-site_new-tab_session_variant_two.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Buy now"`
  - L60: `- longPressOn:; text: "Buy now"`
  - L62: `- assertVisible:; text: "Open in New Tab"`
  - L64: `- tapOn:; text: "Open in New Tab"`
  - L66: `- assertVisible:; text: "Checkout"`
  - L68: `- tapOn:; id: "privacy-icon-shield.button"`
  - L70: `- assertVisible:; text: "View Tracker Companies"`
  - L72: `- tapOn:; text: "View Tracker Companies"`
  - L74: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L76: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L78: `- assertVisible:; text: ".*Ad Company"`
  - L80: `- assertVisible:; text: "ad-company.site"`
  - L82: `- tapOn: "Back"`
  - L83: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L85: `- tapOn:; text: "View Non-Tracker Companies"`
  - L87: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L89: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L91: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L93: `- assertVisible:; text: "How our search ads impact our protections"`
  - L95: `- assertVisible:; text: ".*Ad Company"`
  - L97: `- assertVisible:; text: "convert.ad-company.site"`
  - L99: `- tapOn: "Back"`
  - L100: `- tapOn: "Done"`
  - L101: `- assertVisible:; text: "Pay"`
  - L103: `- tapOn:; text: "Pay"`
  - L105: `- tapOn:; text: "High five!"; optional: true`
  - L108: `- assertVisible:; text: ".*Order complete.*"`
  - L110: `- tapOn:; id: "privacy-icon-shield.button"`
  - L112: `- assertVisible:; text: "View Tracker Companies"`
  - L114: `- tapOn:; text: "View Tracker Companies"`
  - L116: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L118: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L120: `- assertVisible:; text: ".*Ad Company"`
  - L122: `- assertVisible:; text: "ad-company.site"`
  - L124: `- tapOn: "Back"`
  - L125: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L127: `- tapOn:; text: "View Non-Tracker Companies"`
  - L129: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L131: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L133: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L135: `- assertVisible:; text: "How our search ads impact our protections"`
  - L137: `- assertVisible:; text: ".*Ad Company"`
  - L139: `- assertVisible:; text: "convert.ad-company.site"`

**04 single-site multi-tab session** — `.maestro/privacy_tests/04_single-site_multi-tab_session.yaml` (`.maestro/privacy_tests/04_single-site_multi-tab_session.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- tapOn:; text: "Publisher site"`
  - L62: `- tapOn:; text: "High five!"; optional: true`
  - L65: `- assertVisible:; text: "Green T-shirt"`
  - L67: `- tapOn:; text: "Green T-shirt"`
  - L69: `- assertVisible:; text: "Buy now"`
  - L71: `- tapOn:; text: "Buy now"`
  - L73: `- assertVisible:; text: "Pay"`
  - L75: `- tapOn:; text: "Pay"`
  - L77: `- assertVisible:; text: ".*Order complete.*"`
  - L79: `- tapOn:; id: "privacy-icon-shield.button"`
  - L81: `- assertVisible:; text: "View Tracker Companies"`
  - L83: `- tapOn:; text: "View Tracker Companies"`
  - L85: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L87: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L89: `- assertVisible:; text: ".*Ad Company"`
  - L91: `- assertVisible:; text: "ad-company.site"`
  - L93: `- tapOn: "Back"`
  - L94: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L96: `- tapOn:; text: "View Non-Tracker Companies"`
  - L98: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L100: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L102: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L104: `- assertVisible:; text: "How our search ads impact our protections"`
  - L106: `- assertVisible:; text: ".*Ad Company"`
  - L108: `- assertVisible:; text: "convert.ad-company.site"`

**05 multi-site single-tab session** — `.maestro/privacy_tests/05_multi-site_single-tab_session.yaml` (`.maestro/privacy_tests/05_multi-site_single-tab_session.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- tapOn:; text: "Publisher site"`
  - L62: `- tapOn:; text: "High five!"; optional: true`
  - L65: `- assertVisible:; text: "Green T-shirt"`
  - L67: `- tapOn:; text: "Green T-shirt"`
  - L69: `- assertVisible:; text: "Buy now"`
  - L71: `- tapOn:; text: "Buy now"`
  - L73: `- assertVisible:; text: "Pay with payment-company!"`
  - L75: `- tapOn:; text: "Pay with payment-company!"`
  - L77: `- assertVisible:; text: "Pay First Party"`
  - L79: `- tapOn:; id: "privacy-icon-shield.button"`
  - L81: `- assertVisible:; text: "View Tracker Companies"`
  - L83: `- tapOn:; text: "View Tracker Companies"`
  - L85: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L87: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L89: `- assertVisible:; text: ".*Ad Company"`
  - L91: `- assertVisible:; text: "ad-company.site"`
  - L93: `- assertVisible:; text: "convert.ad-company.site"`
  - L95: `- tapOn: "Back"`
  - L96: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L98: `- tapOn:; text: "View Non-Tracker Companies"`
  - L100: `- assertVisible:; text: "We did not identify any requests from third-party domains."`
  - L102: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L104: `- tapOn: "Back"`
  - L105: `- tapOn: "Done"`
  - L106: `- assertVisible:; text: "Pay"`
  - L108: `- tapOn:; text: "Pay"`
  - L110: `- assertVisible:; text: "Order complete.*"`
  - L112: `- tapOn:; id: "privacy-icon-shield.button"`
  - L114: `- assertVisible:; text: "View Tracker Companies"`
  - L116: `- tapOn:; text: "View Tracker Companies"`
  - L118: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L120: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L122: `- assertVisible:; text: ".*Ad Company"`
  - L124: `- assertVisible:; text: "ad-company.site"`
  - L126: `- tapOn: "Back"`
  - L127: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L129: `- tapOn:; text: "View Non-Tracker Companies"`
  - L131: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L133: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L135: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L137: `- assertVisible:; text: "How our search ads impact our protections"`
  - L139: `- assertVisible:; text: ".*Ad Company"`
  - L141: `- assertVisible:; text: "convert.ad-company.site"`

**06 multi-tab** — `.maestro/privacy_tests/06_multi-tab.yaml` (`.maestro/privacy_tests/06_multi-tab.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- assertVisible: Tab Switcher`
  - L61: `- tapOn: Tab Switcher`
  - L62: `- assertVisible: "New Tab"`
  - L63: `- tapOn: "New Tab"`
  - L64: `- assertVisible:; id: "searchEntry"`
  - L66: `- tapOn:; id: "searchEntry"`
  - L68: `- inputText: "https://www.publisher-company.site/product.html?p=200"`
  - L69: `- pressKey: Enter`
  - L70: `- assertVisible:; text: "Red shoes"`
  - L72: `- assertVisible:; text: "Buy now"`
  - L74: `- tapOn:; text: "Buy now"`
  - L76: `- tapOn:; text: "High five!"; optional: true`
  - L79: `- assertVisible:; text: "Pay"`
  - L81: `- tapOn:; text: "Pay"`
  - L83: `- assertVisible:; text: ".*Order complete.*"`
  - L85: `- tapOn:; id: "privacy-icon-shield.button"`
  - L87: `- assertVisible:; text: "View Tracker Companies"`
  - L89: `- tapOn:; text: "View Tracker Companies"`
  - L91: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L93: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L95: `- assertVisible:; text: ".*Ad Company"`
  - L97: `- assertVisible:; text: "ad-company.site"`
  - L99: `- assertVisible:; text: "convert.ad-company.site"`
  - L101: `- tapOn: "Back"`
  - L102: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L104: `- tapOn:; text: "View Non-Tracker Companies"`
  - L106: `- assertVisible:; text: "We did not identify any requests from third-party domains."`
  - L108: `- assertVisible:; text: "About our Web Tracking Protections"`

**07 browser restart mid-session** — `.maestro/privacy_tests/07_browser_restart_mid-session.yaml` (`.maestro/privacy_tests/07_browser_restart_mid-session.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- assertVisible:; text: "Buy now"`
  - L62: `- tapOn:; text: "Buy now"`
  - L64: `- tapOn:; text: "High five!"; optional: true`
  - L67: `- assertVisible:; text: "Pay"`
  - L69: `- tapOn:; id: "privacy-icon-shield.button"`
  - L71: `- assertVisible:; text: "View Tracker Companies"`
  - L73: `- tapOn:; text: "View Tracker Companies"`
  - L75: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L77: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L79: `- assertVisible:; text: ".*Ad Company"`
  - L81: `- assertVisible:; text: "ad-company.site"`
  - L83: `- tapOn: "Back"`
  - L84: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L86: `- tapOn:; text: "View Non-Tracker Companies"`
  - L88: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L90: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L92: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L94: `- assertVisible:; text: "How our search ads impact our protections"`
  - L96: `- assertVisible:; text: ".*Ad Company"`
  - L98: `- assertVisible:; text: "convert.ad-company.site"`
  - L100: `- tapOn: "Back"`
  - L101: `- tapOn: "Done"`
  - L102: `- stopApp: "com.duckduckgo.mobile.ios"`
  - L103: `- launchApp:; arguments:; clearState: false; isRunningUITests: true`
  - L107: `- assertVisible:; text: "Pay"`
  - L109: `- tapOn:; text: "Pay"`
  - L111: `- assertVisible:; text: ".*Order complete.*"`
  - L113: `- tapOn:; id: "privacy-icon-shield.button"`
  - L115: `- assertVisible:; text: "View Tracker Companies"`
  - L117: `- tapOn:; text: "View Tracker Companies"`
  - L119: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L121: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L123: `- assertVisible:; text: ".*Ad Company"`
  - L125: `- assertVisible:; text: "ad-company.site"`
  - L127: `- assertVisible:; text: "convert.ad-company.site"`
  - L129: `- tapOn: "Back"`
  - L130: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L132: `- tapOn:; text: "View Non-Tracker Companies"`
  - L134: `- assertVisible:; text: "We did not identify any requests from third-party domains."`
  - L136: `- assertVisible:; text: "About our Web Tracking Protections"`

**08 navigation with back forward** — `.maestro/privacy_tests/08_navigation_with_back_forward.yaml` (`.maestro/privacy_tests/08_navigation_with_back_forward.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- tapOn:; text: "Publisher site"`
  - L62: `- tapOn:; text: "High five!"; optional: true`
  - L65: `- assertVisible:; text: "Green T-shirt"`
  - L67: `- tapOn:; text: "Green T-shirt"`
  - L69: `- assertVisible:; text: "Buy now"`
  - L71: `- tapOn:; text: "Buy now"`
  - L73: `- assertVisible:; text: "Pay with payment-company!"`
  - L75: `- tapOn:; text: "Pay with payment-company!"`
  - L77: `- assertVisible:; text: "Pay First Party"`
  - L79: `- tapOn:; id: "privacy-icon-shield.button"`
  - L81: `- assertVisible:; text: "View Tracker Companies"`
  - L83: `- tapOn:; text: "View Tracker Companies"`
  - L85: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L87: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L89: `- assertVisible:; text: ".*Ad Company"`
  - L91: `- assertVisible:; text: "ad-company.site"`
  - L93: `- assertVisible:; text: "convert.ad-company.site"`
  - L95: `- tapOn: "Back"`
  - L96: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L98: `- tapOn:; text: "View Non-Tracker Companies"`
  - L100: `- assertVisible:; text: "We did not identify any requests from third-party domains."`
  - L102: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L104: `- tapOn: "Back"`
  - L105: `- tapOn: "Done"`
  - L106: `- assertVisible: "Browse Back"`
  - L107: `- tapOn: "Browse Back"`
  - L108: `- assertVisible: "Browse Back"`
  - L109: `- tapOn: "Browse Back"`
  - L110: `- assertVisible: "Browse Forward"`
  - L111: `- tapOn: "Browse Forward"`
  - L112: `- assertVisible: "Browse Forward"`
  - L113: `- tapOn: "Browse Forward"`
  - L114: `- assertVisible:; text: "Pay"`
  - L116: `- tapOn:; text: "Pay"`
  - L118: `- tapOn:; id: "privacy-icon-shield.button"`
  - L120: `- assertVisible:; text: "View Tracker Companies"`
  - L122: `- tapOn:; text: "View Tracker Companies"`
  - L124: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L126: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L128: `- assertVisible:; text: ".*Ad Company"`
  - L130: `- assertVisible:; text: "ad-company.site"`
  - L132: `- tapOn: "Back"`
  - L133: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L135: `- tapOn:; text: "View Non-Tracker Companies"`
  - L137: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L139: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L141: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L143: `- assertVisible:; text: "How our search ads impact our protections"`
  - L145: `- assertVisible:; text: ".*Ad Company"`
  - L147: `- assertVisible:; text: "convert.ad-company.site"`

**09 navigation with refresh** — `.maestro/privacy_tests/09_navigation_with_refresh.yaml` (`.maestro/privacy_tests/09_navigation_with_refresh.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/privacy_tests`; read each helper before driving.

  - L9: `- runFlow:; file: ../shared/setup.yaml`
  - L13: `- assertVisible:; id: "searchEntry"`
  - L15: `- tapOn:; id: "searchEntry"`
  - L17: `- inputText: "https://www.search-company.site/#ad-id-5"`
  - L18: `- pressKey: Enter`
  - L21: `- assertVisible: "[Ad 5] SERP Ad (heuristic)"`
  - L22: `- tapOn: "[Ad 5] SERP Ad (heuristic)"`
  - L23: `- assertVisible:; text: "Publisher site"`
  - L25: `- tapOn:; id: "privacy-icon-shield.button"`
  - L27: `- assertVisible:; text: "View Tracker Companies"`
  - L29: `- tapOn:; text: "View Tracker Companies"`
  - L31: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L33: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L35: `- assertVisible:; text: ".*Ad Company"`
  - L37: `- assertVisible:; text: "ad-company.site"`
  - L39: `- tapOn: "Back"`
  - L40: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L42: `- tapOn:; text: "View Non-Tracker Companies"`
  - L44: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L46: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L48: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L50: `- assertVisible:; text: "How our search ads impact our protections"`
  - L52: `- assertVisible:; text: ".*Ad Company"`
  - L54: `- assertVisible:; text: "convert.ad-company.site"`
  - L56: `- tapOn: "Back"`
  - L57: `- tapOn: "Done"`
  - L58: `- assertVisible:; text: "Publisher site"`
  - L60: `- tapOn:; text: "Publisher site"`
  - L62: `- tapOn:; text: "High five!"; optional: true`
  - L65: `- assertVisible:; text: "Green T-shirt"`
  - L67: `- tapOn:; text: "Green T-shirt"`
  - L69: `- assertVisible:; text: "Buy now"`
  - L71: `- tapOn:; text: "Buy now"`
  - L73: `- assertVisible:; text: "Pay with payment-company!"`
  - L75: `- tapOn:; text: "Pay with payment-company!"`
  - L77: `- assertVisible:; text: "Pay First Party"`
  - L79: `- tapOn:; id: "privacy-icon-shield.button"`
  - L81: `- assertVisible:; text: "View Tracker Companies"`
  - L83: `- tapOn:; text: "View Tracker Companies"`
  - L85: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L87: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L89: `- assertVisible:; text: ".*Ad Company"`
  - L91: `- assertVisible:; text: "ad-company.site"`
  - L93: `- assertVisible:; text: "convert.ad-company.site"`
  - L95: `- tapOn: "Back"`
  - L96: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L98: `- tapOn:; text: "View Non-Tracker Companies"`
  - L100: `- assertVisible:; text: "We did not identify any requests from third-party domains."`
  - L102: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L104: `- tapOn: "Back"`
  - L105: `- tapOn: "Done"`
  - L106: `- assertVisible: "Refresh Page"`
  - L107: `- tapOn: "Refresh Page"`
  - L108: `- assertVisible:; text: "Pay"`
  - L110: `- tapOn:; text: "Pay"`
  - L112: `- tapOn:; id: "privacy-icon-shield.button"`
  - L114: `- assertVisible:; text: "View Tracker Companies"`
  - L116: `- tapOn:; text: "View Tracker Companies"`
  - L118: `- assertVisible:; text: "The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`
  - L120: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L122: `- assertVisible:; text: ".*Ad Company"`
  - L124: `- assertVisible:; text: "ad-company.site"`
  - L126: `- tapOn: "Back"`
  - L127: `- assertVisible:; text: "View Non-Tracker Companies"`
  - L129: `- tapOn:; text: "View Non-Tracker Companies"`
  - L131: `- assertVisible:; text: "The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`
  - L133: `- assertVisible:; text: "About our Web Tracking Protections"`
  - L135: `- assertVisible:; text: "The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`
  - L137: `- assertVisible:; text: "How our search ads impact our protections"`
  - L139: `- assertVisible:; text: ".*Ad Company"`
  - L141: `- assertVisible:; text: "convert.ad-company.site"`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

A single successful checkout does not cover cross-tab or cross-site lifetime rules. Test sites and privacy configuration must be reachable. Dax tips or optional High five! can cover content. Restart variant must retain state. Expanded dashboard text and the actual loaded/blocked domains are required proof; shield visibility alone is insufficient.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
