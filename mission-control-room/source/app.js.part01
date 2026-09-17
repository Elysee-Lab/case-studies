const body=document.body;
const buttons=[...document.querySelectorAll("[data-lang-btn]")];

function setLang(lang){
  body.dataset.lang=lang;
  document.documentElement.lang=lang;
  buttons.forEach(btn=>{
    const active=btn.dataset.langBtn===lang;
    btn.classList.toggle("active",active);
    btn.setAttribute("aria-pressed",String(active));
  });
  try{localStorage.setItem("mcr-lang",lang)}catch(e){}
}

buttons.forEach(btn=>btn.addEventListener("click",()=>setLang(btn.dataset.langBtn)));
try{
  const saved=localStorage.getItem("mcr-lang");
  if(saved==="pl"||saved==="en") setLang(saved);
}catch(e){}

const progress=document.querySelector(".progress");
function updateProgress(){
  const doc=document.documentElement;
  const max=doc.scrollHeight-doc.clientHeight;
  progress.style.width=(max ? (doc.scrollTop/max)*100 : 0)+"%";
}
document.addEventListener("scroll",updateProgress,{passive:true});
updateProgress();

const navLinks=[...document.querySelectorAll(".nav a")];
const sections=navLinks.map(a=>document.querySelector(a.getAttribute("href"))).filter(Boolean);
const observer=new IntersectionObserver(entries=>{
  const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>b.intersectionRatio-a.intersectionRatio)[0];
  if(!visible) return;
  navLinks.forEach(a=>a.classList.toggle("active",a.getAttribute("href")==="#"+visible.target.id));
},{rootMargin:"-26% 0px -60% 0px",threshold:[0.05,.2,.5]});
sections.forEach(s=>observer.observe(s));

function ensureInfographicStyles(){
  if(document.querySelector('link[href="infographics.css"]')) return;
  const link=document.createElement("link");
  link.rel="stylesheet";
  link.href="infographics.css";
  document.head.appendChild(link);
}

const icon=(name)=>{
  const common='viewBox="0 0 48 48" aria-hidden="true" focusable="false"';
  const icons={
    document:`<svg ${common}><rect x="13" y="8" width="22" height="32" rx="3"/><path d="M18 17h12M18 24h12M18 31h9"/></svg>`,
    search:`<svg ${common}><circle cx="21" cy="21" r="11"/><path d="m29 29 9 9"/></svg>`,
    people:`<svg ${common}><circle cx="24" cy="16" r="6"/><circle cx="12" cy="21" r="4"/><circle cx="36" cy="21" r="4"/><path d="M14 38c1-7 5-11 10-11s9 4 10 11M4 37c.8-5 3.5-8 8-8M44 37c-.8-5-3.5-8-8-8"/></svg>`,
    refresh:`<svg ${common}><path d="M35 16a14 14 0 0 0-23 4"/><path d="m11 12 1 8 8-1"/><path d="M13 32a14 14 0 0 0 23-4"/><path d="m37 36-1-8-8 1"/></svg>`,
    bars:`<svg ${common}><path d="M10 38V27h7v11M21 38V18h7v20M32 38V10h7v28"/></svg>`,
    human:`<svg ${common}><circle cx="24" cy="16" r="7"/><path d="M12 39c1-9 6-14 12-14s11 5 12 14"/></svg>`,
    ai:`<svg ${common}><rect x="13" y="13" width="22" height="22" rx="4"/><path d="M19 5v8M29 5v8M19 35v8M29 35v8M5 19h8M5 29h8M35 19h8M35 29h8"/><text x="24" y="28" text-anchor="middle">AI</text></svg>`,
    bolt:`<svg ${common}><path d="M27 4 13 26h11l-3 18 14-24H24z"/></svg>`,
    gear:`<svg ${common}><circle cx="24" cy="24" r="7"/><path d="M24 6v5M24 37v5M6 24h5M37 24h5M11 11l4 4M33 33l4 4M37 11l-4 4M15 33l-4 4"/></svg>`,
    database:`<svg ${common}><ellipse cx="24" cy="11" rx="12" ry="5"/><path d="M12 11v9c0 3 5 5 12 5s12-2 12-5v-9M12 20v9c0 3 5 5 12 5s12-2 12-5v-9M12 29v8c0 3 5 5 12 5s12-2 12-5v-8"/></svg>`
  };
  return icons[name]||"";
};

