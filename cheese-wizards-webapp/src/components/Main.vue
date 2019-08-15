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
      title: "Strategy Simulator"
    };
  },
  created: function() {
    // Remove previous address (if exists) from local storage
    localStorage.removeItem('address');
  }
};
</script>

<style scoped>
@font-face {
  font-family: exocet;
  src: url(/staticfiles/font/exocet.ttf);
}

.page1 {
  margin-top: 100px;
  width: 100%;
  height: 100%;
  background-image: url(/staticfiles/img/dark_cheese.png);
  background-repeat: no-repeat;
  background-size: 70rem auto;
  background-position: bottom;
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
