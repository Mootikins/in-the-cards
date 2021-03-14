<script lang="ts">
	let cards: string[] = [
		'"Tweeting."',
		'(I am doing Kegels right now.)',
		'10,000 Syrian refugees.',
		'100% Pure New Zealand.',
		'2 Girls 1 Cup.',
		'400 years of colonial atrocities.',
		'50 mg of Zoloft daily.',
	];
</script>

<div class="hand">
	<div class="inner-wrapper">
		{#each cards as text, i (i)}
			<div class="card">{text}</div>
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
			content: 'padding';
			color: transparent;
			width: calc(50vw - (var(--card-width) / 2));
		}
	}

	.card {
		background-color: white;
		color: black;
		padding: 1rem;
		font-size: 1.5rem;
		font-weight: 700;
		border-radius: 1rem;
		width: var(--card-width);
		height: var(--card-height);
		scroll-snap-align: center;
		
		@media (max-width: 320px) {
			font-size: 1.25rem;
			padding: 0.75rem;
		}
	}
</style>
