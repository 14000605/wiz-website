<template>
  <div id = "wizard-sidebar">
    <div id = "cheese-top"></div>
    <div id = "sidebar-content">
      <div class = "h5" id = "sidebar-title">Wizards</div>
      <div id = "solid-cheese-top"></div>
      <div id = "wizard-content">
        <div v-if = "isLoading" id = "spinner" class = "text-center">
          <b-spinner variant="secondary" label="Spinning"></b-spinner>
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
      modalBodyClass: ['border-2']
    };
  },
  methods: {
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
  margin-top: 55%;
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

#modal-cheese-melt{
  background-image: url(/staticfiles/img/melt_bg_grey.png);
  background-size: cover;
  background-repeat: no-repeat;
  width: 100%;
  height: 50px;
}

.wizard-blocks :hover {
  transform: scale(1.1);
}

.pointer-cursor {
  cursor: pointer;
}



</style>
