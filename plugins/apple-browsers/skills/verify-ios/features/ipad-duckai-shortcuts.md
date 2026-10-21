# iPad Duck.ai chrome shortcuts

Open Duck.ai and contextual actions from the browser chrome; manage shortcut availability in Settings and in the contextual sheet. Source-grounded draft at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this document was executed.

## Sub-features

- duckai chrome shortcut contextual sheet toggle
- duckai chrome shortcut global disable
- duckai chrome shortcut menu actions
- duckai chrome shortcut settings toggle
- duckai chrome shortcut tap opens duckai
- duckai chrome shortcut visible on duckai page

## How to get to it (user POV)

On iPad use `Browser.TabsBar.AIChatMenuButton`; Settings → AI Features → Manage Duck.ai Shortcuts exposes `Settings.AIChat.TabBarToggle`.

## Driving it with MobileBuildMCP

Preconditions: follow the parent verify-ios preparation using MobileBuildMCP, a matching app resolved by build-ios from the explicit checkout and a designated disposable simulator of the source tag’s idiom. Read `.maestro/AGENTS.md` and each linked setup helper. Preserve state for restart tests. Set actual launch flags through `iOS/Core/LaunchOptionsHandler.swift`; quote flag booleans and include internal-user status where required. Resolve source environment placeholders explicitly.

Call `snapshot_ui`, find the sourced identifier or label in that result, and pass its current `elementRef` to `tap` / `type_text` (the latter needs `elementRef` and `text`). Use a fresh snapshot after navigation. For each source assertion call `wait_for_ui` with the exposed `exists`, `gone` or `textContains` predicate and inspect the resulting snapshot. Do not pass YAML commands to any runner. Do not invent an elementRef from a source identifier. Translate longPressOn with long_press on the current elementRef. Submit every source pressKey: Enter through the current keyboard Return/Search/Go ref or a schema-checked key_press/key_sequence call before waiting for navigation. A runFlow setup command is a required dependency, not an optional hint.

Exercise every scenario below: open the menu, select each action, verify its resulting surface; toggle Tab Bar off and back on and assert shortcut absence then presence immediately on returning to the browser. Test global Duck.ai disable independently and the chrome on the Duck.ai page.

Retain before/action/after MCP results, UI snapshots, screenshots (`returnFormat:"path"`), exact launch arguments, UDID and fixture names in the parent external review-artifacts directory. Distinguish expected source assertions from observed results. Stop the app through `stop_app_sim`; preserve evidence and the simulator.

**duckai chrome shortcut contextual sheet toggle** — `.maestro/browser_features/duckai_chrome_shortcut_contextual_sheet_toggle.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_contextual_sheet_toggle.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L12: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L15: `- assertVisible:; id: "searchEntry"`
  - L17: `- tapOn:; id: "searchEntry"`
  - L19: `- inputText: "https://example.com"`
  - L20: `- pressKey: Enter`
  - L21: `- assertVisible: ".*Example Domain.*"`
  - L23: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L27: `- tapOn:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L29: `- waitForAnimationToEnd:; timeout: 2000`
  - L31: `- tapOn: "Ask About Page"`
  - L32: `- waitForAnimationToEnd:; timeout: 3000`
  - L34: `- assertVisible:; id: "AIChat.ContextualSheet"`
  - L39: `- tapOn:; id: "AIChat.ContextualSheet.CloseButton"`
  - L41: `- waitForAnimationToEnd:; timeout: 3000`
  - L43: `- assertNotVisible:; id: "AIChat.ContextualSheet"`
  - L47: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L49: `- tapOn:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L51: `- waitForAnimationToEnd:; timeout: 2000`
  - L53: `- assertVisible: "Ask About Page"`

**duckai chrome shortcut global disable** — `.maestro/browser_features/duckai_chrome_shortcut_global_disable.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_global_disable.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L12: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L14: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L18: `- runFlow: ../shared/open_ai_features_settings.yaml`
  - L19: `- assertVisible:; id: "Settings.AIFeatures.EnableToggle"`
  - L21: `- tapOn:; id: "Settings.AIFeatures.EnableToggle"`
  - L23: `- waitForAnimationToEnd`
  - L24: `- tapOn: "Settings"`
  - L25: `- tapOn: "Done"`
  - L26: `- waitForAnimationToEnd:; timeout: 2000`
  - L30: `- assertNotVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L34: `- runFlow: ../shared/open_ai_features_settings.yaml`
  - L35: `- tapOn:; id: "Settings.AIFeatures.EnableToggle"`
  - L37: `- waitForAnimationToEnd`
  - L38: `- tapOn: "Settings"`
  - L39: `- tapOn: "Done"`
  - L40: `- waitForAnimationToEnd:; timeout: 2000`
  - L44: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`

