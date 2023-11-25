<template>
	<div class="input__wrapper">
		<div class="input__inner">
			<input :class="{ input: true }" required :value="value" @input="$emit('input', $event)" placeholder="Write down your question..." />
			<img class="input__img" src="../../assets/img/send_button.svg" />
		</div>
	</div>
</template>

<script>
export default {
	name: "input",
	props: {
		value: {
			type: String,
			default: "",
		},
	},
};
</script>

<style scoped>
.input__wrapper {
	display: flex;
	flex-direction: column;
	width: 600px;
}
.input {
	color: black;
	padding: 16px 55px 16px 40px;
	width: inherit;
	outline: none;
	font-family: "Inter", sans-serif;
	font-size: 20px;
	font-style: normal;
	font-weight: 500;
	border-radius: 15px;
	background: #ede3e8;
	border: none;
}
.input__inner {
	width: inherit;
	position: relative;
	display: flex;
	align-items: center;
}
.input__img {
	box-sizing: content-box;
	display: block;
	position: absolute;
	cursor: pointer;
	right: 0;
	width: 28px;
	height: 28px;
	padding-right: 27px;
}
</style>
