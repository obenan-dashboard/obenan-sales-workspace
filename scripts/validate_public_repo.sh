#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

fail=0

check_forbidden() {
  local label="$1"
  local pattern="$2"
  if rg -n -I --hidden \
    --glob '!.git/**' \
    --glob '!scripts/validate_public_repo.sh' \
    --glob '!tasks/todo.md' \
    -e "$pattern" .; then
    printf 'FAIL: %s\n' "$label" >&2
    fail=1
  fi
}

check_forbidden 'local absolute paths remain' '/Users/[A-Za-z0-9._-]+/'
check_forbidden 'real account selector remains in shared material' 'Switch the MCP to [0-9]+'
check_forbidden 'private authentication detail remains' 'session token|preprodapi\.obenan\.com'
check_forbidden 'unsafe connector scope remains' 'agency-scoped|can see every Obenan customer'
check_forbidden 'internal implementation path remains' 'apps/omnipulse/src|packages/obenan-(ui|theme)|origin/main|\.tsx`|\.scss`'
check_forbidden 'private customer structure remains' 'Le Pain Quotidien account|[0-9]+ users, [0-9]+ groups|[0-9]+ scheduled reports typical'
check_forbidden 'unapproved partner names remain' 'Mastercard|Visa'
check_forbidden 'stale proposal count remains' '~130 (directories|Verzeichnisse)'
check_forbidden 'unapproved comparative price claim remains' '20% less'
check_forbidden 'obsolete filename remains' 'DESIGN_CORE_v1\.md|TOKEN_COMPONENT_CONTRACT_v1\.md|APPLIED_DESIGN_GUIDE_v1\.md|MESSAGING_CORE_v2\.md|APPLIED_MESSAGING_GUIDE_v2\.md|[0-9]+_Proposal_(Generator|Procedure)\.md|[0-9]+_Design_Reconciliation\.md'

node <<'NODE'
const fs = require('fs');
const path = require('path');
const cp = require('child_process');

const files = cp.execFileSync('rg', ['--files', '-g', '*.md', '-g', '!tasks/todo.md'], { encoding: 'utf8' })
  .trim().split('\n').filter(Boolean);
const missing = [];

for (const file of files) {
  if (!fs.existsSync(file)) continue;
  const body = fs.readFileSync(file, 'utf8');
  const link = /\[[^\]]*\]\(([^)]+)\)/g;
  let match;
  while ((match = link.exec(body))) {
    const raw = match[1].trim().replace(/^<|>$/g, '');
    const target = raw.split('#')[0];
    if (!target || /^(https?:|mailto:|#)/.test(target)) continue;
    const resolved = path.resolve(path.dirname(file), decodeURIComponent(target));
    if (!fs.existsSync(resolved)) {
      const line = body.slice(0, match.index).split('\n').length;
      missing.push(`${file}:${line}: ${raw}`);
    }
  }
}

const htmlFiles = cp.execFileSync('rg', ['--files', '-g', '*.html'], { encoding: 'utf8' })
  .trim().split('\n').filter(Boolean);

for (const file of htmlFiles) {
  if (!fs.existsSync(file)) continue;
  const body = fs.readFileSync(file, 'utf8');
  const asset = /(?:src|href)=["']([^"']+)["']/g;
  let match;
  while ((match = asset.exec(body))) {
    const raw = match[1].trim();
    const target = raw.split('#')[0];
    if (!target || /^(https?:|mailto:|data:|javascript:|#)/.test(target)) continue;
    const resolved = path.resolve(path.dirname(file), decodeURIComponent(target));
    if (!fs.existsSync(resolved)) {
      const line = body.slice(0, match.index).split('\n').length;
      missing.push(`${file}:${line}: ${raw}`);
    }
  }
}

if (missing.length) {
  console.error('FAIL: broken local links or assets');
  console.error(missing.join('\n'));
  process.exit(1);
}
NODE

if [[ "$fail" -ne 0 ]]; then
  exit 1
fi

printf 'Public repository validation passed.\n'
