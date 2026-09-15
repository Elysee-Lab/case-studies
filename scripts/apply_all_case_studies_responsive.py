from pathlib import Path

MARKER = 'global-responsive-contract-2026-09-15'

COMMON = r'''<style id="global-responsive-contract-2026-09-15">
html,body{max-width:100%;overflow-x:hidden}
img,svg,video,canvas{max-width:100%;height:auto}
*,*:before,*:after{min-width:0}
@media(max-width:760px){
  .wrap{max-width:100%}
  .jump-nav{max-width:100%;overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}
  .scenarioWrap,.scenarioCard{max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}
}
</style>'''

INTELEVENT = r'''<style id="global-responsive-contract-2026-09-15">
html,body{max-width:100%;overflow-x:hidden}
img,svg,video,canvas{max-width:100%;height:auto}
*,*:before,*:after{min-width:0}
@media(max-width:760px){
  .wrap{width:calc(100% - 28px);max-width:100%;margin-inline:auto}
  .topbar{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;padding:10px 0;align-items:center}
  .brand{white-space:normal;font-size:1.22rem;line-height:1.1;overflow-wrap:anywhere}
  .brand small{display:block;font-size:.68rem;margin-top:4px}
  .lang{margin-left:0;justify-self:end;align-self:start}
  .nav{grid-column:1/-1;order:3;width:100%;max-width:100%;display:flex;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;padding:3px 0 5px}
  .nav::-webkit-scrollbar{display:none}
  .nav a{flex:0 0 auto;font-size:.82rem;padding:8px 10px}
  .hero{padding:42px 0 48px}
  .heroGrid{grid-template-columns:1fr;gap:26px}
  .heroCopy{gap:18px}
  h1{font-size:clamp(2.7rem,13vw,4.25rem);line-height:.98;letter-spacing:-.05em}
  h2{font-size:clamp(2rem,9vw,3.15rem);line-height:1.02}
  .lead{font-size:1.04rem;line-height:1.58}
  .heroVisual{min-height:0;position:relative;display:block;padding:0}
  .cardStack{position:static;inset:auto;display:grid;gap:12px}
  .vcard{position:relative;left:auto!important;right:auto!important;top:auto!important;bottom:auto!important;transform:none!important;width:100%;min-height:0;padding:18px;border-radius:20px}
  .vcard.one,.vcard.two,.vcard.three{left:auto;right:auto;top:auto;bottom:auto;transform:none}
  .vcard .name{font-size:1.42rem;line-height:1.05;margin-top:10px}
  .vcard .line{font-size:.98rem;line-height:1.45;overflow-wrap:anywhere}
  .snap{position:relative;right:auto;bottom:auto;width:auto;height:auto;min-height:0;border:0;border-radius:999px;justify-self:start;display:inline-flex;place-items:unset;align-items:center;gap:8px;padding:10px 14px;text-align:left}
  .section{padding:52px 0}
  .head{grid-template-columns:1fr;gap:12px;margin-bottom:26px}
  .head p{font-size:1rem;line-height:1.6}
  .card,.callout,.cost,.phase,.stake,.phone,.result,.node,.metricBoard,.evidence,.articleBox{max-width:100%;min-width:0}
  .callout{grid-template-columns:1fr;padding:22px;border-radius:22px}
  .costGrid,.stakeholders,.g2,.g3,.g4,.lifecycle,.pipeline,.agentStrip,.metricTop{grid-template-columns:1fr}
  .capture{grid-template-columns:1fr;gap:16px}
  .arrow{transform:rotate(90deg)}
  .camera{min-height:250px;padding:18px}
  .businesscard{width:100%;transform:none}
  .phase,.node{min-height:auto;padding:16px}
  .phase:not(:last-child):after,.node:not(:last-child):after{content:"↓";display:block;right:auto;left:50%;transform:translateX(-50%);top:auto;bottom:-17px}
  .evidence,.articleBox,.foot{grid-template-columns:1fr}
  .articleBox a{justify-self:stretch;text-align:center}
  .footer{padding:56px 0 72px}
}
</style>'''

