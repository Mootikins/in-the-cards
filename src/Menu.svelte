<script lang="typescript">
	import { fly } from 'svelte/transition';
	let open: boolean = false;
</script>

{#if open}
	<!-- X icon -->
	<button on:click={() => (open = !open)}>
		<svg
			transition:fly={{ x: 100, duration: 500, opacity: 1.0 }}
			viewBox="0 0 24 24"
			stroke="white"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M6 18L18 6M6 6l12 12"
			/>
		</svg>
	</button>
{:else}
	<!-- Hamburger icon -->
	<button on:click={() => (open = !open)}>
		<svg
			transition:fly={{ x: -200, duration: 500, opacity: 1.0 }}
			viewBox="0 0 24 24"
			stroke="black"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M4 6h16M4 12h16M4 18h16"
			/>
		</svg>
	</button>
{/if}

{#if open}
	<div
		transition:fly={{
			x: Math.min(384, Math.floor(window.innerWidth)),
			opacity: 1.0,
			duration: 500,
		}}
		class="menu"
	/>
{/if}

<style type="text/scss">
	.menu {
		position: absolute;
		height: calc(var(--vh, 1vh) * 100);
		color: white;
		background-color: black;
		border-left: 0.1rem solid darkgray;
		box-shadow: 0px 0px 1rem rgba($color: #000000, $alpha: 0.5);
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

		svg {
			position: absolute;
			top: 0;
			right: 0;
			left: 0;
			bottom: 0;
		}
	}
</style>
