<template>
	<div class="input__wrapper">
		<div class="input__inner">
			<input :class="{ input: true, password: password, incorrect: errorType > 0, correct: correct }" :type="inputType" id="name" name="name" required :value="inputValue" @input="$emit('input', $event)" />
			<img class="input__img" :src="imgSrc" alt="" v-if="password" @click="toggleInputType" />
		</div>
		<span class="input__text-error">{{ errors[errorType] }}</span>
	</div>
</template>

<script>
export default {
	name: "input",
	props: {
		errorType: {
			type: Number,
			default: 0,
		},
		password: {
			type: Boolean,
			default: false,
		},
		correct: {
			type: Boolean,
			default: false,
		},
		value: {
			type: String, // Встановіть тип на той, який ви очікуєте (String, Number і т. д.)
			default: "",
		},
	},
	data() {
		return {
			errors: ["", "This email is invalid. Please check it and try again.", "Seems this password is wrong. Please try again.", "This doesn’t seem a real name. Please try again.", "Seems your passwords do not match"],
			inputType: this.password ? "password" : "text",
		};
	},
};
</script>

<style scoped>
.input__wrapper {
	display: flex;
	flex-direction: column;
	width: 284px;
}
.input {
	padding: 8px;
	height: 48px;
	width: inherit;
	border-radius: 6px;
	border: 1px solid var(--input-stroke, #c7c8c9);
	background: var(--input-inactive, #f3f7ff);
	outline: none;
	color: var(--text-dark, #00040d);
	font-family: Roboto;
	font-size: 14px;
}
.input:focus {
	background: var(--input-active, #f8faff);
}
.correct {
	border: 1px solid var(--input-correct, #3a8a51);
	background: var(--input-active, #f8faff);
}
.incorrect {
	border: 1px solid var(--input-error, #c95545);
	background: var(--input-active, #f8faff);
}
.password {
	padding-right: 32px;
}
.input__text-error {
	color: var(--text-error, #c95545);
	font-family: Helvetica;
	font-size: 11px;
}
.input__inner {
	height: 48px;
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
	width: 16px;
	height: 16px;
	padding: 15px 8px;
}
</style>
