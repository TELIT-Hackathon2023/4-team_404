<template>
    <button class="base-button">
        <slot>Log in</slot>
    </button>
</template>

<script>
export default {
    name: "base-button"
}
</script>

<style scoped>
    .base-button{
        width: 284px;
        text-decoration: none;
        padding: 12px 0;
        border-radius: 6px;
        background-color: #1B74AC;
        color: #F8FAFF;
        display: inline-block;
        border: none;
        font-family: Helvetica;
        font-size: 18px;
    }
    .base-button:disabled{
        pointer-events: none;
        background-color: #8CB6D1;
    }
    .base-button:active{
        background-color: #2E495A;
    }
    
</style>