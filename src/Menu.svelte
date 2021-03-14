<script lang="typescript">
	import { fly } from 'svelte/transition';
	let sidebarOpen: boolean = false;
</script>

<button on:click={() => (sidebarOpen = !sidebarOpen)}>
	{#if sidebarOpen}
		<svg viewBox="0 0 24 24" stroke="white">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M6 18L18 6M6 6l12 12"
			/>
		</svg>
	{:else}
		<svg viewBox="0 0 24 24" stroke="black">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M4 6h16M4 12h16M4 18h16"
			/>
		</svg>
	{/if}
</button>

{#if sidebarOpen}
	<div
		transition:fly={{
			x: Math.min(384, Math.floor(window.innerWidth)),
			opacity: 1.0,
		}}
		class="menu"
	/>
{/if}

<style type="text/scss">
	.menu {
		position: absolute;
		height: calc(var(--vh, 1vh) * 100);
		color: white;
		background-color: hsl(0, 0, 15%);
		width: min(100vw, 24rem);
		top: 0;
		bottom: 0;
		right: 0;
		font-size: 3rem;
		font-weight: 700;
	}

	button {
		position: absolute;
		border: none;
		background-color: unset;
		cursor: pointer;
		top: 1rem;
		right: 1rem;
		z-index: 10;
		width: 3rem;
		height: 3rem;
		padding: 0;
	}
</style>
