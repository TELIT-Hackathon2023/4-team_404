<template>
	<div class="main">
		<div class="registration">
			<div class="header"><span class="color-text">Film</span> Assistant</div>
			<div class="description">Here you can find a movie to watch and get some information about it from our chat assistant. Get started!</div>
			<hr class="hr" />
			<div class="button-row">
				<BaseButton @click="this.$router.push('/login')"></BaseButton>
				<BaseButton border @click="this.$router.push('/login')" >Sign up</BaseButton>
			</div>
			<BaseButton @click="this.$router.push('/login')">Quick question</BaseButton>
		</div>
	</div>
</template>

<style>
@import url("~/assets/css/global.css");
.main {
	height: 100vh;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 0 50px;
}
.description {
	font-weight: 400;
	font-size: 13px;
	max-width: 400px;
	margin-top: 10px;
}
.button-row {
	display: flex;
	flex-wrap: wrap;
}
.base-button {
	margin: 30px auto 0 auto;
}
</style>
