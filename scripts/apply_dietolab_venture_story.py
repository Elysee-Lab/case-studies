from pathlib import Path
import re
from html.parser import HTMLParser

p = Path("index.html")
s = p.read_text(encoding="utf-8")

# Safety: refuse to patch an unexpected source.
required_before = [
    'Case Study <span class="case-sep">|</span> Eliza Bingul',
    'urgent-ui-fix-2026-09-14',
    'id="model-en"',
    'id="model-pl"',
    'id="learning-path-en"',
    'id="learning-path-pl"',
]
for marker in required_before:
    if marker not in s:
        raise SystemExit(f"Safety stop: missing production marker: {marker}")

# Hero framing.
s = s.replace(
    'A Warsaw-first healthcare growth case study: how I designed and built the go-to-market model, end-to-end customer and partner journeys, digital product layer, measurement architecture and growth mechanisms that connect patient acquisition, specialist supply and B2B demand. With one active public dietitian, this remains a local proof-of-model rather than nationwide scale. The next stage is partner-led replication across Polish cities.',
    'A Warsaw-first healthcare venture-building case study: how I created the brand and positioning, business and commercialisation model, value propositions, go-to-market and acquisition system, end-to-end patient, partner and B2B journeys, product platform, Clinical Brain / Single Spine, operating standards and measurement architecture from the ground up. The results that follow show how I then began optimising and scaling that system. With one active public dietitian, this remains a local proof-of-model rather than nationwide scale. The next stage is partner-led replication across Polish cities.'
)
s = s.replace(
    'To studium rozwoju DietoLab na rynku warszawskim pokazuje, jak zaprojektowałam i zbudowałam strategię wejścia na rynek, pełne ścieżki pacjenta, partnera i klienta B2B, warstwę produktową, model pomiaru oraz mechanizmy wzrostu łączące pozyskiwanie pacjentów, rozwój sieci specjalistów i sprzedaż do firm oraz instytucji. Przy jednym aktywnym publicznym dietetyku jest to nadal potwierdzanie modelu lokalnego, a nie skala ogólnopolska. Kolejny etap to powielanie tego modelu w następnych miastach dzięki rozwojowi sieci partnerów.',
    'To studium budowy DietoLab na rynku warszawskim pokazuje, jak od podstaw stworzyłam strategię marki i pozycjonowanie, model biznesowy i ścieżki komercjalizacji, propozycje wartości, system wejścia na rynek i pozyskiwania popytu, pełne ścieżki pacjenta, partnera i klienta B2B, platformę produktową, Clinical Brain / Single Spine, standardy operacyjne oraz architekturę pomiaru. Dopiero na tym fundamencie zaczęłam systematycznie optymalizować i skalować poszczególne elementy. Przy jednym aktywnym publicznym dietetyku jest to nadal potwierdzanie modelu lokalnego, a nie skala ogólnopolska. Kolejny etap to powielanie tego modelu w następnych miastach dzięki rozwojowi sieci partnerów.'
)

s = s.replace(
    '<b>Built from end to end</b><span>Go-to-market strategy, journeys, product, operations and measurement.</span>',
    '<b>Built from the ground up</b><span>Brand, business model, commercialisation, GTM, product, clinical/AI spine, operations and measurement.</span>'
)
s = s.replace(
    '<b>Model zbudowany od początku do końca</b><span>Strategia wejścia na rynek, ścieżki, produkt, operacje i pomiar.</span>',
    '<b>Zbudowane od podstaw</b><span>Marka, model biznesowy, komercjalizacja, GTM, produkt, warstwa clinical/AI, operacje i pomiar.</span>'
)

