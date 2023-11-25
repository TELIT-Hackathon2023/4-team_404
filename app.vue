<template>
	<div class="main">
		<div class="registration">
			<div class="header"><span>Film</span> Assistant</div>
			<div class="description">Here you can find a movie to watch and get some information about it from our chat assistant. Get started!</div>
			<hr>
			<BaseButton></BaseButton>
			<BaseButton>Sign up</BaseButton>
			<BaseButton>Quick question</BaseButton>
		</div>			
	</div>
</template>
<style scoped>
	*{
		box-sizing: border-box;
		font-family: 'Inter', sans-serif;
		color: white;
	}
	.main{
		height: 100vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		background: #1C1419;
	}
	.registration{
		display: block;
		flex-direction: column;
		width: 737px;
		height: 415px;
		border-radius: 15px;
		background: #371B29;
		padding: 50px 100px;
	}
	.header{
		font-weight: 900;
		font-size: 50px;
	}
	.description{
		font-weight: 400;
		font-size: 13px;
	}
	hr{
		height: 2px;
		width: 50%;
		background: white;;
		border: none;
	}
	.base-button{
		margin-top: 20px;
		margin-left: auto;
    	margin-right: auto;
	}
</style>