**duckai chrome shortcut menu actions** — `.maestro/browser_features/duckai_chrome_shortcut_menu_actions.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_menu_actions.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L12: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L15: `- tapOn:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L17: `- waitForAnimationToEnd:; timeout: 2000`
  - L19: `- assertVisible: "New Chat"`
  - L20: `- assertVisible: "Chats"`
  - L21: `- assertNotVisible: "Ask About Page"`
  - L24: `- tapOn:; point: "50%,90%"`
  - L26: `- waitForAnimationToEnd:; timeout: 2000`
  - L28: `- assertNotVisible: "New Chat"`
  - L30: `- assertVisible:; id: "searchEntry"`
  - L32: `- tapOn:; id: "searchEntry"`
  - L34: `- inputText: "https://example.com"`
  - L35: `- pressKey: Enter`
  - L36: `- assertVisible: ".*Example Domain.*"`
  - L39: `- tapOn:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L41: `- waitForAnimationToEnd:; timeout: 2000`
  - L43: `- assertVisible: "New Chat"`
  - L44: `- assertVisible: "Ask About Page"`
  - L45: `- assertVisible: "Chats"`

**duckai chrome shortcut settings toggle** — `.maestro/browser_features/duckai_chrome_shortcut_settings_toggle.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_settings_toggle.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L12: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L14: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L18: `- runFlow: ../shared/open_manage_duckai_shortcuts.yaml`
  - L19: `- tapOn:; id: "Settings.AIChat.TabBarToggle"`
  - L21: `- tapOn: "AI Features"`
  - L22: `- tapOn: "Settings"`
  - L23: `- tapOn: "Done"`
  - L24: `- waitForAnimationToEnd:; timeout: 2000`
  - L28: `- assertNotVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L32: `- runFlow: ../shared/open_manage_duckai_shortcuts.yaml`
  - L33: `- tapOn:; id: "Settings.AIChat.TabBarToggle"`
  - L35: `- tapOn: "AI Features"`
  - L36: `- tapOn: "Settings"`
  - L37: `- tapOn: "Done"`
  - L38: `- waitForAnimationToEnd:; timeout: 2000`
  - L42: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`

**duckai chrome shortcut tap opens duckai** — `.maestro/browser_features/duckai_chrome_shortcut_tap_opens_duckai.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_tap_opens_duckai.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L11: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L14: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L18: `- tapOn:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L20: `- waitForAnimationToEnd:; timeout: 2000`
  - L22: `- assertVisible: "New Chat"`
  - L24: `- tapOn: "New Chat"`
  - L25: `- waitForAnimationToEnd:; timeout: 3000`
  - L29: `- assertVisible: "Ask anything privately"`

**duckai chrome shortcut visible on duckai page** — `.maestro/browser_features/duckai_chrome_shortcut_visible_on_duckai_page.yaml` (`.maestro/browser_features/duckai_chrome_shortcut_visible_on_duckai_page.yaml`).

Translate every ordered behavior checkpoint below to provider calls. These are complete source commands, not commands to execute through Maestro. Resolve runFlow file paths relative to `.maestro/browser_features`; read each helper before driving.

  - L12: `- runFlow: ../shared/duckai_chrome_shortcut_setup.yaml`
  - L15: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`
  - L19: `- assertVisible:; id: "searchEntry"`
  - L21: `- tapOn:; id: "searchEntry"`
  - L23: `- inputText: "https://duck.ai"`
  - L24: `- pressKey: Enter`
  - L25: `- waitForAnimationToEnd:; timeout: 3000`
  - L29: `- assertVisible:; id: "Browser.TabsBar.AIChatMenuButton"`

## Gotchas

When a recipe references `.maestro/shared/setup.yaml`, its baseline clears app/keychain state and pins `ff.floatingUIAugust2026` to the string `false`. Establish these prerequisites through the parent skill before the first launch; do not assume installation resets state. Preserve state on later restart/restoration steps.

Use an iPad. Pin the four `aiChatChromeShortcutIPad`, `aiChatChromeMenuButtonIPad`, `contextualDuckAIMode`, `aiChatAddressBarRecentChats` flags and `browsingMenuSheetEnabledByDefault` as quoted true values from shared setup; global-disable scenarios override their own prerequisites. Menu shape depends on flags; never assume the old split chip.

All linked Maestro YAML is behavior reference only. Source selectors are candidates to locate in a live snapshot, not proof that the current build exposes them. An unsupported gesture, system sheet or unexposed text must be recorded as blocked coverage; do not silently substitute shell automation or coordinate taps.
