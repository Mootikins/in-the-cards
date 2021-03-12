<script lang="typescript">
	import { fly } from 'svelte/transition';
	let sidebarOpen: boolean = true;
</script>

<button on:click={() => (sidebarOpen = !sidebarOpen)}>
	{sidebarOpen ? 'Close Menu' : 'Open Menu'}
</button>

{#if sidebarOpen}
	<div transition:fly={{ x: 384 }} class="menu">
		Menu
	</div>
{/if}

<style type="text/scss">
	.menu {
		position: absolute;
		height: calc(var(--vh, 1vh) * 100);
		color: white;
		background-color: hsl(0, 0, 15%);
		width: 24rem;
		top: 0;
		bottom: 0;
		right: 0;
		font-size: 3rem;
		font-weight: 700;
	}

	button {
		position: absolute;
		top: 1rem;
		right: 1rem;
		z-index: 10;
	}
</style>