en_origin = '''<section class="origin" id="model-en">
<article class="originLead"><div class="eyebrow" style="color:#d7eeee">What I built first</div><h2>First I built the system. Then I started scaling it.</h2><p>This is not a case of optimising a business engine that was already running. I first defined the brand strategy and positioning, business model and commercialisation paths, audience-specific value propositions, offer architecture, go-to-market and acquisition system, end-to-end journeys, digital platform, clinical knowledge spine, operating standards and measurement layer. Only once that foundation existed did channel optimisation and scaling become the main question.</p></article>
<div class="builderStatement"><b>Venture-building scope:</b> I treated DietoLab as one connected business system, not a collection of marketing initiatives. Brand, offer, revenue model, customer journeys, technology, clinical quality, sales and measurement were designed to reinforce one another.</div>
<div class="originGrid ventureGrid">
<article class="originCard"><div class="num">1</div><h3>Brand strategy &amp; positioning</h3><p>I defined what DietoLab should stand for, which problems it should credibly solve and how a specialist nutrition brand could combine clinical quality, accessibility and technology without reducing care to a generic marketplace.</p></article>
<article class="originCard"><div class="num">2</div><h3>Business model &amp; commercialisation</h3><p>I designed several complementary revenue paths rather than relying on one consultation model: B2C care, employer and institutional services, Health Days, research-led offers, value-added services and a partner network that can add local capacity over time.</p></article>
<article class="originCard"><div class="num">3</div><h3>Value proposition &amp; service design</h3><p>I translated different audience needs into distinct propositions for patients, dietitians, companies and institutions, then shaped packages, supporting services and value-added elements around the outcome each group actually needs.</p></article>
<article class="originCard"><div class="num">4</div><h3>Full-funnel GTM &amp; acquisition</h3><p>I designed acquisition across organic search, local SEO, content, paid media, social, newsletter and owned channels, partnerships, referrals, B2B outbound, institutional outreach and dietitian recruitment, with different entry points for different audiences.</p></article>
<article class="originCard"><div class="num">5</div><h3>End-to-end journeys &amp; lifecycle</h3><p>I mapped what should happen from first contact through qualification, booking or offer, delivery, payment, follow-up, retention and expansion. These journeys became the blueprint for CRM states, automation and operational ownership.</p></article>
<article class="originCard"><div class="num">6</div><h3>Product platform &amp; toolset</h3><p>I built the digital operating layer: public acquisition surfaces, patient and dietitian panels, booking, CRM, sales tooling, research workflows, Health Days, payments, documentation, automation and analytics needed to run the model.</p></article>
<article class="originCard"><div class="num">7</div><h3>Clinical Brain / Single Spine &amp; AI</h3><p>I designed a shared knowledge and decision spine so clinical and AI-enabled tools use consistent sources, rules and quality controls rather than becoming isolated features. The aim is better organised work and more consistent patient support, with professional judgement retained.</p></article>
<article class="originCard"><div class="num">8</div><h3>Operating model, quality &amp; measurement</h3><p>I defined processes, standards, roles, documentation, auditability and measurement so the business could learn from real behaviour. Growth analytics and attribution were therefore part of the operating system, not a reporting layer added at the end.</p></article>
</div>
<div class="buildFlow" aria-label="Venture-building sequence"><span>Brand &amp; business model</span><i>→</i><span>Value proposition</span><i>→</i><span>Offer &amp; commercialisation</span><i>→</i><span>GTM</span><i>→</i><span>E2E journeys</span><i>→</i><span>Platform</span><i>→</i><span>Clinical / AI spine</span><i>→</i><span>Operations &amp; standards</span><i>→</i><span>Measurement</span><i>→</i><span>Scale</span></div>
'''

