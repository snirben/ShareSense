<template>

  <div class="container" v-if="token==null">
    <h1>התחברות</h1>
    <form action="" method="post" @submit.prevent="login">
      <div>
        <label for="username">
          שם משתמש
        </label>
        <input v-model="username" type="text" id="username" name="username" placeholder="username">
      </div>
      <div class="password">
        <label for="password">
          סיסמה
        </label>
        <input v-model="password" type="password" id="password" name="password" placeholder="password">
      </div>
      <p class="error" v-if="incorrectAuth">User name or password is incorrect</p>
      <div>
        <button class="submit-login" type="submit">התחבר</button>
      </div>
    </form>
    <div class="to-sign-up">
      <p><a @click="register"> צור חשבון</a> </p><p>?אין לך עדיין חשבון </p>
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
        '1': 'goodmans',
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
            console.log(resp.data)
            this.incorrectAuth = false;
            this.token = resp.data.access
            this.$router.push({
              name: this.redirect[resp.data.role],
              params: {id: resp.data.id, isPanic: resp.data.isPanic, name: resp.data.name}
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
@import url('https://fonts.googleapis.com/css2?family=Nunito&family=Varela+Round&display=swap');
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
font-family: 'Varela Round', sans-serif;
  height: 100%;
}

h1 {
  color: #F55353;
  font-size: 40px;
}

input[type=password], input[type=text] {
  width: 100%;
  padding: 12px;
  margin: 8px 0;
  box-sizing: border-box;
  font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
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
  border: 3px solid #F55353;
  padding: 8px;
  margin-top: 14px;
  width: 100%;
font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
}

.submit-login:hover {
  background: #F55353;
}

.to-sign-up {
  cursor: pointer;
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