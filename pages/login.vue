<template>
	<div class="main">
		<div class="registration">
            <div class="wrapper_registration">
                <div class="wrapper-header">
                    <div class="hr_login"></div>
                    <div class="header"><span class="color-text">Log</span> in</div>
                    <div class="hr_login"></div>
                </div>
                <AuthInput class="input-reg" placeholder="Enter your email" v-model="password"/>
                <AuthInput class="input-reg" placeholder="Enter your password" v-model="login"/>
                <BaseButton @click="goToChat"></BaseButton>
            </div>
        </div>
	</div>
</template>

<script>
export default {
	name: "Login",
    data() {
		return {
			login: "",
            password: ""
		};
	},
	methods: {
		goToChat(){
            this.$router.push('/chat');
        },
	}
};
</script>

<style>
@import url("~/assets/css/global.css");
.registration{
    width: 737px;
}
.main {
    height: 100vh;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 0 50px;
}
.wrapper-registration{
    width: 498px;
}
.wrapper-header{
    display: flex;
    align-items: center;
    width: 100%;
}
.header{
    padding: 0 75px;
}
.hr_login{
    height: 2px;
    background: #E10075;
    margin: 0;
    flex: 1;
}
.input-reg{
    margin-top: 45px;;
}
.base-button{
    margin-top: 30px;
}
</style>
