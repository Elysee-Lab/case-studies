from pathlib import Path

html = Path('index.html').read_text(encoding='utf-8')
start = html.index('<div class="lang-report" data-lang="en"')
end = html.index('<div class="lang-report active" data-lang="pl"')
en = html[start:end]

bad_markers = [
    'Baza produkcyjna',
    'Spis głównych części case study',
    'Wniosek główny',
    'Kontekst biznesowy',
    'B2C · Pacjenci',
    'B2B · Sieć partnerów',
    'B2B · Firmy i instytucje',
    'Oś czasu',
    'Reklama / post / e-mail',
    'lokalnym SEO',
    'algotowe',
    ' gotowe',
    'punkt odniesienia',
    'mała próba',
    'porządkowanie',
    'porządek w pomiarze reklam',
    'rozwiązane',
    'brak nakładania się okresów',
    'Media społecznościowe',
    'październik 2024–wrzesień 2025',
    'oferta wysłana',
    'nieobecność na rozmowie',
    'odrzucone',
    'rozmowa zakończona',
    'w toku.',
]

found = [marker for marker in bad_markers if marker in en]
assert not found, 'Polish/malformed copy remains in English report: ' + ', '.join(found)

required_good = [
    'First I built the system. Then I started scaling it.',
    'Clinical Brain / Single Spine',
    'urgent-ui-fix-2026-09-14',
]
for marker in required_good:
    assert marker in en, f'Missing English invariant: {marker}'

print('English copy isolation test: PASS')
