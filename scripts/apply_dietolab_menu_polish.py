from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')
marker = 'id="menu-polish-2026-09-14"'

if marker in html:
    raise SystemExit('menu polish already present')

css = r'''
<style id="menu-polish-2026-09-14">
/* Compact, editorial navigation. Fixes the oversized active pill and header separator wrapping. */
.case-label b{white-space:nowrap!important}
.case-label .case-sep{display:inline!important;margin:0!important;padding:0 4px!important;color:var(--teal)!important;font:inherit!important;letter-spacing:inherit!important;text-transform:none!important}

.jumpbar{background:rgba(255,255,255,.97)!important;border-top:1px solid rgba(27,50,50,.055)!important;border-bottom:1px solid rgba(27,50,50,.08)!important;box-shadow:0 6px 18px rgba(27,50,50,.025)!important}
.jumpbar .wrap{max-width:1240px!important}
.jump-nav{height:52px!important;min-height:52px!important;display:none;align-items:center!important;align-content:center!important;gap:2px!important;padding:6px 0!important;white-space:nowrap!important;overflow-x:auto!important;overflow-y:hidden!important;scrollbar-width:none!important;-webkit-overflow-scrolling:touch!important}
.jump-nav.active{display:flex!important}
.jump-nav::-webkit-scrollbar{display:none!important}
.jump-nav a{position:relative!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;flex:0 0 auto!important;color:#526665!important;background:transparent!important;border:0!important;border-radius:8px!important;box-shadow:none!important;font-family:Montserrat,Inter,Arial,sans-serif!important;font-size:13px!important;font-weight:650!important;line-height:1.2!important;padding:8px 11px 10px!important;transition:color .16s ease,background-color .16s ease!important}
.jump-nav a:hover{color:var(--teal)!important;background:var(--limeSoft)!important;border-color:transparent!important}
.jump-nav a.active{color:var(--teal)!important;background:transparent!important;font-weight:800!important;box-shadow:none!important}
.jump-nav a.active:after{content:""!important;position:absolute!important;left:16%!important;right:16%!important;bottom:3px!important;height:3px!important;border-radius:999px!important;background:var(--lime)!important}

@media (min-width:1101px){
  .jump-nav{justify-content:center!important;flex-wrap:nowrap!important;overflow-x:visible!important}
  .jump-nav a{font-size:12.75px!important;padding-left:10px!important;padding-right:10px!important}
}
@media (max-width:1100px){
  .jumpbar .wrap{padding-left:18px!important;padding-right:18px!important}
  .jump-nav{justify-content:flex-start!important;flex-wrap:nowrap!important;overflow-x:auto!important}
}
@media (max-width:640px){
  .case-label b{font-size:12px!important}
  .jump-nav{height:50px!important;min-height:50px!important}
  .jump-nav a{font-size:12.25px!important;padding:8px 10px 9px!important}
}
</style>
'''

if '</head>' not in html:
    raise SystemExit('missing </head>')

html = html.replace('</head>', css + '\n</head>', 1)
path.write_text(html, encoding='utf-8')
print('menu polish applied')
