<template>
  <div id = "progress">
    
  </div>
</template>

<script>
import Login from "./Login.vue";
export default {
  name: "progress",
  components: {
   
  },
  data() {
    return {
      userAddress : null
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
      var requestUrl = "/wizards?"+ queryParams;

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
    this.userAddress = this.$route.params.address;
    // Example of how to get wizards
    this.getWizards({'owner' : this.userAddress});
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
