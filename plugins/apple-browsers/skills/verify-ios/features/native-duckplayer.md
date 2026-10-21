# Native Duck Player

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `02_serp_off_organic` — `.maestro/duckplayer_native/02_serp_off_organic.yaml`.
- `03_serp_off_videos` — `.maestro/duckplayer_native/03_serp_off_videos.yaml`.
- `05_serp_on_organic` — `.maestro/duckplayer_native/05_serp_on_organic.yaml`.
- `06_serp_on_videos` — `.maestro/duckplayer_native/06_serp_on_videos.yaml`.
- `07_youtube_dont_show` — `.maestro/duckplayer_native/07_youtube_dont_show.yaml`.
- `08_youtube_let_me_choose` — `.maestro/duckplayer_native/08_youtube_let_me_choose.yaml`.
- `09_youtube_auto` — `.maestro/duckplayer_native/09_youtube_auto.yaml`.
- `10_youtube_open_settings` — `.maestro/duckplayer_native/10_youtube_open_settings.yaml`.
- `11_serp_watch_in_youtube` — `.maestro/duckplayer_native/11_serp_watch_in_youtube.yaml`.
- `12_youtube_watch_in_youtube` — `.maestro/duckplayer_native/12_youtube_watch_in_youtube.yaml`.
- `close_player` (helper/configuration) — `.maestro/duckplayer_native/shared/close_player.yaml`.
- `close_settings` (helper/configuration) — `.maestro/duckplayer_native/shared/close_settings.yaml`.
- `constants` (helper/configuration) — `.maestro/duckplayer_native/shared/constants.yaml`.
- `duckplayer_is_visible` (helper/configuration) — `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
- `load_serp_url` (helper/configuration) — `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
- `load_youtube_url` (helper/configuration) — `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
- `open_settings` (helper/configuration) — `.maestro/duckplayer_native/shared/open_settings.yaml`.
- `pill_is_visible` (helper/configuration) — `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.
- `tap_serp_title` (helper/configuration) — `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.

## How to get to it (user POV)

Browsing Menu → Settings → Duck Player. Set Search-result playback and YouTube policy as specified; navigate the exact SERP or YouTube fixture, then choose the video or native-player action shown in the scenario.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### 02_serp_off_organic

Source: `.maestro/duckplayer_native/02_serp_off_organic.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_serp_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap text `"${output.serpToggleOn}"`, index `0`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
5. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
8. Require visible label/text `"${output.youtubeMobileDomain}"`.
9. Follow visible behavior from `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.

### 03_serp_off_videos

Source: `.maestro/duckplayer_native/03_serp_off_videos.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_serp_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap text `"${output.serpToggleOn}"`, index `0`. Coordinate/ordinal hint only: obtain a current identifiable elementRef first.
5. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
7. Require visible label/text `"${output.videosTabLabel}"`.
8. Tap label/text `"${output.videosTabLabel}"`.
9. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
10. Require visible label/text `"${output.youtubeMobileDomain}"`.
11. Follow visible behavior from `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.

### 05_serp_on_organic

Source: `.maestro/duckplayer_native/05_serp_on_organic.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/load_serp_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`, `.maestro/duckplayer_native/shared/close_player.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
4. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
5. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
6. Require visible identifier `"${output.watchOnYoutubeLabel}"`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.

### 06_serp_on_videos

Source: `.maestro/duckplayer_native/06_serp_on_videos.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/load_serp_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`, `.maestro/duckplayer_native/shared/close_player.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
4. Require visible label/text `"${output.videosTabLabel}"`.
5. Tap label/text `"${output.videosTabLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
8. Require visible identifier `"${output.watchOnYoutubeLabel}"`.
9. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.

### 07_youtube_dont_show

Source: `.maestro/duckplayer_native/07_youtube_dont_show.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap identifier `"chevron.up.chevron.down"`.
5. Tap label/text `"${output.dontShowLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
8. Require visible label/text `"${output.videoTitle}"`.
9. Tap label/text `"${output.videoTitle}"`.
10. Require visible label/text `"${output.youtubeMobileDomain}"`.
11. Require absent identifier `"duckPlayerWelcomePill"`.
12. Require absent identifier `"${output.playInDuckPlayerLabel}"`.
13. Require absent identifier `"${output.resumeInDuckPlayerLabel}"`.

