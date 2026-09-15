from pathlib import Path

TARGETS = {
    "intelevent/index.html": [
        'id="shared-case-nav-2026-09-15"',
        'class="topbar shared-case-topbar"',
        'class="nav shared-case-nav"',
        'class="lang shared-case-lang"',
    ],
    "mission-control-room/index.html": [
        'id="shared-case-nav-2026-09-15"',
        'class="topbar shared-case-topbar"',
        'class="nav shared-case-nav"',
        'class="lang shared-case-lang"',
    ],
}

for path, markers in TARGETS.items():
    text = Path(path).read_text(encoding="utf-8")
    for marker in markers:
        assert marker in text, f"{path}: missing {marker}"
    assert '.shared-case-nav a.active:after' in text, f"{path}: active underline missing"
    assert '.shared-case-nav{grid-column:1/-1' in text, f"{path}: second-row nav rule missing"
    assert '@media(max-width:760px)' in text, f"{path}: mobile rule missing"

print("All shared case-study navigation checks passed")
