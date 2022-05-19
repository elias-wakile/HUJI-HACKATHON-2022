<template>
  <div class="navbar">
    <img src="@/assets/logo.svg" alt="" width="40" height="40" />
    <nav>
      <RouterLink class="nav-item" to="/">Find My Outfit</RouterLink>
      <RouterLink class="nav-item" to="/manage-closet"
        >Manage Closet</RouterLink
      >
    </nav>
  </div>
</template>

<script>
export default {
  name: "navbar",
};
</script>

<style scoped>
.navbar {
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  text-align: center;
  padding-left: auto;
  padding-right: auto;
  height: 100px;
  width: 100%;
}

.nav-item {
  margin: 3vh;
  color: white;
  text-decoration: none;
}
</style>
