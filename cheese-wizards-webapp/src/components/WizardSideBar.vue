<template>
  <div id = "sidebar-wrapper">
    <div id = "cheese-arrow-control" @click="onCheeseArrowClicked" v-b-tooltip.hover.v-warning :title = "toolTip.arrowControl">
      <img id = "cheese-arrow" class = "cheese-arrow-right" src = "/staticfiles/img/cheese_slice.png" />
    </div>
   <div id = "wizard-sidebar">
      <div id = "cheese-top"></div>
      <div id = "sidebar-content">
        <div class = "h5" id = "sidebar-title">Wizards</div>
        <!--This is the fancy cheese top bar-->
        <div id = "solid-cheese-top"></div>
        <div id = "wizard-content">
          <div v-if = "isLoading" id = "wizard-content-spinner" class = "text-center">
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
        <!--Filter options-->
        <div id = "filter-options">
          <b-form-group>
            <b-form-checkbox-group 
              class = "mt-4" 
              v-model = "filterOptions" 
              @change = "onFilterOptionsChanged($event)" 
              offset = "200"
              :disabled = "wizards.length <= 0"
              stacked 
              buttons
            >
              <b-form-checkbox class = "mb-2 dark-grey" value = "Energy Transfers">Energy Transfers</b-form-checkbox>
              <b-form-checkbox class = "mb-2 dark-grey" value = "Duals">Duals</b-form-checkbox>
              <b-form-checkbox class = "mb-2 dark-grey" value = "Ascentions">Ascentions</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
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
          centered
        >
          <template slot = "modal-header">
            <!--Header texture-->
            <div id = "modal-cheese-melt"></div>
          </template>
          <template slot = "default">
            <!--Modal body content-->
             <div v-if = "isModalLoading" id = "modal-content-spinner" class = "text-center">
              <div><img class = "cheese-spinner" src = "/staticfiles/img/cheese_spinner_icon.png" width = "60px" height = "60px"/></div>
              <small>fetching wizard data...</small>
            </div>
            <b-container v-if = "!isModalLoading" style = "font-family: code saver;">
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
      isModalLoading: true,
      showModal: false,
      modalInfo: {
        src: null,
        affinity: null,
        power: null,
        initialPower: null
      },
      modalHeaderClass: ['p-0', 'border-2'],
      modalBodyClass: ['border-2'],
      isActive: false,
      filterOptions: [],
      toolTip: {
        arrowControl: "toggle sidebar",
        filterOptions: "choose one or more filters to generate suggestions."
      }
    };
  },
  methods: {
    // Triggered on any filter option selected or deselected
    // Emits an event 'filterOptionsChanged' that the parent component can listen to
    onFilterOptionsChanged: function(event) {
      // Just cleaning up recieved data from event before sending it
      var selected = [];
      for (var i = 0; i < event.length; i++) {
        selected.push(event[i]);
      }
      console.log("filters: " + selected);
      // Perhaps we should only register a change if there are any filters selected
      if (selected.length > 0) {
        this.$emit("filterOptionsChanged", selected);
      }
    },
    onCheeseArrowClicked: function(){
      // set target to sidebar and cheese arrow control position/rotation
      var direction = $('#sidebar-wrapper').width() - 35;
      var degrees = 180;
      
      this.$set(this.toolTip, "arrowControl", "hide sidebar");
      // set target to initial position/rotation
      if (slideDirection < 0) {
        direction = 0;
        degrees = 0;
        this.$set(this.toolTip, "arrowControl", "toggle sidebar");
      }
      
      // slide sidebar
      Velocity($('#sidebar-wrapper'), {'translateX' : direction + "px"});
      slideDirection = slideDirection * -1;

      // change cheese arrow control direction
      Velocity($('#cheese-arrow'), {
        'rotateZ': degrees + "deg" 
      });

      // Load wizard data if not already loaded (Lazy)
      if (!this.isActive) {
          this.isActive = true;
          this.fetchWizards({'owner' : this.userAddress}, (wizards)=>{
            if (wizards == null) {
              console.log("error occurred while fetching wizards");
            } else {
              this.wizards = wizards;
              this.getWizardImages();
              this.isLoading = false;
            }
          });
      }
    },
    // get affinity directory names from integer values
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
   // get formatted text to display from affinity integer values
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
   // Choose random image for wizard based on provided affinity
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
    onWizardIconClicked: function(img) {
      this.isModalLoading = true;
      var id = this.wizards[img.id].id;
      console.log("clicked on wizard with id: " + id);
      
      this.showModal = true;
      this.fetchWizards({'id' : id}, (wizards)=>{
        if (wizards == null) {
          console.log("an error has occurred while fetching wizard with id " + id);
        } else {
          var wizard = wizards[0];
          wizard['src'] = img.src;
          this.modalInfo = wizard;
          this.isModalLoading = false;
        }
    });
  },
  // The callback function must take one argument - that is the data fetched
  // If data passed is null, an error has occurred
  fetchWizards: function(params, callback) {
      var requestUrl = "";

      if (params['id'] != undefined) {
        requestUrl = "/wizards/" + params['id'];
      } else {
        var queryParams = this.encodeJsonToParams(params);
        requestUrl = "/wizards?" + queryParams;
      }
      // This will store data fetched and pass it into the callback as an argument
      var intermediate = [];

      $.ajax({
        url: requestUrl,
        method: "get",
        success: (data) => {
          intermediate = data.wizards;
          console.log("succesfully fetched wizard data");
        },
        error: function(err) {
          intermediate = null;
          console.log(err);
        }
      }).done(()=>{
        console.log(intermediate);
        callback(intermediate);
      });
    }
  }
};
</script>

<style scoped>
@font-face {
  font-family: exocet;
  src: url(/staticfiles/font/exocet.ttf);
}

@font-face {
  font-family: code saver;
  src: url(/staticfiles/font/codesaver-regular-webfont.woff);
}

.custom-tooltip {
  font-size: 0.5em;
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

/* #cheese-top :hover {
   background-image: url(/staticfiles/img/orange_melt_warped.png); 
} */

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

.dark-grey {
  background-color: #35393c;
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

#wizard-content-spinner {
  margin-top: 50%;
  color: #b3adad;
  font-size: 0.5em;
}

#modal-content-spinner {
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
