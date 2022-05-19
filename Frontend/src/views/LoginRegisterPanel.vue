<template>
  <div class="login-register-panel">
    <center>
      <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="280"
        height="280"
      />
      <br />
      <button class="btn-register-login" @click="$router.push('/login')">
        Login
      </button>
      <br />
      <button class="btn-register-login" @click="$router.push('/register')">
        Register
      </button>
    </center>
  </div>
</template>

<script>
import Button from "primevue/button";

export default {
  name: "LoginRegisterPanel",
  data() {
    return {};
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Grape+Nuts&display=swap");
.login-register-panel {
  justify-content: center;
  align-items: center;
}

.logo {
  margin-top: 40px;
}

.btn-register-login {
  margin-top: 15px;
  width: 280px;
  color: #fff;
  background-color: #171717;
  border: 1px solid #fff;
  border-radius: 10px;
  font-size: 28px;
  cursor: pointer;
  font-family: "Grape", "David";
  padding: 5px;
}
</style>