MISSION = r'''<style id="global-responsive-contract-2026-09-15">
html,body{max-width:100%;overflow-x:hidden}
img,svg,video,canvas{max-width:100%;height:auto}
*,*:before,*:after{min-width:0}
@media(max-width:760px){
  .wrap{width:calc(100% - 28px);max-width:100%;margin-inline:auto}
  .topbar{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;padding:10px 0;align-items:center}
  .brand{white-space:normal;font-size:1.14rem;line-height:1.12;overflow-wrap:anywhere}
  .brand small{display:block;font-size:.68rem;margin-top:4px}
  .lang{margin-left:0;justify-self:end;align-self:start}
  .nav{grid-column:1/-1;order:3;width:100%;max-width:100%;display:flex;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;padding:3px 0 5px}
  .nav::-webkit-scrollbar{display:none}
  .nav a{flex:0 0 auto;font-size:.82rem;padding:8px 10px}
  .hero{padding:42px 0 48px}
  .heroGrid{grid-template-columns:1fr;gap:26px}
  .heroCopy{gap:18px}
  h1{font-size:clamp(2.7rem,13vw,4.25rem);line-height:.98;letter-spacing:-.05em}
  h2{font-size:clamp(2rem,9vw,3.15rem);line-height:1.02}
  .lead{font-size:1.04rem;line-height:1.58}
  .heroVisual{min-height:0;position:relative;display:grid;gap:12px;padding:0}
  .panel{position:relative;max-width:100%;transform:none!important;box-shadow:0 10px 28px rgba(20,31,45,.08)}
  .panel.label{order:1;width:100%;left:auto;right:auto;top:auto;bottom:auto;padding:15px;border-radius:18px}
  .panel.main{order:2;inset:auto;width:100%;padding:18px;border-radius:22px}
  .panel.note{order:3;width:100%;left:auto;right:auto;top:auto;bottom:auto;padding:16px;border-radius:18px}
  .systemFlow{margin-top:16px;gap:6px}
  .flowRow{grid-template-columns:28px minmax(0,1fr);gap:9px;padding:12px 8px}
  .flowRow .signal{grid-column:2;justify-self:start}
  .section{padding:52px 0}
  .head{grid-template-columns:1fr;gap:12px;margin-bottom:26px}
  .head p{font-size:1rem;line-height:1.6}
  .bigStatement{grid-template-columns:1fr;padding:24px;border-radius:22px}
  .timeline,.chain,.redteam,.g2,.g3,.g4{grid-template-columns:1fr}
  .stage{min-height:auto;padding:18px}
  .stage:after{display:none}
  .chain .node{min-height:auto;padding:16px}
  .chain .node:not(:last-child):after{content:"↓";display:block;right:auto;left:50%;transform:translateX(-50%);top:auto;bottom:-17px}
  .compare{grid-template-columns:1fr}
  .arrow{transform:rotate(90deg)}
  .layer,.claim{grid-template-columns:1fr;gap:8px}
  .layer .badge{justify-self:start}
  .control{padding:18px;border-radius:22px}
  .controlGrid{grid-template-columns:1fr;gap:18px}
  .controlScreen{min-height:0;padding:18px;border-radius:18px}
  .card,.stage,.state,.layer,.control,.controlScreen,.challenge,.claim{max-width:100%;min-width:0}
  .foot{grid-template-columns:1fr}
  .footer{padding:56px 0 72px}
}
</style>'''

TARGETS = {
    Path('index.html'): COMMON,
    Path('intelevent/index.html'): INTELEVENT,
    Path('mission-control-room/index.html'): MISSION,
}

for path, css in TARGETS.items():
    html = path.read_text(encoding='utf-8')
    if MARKER in html:
        print(f'{path}: already patched')
        continue
    if '</head>' not in html:
        raise RuntimeError(f'{path}: </head> not found')
    path.write_text(html.replace('</head>', css + '</head>', 1), encoding='utf-8')
    print(f'{path}: responsive contract applied')
