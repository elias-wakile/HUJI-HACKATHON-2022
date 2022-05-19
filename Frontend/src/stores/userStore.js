import { defineStore } from "pinia";
import User from "./User";

export const useUserStore = defineStore({
  id: "userStore",
  state: () => ({
    loggedIn:
      localStorage["loggedIn"] || localStorage["loggedIn"] === "true"
        ? true
        : false,
    user: null,
    clothes: [],
  }),
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
  actions: {
    increment() {
      this.counter++;
    },
    setUser(username = "", weight = null, height = null, bodyShape = null) {
      this.loggedIn = true;
      localStorage.setItem("loggedIn", true);
      this.user = new User(username, weight, height, bodyShape);
    },
    async setClothes(res) {
      this.clothes = [];
      res.pictures.forEach((image) => {
        fetch(`http://localhost:8080/?image_name=${image}`, {
          headers: {
            "Content-Type": "image/jpeg",
          },
          mode: "no-cors",
        })
          .then((res) => {
            this.clothes.push(URL.createObjectURL(res));
          })
          .catch((err) => {
            return;
          });
      });
    },
  },
});
