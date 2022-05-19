<template>
  <div class="outfit-found">
    <Nav />
    <div class="items-found">
      <img
        v-for="(image, i) in userStore.clothes"
        :key="`image ${i}`"
        class="img-of-found-item"
        :src="image"
        alt=""
      />

      <img
        class="img-of-found-item"
        src=
        alt=""
      />

      <img
        class="img-of-found-item"
        src=
        alt=""
      />
    </div>

    <div class="action-buttons">
      <button class="btn-login">Dislike</button>
      <button class="btn-login">Another Outfit</button>
      <button class="btn-login">Like</button>
    </div>
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";
import { useUserStore } from "@/stores/userStore";

export default {
  name: "OutfitFound",
  components: { Nav },
  data() {
    return {
      userStore: useUserStore(),
    };
  },
};
</script>

<style scoped>
.outfit-found {
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  text-align: center;
}

.btn-login {
  margin-top: 15px;
  width: 200px;
  color: #fff;
  background-color: #171717;
  border: 1px solid #fff;
  border-radius: 10px;
  font-size: 28px;
  cursor: pointer;
  font-family: "Quicksand", "Grape", "David";
  padding: 5px;
  margin: 4vh;
}

.login-form {
  margin-top: 10%;
  border: 1px solid #fff;
  width: 500px;
  margin-left: 30%;
  padding: 10px;
}

.img-of-found-item {
  max-width: 300px;
  margin: 1vh;
}
</style>
