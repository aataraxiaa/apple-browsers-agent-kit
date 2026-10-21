---
name: build-ios
description: Resolve a matching DuckDuckGo apple-browsers iOS build, reusing a verified app or building through MobileBuildMCP. Use with an explicitly selected Apple browsers checkout. Excludes macOS and Android.
---

# Build Apple browsers iOS

Read [the provider policy](../../policy.md) and the caller's checkout AGENTS.md. Confirm `DuckDuckGo.xcworkspace` and `iOS/DuckDuckGo-iOS.xcodeproj` exist. Keep build products and receipts in an external `review-artifacts` directory, using `~/.agents/bin/agent-task-dir` when available.

Use the bundled MobileBuildMCP tools. Inspect their exposed schemas. Use explicit target schemas; never set, clear, or switch defaults or profiles. Pass the exact `simulatorId` UUID on every simulator-targeted call. Use `list_sims` to resolve the assigned target and requested idiom. Concurrent builders need separate derived-data directories; agents driving UI need separate assigned simulators.

## Resolve the app

1. Record the absolute checkout, HEAD, source fingerprint, workspace, scheme `iOS Browser`, configuration `Debug`, Xcode/toolchain and SDK identity, simulator platform and architecture, and external `derivedDataPath`.
2. Look for a completed build receipt matching those inputs except `derivedDataPath`, which records the product location and need not match a new builder's directory. Reuse its `.app` only if the directory exists, its content hash matches the receipt, and `get_app_bundle_id` confirms `com.duckduckgo.mobile.ios`. A matching commit alone is insufficient.
3. If the receipt or product is missing or differs, call `build_sim` with explicit `workspacePath`, `scheme`, `configuration`, `derivedDataPath`, and `simulatorId`. For a project build, use `projectPath` instead of `workspacePath`. Supply any other required fields from the exposed schema, including the simulator platform where required. Do not rely on a simulator name or inherited build settings.
4. After a successful build, call `get_sim_app_path` with the same explicit build fields and `simulatorId`, plus `platform:"iOS Simulator"`. Check the returned app's bundle ID and content hash. Recompute the source fingerprint; if inputs changed during the build, do not mark the product reusable. Otherwise write a completed receipt beside the evidence.

Use one external `build-receipt.json` beside each build product. Store `schemaVersion:1`, `status:"completed"`, `checkoutPath`, `head`, `sourceHash`, `workspacePath` or `projectPath`, `scheme`, `configuration`, `toolchain`, `sdk`, `platform`, `architecture`, `buildOverrides`, `derivedDataPath`, `appPath`, `bundleId`, and `appHash`. Compare all build inputs before reuse; paths to derived data and the product are locations, not cache keys.

For both hashes, use SHA-256 over UTF-8 JSON with sorted keys and compact separators. The manifest is an array sorted by relative path, with entries `[path, type, executable, contentHash]`; `type` is `file` or `symlink`, `executable` is a boolean, and `contentHash` is SHA-256 of file bytes or the UTF-8 symlink target. Do not follow symlinks. Hash the app manifest array directly. For `sourceHash`, hash `{ "files": manifest, "submodules": [[path, head]] }`, sorting submodules by path and including their working files in the manifest under checkout-relative paths. The source fingerprint must cover tracked file contents and modes, local additions/deletions, non-ignored untracked source files, submodule revisions and local changes, and any ignored files used as build inputs. Hash a deterministic, path-sorted manifest. Record dependency lockfiles and explicit build overrides too. If an input cannot be identified reliably, build instead of reusing. Hash the `.app` contents and relative paths, including resources and symlink targets; executable identity alone misses changed resources.

Check tool errors before accepting a product. A compile-only request ends here and does not authorize installing, launching, or resetting a simulator. Return whether the app was reused or built, source identity, app path, bundle ID, and receipt/evidence path. Report provider failures without switching build tools.
