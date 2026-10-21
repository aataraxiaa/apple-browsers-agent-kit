# Duck Player Classic mode and entry routes

Choose Always, Ask Every Time or Never and verify playback routing from direct duck:// links, search organic/video results and YouTube. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- 01 direct duckplayer
- 02 always serp organic
- 03 always serp videos
- 04 always youtube
- 06 ask serp videos
- 07 ask youtube
- 08 never serp organic
- 09 never serp videos
- 10 never youtube
- 11 watch on youtube

## How to get to it (user POV)

On iPad `Browser.OmniBar.Button.BrowsingMenu` → Settings → Duck Player → `chevron.up.chevron.down`. Use Always, Ask Every Time or Never. Direct route is `duck://player/3ml7yeKBUhc`; YouTube route is `https://www.youtube.com/watch?v=3ml7yeKBUhc`.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Always: test direct route and organic/video/YouTube entries, asserting Duck Player and its controls. Ask Every Time: test organic/video/YouTube entries and the offered Watch In Duck Player choice. Never: test organic/video/YouTube paths and assert YouTube origin, Sign In and YouTube Home instead. On the player choose Watch on YouTube and prove the external page. Exact search URL and video title come from shared/constants.yaml; keep all 11 routes as separate scenarios.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**01 direct duckplayer** — `.maestro/duckplayer_classic/01_direct_duckplayer.yaml` (`.maestro/duckplayer_classic/01_direct_duckplayer.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L18: `- runFlow:; file: shared/open_settings.yaml`
  - L21: `- tapOn:; id: chevron.up.chevron.down`
  - L25: `- tapOn: ${output.alwaysLabel}`
  - L28: `- runFlow:; file: shared/close_settings.yaml`
  - L32: `- runFlow:; file: shared/load_duck_url.yaml`
  - L36: `- runFlow:; file: shared/duckplayer_is_visible.yaml`

**02 always serp organic** — `.maestro/duckplayer_classic/02_always_serp_organic.yaml` (`.maestro/duckplayer_classic/02_always_serp_organic.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L17: `- runFlow:; file: shared/open_settings.yaml`
  - L20: `- tapOn:; id: chevron.up.chevron.down`
  - L24: `- tapOn: ${output.alwaysLabel}`
  - L27: `- runFlow:; file: shared/close_settings.yaml`
  - L31: `- runFlow:; file: shared/load_serp_url.yaml`
  - L35: `- waitForAnimationToEnd`
  - L38: `- tapOn:; text: ${output.videoTitle}.*`
  - L42: `- runFlow:; file: shared/duckplayer_is_visible.yaml`

**03 always serp videos** — `.maestro/duckplayer_classic/03_always_serp_videos.yaml` (`.maestro/duckplayer_classic/03_always_serp_videos.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L17: `- runFlow:; file: shared/open_settings.yaml`
  - L20: `- tapOn:; id: chevron.up.chevron.down`
  - L24: `- tapOn: ${output.alwaysLabel}`
  - L27: `- runFlow:; file: shared/close_settings.yaml`
  - L31: `- runFlow:; file: shared/load_serp_url.yaml`
  - L35: `- tapOn: ${output.videosTabLabel}`
  - L38: `- waitForAnimationToEnd`
  - L41: `- tapOn:; text: ${output.videoTitle}`
  - L45: `- runFlow:; file: shared/duckplayer_is_visible.yaml`

**04 always youtube** — `.maestro/duckplayer_classic/04_always_youtube.yaml` (`.maestro/duckplayer_classic/04_always_youtube.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L10: `- runFlow:; file: shared/constants.yaml`
  - L14: `- runFlow:; file: ../shared/setup.yaml`
  - L18: `- runFlow:; file: shared/open_settings.yaml`
  - L21: `- tapOn:; id: chevron.up.chevron.down`
  - L25: `- tapOn: ${output.alwaysLabel}`
  - L28: `- runFlow:; file: shared/close_settings.yaml`
  - L32: `- runFlow:; file: shared/load_youtube_url.yaml`
  - L36: `- runFlow:; file: shared/duckplayer_is_visible.yaml`

**06 ask serp videos** — `.maestro/duckplayer_classic/06_ask_serp_videos.yaml` (`.maestro/duckplayer_classic/06_ask_serp_videos.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L17: `- runFlow:; file: shared/open_settings.yaml`
  - L20: `- tapOn:; id: chevron.up.chevron.down`
  - L24: `- tapOn: ${output.askLabel}`
  - L27: `- runFlow:; file: shared/close_settings.yaml`
  - L31: `- runFlow:; file: shared/load_serp_url.yaml`
  - L35: `- tapOn: ${output.videosTabLabel}`
  - L38: `- waitForAnimationToEnd`
  - L41: `- tapOn:; text: ${output.videoTitle}`
  - L45: `- waitForAnimationToEnd`
  - L48: `- tapOn:; text: ${output.watchInDuckPlayerLabel}`
  - L52: `- waitForAnimationToEnd`
  - L55: `- runFlow:; file: shared/duckplayer_is_visible.yaml`

**07 ask youtube** — `.maestro/duckplayer_classic/07_ask_youtube.yaml` (`.maestro/duckplayer_classic/07_ask_youtube.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L10: `- runFlow:; file: shared/constants.yaml`
  - L14: `- runFlow:; file: ../shared/setup.yaml`
  - L18: `- runFlow:; file: shared/open_settings.yaml`
  - L21: `- tapOn:; id: chevron.up.chevron.down`
  - L25: `- tapOn: ${output.askLabel}`
  - L28: `- runFlow:; file: shared/close_settings.yaml`
  - L32: `- runFlow:; file: shared/load_youtube_url.yaml`
  - L36: `- waitForAnimationToEnd`
  - L40: `- runFlow:; when:; visible: ${output.turnOnDuckPlayerLabel}; commands:; - tapOn: ${output.turnOnDuckPlayerLabel}; - runFlow:; file: shared/duckplayer_is_visible.yaml`

**08 never serp organic** — `.maestro/duckplayer_classic/08_never_serp_organic.yaml` (`.maestro/duckplayer_classic/08_never_serp_organic.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L17: `- runFlow:; file: shared/open_settings.yaml`
  - L20: `- tapOn:; id: chevron.up.chevron.down`
  - L24: `- tapOn: ${output.neverLabel}`
  - L27: `- runFlow:; file: shared/close_settings.yaml`
  - L31: `- runFlow:; file: shared/load_serp_url.yaml`
  - L35: `- assertVisible: ${output.videoTitle}.*`
  - L36: `- tapOn:; text: ${output.videoTitle}.*`
  - L40: `- waitForAnimationToEnd`
  - L43: `- runFlow:; file: shared/youtube_is_visible.yaml`

**09 never serp videos** — `.maestro/duckplayer_classic/09_never_serp_videos.yaml` (`.maestro/duckplayer_classic/09_never_serp_videos.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L17: `- runFlow:; file: shared/open_settings.yaml`
  - L20: `- tapOn:; id: chevron.up.chevron.down`
  - L24: `- tapOn: ${output.neverLabel}`
  - L27: `- runFlow:; file: shared/close_settings.yaml`
  - L31: `- runFlow:; file: shared/load_serp_url.yaml`
  - L35: `- tapOn: ${output.videosTabLabel}`
  - L38: `- waitForAnimationToEnd`
  - L41: `- tapOn:; text: ${output.videoTitle}`
  - L45: `- waitForAnimationToEnd`
  - L48: `- runFlow:; file: shared/youtube_is_visible.yaml`

**10 never youtube** — `.maestro/duckplayer_classic/10_never_youtube.yaml` (`.maestro/duckplayer_classic/10_never_youtube.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L10: `- runFlow:; file: shared/constants.yaml`
  - L14: `- runFlow:; file: ../shared/setup.yaml`
  - L18: `- runFlow:; file: shared/open_settings.yaml`
  - L21: `- tapOn:; id: chevron.up.chevron.down`
  - L25: `- tapOn: ${output.neverLabel}`
  - L28: `- runFlow:; file: shared/close_settings.yaml`
  - L32: `- runFlow:; file: shared/load_youtube_url.yaml`
  - L36: `- waitForAnimationToEnd`
  - L39: `- runFlow:; file: shared/youtube_is_visible.yaml`

**11 watch on youtube** — `.maestro/duckplayer_classic/11_watch_on_youtube.yaml` (`.maestro/duckplayer_classic/11_watch_on_youtube.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/duckplayer_classic`; read each helper before driving.

  - L9: `- runFlow:; file: shared/constants.yaml`
  - L13: `- runFlow:; file: ../shared/setup.yaml`
  - L18: `- runFlow:; file: shared/open_settings.yaml`
  - L21: `- tapOn:; id: chevron.up.chevron.down`
  - L25: `- tapOn: ${output.alwaysLabel}`
  - L28: `- runFlow:; file: shared/close_settings.yaml`
  - L32: `- runFlow:; file: shared/load_duck_url.yaml`
  - L36: `- runFlow:; file: shared/duckplayer_is_visible.yaml`
  - L39: `- tapOn:; point: "50%,15%"`
  - L42: `- tapOn:; text: ${output.watchOnYoutubeLabel}`
  - L45: `- waitForAnimationToEnd`
  - L47: `- runFlow:; file: shared/youtube_is_visible.yaml`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Sources tag these flows ipad. `iOS/DuckDuckGo/DuckPlayer/DuckPlayerSettings.swift:298-307` enables Classic with `.duckPlayer` and restricts native UI to iPhone. Pin `-ff.duckPlayer true`, `-ff.duckPlayerNativeUI false`, and `-isRunningUITests true` as string launch arguments through the parent driver. Native UI can be forced by internal-user status on iPhone, so preserve the iPad requirement. `FeatureFlag.swift:710-715` lists the remote configuration sources; report a missing Classic setting or disabled player if the effective flag does not produce it. The historical player visibility helper taps 50%,15% to reveal controls: replace with a real snapshot elementRef, or report blocked visibility proof if the web video exposes no usable control. YouTube availability/consent and search ranking can change.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