function processInfographic(){
  return `
  <section class="mcri-section mcri-section--paper" aria-label="Inquiry to evidence infographic">
    <div class="wrap">
      <div class="mcri-shell">
        <div class="mcri-head">
          <span class="mcri-rule"></span>
          <div class="lang-en"><h2 class="mcri-title">From inquiry to evidence</h2><p class="mcri-subtitle">How a manual operational prototype turned incoming inquiries into structured knowledge and action.</p></div>
          <div class="lang-pl"><h2 class="mcri-title">Od zapytania do dowodu</h2><p class="mcri-subtitle">Jak ręczny prototyp operacyjny zamieniał napływające zapytania w uporządkowaną wiedzę i działania.</p></div>
        </div>
        <div class="mcri-flow">
          <article class="mcri-flow-step tone-warm"><div class="mcri-icon">${icon("document")}</div><span class="mcri-num">01</span><span class="mcri-mini-rule"></span><h3><span class="lang-en inline">Manual review</span><span class="lang-pl inline">Ręczny przegląd</span></h3><p><span class="lang-en inline">Review of incoming inquiries.</span><span class="lang-pl inline">Przegląd wpływających zapytań.</span></p></article>
          <article class="mcri-flow-step tone-cool"><div class="mcri-icon">${icon("search")}</div><span class="mcri-num">02</span><span class="mcri-mini-rule"></span><h3><span class="lang-en inline">Value identification</span><span class="lang-pl inline">Identyfikacja wartości</span></h3><p><span class="lang-en inline">Finding the signals that distinguish potential from noise.</span><span class="lang-pl inline">Wyszukiwanie sygnałów odróżniających potencjał od szumu.</span></p></article>
          <article class="mcri-flow-step tone-warm"><div class="mcri-icon">${icon("people")}</div><span class="mcri-num">03</span><span class="mcri-mini-rule"></span><h3><span class="lang-en inline">Nudge / escalation</span><span class="lang-pl inline">Nudge / eskalacja</span></h3><p><span class="lang-en inline">Helping important inquiries reach the right people.</span><span class="lang-pl inline">Pomoc w dotarciu ważnych zapytań do właściwych osób.</span></p></article>
          <article class="mcri-flow-step tone-cool"><div class="mcri-icon">${icon("refresh")}</div><span class="mcri-num">04</span><span class="mcri-mini-rule"></span><h3>Follow-up</h3><p><span class="lang-en inline">Maintaining momentum in conversations with business potential.</span><span class="lang-pl inline">Utrzymanie tempa rozmów o potencjale biznesowym.</span></p></article>
          <article class="mcri-flow-step tone-warm"><div class="mcri-icon">${icon("bars")}</div><span class="mcri-num">05</span><span class="mcri-mini-rule"></span><h3><span class="lang-en inline">Evidence</span><span class="lang-pl inline">Dowody</span></h3><p><span class="lang-en inline">Recording the outcome and the key signals.</span><span class="lang-pl inline">Zapisanie rezultatu i kluczowych sygnałów.</span></p></article>
        </div>
        <div class="mcri-footer-note"><span class="lang-en inline">The first prototype was operational, not technical — the process built knowledge first.</span><span class="lang-pl inline">Pierwszy prototyp był operacyjny, nie techniczny — proces najpierw budował wiedzę.</span></div>
      </div>
    </div>
  </section>`;
}