pl_origin = '''<section class="origin" id="model-pl">
<article class="originLead"><div class="eyebrow" style="color:#d7eeee">Od czego zaczęłam</div><h2>Najpierw zbudowałam system. Potem zaczęłam go skalować.</h2><p>To nie jest studium optymalizacji gotowego biznesu. Najpierw zaprojektowałam strategię marki i pozycjonowanie, model biznesowy i ścieżki komercjalizacji, propozycje wartości dla różnych grup, architekturę oferty, system wejścia na rynek i pozyskiwania popytu, pełne ścieżki użytkowników, platformę cyfrową, wspólny kręgosłup wiedzy klinicznej, standardy operacyjne oraz warstwę pomiaru. Dopiero kiedy ten fundament powstał, głównym pytaniem stało się to, jak poszczególne elementy optymalizować i skalować.</p></article>
<div class="builderStatement"><b>Zakres budowy przedsięwzięcia:</b> potraktowałam DietoLab jako jeden połączony system biznesowy, a nie zbiór działań marketingowych. Marka, oferta, model przychodowy, ścieżki klientów, technologia, jakość kliniczna, sprzedaż i pomiar zostały zaprojektowane tak, aby wzajemnie się wzmacniały.</div>
<div class="originGrid ventureGrid">
<article class="originCard"><div class="num">1</div><h3>Strategia marki i pozycjonowanie</h3><p>Określiłam, czym ma być DietoLab, jakie problemy ma wiarygodnie rozwiązywać i jak połączyć ekspercką dietetykę, dostępność i technologię bez sprowadzania opieki do kolejnego katalogu specjalistów.</p></article>
<article class="originCard"><div class="num">2</div><h3>Model biznesowy i komercjalizacja</h3><p>Zaprojektowałam kilka uzupełniających się ścieżek przychodowych zamiast opierać biznes wyłącznie na pojedynczej konsultacji: opiekę B2C, usługi dla firm i instytucji, Dni Zdrowia, oferty oparte na badaniach, usługi dodatkowe oraz sieć partnerską zwiększającą lokalną dostępność.</p></article>
<article class="originCard"><div class="num">3</div><h3>Propozycja wartości i projektowanie usług</h3><p>Przełożyłam różne potrzeby pacjentów, dietetyków, firm i instytucji na osobne propozycje wartości, a następnie na konkretne pakiety, usługi wspierające i elementy dodatkowe, które mają rozwiązywać realny problem danej grupy.</p></article>
<article class="originCard"><div class="num">4</div><h3>Go-to-market i pozyskiwanie popytu</h3><p>Zaprojektowałam pozyskiwanie leadów we wszystkich istotnych kanałach: organic search, local SEO, treści, kampanie płatne, social media, newsletter i kanały własne, partnerstwa, polecenia, outbound B2B, dotarcie do instytucji oraz rekrutację dietetyków.</p></article>
<article class="originCard"><div class="num">5</div><h3>Ścieżki E2E i lifecycle</h3><p>Rozpisałam, co powinno wydarzyć się od pierwszego kontaktu przez kwalifikację, rezerwację lub ofertę, realizację, płatność, dalszą relację, utrzymanie i rozwój. Te ścieżki stały się podstawą statusów CRM, automatyzacji i odpowiedzialności operacyjnej.</p></article>
<article class="originCard"><div class="num">6</div><h3>Platforma produktowa i zestaw narzędzi</h3><p>Zbudowałam cyfrową warstwę operacyjną: publiczne powierzchnie pozyskania, panele pacjenta i dietetyka, rezerwacje, CRM, narzędzia sprzedażowe, badania, Dni Zdrowia, płatności, dokumentację, automatyzacje i analitykę potrzebne do działania całego modelu.</p></article>
<article class="originCard"><div class="num">7</div><h3>Clinical Brain / Single Spine i AI</h3><p>Zaprojektowałam wspólną warstwę wiedzy i reguł, aby narzędzia kliniczne i funkcje wykorzystujące AI korzystały ze spójnych źródeł, zasad i kontroli jakości, zamiast działać jako osobne funkcje. Celem jest lepiej zorganizowana praca i bardziej spójna opieka, przy zachowaniu odpowiedzialności specjalisty.</p></article>
<article class="originCard"><div class="num">8</div><h3>Model operacyjny, jakość i pomiar</h3><p>Określiłam procesy, standardy, role, dokumentację, ślad audytowy oraz sposób pomiaru, aby biznes mógł uczyć się na podstawie rzeczywistych zachowań. Analityka wzrostu i atrybucja były więc częścią systemu operacyjnego, a nie raportem dodanym na końcu.</p></article>
</div>
<div class="buildFlow" aria-label="Kolejność budowy systemu"><span>Marka i model biznesowy</span><i>→</i><span>Propozycja wartości</span><i>→</i><span>Oferta i komercjalizacja</span><i>→</i><span>GTM</span><i>→</i><span>Ścieżki E2E</span><i>→</i><span>Platforma</span><i>→</i><span>Clinical / AI spine</span><i>→</i><span>Operacje i standardy</span><i>→</i><span>Pomiar</span><i>→</i><span>Skala</span></div>
'''

