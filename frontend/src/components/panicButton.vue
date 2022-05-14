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
    this.isPanic = this.$route.params.isPanic
    this.name = this.$route.params.name
  },
  methods: {
    togglePanic() {
      console.log(this)
      axios.post('http://127.0.0.1:8000/api/togglePanic/', {"id": this.$route.params.id}).then(
          resp => {
            console.log(resp)
            this.isPanic = true;
          }
      ).catch(
          err => {
            console.log(err)
          }
      )
    }
  }
}
</script>


<style scoped lang="scss">
.panic-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 60px;

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