<template>
  <div class="container" v-if="token==null">
    <h1>Sign In</h1>
    <form action="" method="post" @submit.prevent="login">
      <div>
        <label for="username">
          Username
        </label>
        <input v-model="username" type="text" id="username" name="username" placeholder="username">
      </div>
      <div class="password">
        <label for="password">
          Password
        </label>
        <input v-model="password" type="password" id="password" name="password" placeholder="password">
      </div>
      <p class="error" v-if="incorrectAuth">User name or password is incorrect</p>
      <div>
        <button class="submit-login" type="submit">Login</button>
      </div>
    </form>
    <div class="to-sign-up">
      <p>Don't have an account? </p><a href="#" @click="register"> create</a>
    </div>
  </div>

</template>


<script>
import axios from 'axios';

export default {
  name: 'loginPage',
  data() {
    return {
      username: '',
      password: '',
      incorrectAuth: false,
      token: null,
      redirect: {
        '0': 'panicbutton',
        '1': 'reguler',
        '2': 'alertcenter',
      }
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/login/', {
        username: this.username,
        password: this.password
      }).then(
          resp => {
            this.incorrectAuth = false;
            this.token = resp.data.access
            this.$router.push({
              name: this.redirect[resp.data.role],
              params: {id: resp.data.id, isPanic: resp.data.isPanic}
            });
            localStorage.setItem('user-token', resp.data.access)
          }
      ).catch(
          err => {
            this.incorrectAuth = true;
            localStorage.removeItem('user-token')
            console.log(err)
          }
      )
    },
    register() {
      console.log("test")
      this.$router.push({path: '/register'}).catch();
    }
  }
}
</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');

html, body {
  height: 90%;
}

.container {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  justify-content: center;
  align-items: center;
  font-family: 'Nunito', sans-serif;
  height: 100%;
}

h1 {
  color: rgba(252, 176, 69, 1);
  font-size: 40px;
}

input[type=password], input[type=text] {
  width: 100%;
  padding: 12px;
  margin: 8px 0;
  box-sizing: border-box;
  font-family: 'Nunito', sans-serif;
  border-radius: 5px;
  border: 1px solid gray;
}

.submit-login {
  transition: all .5s ease;
  font-family: 'Nunito', sans-serif;
  background-color: transparent;
  color: black;
  border-radius: 5px;
  font-size: 17px;
  border: 3px solid rgba(252, 176, 69, 1);
  padding: 8px;
  margin-top: 14px;
  width: 100%;

}

.submit-login:hover {
  background: rgba(252, 176, 69, 1);
}

.to-sign-up {
  display: flex;
  flex-direction: row;
  gap: 5px;
  align-items: center;
  font-size: 14px;
}

a {
  color: #3c3cdb;
  text-decoration: none;
}

.error {
  color: #f10a0a;
}

a:hover {
  color: blue;
}
</style>