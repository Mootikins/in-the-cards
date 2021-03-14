<script lang="ts">
	let text =
		'Hi, this is Jim from accounting. We noticed a $1,200 charge labeled "___" Can you explain?';
	let pick = 1;
</script>

<div class="play-area">
	<div class="black-card">
		{text}
	</div>
</div>

<style type="text/scss">
	.play-area {
		height: calc(var(--vh, 1vh) * 50);
		display: flex;
		flex-direction: row;
		justify-content: center;
		place-items: center;
	}

	.black-card {
		font-size: 1.5rem;
		font-weight: 700;
		background-color: black;
		color: white;
		padding: 1.5rem;
		border-radius: 1rem;
		max-width: 60%;

		@media (max-width: 320px) {
			font-size: 1.25rem;
			padding: 1rem;
			max-width: 75%;
		}
	}
</style>
