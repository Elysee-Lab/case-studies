from pathlib import Path

# Portfolio-wide responsive regression contract: every published case study must remain mobile-safe.
TARGETS = {
    Path('index.html'): {
        'marker': 'global-responsive-contract-2026-09-15',
        'needles': [
            'overflow-x:hidden',
            '@media(max-width:760px)',
            '.jump-nav',
        ],
    },
    Path('intelevent/index.html'): {
        'marker': 'global-responsive-contract-2026-09-15',
        'needles': [
            'overflow-x:hidden',
            '.cardStack{position:static',
            '.vcard{position:relative',
            '.snap{position:relative',
            '.nav{grid-column:1/-1',
        ],
    },
    Path('mission-control-room/index.html'): {
        'marker': 'global-responsive-contract-2026-09-15',
        'needles': [
            'overflow-x:hidden',
            '.heroVisual{min-height:0',
            '.panel{position:relative',
            '.panel.main{order:2;inset:auto',
            '.nav{grid-column:1/-1',
        ],
    },
}

for path, contract in TARGETS.items():
    assert path.exists(), f'missing case study: {path}'
    html = path.read_text(encoding='utf-8')
    assert 'name="viewport"' in html, f'{path}: viewport meta missing'
    assert contract['marker'] in html, f'{path}: responsive contract marker missing'
    for needle in contract['needles']:
        assert needle in html, f'{path}: missing responsive rule: {needle}'

print('All case studies satisfy the responsive contract')
