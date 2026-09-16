from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "mission-control-room"
html = (CASE / "index.html").read_text(encoding="utf-8")
css = (CASE / "styles.css").read_text(encoding="utf-8")
js = (CASE / "app.js").read_text(encoding="utf-8")

required_sections = ["challenge", "human", "measurement", "operating", "mcr", "human-ai", "results", "learnings"]
for section in required_sections:
    assert f'id="{section}"' in html, f"missing section: {section}"

assert html.count('class="flow-copy"') == 4, "hero signal rows must keep label and description separate"
assert ".hero-note{" in css and "position:static" in css, "hero note must stay in normal flow"
assert "grid-template-columns:repeat(8,minmax(0,1fr))" in css, "desktop nav must use fixed 8-column grid"
assert "@media(max-width:1180px)" in css and "overflow-x:auto" in css, "tablet/mobile nav needs horizontal scrolling"
assert "human-ai-balance" in html and ".human-ai-balance{" in css, "stable Human + AI layout missing"
assert 'class="venn"' not in html and ".circle.human" not in css, "legacy overlapping Venn layout must be removed"

for asset in ["assets/human-prototype.png", "assets/mission-control-room.png", "assets/human-ai.png", "assets/results-learnings.png"]:
    assert asset not in html, f"language-specific infographic still embedded: {asset}"

assert '<link rel="stylesheet" href="styles.css">' in html
assert '<script src="app.js" defer></script>' in html
assert 'data-lang-btn="en"' in html and 'data-lang-btn="pl"' in html
assert 'IntersectionObserver' in js and 'localStorage.setItem("mcr-lang"' in js

print("MCR static regression contract passed")
