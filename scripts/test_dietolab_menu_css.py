from pathlib import Path

html = Path('index.html').read_text(encoding='utf-8')

assert 'id="menu-polish-2026-09-14"' in html, 'new menu CSS marker missing'
assert '.jump-nav a.active{color:var(--teal)!important;background:transparent!important;' in html, 'active nav must no longer be a solid teal pill'
assert '.jump-nav a.active:after{' in html, 'active nav underline missing'
assert '@media (min-width:1101px)' in html, 'desktop menu layout guard missing'
assert 'flex-wrap:nowrap!important' in html, 'desktop menu should remain single-line'
assert 'justify-content:center!important' in html, 'desktop menu should be centered'
assert 'overflow-x:auto!important' in html, 'responsive horizontal overflow guard missing'
print('menu CSS assertions passed')
