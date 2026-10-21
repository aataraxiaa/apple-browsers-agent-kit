# Subscription settings and setup re-entry

Source-derived coverage only; no paid, authenticated or backend path was executed.

## Sub-features

- `subscription-settings-state` distinguishes signed out, activating, expired, trial and subscribed configurations.
- `subscription-settings-setup` exposes the Continue Setup re-entry card for eligible remaining setup.
- `subscription-settings-devices` displays Add to Device and account email management for subscribed, expired or trial configurations.
- `subscription-settings-plans` displays applicable plan/billing rows and transient errors.

## How to get to it (user POV)

Browsing Menu → Settings → the visible subscription management row. Its localized title comes from `UserText.settingsPProManageSubscription`; inspect the current snapshot before choosing it. Signed-out users do not qualify for the subscription-settings destination. Do not create a subscription or modify an account to make the row appear as part of a default verification pass.

## Driving it with MobileBuildMCP

Sources in the active checkout:

- `iOS/DuckDuckGo/Settings/Views/Sections/Subscription/SettingsSubscriptionView.swift`
- `iOS/DuckDuckGo/Settings/Views/SettingsRootView.swift` (`subscriptionSettingsConfiguration`)
- `iOS/DuckDuckGo/Subscription/Views/SubscriptionSettingsView.swift` (`SubscriptionSettingsViewV2`)
- `iOS/DuckDuckGo/Subscription/Onboarding/Navigation/SubscriptionOnboardingFlowViewModel.swift`

1. On an explicitly authorized disposable account fixture, retain the known account state outside screenshots; capture Settings and its subscription row using `snapshot_ui`. Match the row's actual label, tap its current elementRef and wait for the management title. Keep account email and recovery material out of proof artifacts.
2. The source chooses no destination when signed out; activating when signed in but subscription or entitlements are missing; expired when inactive; trial when active and trial offer applies; otherwise subscribed. Compare only against the fixture state actually established. A single account does not prove every configuration.
3. Capture header, displayed sections, loading completion and applicable plan/billing text. The source shows devices for subscribed/expired/trial and hides them while activating. Upgrade and downgrade notices are conditional; absence is not a failure without corresponding fixture eligibility.
4. If the source-driven setup card is visible, inspect the actual Continue Setup label and choose its current elementRef. Wait for the first onboarding screen and record it. Eligibility/entitlements are fetched asynchronously; repeated tapping must not launch multiple flows. Dismiss the opened cover through its visible close affordance and verify management returns. Do not complete VPN, PIR, identity or subscription activation steps without their separately authorized disposable fixtures.
5. Plans, management, email edit, restore and downgrade actions can enter external providers or mutate the account. Mapping them does not authorize changes; stop at navigation presentation when that presentation is authorized. Record any backend, storefront, entitlement or region dependency as unresolved.

## Gotchas

`SubscriptionSettingsViewV2` refreshes onboarding state asynchronously. Only subscribed/trial count as active setup candidates. PIR availability changes the checklist and destination; a missing iOS provider can lead to the desktop fallback. The source has no dedicated stable identifiers on these subscription rows, so selectors must come from the current localized snapshot. Debug mock onboarding is separate from production subscription state and cannot prove entitlements or successful payment. No paid-state runtime acceptance is claimed by this map.
