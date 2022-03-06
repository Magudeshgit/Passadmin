setTimeout(start, 10000)
function start(){
console.log("go die")
document.onload = function init(){
var navbtn = document.querySelector('.nav-tabb')
var nav = document.querySelector('.nav-open-tab')
var navexit = document.querySelector('.nav-exit')
navbtn.addEventListener('click', function navfunc(){
	nav.classList.toggle('active')
})
}
}
