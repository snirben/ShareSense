<template>
  <div class="container" v-if="token==null">
    <h1>הרשמה</h1>
    <form action="" method="post" @submit.prevent="register">
      <div>
        <label for="username">
          שם משתמש
        </label>
        <input v-model="username" type="text" id="username" name="username" placeholder="שם משתמש">
      </div>
      <div>
        <label for="password">
          סיסמה
        </label>
        <input v-model="password" type="password" id="password" name="password" placeholder="סיסמה">
      </div>
      <div>
        <label for="password2">
          אישור סיסמה
        </label>
        <input v-model="password2" type="password" id="password2" name="password2" placeholder="אישור סיסמה">
      </div>
      <div>
        <label for="email">
          מייל
        </label>
        <input v-model="email" type="email" id="email" name="email" placeholder="מייל">
      </div>
      <div>
        <label for="first_name">
          שם פרטי
        </label>
        <input v-model="first_name" type="text" id="first_name" name="first_name" placeholder="שם פרטי">
      </div>
      <div>
        <label for="last_name">
          שם משפחה
        </label>
        <input v-model="last_name" type="text" id="last_name" name="last_name" placeholder="שם משפחה">
      </div>
      <div>
        <label for="city">
          עיר
        </label>
        <input v-model="city" type="text" id="city" name="city" placeholder="עיר">
      </div>
      <div>
        <label for="address">
          כתובת
        </label>
        <input v-model="address" type="text" id="address" name="address" placeholder="כתובת">
      </div>
      <div>
        <label for="role">
          סוג משתמש
        </label>
        <v-select v-model="role" :options="[{label: 'Regular User', code: '0'},{label: 'Good Pepole', code: '1'}]"/>
      </div>
      <div>
        <label for="district">
          מחוז
        </label>
        <v-select v-model="district"
                  :options="[{label: 'North', code: 'North'},{label: 'South', code: 'South'},{label: 'Center', code: 'Center'}]"/>
      </div>
      <p class="error" v-if="incorrectAuth">אחד או יותר מהנתונים חסרים או לא תקינים</p>
      <div>
        <button class="submit-login" type="submit">הרשם</button>
      </div>
    </form>
    <div class="to-sign-up">
      <a @click="login"> התחבר</a><p>?יש לך כבר חשבון </p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

export default {
  name: 'loginPage',
  components: {
    vSelect
  },
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      email: '',
      first_name: '',
      last_name: '',
      address: '',
      city: '',
      role: '',
      district: '',
      incorrectAuth: false,
      token: null,
      redirect: {
        '0': '/panicbutton',
        '1': '/goodmans',
        '2': '/alertcenter',
      }
    }
  },
  methods: {
    register() {
      axios.post('http://127.0.0.1:8000/api/register/', {
        username: this.username,
        password: this.password,
        password2: this.password2,
        email: this.email,
        address: this.address,
        first_name: this.first_name,
        last_name: this.last_name,
        city: this.city,
        role: this.role.code,
        district: this.district.code
      }).then(
          resp => {
            this.incorrectAuth = false;
            this.token = resp.data.access
            this.$router.push({path: '/'});
            localStorage.setItem('user-token', resp.data.access)
            console.log(resp);
            // this.$router.push({
            //   name: this.redirect[resp.data.role],
            //   params: {id: resp.data.id, isPanic: resp.data.isPanic}
            // });
            // localStorage.setItem('user-token', resp.data.access)
          }
      ).catch(
          err => {
            this.incorrectAuth = true;
            localStorage.removeItem('user-token')
            console.log(err.data)
          }
      )
    },
    login() {
      console.log("test")
      this.$router.push({path: '/'}).catch();
    }
  }
}
</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito&family=Varela+Round&display=swap');

html, body {
  //height: 90%;
}

.container {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  justify-content: center;
  align-items: center;
    font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
  //height: 100%;
}

h1 {
  color: #F55353;
  font-size: 40px;
}

input {
  width: 100%;
  padding: 12px;
  margin: 8px 0;
  box-sizing: border-box;
  border-radius: 5px;
  border: 1px solid gray;
    font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
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
  cursor: pointer;
    font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;

}

.submit-login:hover {
  background: #F55353;
  cursor: pointer;
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