s, n1 = re.subn(r'<section class="origin" id="model-en">.*?(?=<article class="journeyMap">)', en_origin, s, count=1, flags=re.S)
s, n2 = re.subn(r'<section class="origin" id="model-pl">.*?(?=<article class="journeyMap">)', pl_origin, s, count=1, flags=re.S)
if (n1, n2) != (1, 1):
    raise SystemExit(f"Safety stop: origin replacements {n1}, {n2}")

# Learning path is explicitly post-foundation.
s = s.replace(
    '<div class="sectionHead"><div><div class="eyebrow">How I built it</div><h2>The learning path is part of the outcome.</h2></div><p>This case is not a list of features. It shows how strategy changed when better evidence became available.</p></div>',
    '<div class="sectionHead"><div><div class="eyebrow">After the foundations were built</div><h2>After building the foundations: I measured, learned and rebuilt.</h2></div><p>The brand, offer, journeys and first product system came first. This section shows what happened next: how evidence changed hypotheses, priorities and the way individual parts of the system were improved.</p></div>'
)
s, en_lesson = re.subn(
    r'<article class="lesson"><div class="lessonTop"><span class="lessonNo">01 · Measurement</span><span class="lessonTag">Growth analytics</span></div>.*?</article>',
    '<article class="lesson"><div class="lessonTop"><span class="lessonNo">01 · Baseline after build</span><span class="lessonTag">Growth analytics</span></div><h3>After the first system version: establish a baseline</h3><p>Measurement was not the beginning of DietoLab. It was the first optimisation layer after the initial brand, offer, journeys and platform had been designed: GA4, GTM, Clarity, SEO metadata and a reliable point of reference.</p><div class="shift"><b>Learning:</b> once a system exists, the next job is to make it observable. Without a trustworthy baseline, optimisation creates activity, not knowledge.</div></article>',
    s, count=1, flags=re.S
)
s = s.replace(
    '<div class="sectionHead"><div><div class="eyebrow">Jak to budowałam</div><h2>Sposób uczenia się jest częścią wyniku.</h2></div><p>To studium przypadku nie jest listą wdrożonych funkcji. Pokazuje, jak wraz z pojawianiem się nowych danych zmieniały się hipotezy, priorytety i decyzje.</p></div>',
    '<div class="sectionHead"><div><div class="eyebrow">Po zbudowaniu fundamentów</div><h2>Po zbudowaniu fundamentów: mierzyłam, uczyłam się i przebudowywałam.</h2></div><p>Marka, oferta, ścieżki i pierwsza wersja systemu produktowego powstały wcześniej. Ta część pokazuje kolejny etap: jak dane zmieniały hipotezy, priorytety i sposób rozwijania poszczególnych elementów.</p></div>'
)
s, pl_lesson = re.subn(
    r'<article class="lesson"><div class="lessonTop"><span class="lessonNo">01 · Pomiar</span><span class="lessonTag">Analityka wzrostu</span></div>.*?</article>',
    '<article class="lesson"><div class="lessonTop"><span class="lessonNo">01 · Punkt odniesienia po budowie</span><span class="lessonTag">Analityka wzrostu</span></div><h3>Po pierwszej wersji systemu: ustanowienie punktu odniesienia</h3><p>Pomiar nie był początkiem DietoLab. Był pierwszą warstwą optymalizacji po zaprojektowaniu marki, oferty, ścieżek i pierwszej wersji platformy: GA4, GTM, Clarity, metadane SEO i wiarygodny punkt odniesienia.</p><div class="shift"><b>Wniosek:</b> kiedy system już istnieje, trzeba uczynić go obserwowalnym. Bez wiarygodnego punktu odniesienia można zwiększać liczbę działań, ale nie jakość wiedzy o tym, co rzeczywiście działa.</div></article>',
    s, count=1, flags=re.S
)
if en_lesson != 1 or pl_lesson != 1:
    raise SystemExit(f"Safety stop: learning replacements {en_lesson}, {pl_lesson}")

