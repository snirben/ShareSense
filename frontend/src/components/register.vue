<template>
  <div class="container" v-if="token==null">
    <h1>Sign Up</h1>
    <form action="" method="post" @submit.prevent="register">
      <div>
        <label for="username">
          Username
        </label>
        <input v-model="username" type="text" id="username" name="username" placeholder="username">
      </div>
      <div>
        <label for="password">
          Password
        </label>
        <input v-model="password" type="password" id="password" name="password" placeholder="password">
      </div>
      <div>
        <label for="password2">
          Confirm Password
        </label>
        <input v-model="password2" type="password" id="password2" name="password2" placeholder="confirm password">
      </div>
      <div>
        <label for="email">
          Email
        </label>
        <input v-model="email" type="email" id="email" name="email" placeholder="email">
      </div>
      <div>
        <label for="first_name">
          First Name
        </label>
        <input v-model="first_name" type="text" id="first_name" name="first_name" placeholder="first name">
      </div>
      <div>
        <label for="last_name">
          Last Name
        </label>
        <input v-model="last_name" type="text" id="last_name" name="last_name" placeholder="last name">
      </div>
      <div>
        <label for="city">
          City
        </label>
        <input v-model="city" type="text" id="city" name="city" placeholder="city">
      </div>
      <div>
        <label for="address">
          Address
        </label>
        <input v-model="address" type="text" id="address" name="address" placeholder="address">
      </div>
      <div>
        <label for="role">
          Role
        </label>
        <v-select v-model="role" :options="[{label: 'Regular User', code: '0'},{label: 'Good Pepole', code: '1'}]"/>
      </div>
      <div>
        <label for="district">
          District
        </label>
        <v-select v-model="district"
                  :options="[{label: 'North', code: 'North'},{label: 'South', code: 'South'},{label: 'Center', code: 'Center'}]"/>
      </div>
      <p class="error" v-if="incorrectAuth">One or more of the fields is missing or incorrect</p>
      <div>
        <button class="submit-login" type="submit">Register</button>
      </div>
    </form>
    <div class="to-sign-up">
      <p>Already have an account? </p><a href=""> login</a>
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
    }
  }
}
</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');

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
  //height: 100%;
}

h1 {
  color: rgba(252, 176, 69, 1);
  font-size: 40px;
}

input {
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