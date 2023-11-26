<template>
	<div class="container">
		<div class="history">
			<div class="user-description">
				<img class="user-photo" src="../assets/img/avatar.png" alt="" />
				<div class="user-info">
					<div class="user-fullname"><span class="color-text">Diana</span> Osyka</div>
					<div class="user-email">diana.osyka@outlook.com</div>
				</div>
			</div>
			<div class="prompts">
				<div class="prompt-card"
					v-for="name in namesOfChates"
					:key="name"
					@click="changeCurrentChat(name)"
				>
					<div class="hr-card"></div>
					<div class="chat-name">{{ name }}</div>
					<img @click.stop="handleRemove(name)" src="../assets/img/bin.svg" alt="" class="bin" />
				</div>
				
			</div>
		</div>
		<div class="chat-bot" v-if="currentChat">
			<div class="film-name">
				<div class="text">{{currentChat}}</div>
				<div class="hr-chat"></div>
			</div>
			<div class="chat">
				<div class="message">Why do certain filmmakers gravitate towards specific genres, and how does the choice of genre impact the overall narrative and audience engagement?</div>
				<div class="message user-prompt">Why do certain filmmakers gravitate towards specific genres, and how does the choice of genre impact the overall narrative and audience engagement?</div>
				<div class="message">In the vast galaxy of cinema, where storytelling takes on myriad forms and emotions, questions often arise, leading us to explore the depths of narrative creativity and filmmaking magic. Join us on a journey through the lens of uncertainty as we delve into the world of films and pose intriguing questions that spark curiosity and contemplation. Join us on a journey through the lens of uncertainty as we delve into the world of films and.</div>
				<div class="message user-prompt">In the vast galaxy of cinema, where storytelling takes on myriad forms and emotions, questions often arise, leading us to explore the depths of narrative creativity and filmmaking magic. Join us on a journey through the lens of uncertainty as we delve into the world of films and pose intriguing questions that spark curiosity and contemplation. Join us on a journey through the lens of uncertainty as we delve into the world of films and.</div>
				<div class="message">Why do certain filmmakers gravitate towards specific genres, and how does the choice of genre impact the overall narrative and audience engagement?</div>
			</div>
			<BaseInput></BaseInput>
		</div>
	</div>
</template>

<script>
export default {
	name: "Chat",

	data() {
		return {
			namesOfChates: [
				"Film Titanic questions",
				"Film Twilight questions",
				"Anime Death Note questions",
				"Cartoon Avatar questions",
				"Film Harry Potter questions",
				"Anime Attack on Titan questions",
				"Film Star Wars questions",
				"Film Jurassic Park questions",
				"Cartoon Tom and Jerry questions",
			],
			currentChat: "",
			chatHistory: [[],[],[],[],[]],
		};
	},
	methods: {
		changeCurrentChat(chat){
			this.currentChat = chat;
		},
		handleRemove(chateToRemove) {
			if(this.currentChat == chateToRemove) this.currentChat = 0;
			this.namesOfChates = this.namesOfChates.filter((n, i) => {
				if (n !== chateToRemove) return true;
				return false;
			});
		},
	}
};
</script>

<style>
@import url("~/assets/css/global.css");
.container {
	display: flex;
}
.bin{
	cursor: pointer;
}
.history {
	width: 650px;
	background: #371b29;
	display: flex;
	height: 100vh;
	flex-direction: column;
}
.user-description {
	display: flex;
	align-items: center;
	margin: 60px 50px;
}
.user-info {
	margin-left: 45px;
}
.user-fullname {
	font-size: 32px;
	font-weight: 700;
}
.user-photo {
	display: block;
	width: 127px;
	height: 127px;
}
.user-email {
	font-size: 22px;
	font-weight: 400;
}
.prompts{
	flex: 1;
	overflow-y: scroll;
}
.prompt-card {
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 3px solid #371b29;
	background: #2c131f;
	height: 100px;
	padding-right: 35px;
}
.hr-card {
	padding: 0;
	border: none;
	width: 60px;
	height: 2px;
	background: #e10075;
}
::-webkit-scrollbar {
	display: flex;
	width: 10px;
}
::-webkit-scrollbar-track {
	background: transparent;
}
::-webkit-scrollbar-thumb {
	background: rgba(255, 255, 255, 0.2);
	height: 50px;
}
::-webkit-scrollbar-thumb:hover {
	background: rgba(255, 255, 255, 0.2);
}
.chat-name {
	font-size: 25px;
	font-weight: 500;
}
.chat-bot {
	flex-grow: 1;
	display: flex;
	flex-direction: column;
	padding: 35px 130px 90px 130px ;
	height: 100vh;
}

.film-name{
	position: relative;
	font-size: 32px;
	font-weight: 700;
	display: flex;
	align-items: center;
	margin-bottom: 10px;
}
.chat{
	flex: 1;
	overflow-y: scroll;
	display: flex;
	flex-direction: column;
}
.hr-chat{
	padding: 0;
	border: none;
	flex: 1;
	height: 2px;
	background: #e10075;
	margin-left: 35px;
}
.film-name::before{
	position: absolute;
	left: -130px;
	content: "";
	padding: 0;
	border: none;
	width: 100px;
	height: 2px;
	background: #e10075;
}
.input__wrapper{
	margin-top: 10px;
}
.message{
	font-size: 20px;
	width: 700px;
	padding: 10px 15px;
	background: #371B29;
	margin-top: 30px;
}
.user-prompt{
	align-self: flex-end;
}
</style>
