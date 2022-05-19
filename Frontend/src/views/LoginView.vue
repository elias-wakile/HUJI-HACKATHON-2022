<template>
  <div class="login-view">
    <form @submit.prevent="submitForm" class="login-form">
      <!-- <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="125"
        height="125"
      /> -->
      <br />
      <br />
      <span class="p-float-label">
        <InputText
          id="username"
          type="text"
          v-model="username"
          class="p-inputtext-lg"
          placeholder="Email"
        />
      </span>

      <br />
      <span class="p-float-label">
        <Password
          v-model="pwd"
          class="p-inputtext-lg"
          placeholder="Password"
          toggleMask
          :feedback="false"
        />
      </span>
      <br />
      <button type="submit" class="btn-login">Login</button>
      <h3 style="color: #fff">
        {{ this.error_login }}
      </h3>
      <br />
    </form>
    <br />
    <button class="btn-login" @click="$router.push('/register')">
      Register
    </button>

    <!-- <button @click="log">log</button> -->
  </div>
</template>

<script>
import { performLogin } from "../util";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Image from "primevue/image";
import TabMenu from "primevue/tabmenu";
import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import InputNumber from "primevue/inputnumber";
import { useUserStore } from "@/stores/userStore";

export default {
  name: "LoginView",
  components: {
    InputText,
    Password,
    Image,
    TabMenu,
    Button,
    Dropdown,
    InputNumber,
  },
  data() {
    return {
      username: null,
      pwd: null,
      weight: null,
      height: null,
      bodyType: null,
      loading: false,
      submit_login: true,
      submit_register: false,
      error_login: "",
      bodyTypeOptions: [
        { name: "Shreded" },
        { name: "Fit" },
        { name: "Average" },
        { name: "Above Average" },
        { name: "Overweight" },
      ],
      userStore: useUserStore(),
    };
  },
  computed: {
    enableSubmitButton() {
      if (this.username && this.pwd && !this.loading) return true;
      else return false;
    },
  },
  methods: {
    async submitForm() {
      this.loading = true;
      this.error_login = "";
      if (this.submit_login) await this.login();
      if (this.submit_register) await this.register();
      this.loading = false;
    },
    async login() {
      performLogin({ email: this.username, password: this.pwd })
        .then((res) => {
          this.userStore.setUser(
            res.data.username,
            res.data.weight,
            res.data.height,
            res.data.bodyShape
          );
          this.$router.push("/");
        })
        .catch((err) => {
          this.error_login = "Invalid credentials or user not found.";
          this.loading = false;
        });
    },
    async register() {
      return "registered";
    },
    toggleNav(option) {
      if (option === "login") {
        this.submit_login = true;
        this.submit_register = false;
      }

      if (option === "register") {
        this.submit_login = false;
        this.submit_register = true;
      }
    },
    log() {
      console.log(
        `username: ${this.username} pwd: ${this.pwd} loading: ${this.loading} enabled: ${this.enableSubmitButton}`
      );
    },
  },
};
</script>

<style scoped>
.login-view {
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  text-align: center;
}

.login-or-register-nav {
  margin-bottom: 5vh;
  width: 100%;
}

.login-or-register-item {
  width: 50%;
  text-align: center;
  cursor: pointer;
}

.login-or-register-item:hover,
.login-or-register-item-active {
  background-color: #d0d3d8;
}

.register-item {
  float: right;
}
.login-item {
  float: left;
}

.btn-login {
  margin-top: 15px;
  width: 280px;
  color: #fff;
  background-color: #171717;
  border: 1px solid #fff;
  border-radius: 10px;
  font-size: 28px;
  cursor: pointer;
  font-family: "Quicksand", "Grape", "David";
  padding: 5px;
}

.login-form {
  margin-top: 10%;
  border: 1px solid #fff;
  width: 500px;
  margin-left: 30%;
  padding: 10px;
}
</style>