function rolesInfographic(){
  return `
  <section class="mcri-section" aria-label="Human and AI roles infographic">
    <div class="wrap">
      <div class="mcri-shell">
        <div class="mcri-head">
          <span class="mcri-rule"></span>
          <div class="lang-en"><h2 class="mcri-title">Human + AI: division of roles</h2><p class="mcri-subtitle">The best results appeared when human market knowledge met a structured workflow supported by AI.</p></div>
          <div class="lang-pl"><h2 class="mcri-title">Człowiek + AI: podział ról</h2><p class="mcri-subtitle">Najlepsze wyniki pojawiły się wtedy, gdy wiedza rynkowa człowieka spotkała się z uporządkowanym workflow wspieranym przez AI.</p></div>
        </div>
        <div class="mcri-roles">
          <article class="mcri-role-panel tone-warm">
            <div class="mcri-icon mcri-icon--large">${icon("human")}</div>
            <h3><span class="lang-en inline">Human layer</span><span class="lang-pl inline">Warstwa ludzka</span></h3>
            <ul>
              <li><span class="lang-en inline">Industry expertise</span><span class="lang-pl inline">Ekspertyza branżowa</span></li>
              <li><span class="lang-en inline">Client and market context</span><span class="lang-pl inline">Kontekst klienta i rynku</span></li>
              <li><span class="lang-en inline">Assessment of nuance</span><span class="lang-pl inline">Ocena niuansów</span></li>
              <li><span class="lang-en inline">Relationship knowledge</span><span class="lang-pl inline">Wiedza o relacjach</span></li>
              <li><span class="lang-en inline">Assessment of strategic fit</span><span class="lang-pl inline">Ocena dopasowania strategicznego</span></li>
            </ul>
          </article>
          <div class="mcri-role-core"><span>Validate</span><span>Interpret</span><span>Decide</span></div>
          <article class="mcri-role-panel tone-cool">
            <div class="mcri-icon mcri-icon--large">${icon("ai")}</div>
            <h3><span class="lang-en inline">AI layer</span><span class="lang-pl inline">Warstwa AI</span></h3>
            <ul>
              <li><span class="lang-en inline">Summarising and structuring inquiries</span><span class="lang-pl inline">Podsumowanie i strukturyzacja zapytań</span></li>
              <li><span class="lang-en inline">Classification and context enrichment</span><span class="lang-pl inline">Klasyfikacja i wzbogacanie kontekstu</span></li>
              <li><span class="lang-en inline">Opportunity prioritisation</span><span class="lang-pl inline">Priorytetyzacja szans</span></li>
              <li><span class="lang-en inline">Routing recommendation</span><span class="lang-pl inline">Rekomendacja routingu</span></li>
              <li><span class="lang-en inline">Showing confidence and gaps</span><span class="lang-pl inline">Pokazanie confidence i luk</span></li>
            </ul>
          </article>
        </div>
        <div class="mcri-footer-note"><span class="lang-en inline">AI organises the signal. Humans give it meaning and decide what to do.</span><span class="lang-pl inline">AI porządkuje sygnał. Człowiek nadaje mu znaczenie i decyduje o działaniu.</span></div>
      </div>
    </div>
  </section>`;
}

