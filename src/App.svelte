<script lang="ts">
	import './index.css';
	import Menu from './Menu.svelte';
	let vh: number = window.innerHeight * 0.01;
</script>

<svelte:window
	on:resize={() => {
		vh = window.innerHeight * 0.01;
		document.documentElement.style.setProperty('--vh', `${vh}px`);
	}}
/>

<div class="App">
	<Menu />
	<div class="play-card">Play</div>
	<div class="hand">Hand</div>
</div>

<style type="text/scss">
	:global(*) {
		padding: 0;
		margin: 0;
	}

	.App {
		position: relative;
		height: 100vh;
		height: calc(var(--vh, 1vh) * 100);
		font-family: Product Sans, Arial, Helvetica, sans-serif;
		overflow: hidden;

		.play-card {
			font-size: 3rem;
			font-weight: 700;
			height: calc(var(--vh, 1vh) * 50);
		}

		.hand {
			font-size: 3rem;
			font-weight: 700;
			height: calc(var(--vh, 1vh) * 50);
			background-color: black;
			color: white;
		}
	}
</style>
