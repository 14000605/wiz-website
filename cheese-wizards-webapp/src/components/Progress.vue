<template>
  <div id="progress">
    <WizardSideBar 
      :userAddress = "userAddress" 
      v-on:filterOptionsChanged = "filtersChanged"
    >
    </WizardSideBar>
  </div>
</template>

<script>
import WizardSideBar from './WizardSideBar'
export default {
  name: "progress",
  components: { WizardSideBar },
  data() {
    return {
      userAddress: null,
      wizards: []
    };
  },
  methods: {
    filtersChanged: function(options) {
      console.log("Detected change in filter options: " + options);
    }
  },
  created: function(){
    var address = this.$route.params.address;
    // If user address is undefined, we try to retrieve it from local storage
    if (address == undefined) {
      var address = localStorage.getItem('address');
      // If nothing found in local storage, then redirect to main page
      if (address == undefined) {
        this.$router.push({name : "Main"});
        return;

      } else {
        this.userAddress = address;
        console.log("address retreived from local storage" + address);
      }
    } else {
      // Store user address in local storage for page refreshes
      this.userAddress = address;
      localStorage.setItem('address', this.userAddress);
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
</style>
