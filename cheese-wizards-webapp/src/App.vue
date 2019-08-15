<template>
  <div class="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style>
@font-face {
  font-family: code saver;
  src: url(/staticfiles/font/codesaver-regular-webfont.woff);
}

.app {
  font-family: code saver, sans-serif;
  width: 100%;
  height: 100%;
}

html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: black;
  height: 100%;
  background-image: url(/staticfiles/img/dark_melt.png);
  background-repeat: repeat-x;
  background-size: 70rem auto;
  background-position: top;
}
</style>
