<script lang="ts">
	import './index.css';
	import Menu from './Menu.svelte';
	import PlayArea from './PlayArea.svelte';
	import Hand from './Hand.svelte';
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
	<PlayArea />
	<Hand />
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
