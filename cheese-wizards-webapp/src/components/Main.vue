<template>
  <div class="page1">
    <div class="container">
      <div class="wiz-main-title">{{ title }}</div>
    </div>
    <login></login>
  </div>
</template>

<script>
import Login from "./Login.vue";
export default {
  name: "main",
  components: {
    Login
  },
  data() {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      title: "Strategy Simulator"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: exocet;
  src: url(/staticfiles/font/exocet.ttf);
}

.page1 {
  margin-top: 100px;
}
.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
.wiz-main-title {
  color: white;
  font-size: 50px;
  text-transform: uppercase;
  letter-spacing: -0.25rem;
  line-height: 1.1;
  text-align: center;
  font-family: exocet;
}
</style>
