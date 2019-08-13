<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
@font-face {
  font-family: code saver;
  src: url(assets/font/codesaver-regular-webfont.woff);
}

#app { 
  font-family: code saver, sans-serif;
}

</style>