en_caps = '''<div class="capMatrix"><h3>Capabilities demonstrated by the case</h3><div class="capMatrixGrid">
<div class="capProof"><b>Brand strategy &amp; positioning</b><span>Defining the role of the brand, target audiences, differentiation and the relationship between clinical credibility, accessibility and technology.</span></div>
<div class="capProof"><b>Business model &amp; commercialisation</b><span>Designing complementary B2C, B2B, institutional, value-added-service and partner-network revenue paths.</span></div>
<div class="capProof"><b>Value proposition &amp; service design</b><span>Translating audience needs into propositions, packages, supporting services and clear reasons to choose DietoLab.</span></div>
<div class="capProof"><b>Go-to-market &amp; full-funnel growth</b><span>Organic, local, content, paid, social, owned, partnership, referral, outbound B2B and partner-recruitment acquisition systems.</span></div>
<div class="capProof"><b>Product strategy &amp; platform design</b><span>Patient, dietitian, partner and B2B workflows designed as one operating platform rather than disconnected features.</span></div>
<div class="capProof"><b>Clinical Brain / Single Spine</b><span>Shared clinical knowledge, rules and quality controls for AI-enabled and clinical tools, with specialist judgement retained.</span></div>
<div class="capProof"><b>Revenue Operations &amp; B2B sales</b><span>Company CRM, research-led entry products, Health Days, offers, contracts, institutional selling and commercial follow-up.</span></div>
<div class="capProof"><b>CRM, automation &amp; lifecycle</b><span>Newsletter, drip sequences, lead states, booking, partner onboarding, patient follow-up and relationship management.</span></div>
<div class="capProof"><b>Analytics, attribution &amp; experimentation</b><span>Cohorts, identity stitching, click IDs, consent-aware server-side delivery, event hygiene and evidence-led iteration.</span></div>
<div class="capProof"><b>Operating model &amp; quality standards</b><span>Processes, roles, documentation, procedures, auditability and quality controls across clinical and commercial workflows.</span></div>
<div class="capProof"><b>Partner ecosystem &amp; network strategy</b><span>Designing how central infrastructure and specialist supply can reinforce each other city by city.</span></div>
<div class="capProof"><b>SEO, content &amp; local acquisition</b><span>Information architecture, technical SEO, expert/local surfaces, content operations and crawler readiness.</span></div>
</div></div>'''

pl_caps = '''<div class="capMatrix"><h3>Kompetencje pokazane w tym projekcie</h3><div class="capMatrixGrid">
<div class="capProof"><b>Strategia marki i pozycjonowanie</b><span>Określenie roli marki, grup docelowych, wyróżników oraz sposobu połączenia wiarygodności klinicznej, dostępności i technologii.</span></div>
<div class="capProof"><b>Model biznesowy i komercjalizacja</b><span>Zaprojektowanie uzupełniających się ścieżek przychodowych B2C, B2B, instytucjonalnych, usług dodatkowych i sieci partnerskiej.</span></div>
<div class="capProof"><b>Propozycja wartości i projektowanie usług</b><span>Przełożenie potrzeb odbiorców na konkretne propozycje wartości, pakiety, usługi wspierające i jasne powody wyboru DietoLab.</span></div>
<div class="capProof"><b>Go-to-market i full-funnel growth</b><span>Organic, local, content, paid, social, kanały własne, partnerstwa, polecenia, outbound B2B i rekrutacja partnerów jako jeden system pozyskania.</span></div>
<div class="capProof"><b>Strategia produktu i projekt platformy</b><span>Ścieżki pacjenta, dietetyka, partnera i klientów B2B zaprojektowane jako jedna platforma operacyjna, a nie zestaw osobnych funkcji.</span></div>
<div class="capProof"><b>Clinical Brain / Single Spine</b><span>Wspólna wiedza kliniczna, reguły i kontrola jakości dla narzędzi AI i klinicznych, przy zachowaniu odpowiedzialności specjalisty.</span></div>
<div class="capProof"><b>Revenue Operations i sprzedaż B2B</b><span>CRM firmowy, produkty otwierające rozmowę, Dni Zdrowia, oferty, umowy, sprzedaż do instytucji i dalsza obsługa procesu.</span></div>
<div class="capProof"><b>CRM, automatyzacja i lifecycle</b><span>Newsletter, automatyczne sekwencje wiadomości, statusy kontaktów, rezerwacje, wdrażanie partnerów, dalsza opieka i zarządzanie relacją.</span></div>
<div class="capProof"><b>Analityka, atrybucja i eksperymenty</b><span>Kohorty, łączenie tożsamości, identyfikatory kliknięć, wysyłka z poszanowaniem zgód, porządek zdarzeń i iteracja oparta na dowodach.</span></div>
<div class="capProof"><b>Model operacyjny i standardy jakości</b><span>Procesy, role, dokumentacja, procedury, audytowalność i kontrola jakości w ścieżkach klinicznych i komercyjnych.</span></div>
<div class="capProof"><b>Ekosystem partnerski i strategia sieci</b><span>Zaprojektowanie mechanizmu, w którym wspólne zaplecze centralne i rosnąca podaż specjalistów wzmacniają się wraz z wejściem do kolejnych miast.</span></div>
<div class="capProof"><b>SEO, treści i lokalne pozyskanie</b><span>Architektura informacji, techniczne SEO, strony eksperckie i lokalne, proces tworzenia treści oraz przygotowanie serwisu do prawidłowego odczytu przez roboty.</span></div>
</div></div>'''