function loopInfographic(){
  return `
  <section class="mcri-section mcri-section--paper" aria-label="Mission Control Room operating loop infographic">
    <div class="wrap">
      <div class="mcri-shell">
        <div class="mcri-head">
          <span class="mcri-rule"></span>
          <div class="lang-en"><h2 class="mcri-title">Mission Control Room in practice</h2><p class="mcri-subtitle">From an operational prototype emerged a repeatable operating model: from signal to action and recorded knowledge.</p></div>
          <div class="lang-pl"><h2 class="mcri-title">Mission Control Room w praktyce</h2><p class="mcri-subtitle">Z operacyjnego prototypu powstał powtarzalny model pracy: od sygnału do działania i zapisanej wiedzy.</p></div>
        </div>
        <div class="mcri-loop-layout">
          <div class="mcri-callouts mcri-callouts--left">
            <div class="mcri-callout tone-warm"><div class="mcri-icon">${icon("bolt")}</div><div><h3><span class="lang-en inline">Signal visible faster</span><span class="lang-pl inline">Szybciej widoczny sygnał</span></h3><p><span class="lang-en inline">Important value is recognised earlier.</span><span class="lang-pl inline">Ważne zapytania są szybciej zauważane.</span></p></div></div>
            <div class="mcri-callout tone-cool"><div class="mcri-icon">${icon("database")}</div><div><h3><span class="lang-en inline">Better organisational memory</span><span class="lang-pl inline">Lepsza pamięć organizacyjna</span></h3><p><span class="lang-en inline">Outcomes and insights become reusable knowledge.</span><span class="lang-pl inline">Wiedza nie ginie w skrzynkach, tylko zasila kolejne decyzje.</span></p></div></div>
          </div>
          <div class="mcri-orbit" aria-label="Signal, qualification, routing, evidence loop">
            <span class="mcri-orbit-ring" aria-hidden="true"></span>
            <span class="mcri-orbit-arrow a1" aria-hidden="true">↘</span><span class="mcri-orbit-arrow a2" aria-hidden="true">↙</span><span class="mcri-orbit-arrow a3" aria-hidden="true">↖</span><span class="mcri-orbit-arrow a4" aria-hidden="true">↗</span>
            <article class="mcri-orbit-node pos-top tone-warm"><span class="mcri-num">01</span><div class="mcri-icon">${icon("document")}</div><h3><span class="lang-en inline">Signal</span><span class="lang-pl inline">Sygnał</span></h3><p><span class="lang-en inline">Incoming inquiries and first signals of value.</span><span class="lang-pl inline">Napływające zapytania i pierwsze sygnały wartości.</span></p></article>
            <article class="mcri-orbit-node pos-right tone-cool"><span class="mcri-num">02</span><div class="mcri-icon">${icon("search")}</div><h3><span class="lang-en inline">Qualification</span><span class="lang-pl inline">Kwalifikacja</span></h3><p><span class="lang-en inline">Assessment of potential, context and urgency.</span><span class="lang-pl inline">Ocena potencjału, kontekstu i pilności.</span></p></article>
            <article class="mcri-orbit-node pos-bottom tone-warm"><span class="mcri-num">03</span><div class="mcri-icon">${icon("refresh")}</div><h3><span class="lang-en inline">Routing &amp; follow-up</span><span class="lang-pl inline">Routing i follow-up</span></h3><p><span class="lang-en inline">Routing to the right people and maintaining momentum.</span><span class="lang-pl inline">Skierowanie do właściwych osób i utrzymanie tempa rozmów.</span></p></article>
            <article class="mcri-orbit-node pos-left tone-cool"><span class="mcri-num">04</span><div class="mcri-icon">${icon("bars")}</div><h3><span class="lang-en inline">Evidence &amp; knowledge</span><span class="lang-pl inline">Dowód i wiedza</span></h3><p><span class="lang-en inline">Capturing outcomes, signals and lessons for further learning.</span><span class="lang-pl inline">Zapisanie rezultatu, sygnałów i wniosków do dalszego uczenia procesu.</span></p></article>
            <div class="mcri-orbit-core"><span class="mcri-mini-rule"></span><h3>Mission<br>Control Room</h3><p><span class="lang-en inline">People + process + AI</span><span class="lang-pl inline">Ludzie + proces + AI</span></p></div>
          </div>
          <div class="mcri-callouts mcri-callouts--right">
            <div class="mcri-callout tone-cool"><div class="mcri-icon">${icon("gear")}</div><div><h3><span class="lang-en inline">Less manual chaos</span><span class="lang-pl inline">Mniej ręcznego chaosu</span></h3><p><span class="lang-en inline">A clearer process reduces scattered follow-up.</span><span class="lang-pl inline">Jasny proces zastępuje rozproszone działania.</span></p></div></div>
          </div>
        </div>
        <div class="mcri-footer-note"><span class="lang-en inline">The process came first. Only then could it be automated deliberately.</span><span class="lang-pl inline">Najpierw powstał proces. Dopiero potem można było go świadomie automatyzować.</span></div>
      </div>
    </div>
  </section>`;
}

function injectInfographics(){
  if(document.querySelector(".mcri-section")) return;
  ensureInfographicStyles();
  const human=document.querySelector("#human");
  const mcr=document.querySelector("#mcr");
  const humanAi=document.querySelector("#human-ai");
  if(human) human.insertAdjacentHTML("afterend",processInfographic());
  if(mcr) mcr.insertAdjacentHTML("afterend",loopInfographic());
  if(humanAi) humanAi.insertAdjacentHTML("afterend",rolesInfographic());
}

injectInfographics();
