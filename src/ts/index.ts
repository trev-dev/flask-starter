import '../scss/styles.scss';

const home = document.querySelector<HTMLElement>('.home');
const switchOn = (el: HTMLElement) => el.classList.add('on')

if (home !== null) {
	window.addEventListener('load', () => switchOn(home))
}