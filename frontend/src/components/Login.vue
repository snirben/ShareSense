<template>
    <div class="container">
        <h1>Sign In</h1>
        <form action="" method="post">
            <div>
                <label for="email">
                    Email
                </label>
                <input type="email" id="email" name="email" placeholder="email">
            </div>
            <div>
                <label for="password">
                    Password
                </label>
                <input type="password" id="password" name="password" placeholder="password">
            </div>
            <div>
                <input class="submit-login" type="submit" value="login">
            </div>
        </form>
        <div class="to-sign-up">
            <p>Don't have an account? </p><a href=""> create</a>
        </div>
    </div>

</template>



<script>

</script>


<style scoped lang="scss">
html, body{
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

h1{
    color: rgba(252,176,69,1);
}

input[type=password], input[type=email]{
    width: 100%;
    padding: 12px ;
    margin: 8px 0;
    box-sizing: border-box;
    font-family: 'Nunito', sans-serif;
    border-radius: 5px;
    border: 1px solid gray;
}

.submit-login{
    transition: all .5s ease;
    font-family: 'Nunito', sans-serif;
    background-color: transparent;
    color: black;
    border-radius: 5px;
    font-size: 17px;
    border: 3px solid rgba(252,176,69,1);
    padding: 8px;
    margin-top: 14px;
    width: 100%;

}

.submit-login:hover {
    background: rgba(252,176,69,1);
}

.to-sign-up {
    display: flex;
    flex-direction: row;
    gap: 5px;
    align-items: center;
    font-size: 14px;
}

a{
    color: #3c3cdb;
    text-decoration: none;
}

a:hover{
    color: blue;
  }
</style>