from pathlib import Path

# Re-run after aligning the regression contract with the existing wrap class.
TARGETS = [
    Path("intelevent/index.html"),
    Path("mission-control-room/index.html"),
]

STYLE = r'''
<style id="shared-case-nav-2026-09-15">
/* Shared two-row case-study navigation, aligned with the DietoLab case-study pattern. */
.shared-case-topbar{
  display:grid!important;
  grid-template-columns:minmax(0,1fr) auto!important;
  grid-template-rows:auto auto!important;
  column-gap:18px!important;
  row-gap:0!important;
  align-items:center!important;
  min-height:0!important;
  padding:12px 0 0!important;
}
.shared-case-topbar>.brand{
  grid-column:1!important;
  grid-row:1!important;
  align-self:center!important;
  padding:0 0 12px!important;
  white-space:normal!important;
  line-height:1.12!important;
}
.shared-case-topbar>.brand small{
  display:block!important;
  margin-top:5px!important;
  font-size:.72rem!important;
  line-height:1.2!important;
}
.shared-case-lang{
  grid-column:2!important;
  grid-row:1!important;
  justify-self:end!important;
  align-self:center!important;
  margin:0 0 12px!important;
}
.shared-case-nav{
  grid-column:1/-1!important;
  grid-row:2!important;
  width:100%!important;
  min-height:52px!important;
  display:flex!important;
  align-items:center!important;
  justify-content:center!important;
  gap:2px!important;
  padding:6px 0!important;
  margin:0!important;
  border-top:1px solid rgba(90,100,105,.10)!important;
  overflow-x:auto!important;
  overflow-y:hidden!important;
  white-space:nowrap!important;
  scrollbar-width:none!important;
  -webkit-overflow-scrolling:touch!important;
  overscroll-behavior-x:contain!important;
}
.shared-case-nav::-webkit-scrollbar{display:none!important}
.shared-case-nav a{
  position:relative!important;
  display:inline-flex!important;
  align-items:center!important;
  justify-content:center!important;
  flex:0 0 auto!important;
  padding:9px 11px 11px!important;
  border-radius:8px!important;
  background:transparent!important;
  color:var(--muted)!important;
  font-size:13px!important;
  font-weight:750!important;
  line-height:1.15!important;
  text-decoration:none!important;
  box-shadow:none!important;
  transition:color .16s ease,background-color .16s ease!important;
}
.shared-case-nav a:hover{
  color:var(--blue)!important;
  background:rgba(36,93,255,.07)!important;
}
.shared-case-nav a.active{
  color:var(--blue)!important;
  background:transparent!important;
  font-weight:900!important;
  box-shadow:none!important;
}
.shared-case-nav a.active:after{
  content:""!important;
  position:absolute!important;
  left:16%!important;
  right:16%!important;
  bottom:3px!important;
  height:3px!important;
  border-radius:999px!important;
  background:var(--blue)!important;
}
@media(max-width:1060px){
  .shared-case-topbar{padding-top:10px!important}
  .shared-case-nav{justify-content:flex-start!important}
}
@media(max-width:760px){
  .shared-case-topbar{
    grid-template-columns:minmax(0,1fr) auto!important;
    gap:0 10px!important;
    padding:10px 0 0!important;
  }
  .shared-case-topbar>.brand{padding-bottom:10px!important;font-size:1.05rem!important}
  .shared-case-topbar>.brand small{font-size:.68rem!important}
  .shared-case-lang{margin-bottom:10px!important}
  .shared-case-nav{
    min-height:50px!important;
    justify-content:flex-start!important;
    padding:5px 0!important;
  }
  .shared-case-nav a{font-size:12.25px!important;padding:8px 10px 10px!important}
}
</style>
'''

for path in TARGETS:
    html = path.read_text(encoding="utf-8")
    if 'id="shared-case-nav-2026-09-15"' in html:
        print(f"{path}: shared nav already present")
        continue

    required = [
        '<div class="wrap topbar">',
        '<nav class="nav"',
        '<div class="lang">',
        '</head>',
    ]
    for marker in required:
        if marker not in html:
            raise SystemExit(f"{path}: expected marker missing: {marker}")

    html = html.replace('<div class="wrap topbar">', '<div class="wrap topbar shared-case-topbar">', 1)
    html = html.replace('<nav class="nav"', '<nav class="nav shared-case-nav"', 1)
    html = html.replace('<div class="lang">', '<div class="lang shared-case-lang">', 1)
    html = html.replace('</head>', STYLE + '\n</head>', 1)

    path.write_text(html, encoding="utf-8")
    print(f"{path}: shared nav applied")
