# Resource ownership

`PLUGIN_ROOT` is this installed plugin directory; resolve it from the loaded skill path. `CHECKOUT` is the selected Apple browsers Git worktree. Do not edit the installed cache. Keep the main checkout on main. Use one worktree per PR/branch, sequentially shared by its writers. Read-only helpers need none; retries reuse or safely clean up their prior worktree.

## Build cache

Run `python3 "$PLUGIN_ROOT/scripts/resources.py" prepare "$CHECKOUT"` before a build. When ownership validation and preparation succeed, builds and product lookups use `~/code/apple-browsers-worktrees/.dd/<worktree-name>`. No alternate per-run directories. A matching completed receipt must cover HEAD, local edits, build inputs and app content; see build-ios. Concurrent worktrees use distinct caches; builds in one worktree run sequentially.

Below 60 GiB free, preparation attempts cache-only reclamation in this order: absent worktrees, merged or confirmed remotely deleted branches, then least recently used. It preserves the current cache and live xcodebuild targets. Failed process inspection disables deletion. Low space and cleanup failures never stop the build; report them at the end. Resource preparation is best effort. If ownership metadata is malformed or conflicting, a managed path is a symlink, or preparation fails or times out, the hook warns and leaves the tool inputs unchanged. It does not select the uncertain cache or deny the build. Correct ownership before explicitly selecting that cache; uncertainty never authorizes deletion. Simulator UUID and shared-default protections still apply. No existing legacy DerivedData directories are migrated or deleted.

After a build, run `python3 "$PLUGIN_ROOT/scripts/resources.py" report "$CHECKOUT"` for size observations. The report-only Stop hook uses a half-second budget, local Git state and bounded/cached sizes. Unknown sizes are labelled; local upstream-gone observations are not remote deletion proof. Report failures produce a warning. It never deletes or returns a blocking decision.

## Simulator lease

Use MobileBuildMCP `list_sims` and normalize available devices into a JSON array with `uuid`, `name`, `os`, `idiom` (`phone` or `tablet`), and `state` (`Booted` or `Shutdown`). Keep the exact OS version requested. Supply a stable agent session ID and its live long-running process PID, not the temporary shell PID. The helper acquires claims atomically under `.sim-locks`; a dead owner's claim may be reclaimed, but uncertain ownership stays protected.

```sh
python3 "$PLUGIN_ROOT/scripts/resources.py" lease --inventory inventory.json --session "$SESSION_ID" --pid "$SESSION_PID" --os "$OS_VERSION" --idiom phone
```

Save the returned token externally as `token.json`. Reuse a matching booted device first, then a shutdown one. If none can be leased, save `{ "session": "the-session-id", "pid": 12345 }` with the actual stable identity to `identity.json`, select a supported runtime/device type from the provider inventory, then create:

```sh
python3 "$PLUGIN_ROOT/scripts/resources.py" create --token identity.json --name "agent-$SESSION_ID" --device-type "$DEVICE_TYPE" --runtime "$RUNTIME"
```

Creation returns `provenance` and an already-owned `lease`. Save the `lease` object as `token.json` and refresh provider inventory. Creation records live independently under `.sim-created`; an `agent-` name alone never authorizes deletion. Builds, booting, installs, app launches and all UI operations remain MobileBuildMCP calls with the explicit leased UUID. Pass derivedDataPath only where the tool schema supports it. Never change shared defaults.

On every success, failure or cancellation path, stop this run's app through MobileBuildMCP. Only if this run created the simulator, shut it down before releasing:

```sh
python3 "$PLUGIN_ROOT/scripts/resources.py" shutdown --token token.json
python3 "$PLUGIN_ROOT/scripts/resources.py" release --token token.json
```

For a reused simulator, run only `release`. Refresh inventory and run `delete-stale --inventory inventory.json` at the end. Collection deletes only recorded agent-created shutdown devices unused for seven days, with no live lease and matching UUID/name. Never erase a simulator. Never shut down or delete an existing developer simulator. The internal helper permits only simctl create/shutdown/delete; it is not an app-driver fallback.

## Explicit worktree cleanup

```sh
python3 "$PLUGIN_ROOT/scripts/resources.py" cleanup "$CHECKOUT"
```

Cleanup refuses the main checkout, dirty/untracked/ignored files, unpushed/unmerged commits and live builds. It removes the worktree with Git without force, deletes its managed cache, deletes the proven pushed/merged local branch, then prunes Git worktree metadata. A refusal leaves the source intact. No automatic hook removes worktrees.
