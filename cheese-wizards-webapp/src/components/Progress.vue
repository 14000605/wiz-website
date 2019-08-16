<template>
  <div id="progress">
    <WizardSideBar></WizardSideBar>
  </div>
</template>

<script>
import WizardSideBar from './WizardSideBar'
export default {
  name: "progress",
  components: { WizardSideBar },
  data() {
    return {
      userAddress: null
    };
  },
  methods: {
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
    getWizards: function(params) {
      var queryParams = this.encodeJsonToParams(params);
      var requestUrl = "/wizards?" + queryParams;

      $.ajax({
        url: requestUrl,
        method: "get",
        success: (data) => {
          // TODO: do something with wizards data
          console.log(data);
        },
        error: function(err) {
          console.log(err);
        }
      });
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
    // Example of how to get wizards
    this.getWizards({ owner: this.userAddress });
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
