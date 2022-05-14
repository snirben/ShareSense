<template>
  <div id="app">
  <ul v-if="this.$route.name === 'Login' || this.$route.name === 'Register'"></ul>
  <ul v-else>
  <li id="logout"><a @click="logout"><font-awesome-icon icon="fa-solid fa-right-from-bracket" /> יציאה</a>  </li>
  </ul>

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
  },
  methods: {
      logout() {
      this.$router.push({path: '/'}).catch();
    }
  }
}
</script>

<style>
body{
background-color: #ffbc51;
background-image: linear-gradient(0deg, #ffbc51 0%, #ffffff 68%, #ffffff 100%);
background-repeat: no-repeat;
  background-size: cover;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #fff;
  border: 
}

#logout {
  float: right;
}

li a {
  display: block;
  color: #F55353;;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  cursor: pointer;
}

li a:hover {
  background-color: orange;
  color: white;
}
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
