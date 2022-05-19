import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import ManageClosetView from "../views/ManageClosetView.vue";
import LoginRegisterPanel from "../views/LoginRegisterPanel.vue";
import RegisterView from "../views/RegisterView.vue";
import OutfitFound from "../views/OutfitFound.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/outfit-found",
      name: "OutfitFound",
      component: OutfitFound,
    },
    {
      path: "/intro",
      name: "intro",
      component: LoginRegisterPanel,
    },
    {
      path: "/manage-closet",
      name: "ManageCloset",
      component: ManageClosetView,
    },
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
  ],
});

export default router;
