<template>
  <div id="app">
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
  src: url(assets/font/codesaver-regular-webfont.woff);
}

#app {
  font-family: code saver, sans-serif;
  width: 100%;
  height: 100%;
  background-image: url("./assets/dark_cheese.png");
  background-repeat: no-repeat;
  background-size: 70rem auto;
  background-position: bottom;
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
  background-image: url("./assets/dark_melt.png");
  background-repeat: repeat-x;
  background-size: 70rem auto;
  background-position: top;
}
</style>
