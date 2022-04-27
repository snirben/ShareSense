<template>
  <div id="app">
    <img class="logo" alt="Vue logo" src="./assets/logo.png">
    <router-view />
  </div>
</template>
<script>

export default {
  name: 'App',
  data(){
    return { 
      login: true
    }
  },
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.logo{
  height: 250px;
  width: 300px;
}
</style>
