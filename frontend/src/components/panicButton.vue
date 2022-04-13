<template>
  <div class="panic-container">
  <div class ="punic-button">
    <span class ="sos-text">
      SOS
    </span>
    <span class="sos-subtext">
      Tap to Activate
    </span>
  </div>

  <div class="panic-button-text">
     Tapping SOS will alert your emergency contacts and update them with your current location, if available.
  </div>
  </div>

</template>



<script>

</script>


<style scoped lang="scss">
    .panic-container{
      display:flex;
      flex-direction:column;
      justify-content: center;
      align-items:center;
      gap:60px;
      .punic-button{
       color:white;
      display:flex;
      flex-direction:column;
      border-radius:100px;
      height:200px;
      width:200px;
      background:#F55353;
      justify-content: center;
      align-items:center;
        box-shadow:0px 25px 80px 5px          rgba(0,0,0,0.50);
       cursor:pointer;

       .sos-text{
      font-size:48px;
      color: inherit;
      }

      .sos-subtext{
      color: inherit;
      }
        &:hover{
          color:black;
           box-shadow:0px 25px 80px 5px            rgba(0,0,0,1);

        }

    }

    .panic-button-text{
      display:flex;
      justify-content: center;
      align-items:center;
       width:30%;
      text-align:center;
    }
    }

</style>