### 08_youtube_let_me_choose

Source: `.maestro/duckplayer_native/08_youtube_let_me_choose.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_youtube_url.yaml`, `.maestro/duckplayer_native/shared/pill_is_visible.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`, `.maestro/duckplayer_native/shared/close_player.yaml`, `.maestro/shared/use_firebutton.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap identifier `"chevron.up.chevron.down"`.
5. Tap label/text `"${output.letMeChooseLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
8. Require visible label/text `"${output.videoTitle}"`.
9. Tap label/text `"${output.videoTitle}"`.
10. Require visible label/text `"${output.youtubeMobileDomain}"`.
11. Follow visible behavior from `.maestro/duckplayer_native/shared/pill_is_visible.yaml`.
12. Tap identifier `"duckPlayerWelcomeButton"`.
13. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
14. Require visible identifier `"${output.openVideosHereLabel}"`.
15. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.
16. Require visible identifier `"${output.resumeInDuckPlayerLabel}"`.
17. Tap identifier `"${output.resumeInDuckPlayerLabel}"`.
18. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
19. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.
20. Require visible identifier `"${output.resumeInDuckPlayerLabel}"`.
21. Tap identifier `"${output.resumeInDuckPlayerLabel}"`.
22. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
23. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.
24. Follow visible behavior from `.maestro/shared/use_firebutton.yaml`.
25. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
26. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
27. Require visible identifier `"${output.playThisVideoInDuckPlayerLabel}"`.
28. Tap identifier `"${output.playThisVideoInDuckPlayerLabel}"`.
29. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.

### 09_youtube_auto

Source: `.maestro/duckplayer_native/09_youtube_auto.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_youtube_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`, `.maestro/duckplayer_native/shared/close_player.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap identifier `"chevron.up.chevron.down"`.
5. Tap label/text `"${output.openAutomaticallyLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
8. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
9. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
10. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.
11. Require visible identifier `"${output.resumeInDuckPlayerLabel}"`.

### 10_youtube_open_settings

Source: `.maestro/duckplayer_native/10_youtube_open_settings.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_youtube_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap identifier `"chevron.up.chevron.down"`.
5. Tap label/text `"${output.openAutomaticallyLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
8. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
9. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
10. Tap label/text `"${output.duckPlayerSettingsId}"`.
11. Require visible identifier `"SettingsDuckPlayerHero"`.

### 11_serp_watch_in_youtube

Source: `.maestro/duckplayer_native/11_serp_watch_in_youtube.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/load_serp_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/load_serp_url.yaml`.
4. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
5. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
6. Require visible identifier `"${output.watchOnYoutubeLabel}"`.
7. Require visible identifier `"${output.chevronUpId}"`.
8. Tap identifier `"${output.chevronUpId}"`.
9. Require absent identifier `"${output.watchOnYoutubeLabel}"`.
10. Tap identifier `"${output.chevronUpId}"`.
11. Tap identifier `"${output.watchOnYoutubeLabel}"`.
12. Require visible label/text `"${output.youtubeMobileDomain}"`.
13. Require absent identifier `"${output.playThisVideoInDuckPlayerLabel}"`.
14. Require absent identifier `"${output.playInDuckPlayerLabel}"`.

### 12_youtube_watch_in_youtube

Source: `.maestro/duckplayer_native/12_youtube_watch_in_youtube.yaml`. Tags: `["iphone", "duckplayer_native"]`.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`, `.maestro/shared/setup.yaml`, `.maestro/duckplayer_native/shared/open_settings.yaml`, `.maestro/duckplayer_native/shared/close_settings.yaml`, `.maestro/duckplayer_native/shared/load_youtube_url.yaml`, `.maestro/duckplayer_native/shared/tap_serp_title.yaml`, `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`, `.maestro/duckplayer_native/shared/close_player.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Follow visible behavior from `.maestro/shared/setup.yaml`.
3. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
4. Tap identifier `"chevron.up.chevron.down"`.
5. Tap label/text `"${output.letMeChooseLabel}"`.
6. Follow visible behavior from `.maestro/duckplayer_native/shared/close_settings.yaml`.
7. Follow visible behavior from `.maestro/duckplayer_native/shared/load_youtube_url.yaml`.
8. Follow visible behavior from `.maestro/duckplayer_native/shared/tap_serp_title.yaml`.
9. Require visible label/text `"${output.youtubeMobileDomain}"`.
10. Require visible identifier `"duckPlayerWelcomePill"`.
11. Tap identifier `"duckPlayerWelcomeButton"`.
12. Follow visible behavior from `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`.
13. Require visible identifier `"${output.openVideosHereLabel}"`.
14. Require visible identifier `"${output.chevronUpId}"`.
15. Tap identifier `"${output.chevronUpId}"`.
16. Require absent identifier `"${output.openVideosHereLabel}"`.
17. Tap identifier `"${output.chevronUpId}"`.
18. Tap label/text `"${output.watchInYoutubeOption}"`.
19. Follow visible behavior from `.maestro/duckplayer_native/shared/close_player.yaml`.
20. Follow visible behavior from `.maestro/duckplayer_native/shared/open_settings.yaml`.
21. Require visible label/text `"${output.openAutomaticallyLabel}"`.

