<template>
  <div id = "wizard-sidebar">
    <div id = "cheese-top"></div>
    <div id = "wizard-content">
      <div class = "h5" id = "sidebar-title">Wizards</div>
      <hr/>
      <div class = "wizard-blocks pointer-cursor">
        <div v-for = "img in wizardImages" :key = "img" style = "margin-bottom: 1em;">
          <img class = "wizard-img" :src = "img" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var wizardNames = [
  "wizard_angry",
   "wizard_angry_smile",
   "wizard_sad",
   "wizard_happy"
]

export default {
  name: "wizard-sidebar",
  props: {
    userAddress: String
  },
  data: function(){
    return{
      wizards: [],
      wizardImages: []
    };
  },
  methods: {
   resolveAffinity: function(affinity) {
     switch (affinity) {
       case 0:
         return "default";
         break;
       case 1:
         return "neutral";
         break;
       case 2:
         return "fire";
         break;
       case 3:
         return "wind";
         break;
       case 4:
         return "water";
         break;
       default:
         return "default";
         break;
     }
   },
   getWizardImages: function() {
     var baseImgUrl = "/staticfiles/img/wizards/";
     var names = wizardNames;

     for (var i = 0; i < this.wizards.length; i++) {
       var filepath = "";
       var filename = "";
       var alive = this.wizards.isAlive;
       if (alive != undefined && alive == false) {
         filename = "wizard_dead.png";
         filepath = baseImgUrl + "default/" + filename
       } else if (alive == true || alive == undefined) {
         var randomIndex = Math.floor(Math.random() * (names.length - 1));
         var affinity = this.resolveAffinity(this.wizards[i].affinity);

         filename = names[randomIndex] + ".png";
         filepath = baseImgUrl + affinity + "/" + filename;
       }

       this.wizardImages.push(filepath);
     }
   },
   encodeJsonToParams: function(params) {
      var urlQuery = "";
      for (var param in params) {
        if (urlQuery != "") {
          urlQuery += "&";
        }
        urlQuery += param + "=" + params[param];
      }
      return urlQuery;
    },
    // Geeneral purpose function to fetch wizard data based on given params
    fetchAndRenderWizards: function(params) {
      var queryParams = this.encodeJsonToParams(params);
      var requestUrl = "/wizards?" + queryParams;

      $.ajax({
        url: requestUrl,
        method: "get",
        success: (data) => {
          // TODO: do something with wizards data
          var wizards = data.wizards;
          for (var i = 0; i < wizards.length; i++) {
            this.wizards.push(wizards[i]);
          }
        },
        error: function(err) {
          console.log(err);
        }
      }).done(()=>{
        this.getWizardImages();
      });
    }
  },
  created: function() {
    this.fetchAndRenderWizards({'owner' : this.userAddress});

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
  overflow-y: scroll;
  width: 175px;
  background-color: #2d2d2d;
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

.wizard-img {
  width : 70%;
}
.wizard-blocks {
  height: 100px;
  width: 100px;
  margin: 0 auto;
  transition: transform .6s;
} 

.wizard-blocks :hover {
  transform: scale(1.1);
}

.pointer-cursor {
  cursor: pointer;
}


</style>
