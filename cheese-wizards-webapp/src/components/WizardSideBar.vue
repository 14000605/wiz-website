<template>
  <div id = "wizard-sidebar">
    <div id = "cheese-top"></div>
    <div id = "wizard-content">
      <div class = "h5" id = "sidebar-title">Wizards</div>
      <hr/>
      <div id = "wizard-blocks">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "wizard-sidebar",
  data: function(){
    return{

    };
  },
  methods: {
   
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: exocet;
  src: url(/staticfiles/font/exocet.ttf);
}

@font-face {
  font-family: code saver;
  src: url(/staticfiles/font/codesaver-regular-webfont.woff);
}

#wizard-sidebar {
  height: 100vh;
  width: 175px;
  background-color: #1a1818;
  z-index: 100;
  border-right: 1px solid rgba(250, 250, 250, 0.5);
}

#cheese-top {
  width: 100%;
  height: 50px;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url(/staticfiles/img/cheese_top.png);
}

#wizard-content {
  margin-left: 0.5em;
  margin-right: 0.5em;
}

#sidebar-title {
   font-family: exocet;
   text-align: center;
   color: white;
}

hr {
   border-top: 1px solid #e3e2e1;
   opacity: 0.7;
}

#wizard-blocks {
  height: 100px;
  margin: 0.3em;
  background-color: #262625;
  border: 1px solid rgba(250, 250, 250, 0.2);
}


</style>
