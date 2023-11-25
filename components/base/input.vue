<template>
    <div class="input__wrapper">
        <div class="input__inner">
            <input
                :class="{ input: true}"
                required
                :value="value" 
                @input="$emit('input', $event)"
                placeholder="Write down your question..."
            />
        </div>
        <span>{{value}}</span>
    </div>
</template>
  
<script>  
  export default {
    name: "input",
    props: {
      value: {
        type: String,
        default: '',
      },
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
    padding: 16px 55px 16px 40px;
    width: inherit;
    outline: none;
    font-family: 'Inter', sans-serif;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
  }
  .input__inner{
    height: 48px;
    width: inherit;
    position: relative;
    display: flex;
    align-items: center;
  }
</style>