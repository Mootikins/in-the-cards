<script lang="ts">
	import { scale } from 'svelte/transition';
	export let cards: { text: string; selected: boolean }[] = [];
</script>

<div class="hand">
	<div class="inner-wrapper">
		{#each cards as { selected, text }, i (i)}
			<div class="card" class:selected on:click={() => (selected = !selected)}>
				{#if selected}
					<svg
						viewBox="0 0 20 20"
						fill="currentColor"
						class="checkmark"
						transition:scale={{ duration: 200 }}
					>
						<path
							fill-rule="evenodd"
							d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
							clip-rule="evenodd"
						/>
					</svg>
				{/if}
				{text}
			</div>
		{/each}
	</div>
</div>

<style type="text/scss">
	.hand {
		height: calc(var(--vh, 1vh) * 50);
		background-color: black;
		color: white;
		--card-width: 12rem;
		--card-height: 16rem;

		@media (max-width: 320px) {
			--card-width: 9rem;
			--card-height: 12rem;
		}
	}

	.inner-wrapper {
		display: grid;
		grid-gap: 1rem;
		grid-template-columns: calc(50vw - (var(--card-width) / 2));
		grid-auto-flow: column;
		grid-auto-columns: auto;
		height: 100%;
		align-items: center;
		overflow-x: auto;
		scroll-snap-type: x proximity;

		&::before,
		&::after {
			content: 'p';
			color: transparent;
			width: calc(50vw - (var(--card-width) / 2));
		}
	}

	.card {
		background-color: white;
		color: black;
		padding: 1rem;
		font-size: 1.75rem;
		font-weight: 700;
		border-radius: 1rem;
		width: var(--card-width);
		height: var(--card-height);
		scroll-snap-align: center;
		transition: all 0.2s ease-in-out;

		@media (max-width: 320px) {
			font-size: 1.25rem;
			padding: 0.75rem;
		}

		&.selected {
			transform: scale(0.9);
		}
	}

	.checkmark {
		width: 3rem;
		height: 3rem;
		position: absolute;
		bottom: 0.5rem;
		right: 0.5rem;

		@media (max-width: 320px) {
			width: 2rem;
			height: 2rem;
		}
	}
</style>
