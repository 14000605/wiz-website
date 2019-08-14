<template>
  <div class="hello">
    <div class="h1">{{ msg }}</div>
    <login></login>
    <div class="wiz-login-background">
      <img class="wiz-login-background" src="/staticfiles/img/Cheese.png" />
    </div>
  </div>
</template>

<script>
import Login from "./Login.vue"
export default {
  name : "main",
  components: {
    Login
  },
  data() {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: "Login"
    };
  }
};

console.log($('.h1'));

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang = "scss" scoped>
.wiz-login-background {
  position: fixed;
  bottom: 0px;
  right: 0px;
  left: 0px;
  width: 100vw;
  height: 35vh;
}
img {
  object-fit: contain;
}
</style>
