from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "docs"

REQUIRED_FILES = [
    ROOT / "README.md",
    DOC_ROOT / "README.md",
    DOC_ROOT / "v1" / "README.md",
    DOC_ROOT / "v1" / "quickstart.md",
    DOC_ROOT / "v1" / "concepts" / "architecture.md",
    DOC_ROOT / "v1" / "concepts" / "tenancy-authentication.md",
    DOC_ROOT / "v1" / "guides" / "devices-and-commands.md",
    DOC_ROOT / "v1" / "guides" / "telemetry-location-events.md",
    DOC_ROOT / "v1" / "guides" / "webhooks-and-partner-operations.md",
    DOC_ROOT / "v1" / "sdks" / "typescript.md",
    DOC_ROOT / "v1" / "sdks" / "python.md",
    DOC_ROOT / "v1" / "tools" / "developer-tools.md",
    DOC_ROOT / "v1" / "operations" / "errors-retries-idempotency.md",
    DOC_ROOT / "v1" / "operations" / "troubleshooting.md",
    DOC_ROOT / "v1" / "reference" / "compatibility.md",
    DOC_ROOT / "v1" / "reference" / "maturity.md",
]

MATURITY_TERMS = {"Scaffold", "Experimental", "Alpha", "Beta", "Stable", "Deprecated", "Planned"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_required(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required documentation file: {path.relative_to(ROOT)}")


def check_local_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {path.relative_to(ROOT)} -> {raw_target}")


def check_version_and_identity(errors: list[str]) -> None:
    v1_index = (DOC_ROOT / "v1" / "README.md").read_text(encoding="utf-8")
    quickstart = (DOC_ROOT / "v1" / "quickstart.md").read_text(encoding="utf-8")
    required_markers = {
        "docs/v1/README.md": ["1.0.0-draft", "corelink_device_id", "CoreLink Console"],
        "docs/v1/quickstart.md": [
            "Authorization: Bearer $CORELINK_ACCESS_TOKEN",
            "Idempotency-Key: $CORELINK_IDEMPOTENCY_KEY",
            "/api/v1/tenants/$CORELINK_TENANT_ID/devices",
        ],
    }
    texts = {"docs/v1/README.md": v1_index, "docs/v1/quickstart.md": quickstart}
    for filename, markers in required_markers.items():
        for marker in markers:
            if marker not in texts[filename]:
                errors.append(f"missing required version/contract marker in {filename}: {marker}")


def check_maturity_vocabulary(errors: list[str]) -> None:
    maturity_page = (DOC_ROOT / "v1" / "reference" / "maturity.md").read_text(encoding="utf-8")
    missing = sorted(term for term in MATURITY_TERMS if term not in maturity_page)
    if missing:
        errors.append(f"maturity reference is missing terms: {', '.join(missing)}")


def check_stale_claims(errors: list[str]) -> None:
    forbidden = {
        "future console-web": "Console is the canonical existing frontend repository",
        "API contract repository also has unpopulated": "the contract repository is populated",
        "OpenAPI and AsyncAPI source files in `api-contracts` are also currently empty": "contract sources are populated",
    }
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for phrase, reason in forbidden.items():
            if phrase in text:
                errors.append(f"stale claim in {path.relative_to(ROOT)}: {phrase!r} ({reason})")


def check_headings(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        headings = HEADING_RE.findall(text)
        if not headings:
            errors.append(f"markdown file has no heading: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    if not errors:
        check_version_and_identity(errors)
        check_maturity_vocabulary(errors)
    check_local_links(errors)
    check_stale_claims(errors)
    check_headings(errors)

    if errors:
        print("Documentation integrity check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Documentation integrity check passed for {len(markdown_files())} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
