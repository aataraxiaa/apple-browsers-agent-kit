# Apple browsers iOS provider policy

Use build-ios and verify-ios with MobileBuildMCP. Pass your owned simulator UUID as simulatorId on every targeted call, plus explicit build inputs and a separate derivedDataPath for concurrent builds. Never change shared session defaults or profiles, including sync_xcode_defaults. Keep Xcode auto-sync disabled. Report unsupported operations. The control panel may attach, detach, and take screenshots. Shell simctl is limited to pbcopy or pbpaste with an explicit simulator UUID. This policy does not select a provider for macOS work.
