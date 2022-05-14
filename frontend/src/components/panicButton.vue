<template>
  <div class="panic-wrapper">
  <h1>{{ name }} שלום</h1>
    <div v-if="!isPanic" class="panic-container">
      <div class="punic-button" @click="togglePanic">
    <span class="sos-text">
      SOS
    </span>
        <span class="sos-subtext">
      לחץ להפעלה
    </span>
      </div>

      <div class="panic-button-text">
        לחיצה על לחצן המצוקה תתריע בפני המוקד החירום וזו תשלח אליך סיוע בהקדם
      </div>


    </div>

    <div v-else>

      <p>הקריאה נשלחה למוקד. מיד יגיעו אליך אנשים טובים וכוחות הצלה</p>

    </div>

  </div>

</template>


<script>


import axios from "axios";

export default {
  name: 'panicButton',
  data() {
    return {
      isPanic: "",
      name: ""
    }
  },
  created() {
    let ispanic = {'false': false , 'true': true}
    this.isPanic = ispanic[localStorage.getItem("isPanic")]
    this.name = localStorage.getItem("name")
  },
  methods: {
    togglePanic() {
      console.log(this)
      axios.post('http://127.0.0.1:8000/api/togglePanic/', {"id": localStorage.getItem("user-id") }).then(
          resp => {
            console.log(resp)
            this.isPanic = true;
            localStorage.setItem('isPanic', 'true')
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    }
  },
    mounted: function () {
    let connection = new WebSocket('ws://localhost:8000/ws/sos/');
    connection.onmessage = (event) => {
      // Vue data binding means you don't need any extra work to
      // update your UI. Just set the `time` and Vue will automatically
      // update the `<h2>`.
      console.log(event)
      localStorage.setItem('isPanic', 'false')
      this.isPanic = false

    }
    connection.onopen = (event) => {
      // Vue data binding means you don't need any extra work to
      // update your UI. Just set the `time` and Vue will automatically
      // update the `<h2>`.
      console.log(event)
    }
  },
}
</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&family=Varela+Round&display=swap');


.panic-wrapper{

  h1{
    color: #F55353;
        font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
  }

  p{
            font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
  }
}
.panic-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 60px;
          font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;

  .punic-button {
    color: white;
    display: flex;
    flex-direction: column;
    border-radius: 100px;
    height: 200px;
    width: 200px;
    background: #F55353;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 25px 80px 5px rgba(0, 0, 0, 0.50);
    cursor: pointer;

    .sos-text {
      font-size: 48px;
      color: inherit;
    }

    .sos-subtext {
      color: inherit;
    }

    &:hover {
      color: black;
      box-shadow: 0px 25px 80px 5px rgba(0, 0, 0, 1);

    }

  }

  .panic-button-text {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 30%;
    text-align: center;
  }
}

</style>