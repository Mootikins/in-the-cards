<script lang="ts">
	import './index.css';
	import Menu from './Menu.svelte';
	import PlayArea from './PlayArea.svelte';
	import Hand from './Hand.svelte';

	let cards = [
		{ text: '"Tweeting."', selected: false },
		{ text: '(I am doing Kegels right now.)', selected: false },
		{ text: '10,000 Syrian refugees.', selected: false },
		{ text: '100% Pure New Zealand.', selected: false },
		{ text: '2 Girls 1 Cup.', selected: false },
		{ text: '400 years of colonial atrocities.', selected: false },
		{ text: '50 mg of Zoloft daily.', selected: false },
	];

	let vh: number = window.innerHeight * 0.01;
	function resizeFix() {
		vh = window.innerHeight * 0.01;
		document.documentElement.style.setProperty('--vh', `${vh}px`);
	}
</script>

<svelte:window on:resize={resizeFix} on:load={resizeFix} />

<div class="App">
	<Menu />
	<PlayArea />
	<Hand {cards} />
</div>

<style type="text/scss">
	:global(*) {
		padding: 0;
		margin: 0;
	}

	.App {
		position: relative;
		font-size: 100%;
		height: 100vh;
		height: calc(var(--vh, 1vh) * 100);
		font-family: Product Sans, Arial, Helvetica, sans-serif;
		overflow: hidden;
	}
</style>
