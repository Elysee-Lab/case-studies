from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

STYLE_ID = 'mobile-readability-fix-2026-09-15'
style = r'''
<style id="mobile-readability-fix-2026-09-15">
/* Mobile readability + timeline rail correction based on production screenshots. */
.capMatrix h3{font-size:24px!important;line-height:1.18!important;margin-bottom:16px!important}
.capProof b{font-size:15px!important;line-height:1.25!important}
.capProof span{font-size:14px!important;line-height:1.50!important;margin-top:6px!important}

.state h3{line-height:1.15!important}
.stepTop h3,.lesson h3,.proofCard h3,.nextCard h3,.funnelCard h3,.channelCard h3,.originCard h3,.layerCard h4,.rampCard h4{line-height:1.22!important}
.sectionHead h2,.originLead h2,.partnerCta h3{line-height:1.15!important}

/* The Local SEO explainer sits inside the timeline container, so it must use the same left gutter as timeline steps. */
.timeline > .localSeoScale{margin-left:83px;width:calc(100% - 83px);position:relative;z-index:1;margin-top:18px;margin-bottom:24px}
.localSeoScale h3{font-size:26px;line-height:1.15!important}
.localSeoScale>p{font-size:15.5px;line-height:1.62!important}
.localSeoNode b{font-size:14px!important;line-height:1.3!important}
.localSeoNode code{font-size:12.5px!important;line-height:1.4!important}
.localSeoNode span{font-size:13.5px!important;line-height:1.52!important}
.localSeoOutcome{font-size:14px!important;line-height:1.58!important}
.localSeoLinks{font-size:13px!important;line-height:1.55!important}

@media(max-width:640px){
  .capMatrix h3{font-size:25px!important;line-height:1.16!important}
  .capProof b{font-size:15.5px!important}
  .capProof span{font-size:14.5px!important;line-height:1.48!important}
  .state h3{font-size:29px!important;line-height:1.12!important}
  .sectionHead h2{line-height:1.13!important}
  .timeline > .localSeoScale{margin-left:46px;width:calc(100% - 46px);margin-top:16px;margin-bottom:22px;padding:20px!important}
  .localSeoScale h3{font-size:23px!important;line-height:1.13!important}
  .localSeoScale>p{font-size:15.5px!important;line-height:1.58!important}
  .localSeoNode span{font-size:14px!important}
}
</style>
'''

if STYLE_ID not in s:
    if '</head>' not in s:
        raise SystemExit('Could not find </head>')
    s = s.replace('</head>', style + '\n</head>', 1)

replacements = {
    # English SSR copy
    '<li>SSR was not fully deployed yet</li>': '<li>server-side rendering (SSR) was not fully deployed yet</li>',
    '<h3>6. SSR / crawler rendering: strengthening crawlability</h3>': '<h3>6. Server-side rendering (SSR): making pages easier for search engines to read</h3>',
    '<p>After growth had already in place started, a server-side rendering layer for crawlers was added.</p>': '<p>After organic visibility had already started to grow, I added server-side rendering (SSR). In practice, the server sends search-engine crawlers a complete HTML version of the page, so important content is available immediately instead of depending on JavaScript to build it in the browser.</p>',
    '<li>SSR canary + production Wave 1 / Wave 2</li>': '<li>phased server-side rendering rollout: canary + production Wave 1 / Wave 2</li>',
    '<li>crawler SSR for /dietetycy and the blog</li>': '<li>crawler-ready server-rendered HTML for /dietetycy and the blog</li>',
    '<p class="narrative">SSR likely helped support and extend the trend, but growth started earlier, so it does not get all the credit.': '<p class="narrative">Server-side rendering (SSR) likely helped support and extend the trend, but growth started earlier, so it does not get all the credit.',
    'Later work focused on canonicalisation, SSR and per-page quality rather than simply adding pages.': 'Later work focused on canonicalisation, server-side rendering (SSR) and per-page quality rather than simply adding pages.',
    'The August visibility break started before full SSR rollout. The report therefore treats SSR as supportive, not as the single cause.': 'The August visibility break started before the full server-side rendering (SSR) rollout. The report therefore treats that change as supportive, not as the single cause.',

    # Polish SSR copy
    '<li>SSR jeszcze nie był wtedy w pełni wdrożony</li>': '<li>renderowanie po stronie serwera (SSR) nie było wtedy jeszcze w pełni wdrożone</li>',
    '<h3>6. SSR i renderowanie dla robotów: ułatwienie indeksowania</h3>': '<h3>6. Renderowanie po stronie serwera (SSR): ułatwienie odczytu i indeksowania</h3>',
    '<p>Gdy wzrost widoczności już się rozpoczął, dodaliśmy renderowanie po stronie serwera dla robotów wyszukiwarek.</p>': '<p>Gdy wzrost widoczności już się rozpoczął, dodałam renderowanie po stronie serwera (SSR). W praktyce oznacza to, że robot wyszukiwarki otrzymuje od razu gotową wersję HTML z najważniejszą treścią, zamiast czekać, aż zbuduje ją JavaScript w przeglądarce.</p>',
    '<li>wdrożenie próbne SSR oraz dwa etapy wdrożenia produkcyjnego</li>': '<li>wdrożenie próbne renderowania po stronie serwera (SSR) oraz dwa etapy wdrożenia produkcyjnego</li>',
    '<li>SSR dla robotów na /dietetycy i blogu</li>': '<li>gotowa treść HTML dla robotów na /dietetycy i blogu</li>',
    '<p class="narrative">SSR prawdopodobnie pomógł utrwalić i rozszerzyć trend, ale wzrost rozpoczął się wcześniej, dlatego nie przypisujemy mu całego efektu.': '<p class="narrative">Renderowanie po stronie serwera (SSR) prawdopodobnie pomogło utrwalić i rozszerzyć trend, ale wzrost rozpoczął się wcześniej, dlatego nie przypisuję mu całego efektu.',
    'Później nacisk przesunął się na kanoniczne adresy, SSR i jakość poszczególnych stron, a nie samo dokładanie kolejnych adresów URL.': 'Później nacisk przesunął się na kanoniczne adresy, renderowanie po stronie serwera (SSR) i jakość poszczególnych stron, a nie samo dokładanie kolejnych adresów URL.',
    'Sierpniowy przełom widoczności rozpoczął się przed pełnym wdrożeniem SSR. Dlatego w analizie traktuję SSR jako czynnik wspierający, a nie jedyną przyczynę wzrostu.': 'Sierpniowy przełom widoczności rozpoczął się przed pełnym wdrożeniem renderowania po stronie serwera (SSR). Dlatego w analizie traktuję tę zmianę jako czynnik wspierający, a nie jedyną przyczynę wzrostu.',
}

for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new)

path.write_text(s, encoding='utf-8')
print('Applied DietoLab mobile readability, timeline and SSR copy patch')