### close_player

Source: `.maestro/duckplayer_native/shared/close_player.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Tap identifier `"${output.closeButtonId}"`.

### close_settings

Source: `.maestro/duckplayer_native/shared/close_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Tap label/text `"${output.settingsLabel}"`.
3. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
4. Tap label/text `"${output.doneLabel}"`.
5. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### constants

Source: `.maestro/duckplayer_native/shared/constants.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Fixture constant/assertion expression `"${output.videoTitle = 'DuckDuckGo vs Google: 5 Reasons You Should Switch'}"`; read its meaning only, never execute as a simulator driver.
2. Fixture constant/assertion expression `"${output.videoTitle2 = 'DuckDuckGo vs Google: 5 Reasons You Should Switch - YouTube'}"`; read its meaning only, never execute as a simulator driver.
3. Fixture constant/assertion expression `"${output.videoSearchUrl = 'https://duckduckgo.com/?q=%22DuckDuckGo+vs+Google%3A+5+Reasons+You+Should+Switch%E2%80%9D+site%3Ayoutube.com&atb=v469-1-wb&ia=web'}"`; read its meaning only, never execute as a simulator driver.
4. Fixture constant/assertion expression `"${output.youtubeSearchUrl = 'https://www.youtube.com/results?search_query=%22DuckDuckGo+vs+Google%3A+5+Reasons+You+Should+Switch%22&sp=EgIQAQ%253D%253D'}"`; read its meaning only, never execute as a simulator driver.
5. Fixture constant/assertion expression `"${output.searchEntryId = 'searchEntry'}"`; read its meaning only, never execute as a simulator driver.
6. Fixture constant/assertion expression `"${output.closeButtonId = 'xmark'}"`; read its meaning only, never execute as a simulator driver.
7. Fixture constant/assertion expression `"${output.chevronUpId = 'chevron.up'}"`; read its meaning only, never execute as a simulator driver.
8. Fixture constant/assertion expression `"${output.duckPlayerSettingsId = 'DuckPlayerOpenSettings'}"`; read its meaning only, never execute as a simulator driver.
9. Fixture constant/assertion expression `"${output.duckPlayerLabel = 'Duck Player'}"`; read its meaning only, never execute as a simulator driver.
10. Fixture constant/assertion expression `"${output.settingsLabel = 'Settings'}"`; read its meaning only, never execute as a simulator driver.
11. Fixture constant/assertion expression `"${output.doneLabel = 'Done'}"`; read its meaning only, never execute as a simulator driver.
12. Fixture constant/assertion expression `"${output.browsingMenuLabel = 'Browsing Menu'}"`; read its meaning only, never execute as a simulator driver.
13. Fixture constant/assertion expression `"${output.watchOnYoutubeLabel = 'Watch on YouTube'}"`; read its meaning only, never execute as a simulator driver.
14. Fixture constant/assertion expression `"${output.openVideosHereLabel = 'Open YouTube videos here'}"`; read its meaning only, never execute as a simulator driver.
15. Fixture constant/assertion expression `"${output.youtubeMobileDomain = 'm.youtube.com'}"`; read its meaning only, never execute as a simulator driver.
16. Fixture constant/assertion expression `"${output.playInDuckPlayerLabel = 'Play in Duck Player'}"`; read its meaning only, never execute as a simulator driver.
17. Fixture constant/assertion expression `"${output.playThisVideoInDuckPlayerLabel = 'Play this video in Duck Player'}"`; read its meaning only, never execute as a simulator driver.
18. Fixture constant/assertion expression `"${output.resumeInDuckPlayerLabel = 'Resume in Duck Player'}"`; read its meaning only, never execute as a simulator driver.
19. Fixture constant/assertion expression `"${output.dontShowLabel = \"Don't Show\"}"`; read its meaning only, never execute as a simulator driver.
20. Fixture constant/assertion expression `"${output.videosTabLabel = 'Videos'}"`; read its meaning only, never execute as a simulator driver.
21. Fixture constant/assertion expression `"${output.openAutomaticallyLabel = 'Open Automatically'}"`; read its meaning only, never execute as a simulator driver.
22. Fixture constant/assertion expression `"${output.letMeChooseLabel = 'Let me choose'}"`; read its meaning only, never execute as a simulator driver.
23. Fixture constant/assertion expression `"${output.toggleOff = '0'}"`; read its meaning only, never execute as a simulator driver.
24. Fixture constant/assertion expression `"${output.toggleOn = '1'}"`; read its meaning only, never execute as a simulator driver.
25. Fixture constant/assertion expression `"${output.serpToggleOn = '1'}"`; read its meaning only, never execute as a simulator driver.
26. Fixture constant/assertion expression `"${output.watchInYoutubeOption = '0'}"`; read its meaning only, never execute as a simulator driver.

### duckplayer_is_visible

Source: `.maestro/duckplayer_native/shared/duckplayer_is_visible.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Require visible label/text `"${output.duckPlayerLabel}"`.
3. Require visible identifier `"${output.closeButtonId}"`.
4. Require visible label/text `"${output.duckPlayerSettingsId}"`.
5. Require visible identifier `"${output.chevronUpId}"`.

