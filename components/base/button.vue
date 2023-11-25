<template>
	<button class="base-button" :class="{ border: border }">
		<slot>Log in</slot>
	</button>
</template>

<script>
export default {
	name: "base-button",
	props: {
		border: {
			type: Boolean,
			default: false,
		},
	},
};
</script>

<style scoped>
.base-button {
	display: block;
	width: 250px;
	padding: 13px 0px;
	border-radius: 8px;
	border: 2px solid #e10075;
	background: #371b29;
	cursor: pointer;
}
.border {
	background: white;
	border: none;
	background: #e10075;
}
</style>
