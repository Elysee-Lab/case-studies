from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "mission-control-room"
SOURCE = CASE / "source"


def combine(prefix: str, target: str) -> None:
    parts = sorted(SOURCE.glob(f"{prefix}.part*"))
    if not parts:
        raise SystemExit(f"No source parts found for {prefix}")
    content = "".join(p.read_text(encoding="utf-8") for p in parts)
    (CASE / target).write_text(content, encoding="utf-8")
    print(f"built {target} from {len(parts)} part(s): {len(content)} chars")


combine("index.html", "index.html")
combine("styles.css", "styles.css")
combine("app.js", "app.js")
