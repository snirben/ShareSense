<template>
  <div class="page-warrper">
  <div>
    <h1>מוקד</h1> 
    </div>
    <div class="boxs-warrper">
      <div v-for="(user, index) in users" class="Personal-tab-container" :key="index">
        <div class="customer-photo">
      <span class="photo">
        <img src="https://365webresources.com/wp-content/uploads/2016/09/FREE-PROFILE-AVATARS.png">
      </span>
        </div>

        <div class="customer-details">
     <span class="user-name">
          {{ user.first_name }} {{ user.last_name }}
        </span>
          <span class="user-address">
          {{ user.city || "Unknown" }}
       </span>
        </div>

        <div class="icons">
        <span class="fire" @click="toggleFire(user)">
         <font-awesome-icon class="fire" icon="fa-solid fa-fire"/>
         </span>
          <span @click="togglePanic(user)">
          <font-awesome-icon class="bell" :class="{'bellAlert': user.isPanic ,'alertButton': !user.isPanic}" icon="fa-solid fa-bell"/>
         </span>
          <span @click="sendEmail(user)" class="email">
          <font-awesome-icon class="envelope" icon="fa-solid fa-envelope"/>
         </span>
        </div>

      </div>
    </div>
  </div>

</template>


<script>
import axios from 'axios';

import {library} from '@fortawesome/fontawesome-svg-core'
/* import specific icons */
import {faFire} from '@fortawesome/free-solid-svg-icons'
import {faBell} from '@fortawesome/free-solid-svg-icons'
import {faEnvelope} from '@fortawesome/free-solid-svg-icons'
/* import font awesome icon component */

import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

library.add(faFire, faBell, faEnvelope)

export default {
  name: 'alertPage',
  data() {
    return {
      users: {},
    }
  },
  components: {
    FontAwesomeIcon,

  },
  methods: {
    getCams() {
      axios.get('http://127.0.0.1:5000/cams_check', {}).then(
          resp => {
            console.log(resp)
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    },
    sendEmail(user) {
      if (!user.isPanic && !user.isFire)
        return

      axios.post('http://127.0.0.1:8000/api/email/', {"id": user.id}).then(
          resp => {
            alert("The email was sent successfully");
            console.log(resp)
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    },
    togglePanic(user) {
      if (!user.isPanic)
        return

      axios.post('http://127.0.0.1:8000/api/togglePanic/', {"id": user.id}).then(
          resp => {
            this.getUsers()
            console.log(resp)
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    },
    toggleFire(user) {
      if (!user.isFire)
        return

      axios.post('http://127.0.0.1:8000/api/toggleFire/', {"id": user.id}).then(
          resp => {
            this.getUsers()
            console.log(resp)
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    },
    getUsers() {
      axios.get('http://127.0.0.1:8000/api/users/', {}).then(
          resp => {
            this.users = resp.data
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    },
  },
  mounted: function () {
    let connection = new WebSocket('ws://localhost:8000/ws/socket-server/');
    connection.onmessage = (event) => {
      // Vue data binding means you don't need any extra work to
      // update your UI. Just set the `time` and Vue will automatically
      // update the `<h2>`.
      console.log(event)
      this.getUsers()

    }
    connection.onopen = (event) => {
      // Vue data binding means you don't need any extra work to
      // update your UI. Just set the `time` and Vue will automatically
      // update the `<h2>`.
      console.log(event)
    }
  },
  created() {
    this.getUsers()
    //this.interval = setInterval(() => this.getCams(), 10000);


  },

}

</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&family=Varela+Round&display=swap');
.page-warrper {
  display: flex;
  flex-direction: column;

  p {
    margin: 0;
    padding-bottom: 10px;
    color: darkred;
    font-size: 50px;
  }

  h1 {
    font-size: 50px;
    font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
  }
}

.boxs-warrper {
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: center;
  align-items: center;
}


.Personal-tab-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  // align-items:center;
  border: 2px solid rgba(0, 0, 0, 0.1);
  width: 150px;

  .vertical {
    border-left: 2px dotted rgba(0, 0, 0, 0.1);
    height: 108px;
  }

  .customer-details {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    // margin-top:5px;
    // margin-left:15px;
    .user-name {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: 'Anybody', cursive;
      font-family: 'Archivo', sans-serif;
      font-family: 'Poppins', sans-serif;
      font-family: 'Varela Round', sans-serif;
      font-size: 20px;
      font-weight: bold;
    }

    .user-address {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: 'Anybody', cursive;
      font-family: 'Archivo', sans-serif;
      font-family: 'Poppins', sans-serif;
      font-family: 'Varela Round', sans-serif;
      font-size: 14px;
      color: gray;
      margin-bottom: 12px;
    }

  }

  .customer-photo {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .photo {
      display: flex;
      flex-direction: column;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      overflow: hidden;
      margin-top: 12px;
      margin-bottom: 12px;
      box-shadow: inset 0 -3em 3em rgba(0, 0, 0, 0.1),
      0 0 0 2.5px rgb(255, 255, 255),
      0.3em 0.3em 1em rgba(0, 0, 0, 0.2);

    }
  }

  .icons {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-bottom: 12px;

    .fire {
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: center;

    }

    .alertButton {
      cursor: pointer;
      display: flex;
      flex-direction: column;
      margin-left: 12px;
    }
      .bellAlert {
        cursor: pointer;
        color: red;
        display: flex;
        flex-direction: column;
        margin-left: 12px;
      }

    .email {
      display: flex;
      flex-direction: column;
      margin-left: 12px;
      cursor: pointer;

    }
  }
}
</style>