s, c1 = re.subn(r'<div class="capMatrix"><h3>Capabilities demonstrated by the case</h3><div class="capMatrixGrid">.*?</div></div>', en_caps, s, count=1, flags=re.S)
s, c2 = re.subn(r'<div class="capMatrix"><h3>Kompetencje pokazane w tym projekcie</h3><div class="capMatrixGrid">.*?</div></div>', pl_caps, s, count=1, flags=re.S)
if (c1, c2) != (1, 1):
    raise SystemExit(f"Safety stop: capability replacements {c1}, {c2}")

new_css = '''
<style id="venture-builder-layer-2026-09-14">
.builderStatement{margin:16px 0 0;padding:18px 20px;border-radius:16px;background:linear-gradient(135deg,var(--limeSoft),#fff);border:1px solid rgba(22,123,120,.13);font-size:15.5px;line-height:1.68;color:#415857}
.builderStatement b{color:var(--ink)}
.ventureGrid{grid-template-columns:repeat(4,1fr)}
.buildFlow{margin-top:16px;padding:18px;border-radius:18px;background:#172f2f;color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap}
.buildFlow span{padding:8px 10px;border-radius:10px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.1);font-size:12.5px;line-height:1.35;font-weight:800;text-align:center}
.buildFlow i{font-style:normal;color:var(--lime);font-weight:900}
@media(max-width:900px){.ventureGrid{grid-template-columns:1fr 1fr}.buildFlow{justify-content:flex-start}}
@media(max-width:640px){.ventureGrid{grid-template-columns:1fr}.builderStatement{font-size:15px}.buildFlow{display:grid;grid-template-columns:1fr}.buildFlow i{display:none}.buildFlow span{font-size:13px;text-align:left}}
</style>
'''
if 'venture-builder-layer-2026-09-14' in s:
    raise SystemExit('Safety stop: venture layer already present')
s = s.replace('</head>', new_css + '</head>', 1)

# Post-patch verification before writing.
for marker in [
    'Najpierw zbudowałam system. Potem zaczęłam go skalować.',
    'First I built the system. Then I started scaling it.',
    'Po zbudowaniu fundamentów: mierzyłam, uczyłam się i przebudowywałam.',
    'After building the foundations: I measured, learned and rebuilt.',
    'Po pierwszej wersji systemu: ustanowienie punktu odniesienia',
    'After the first system version: establish a baseline',
    'Strategia marki i pozycjonowanie',
    'Brand strategy &amp; positioning',
    'Clinical Brain / Single Spine',
    'urgent-ui-fix-2026-09-14',
    'class="jump-nav active"',
]:
    if marker not in s:
        raise SystemExit(f"Verification failed: {marker}")

if s.count('class="originCard"') < 16:
    raise SystemExit('Verification failed: origin card count')
if s.count('class="capProof"') < 24:
    raise SystemExit('Verification failed: capability card count')

p.write_text(s, encoding="utf-8")
print(f"DietoLab case study updated safely: {len(s)} bytes")
