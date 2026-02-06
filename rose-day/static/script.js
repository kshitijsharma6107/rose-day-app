const bouquet = document.querySelector(".bouquet");
const headline = document.getElementById("headline");
const msg = document.querySelector(".message");

function typeText(text){
headline.innerHTML="";
let i=0;
let timer=setInterval(()=>{
headline.innerHTML+=text[i++];
if(i>=text.length) clearInterval(timer);
},80);
}

setTimeout(()=>{
typeText(`Happy Rose Day, ${recipient}!`);
},500);

setTimeout(()=>{
msg.style.opacity=1;
},3500);

document.getElementById("replay").onclick=()=>location.reload();

document.getElementById("share").onclick=()=>{
navigator.clipboard.writeText(location.href);
alert("Link copied!");
};
