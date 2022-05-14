<template>
 <div class="text-container">
  <div class ="text-box">
   <h2>{{name}} שלום</h2>
התראות ודיווחים ישלחו אליך למייל באופן אוטומטי 
  </div>
  </div>
</template>



<script>
export default {
  name: 'goodMans',
  data() {
    return {
      name: ""
    }
  },
    created() {
    this.name = this.$route.params.name
  },
}

</script>


<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&family=Varela+Round&display=swap');
.text-container{
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  height:625px;
  border-radius:100px;
  background-image: url("https://images.pexels.com/photos/2030190/pexels-photo-2030190.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260");
  background-position: center;
  background-repeat: no-repeat;
  background-size: 730px 480px;

  filter: grayscale(75%);
  .text-box{
        font-family: 'Nunito', sans-serif;
font-family: 'Varela Round', sans-serif;
    font-weight: bold;
    font-size: 24px;
    color: black;
  display:flex;
  flex-direction:column;
  height:500px;
  width:750px;
  background:#F7F7F7;
  opacity: 0.6;
  justify-content: center;
  align-items:center;
   cursor:pointer;
.text{
  font-family: 'Poppins', sans-serif;
  width:650px;
  display:flex;
  font-size:35px;
  justify-content: center;
  align-items:center;
  text-align:center;
}

}

}
</style>