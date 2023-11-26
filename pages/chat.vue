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
				<div class="prompt-card" v-for="name in namesOfChates" :key="name" @click="changeindexOfCurrentChate(name)">
					<div class="hr-card"></div>
					<div class="chat-name">{{ name }}</div>
					<img @click.stop="handleRemove(name)" src="../assets/img/bin.svg" alt="" class="bin" />
				</div>
			</div>
		</div>
		<div class="chat-bot">
			<div class="film-name" v-if="indexOfCurrentChate != -1">
				<div class="text">{{ namesOfChates[indexOfCurrentChate] }}</div>
				<div class="hr-chat"></div>
			</div>
			<div class="chat" v-for="(mes, i) in chateHistory[indexOfCurrentChate]" :key="i">
				<div class="message" :class="{ 'user-prompt': i % 2 == 0 }">{{ mes }}</div>
			</div>
			<div class="input__wrapper" :class="{ to_bottom: indexOfCurrentChate == -1 }">
				<div class="input__inner">
					<input :class="{ input: true }" v-model="request" placeholder="Write down your question..." @keyup.enter="createContinueChate" />
					<img class="input__img" src="../assets/img/send_button.svg" @click="createContinueChate" />
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
export default {
	name: "Chat",

	data() {
		return {
			namesOfChates: ["Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
			indexOfCurrentChate: -1,
			chateHistory: [
				["1Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions"],
				["2Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["3Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["4Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["5Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["6Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["7Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["8Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
				["9Film Titanic questions", "Film Twilight questions", "Anime Death Note questions", "Cartoon Avatar questions", "Film Harry Potter questions", "Anime Attack on Titan questions", "Film Star Wars questions", "Film Jurassic Park questions", "Cartoon Tom and Jerry questions"],
			],
			request: "",
			counter: 1,
		};
	},
	methods: {
		changeindexOfCurrentChate(chate) {
			this.indexOfCurrentChate = this.namesOfChates.findIndex((el) => el == chate);
		},
		handleRemove(chateToRemove) {
			if (this.indexOfCurrentChate == this.namesOfChates.findIndex((el) => el == chateToRemove)) this.indexOfCurrentChate = -1;
			let indexOfDeleteHistoryChate;
			this.namesOfChates = this.namesOfChates.filter((n, i) => {
				if (n !== chateToRemove) {
					indexOfDeleteHistoryChate = i;
					return true;
				}
				return false;
			});

			this.chateHistory = this.chateHistory.filter((el, k) => {
				if (k != indexOfDeleteHistoryChate) return true;
				return false;
			});
		},
		createContinueChate() {
			if (this.request.trim() == "") {
				this.request = "";
				return;
			}
			if (this.indexOfCurrentChate != -1) {
				this.chateHistory[this.indexOfCurrentChate].push(this.request.trim());

				axios
					.post("https://127.0.0.1:5000/find_data", {
						query: this.request.trim(),
					})
					.then((response) => {
						console.log(response.data);
						this.chateHistory[this.indexOfCurrentChate].push(response.data);
					})
					.catch((error) => {
						console.error(error);
					});


				axios
					.get("https://127.0.0.1:5000/find_data", {
						params: {
							query: this.request.trim(),
						},
					})
					.then((response) => {
						console.log(response.data);
						this.chateHistory[this.indexOfCurrentChate].push(response.data);
					})
					.catch((error) => {
						console.error(error);
					});
			} else {
				this.namesOfChates.unshift("New chat " + this.counter);
				this.chateHistory.unshift([this.request.trim()]);

				axios
					.post("https://127.0.0.1:5000/find_data", {
						query: this.request.trim(),
					})
					.then((response) => {
						console.log(response.data);
					})
					.catch((error) => {
						console.error(error);
					});

				axios
					.get("https://127.0.0.1:5000/find_data", {
						params: {
							query: this.request.trim(),
						},
					})
					.then((response) => {
						this.chateHistory[0].push(response.data);
					})
					.catch((error) => {
						console.error(error);
					});

				this.counter++;
			}
			this.request = "";
		},
	},
};
</script>

<style>
@import url("~/assets/css/global.css");
.container {
	display: flex;
}
.bin {
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
.prompts {
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
	padding: 35px 130px 90px 130px;
	height: 100vh;
}

.film-name {
	position: relative;
	font-size: 32px;
	font-weight: 700;
	display: flex;
	align-items: center;
	margin-bottom: 10px;
}
.chat {
	flex: 1;
	overflow-y: scroll;
	display: flex;
	flex-direction: column;
	position: relative;
}
.hr-chat {
	padding: 0;
	border: none;
	flex: 1;
	height: 2px;
	background: #e10075;
	margin-left: 35px;
}
.film-name::before {
	position: absolute;
	left: -130px;
	content: "";
	padding: 0;
	border: none;
	width: 100px;
	height: 2px;
	background: #e10075;
}
.input__wrapper {
	margin-top: 10px;
}
.message {
	font-size: 20px;
	width: 700px;
	padding: 10px 15px;
	background: #371b29;
	margin-top: 30px;
}
.user-prompt {
	align-self: flex-end;
}
.to_bottom {
	margin-top: 775px;
}
.input__wrapper {
	display: flex;
	flex-direction: column;
	width: 100%;
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
	bottom: 12px;
	padding-right: 27px;
}
</style>