### load_serp_url

Source: `.maestro/duckplayer_native/shared/load_serp_url.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Require visible identifier `"${output.searchEntryId}"`.
3. Tap identifier `"${output.searchEntryId}"`.
4. Enter `"${output.videoSearchUrl}"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### load_youtube_url

Source: `.maestro/duckplayer_native/shared/load_youtube_url.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Require visible identifier `"${output.searchEntryId}"`.
3. Tap identifier `"${output.searchEntryId}"`.
4. Enter `"${output.youtubeSearchUrl}"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
7. Tap label/text `"Refresh page"`.
8. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### open_settings

Source: `.maestro/duckplayer_native/shared/open_settings.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

Dependencies: `.maestro/duckplayer_native/shared/constants.yaml`.

1. Follow visible behavior from `.maestro/duckplayer_native/shared/constants.yaml`.
2. Tap label/text `"${output.browsingMenuLabel}"`.
3. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
4. Tap label/text `"${output.settingsLabel}"`.
5. Scroll toward `"DOWN"` until label/text `"${output.duckPlayerLabel}"` is fully visible; center it before tapping. Refresh the snapshot.
6. Tap label/text `"${output.duckPlayerLabel}"`.
7. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.

### pill_is_visible

Source: `.maestro/duckplayer_native/shared/pill_is_visible.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
2. Conditional branch `{"visible": "duckPlayerWelcomePill"}`: Require visible label/text `"duckPlayerWelcomePill"`. Require absent label/text `"duckPlayerPill"`.
3. Conditional branch `{"visible": "duckPlayerPill"}`: Require visible label/text `"duckPlayerPill"`. Require absent label/text `"duckPlayerWelcomePill"`.

### tap_serp_title

Source: `.maestro/duckplayer_native/shared/tap_serp_title.yaml`. Tags: `[]`. Helper/configuration, not a complete acceptance scenario.

1. Source timing/gesture shorthand `"waitForAnimationToEnd"`; inspect destination state and supported provider tool.
2. Conditional branch `{"visible": "${output.videoTitle}"}`: Tap label/text `"${output.videoTitle}"`.
3. Conditional branch `{"visible": "${output.videoTitle2}"}`: Tap label/text `"${output.videoTitle2}"`.

## Gotchas

Native player and classic player are distinct families. Load shared/constants.yaml values as reference data, not scripts. YouTube network/content and layout can drift. A play/pill assertion does not establish actual playback or audio. Index-based switch targets require inspecting current labeled controls; do not blindly choose a row by ordinal.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
