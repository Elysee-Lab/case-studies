from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')
start_marker = '<div class="lang-report" data-lang="en"'
end_marker = '<div class="lang-report active" data-lang="pl"'
start = html.index(start_marker)
end = html.index(end_marker)
pre, en, post = html[:start], html[start:end], html[end:]

replacements = [
    ('Baza produkcyjna', 'Production database', 1),
    ('Spis głównych części case study', 'Main case study sections', 1),
    ('Wniosek główny', 'Executive thesis', 1),
    ('platform algotowe supports', 'platform already supports', 1),
    ('Kontekst biznesowy', 'Business context', 1),
    ('content, lokalnym SEO, social', 'content, local SEO, social', 1),
    ('Capabilities algotowe built', 'Capabilities already built', 1),
    ('booking inventory, lokalnym SEO presence', 'booking inventory, local SEO presence', 1),
    ('Central layer algotowe exists', 'Central layer already exists', 1),
    ('B2C · Pacjenci', 'B2C · Patients', 1),
    ('B2B · Sieć partnerów', 'B2B · Partner supply', 1),
    ('marketing, lokalnym SEO and B2B sales support', 'marketing, local SEO and B2B sales support', 1),
    ('12 × oferta wysłana · 5 × nieobecność na rozmowie · 2 × odrzucone · 1 × rozmowa zakończona · 1 × w toku.',
     '12 × offer_sent · 5 × no_show · 2 × rejected · 1 × interview_done · 1 × in_progress.', 1),
    ('B2B · Firmy i instytucje', 'B2B · Employer / institution demand', 1),
    ('Oś czasu', 'Timeline', 1),
    ('measurement punkt odniesienia created', 'measurement baseline created', 1),
    ('<b>punkt odniesienia</b><span>technical base for further growth</span>',
     '<b>baseline</b><span>technical base for further growth</span>', 1),
    ('dynamic lokalnym SEO', 'dynamic local SEO', 1),
    ('Systematisation: lokalnym SEO, CMS', 'Systematisation: local SEO, CMS', 1),
    ('<li>lokalnym SEO for cities</li>', '<li>local SEO for cities</li>', 1),
    ('After growth had algotowe started', 'After growth had already started', 1),
    ('click-ID gotowe schema', 'click-ID-ready schema', 1),
    ('<b>mała próba</b>', '<b>low n</b>', 1),
    ('The architecture is largely gotowe.', 'The architecture is largely ready.', 1),
    ('<b>porządkowanie</b>', '<b>clean-up</b>', 1),
    ('<b>porządek w pomiarze reklam</b>', '<b>Ads hygiene</b>', 1),
    ('directional punkt odniesienia', 'directional baseline', 1),
    ('<b>rozwiązane</b><span>pending = false', '<b>resolved</b><span>pending = false', 1),
    ('<b>gotowe</b><span>first/converting touch + refund reconciliation</span>',
     '<b>ready</b><span>first/converting touch + refund reconciliation</span>', 1),
    ('<b>brak nakładania się okresów</b>', '<b>no overlap</b>', 1),
    ('identifiers are gotowe, but', 'identifiers are ready, but', 1),
    ('Media społecznościowe', 'Social media', 1),
    ('Email is algotowe a production nurture layer', 'Email is already a production nurture layer', 1),
    ('was rozwiązane successfully', 'was resolved successfully', 1),
    ('are re-rozwiązane after', 'are re-resolved after', 1),
    ('US data, październik 2024–wrzesień 2025', 'US data, October 2024–September 2025', 1),
    ('<li>lokalnym SEO and expert profiles</li>', '<li>local SEO and expert profiles</li>', 1),
    ('<span class="chainNode">Reklama / post / e-mail</span>',
     '<span class="chainNode">Ad / post / email</span>', 1),
]

for old, new, expected in replacements:
    count = en.count(old)
    if count != expected:
        raise SystemExit(f'Safety stop: expected {expected} occurrence(s) of {old!r}, found {count}')
    en = en.replace(old, new)

updated = pre + en + post
if updated == html:
    raise SystemExit('Safety stop: no changes produced')
path.write_text(updated, encoding='utf-8')
print(f'English-only copy cleanup applied: {len(replacements)} guarded replacements')
