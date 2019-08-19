<template>
  <div id = "sidebar-wrapper">
    <div id = "cheese-arrow-control" @click="onCheeseArrowClicked">
      <img id = "cheese-arrow" class = "cheese-arrow-right" src = "/staticfiles/img/cheese_slice.png" />
    </div>
   <div id = "wizard-sidebar">
      <div id = "cheese-top"></div>
      <div id = "sidebar-content">
        <div class = "h5" id = "sidebar-title">Wizards</div>
        <!--This is the fancy cheese top bar-->
        <div id = "solid-cheese-top"></div>
        <div id = "wizard-content">
          <div v-if = "isLoading" id = "spinner" class = "text-center">
            <!-- <b-spinner variant="secondary" label="Spinning"></b-spinner> -->
            <div><img class = "cheese-spinner" src = "/staticfiles/img/cheese_spinner_icon.png" width = "60px" height = "60px"/></div>
            <small>fetching wizards...</small>
          </div>
          <div id = "empty-state" v-if = "wizardImages.length <= 0 && !isLoading" class = "text-center">
            <small>No Wizards Owned</small>
          </div>
          <div class = "wizard-icon-wrapper" v-for = "img in wizardImages" :key = "img">
            <div class = "wizard-blocks pointer-cursor" @click="onWizardIconClicked(img)">
              <div style = "margin-bottom: 1em;">
                <img class = "wizard-img" :src = "img.src" />
              </div>
            </div>
          </div>
        </div>
        <!--This is the fancy cheese bottom bar-->
        <div id = "solid-cheese-bottom"></div>
      </div>
      <!-- Info modal to show when a wizard icon is clicked -->
      <div id = "info-modal">
        <b-modal
          v-model="showModal"
          body-bg-variant = "light"
          body-text-variant = "dark"
          :header-class = "modalHeaderClass"
          :body-class = "modalBodyClass"
          hide-footer = "true"
          size = "sm"
          centered
        >
          <template slot = "modal-header">
            <!--Header texture-->
            <div id = "modal-cheese-melt"></div>
          </template>
          <template slot = "default">
            <!--Modal body content-->
            <b-container style = "font-family: code saver;">
              <b-row>
                <b-col><img :src = "modalInfo.src" width = "50px" height = "50px"/></b-col>
                <b-col class = "pt-2"><small>{{ getAffinityText(modalInfo.affinity) }}</small></b-col>
              </b-row>
              <hr />
              <b-row>
                <b-col><h6>Current Power</h6></b-col>
                <b-col><small class = "text-success">{{ modalInfo.power }}</small>
              </b-row>
              <hr />
              <b-row>
                <b-col><h6>Initial Power</h6></b-col>
                <b-col><small class = "text-success">{{ modalInfo.initialPower }}</small>
              </b-row>
            </b-container>
          </template>
        </b-modal>
      </div>
    </div>
  </div>
</template>

<script>
import Velocity from 'velocity-animate'
var slideDirection = 1;
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
      wizardImages: [],
      isLoading: true,
      showModal: false,
      modalInfo: {
        src: null,
        affinity: null,
        power: null,
        initialPower: null
      },
      modalHeaderClass: ['p-0', 'border-2'],
      modalBodyClass: ['border-2'],
      isActive: false
    };
  },
  methods: {
    onCheeseArrowClicked: function(){
      var direction = $('#sidebar-wrapper').width() - 35;
      var degrees = 180;

      if (slideDirection < 0) {
        direction = 0;
        degrees = 0;
      }

      Velocity($('#sidebar-wrapper'), {'translateX' : direction + "px"});
      slideDirection = slideDirection * -1;

      Velocity($('#cheese-arrow'), {
        'rotateZ': degrees+ "deg" 
      });

      // Load wizard data if not already loaded
      if (!this.isActive) {
          this.isActive = true;
          this.fetchAndRenderWizards({'owner' : this.userAddress});
      }

    },
    resolveAffinity: function(affinity) {
     switch (affinity) {
       case 1:
         return "neutral";
       case 2:
         return "fire";
       case 3:
         return "wind";
       case 4:
         return "water";
       default:
         return "default";
     }
   },
   getAffinityText: function(affinity) {
     switch (affinity) {
       case 1:
         return "Neutral Wizard";
       case 2:
         return "Fire Wizard";
       case 3:
         return "Wind Wizard";
       case 4:
         return "Water Wizard";
       default:
         return "No Affinity";
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

       this.wizardImages.push({src: filepath, id: i});
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
        this.isLoading = false;
      });
    },
    onWizardIconClicked: function(img) {
      var obj = this.wizards[img.id];
      obj.src = img.src;

      this.modalInfo = obj;
      console.log(this.modalInfo);
      this.showModal = true;
    }
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

#sidebar-wrapper {
  height: 100vh;
  width: 200px;
  position: absolute;
  left: -165px;
}

#wizard-sidebar {
  height: 100vh;
  overflow-y: scroll;
  width: 175px;
  background-color: #2d2d2d;
  z-index: 100;
  border-right: 1px solid rgba(250, 250, 250, 0.5);
  position: absolute;
  top: 0;
}

#cheese-top {
  width: 100%;
  height: 50px;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url(/staticfiles/img/orange_melt.png);
}

#sidebar-content {
  margin-left: 0.5em;
  margin-right: 0.5em;
}

#sidebar-title {
   font-family: exocet;
   text-align: center;
   color: white;
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

#wizard-content {
  overflow-y: scroll;
  height: 50vh;
  border-top: 1px solid #9c9c9c;
  border-bottom: 1px solid #9c9c9c;
  background-color: rgba(0, 0, 0, 0.2);
  text-align: center;
  padding-top: 1em;
}

#spinner {
  margin-top: 50%;
  color: #b3adad;
  font-size: 0.5em;
}

#empty-state {
  margin-top: 80%;
  color: #959798;
}

#solid-cheese-top {
  margin-top: 1em;
  height: 24px;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url(/staticfiles/img/cheese_custom_top.png);
}

#solid-cheese-bottom {
  height: 17px;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url(/staticfiles/img/cheese_custom_bottom.png);
}

#modal-cheese-melt{
  background-image: url(/staticfiles/img/melt_bg_grey.png);
  background-size: cover;
  background-repeat: no-repeat;
  width: 100%;
  height: 50px;
}

.cheese-spinner {
  -webkit-animation:twinkle 1s linear infinite;
  -moz-animation:twinkle 1s linear infinite;
   animation:twinkle 1s linear infinite;
}

.wizard-blocks :hover {
  transform: scale(1.1);
}

.pointer-cursor {
  cursor: pointer;
}

#cheese-arrow-control {
  position: relative;
  z-index: 101;
  top: 40vh;
  transform: scale(0.3);
  left: 44%;
  cursor: pointer;
}

#cheese-arrow-control :hover {
  transform: scale(1.1);
}

@-moz-keyframes twinkle { 100% { -moz-transform: scale(0.5);} }
@-webkit-keyframes twinkle { 100% { -webkit-transform: scale(0.5); } } 
@keyframes twinkle { 100% { -webkit-transform: scale(0.5);} }


</style>
