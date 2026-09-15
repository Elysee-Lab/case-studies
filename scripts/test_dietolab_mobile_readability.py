from pathlib import Path

s = Path('index.html').read_text(encoding='utf-8')

# Responsive/layout contract
assert 'id="mobile-readability-fix-2026-09-15"' in s, 'mobile readability CSS patch missing'
assert '.timeline > .localSeoScale{margin-left:83px;width:calc(100% - 83px)' in s, 'Local SEO card is not offset from the desktop timeline rail'
assert '.timeline > .localSeoScale{margin-left:46px;width:calc(100% - 46px)' in s, 'Local SEO card is not offset from the mobile timeline rail'

# Readability contract
assert '.capProof b{font-size:15px' in s, 'capability-card headings are still too small'
assert '.capProof span{font-size:14px' in s, 'capability-card copy is still too small'
assert '.state h3{line-height:1.15' in s, 'large dark-section headings still inherit oversized leading'
assert '.localSeoScale h3{font-size:26px;line-height:1.15' in s, 'Local SEO heading scale/leading not corrected'
assert '.localSeoScale>p{font-size:15.5px;line-height:1.62' in s, 'Local SEO body copy not corrected'

# Jargon contract: spell out SSR at first meaningful use in both languages.
assert 'Server-side rendering (SSR): making pages easier for search engines to read' in s
assert 'Renderowanie po stronie serwera (SSR): ułatwienie odczytu i indeksowania' in s
assert '6. SSR / crawler rendering: strengthening crawlability' not in s
assert '6. SSR i renderowanie dla robotów: ułatwienie indeksowania' not in s

print('DietoLab mobile readability, timeline and SSR copy contract passed')

# Verification trigger after the production patch commit.
