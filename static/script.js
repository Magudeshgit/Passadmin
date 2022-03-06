var slideout = document.querySelector('.nav-close-tab')
var nav = document.querySelector('.nav')
var arr1 = document.querySelector('.arr1')
var arr2 = document.querySelector('.arr2')
slideout.addEventListener('click', slide)
function slide() {
	slideout.classList.toggle('slide')
	nav.classList.toggle('active')
	arr1.classList.toggle('rot1')
	arr2.classList.toggle('rot2')
};