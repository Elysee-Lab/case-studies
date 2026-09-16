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
