<template>
  <div class="Personal-tab-container">
    <div class="customer-photo">
      <span class="photo">
        <img src="https://365webresources.com/wp-content/uploads/2016/09/FREE-PROFILE-AVATARS.png">
      </span>
    </div>

    <div class="customer-details">
     <span class="user-name">
          Tzlil Levi
        </span>
      <span class="user-address">
          kiryat-Gat
       </span>
    </div>

    <div class="icons">
        <span class="fire">
         <i class="fa-reular fa-fire">fire-icon</i>
         </span>
        <span class="alert-button">
          <i class="fa-regular fa-siren-on">alert-icon</i>
         </span>
    </div>

  </div>

</template>



<script>


</script>


<style scoped lang="scss">
.Personal-tab-container{
  display:flex;
  flex-direction:column;
  justify-content: flex-start;
 // align-items:center;
 border: 2px solid rgba(0, 0, 0, 0.1);
  width: 150px;

  .vertical{
     border-left: 2px dotted rgba(0, 0, 0, 0.1);
     height: 108px;
  }
  .customer-details{
    display: flex;
    flex-direction:column;
    justify-content: center;
    align-items:center;
    // margin-top:5px;
    // margin-left:15px;
    .user-name{
    display: flex;
    flex-direction:column;
    justify-content: center;
     align-items:center;
    font-family: 'Anybody', cursive;
    font-family: 'Archivo', sans-serif;
    font-family: 'Poppins', sans-serif;
    font-family: 'Varela Round', sans-serif;
      font-size:20px;
      font-weight: bold;
    }
    .user-address{
     display: flex;
    flex-direction:column;
    justify-content: center;
      align-items:center;
     font-family: 'Anybody', cursive;
      font-family: 'Archivo', sans-serif;
      font-family: 'Poppins', sans-serif;
      font-family: 'Varela Round', sans-serif;
      font-size:10px;
      color:gray;
      margin-bottom:12px;
    }

  }
  .customer-photo{
   display: flex;
   flex-direction:column;
   justify-content: center;
    align-items:center;
    .photo{
      display:flex;
      flex-direction:column;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      overflow: hidden;
      margin-top:12px;
      margin-bottom:12px;
      box-shadow:
       inset 0 -3em 3em rgba(0,0,0,0.1),
             0 0  0 2.5px rgb(255,255,255),
             0.3em 0.3em 1em rgba(0,0,0,0.2);

    }
  }
  .icons{
    display: flex;
   flex-direction:row;
   justify-content: center;
   margin-bottom:12px;
    .fire{
     display: flex;
     flex-direction:column;
     justify-content: center;

    }
    .alert-button{
      display: flex;
      flex-direction:column;
      margin-left:12px;

    }
  }
}
</style>