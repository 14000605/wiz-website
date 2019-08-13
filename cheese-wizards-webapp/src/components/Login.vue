<template>
  <div class="hello">
    <div v-if = "errMsg" class = "alert alert-warning"><small>{{ errMsg }}</small></div>
    <div class = "h1">{{ msg }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: "Login",
      errMsg: null
    }
  },
  methods: {
    encodeJsonToParams: function(params) {
      var urlQuery = ""
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
       var xEmail = "khalili@sfu.ca";
       var apiToken = "Nf7zvG9vaYOW6cx1ZXXT0_9DPr1srXzZ7phJ3il7";
       var contentType = "application/json";

       var headerObj = {
         'x-email' : xEmail,
         'x-api-token' : apiToken,
         'Content-Type' : contentType
       };

       var queryParams = this.encodeJsonToParams(params);
       var baseUrl = "https://cheezewizards.alchemyapi.io/wizards?";
       var requestUrl = baseUrl + queryParams;
      
       $.ajax({
         url: requestUrl,
         method: "get",
         headers: headerObj,
         success: (data)=> {
            // Listen for this event to retrieve wizards data
            this.$emit("logged-in", data);
            console.log(data);
         },
         error: function(err) {
           console.log(err);
         }
       });
    }
  }
}

async function onDapperWalletLogIn (self) {
  if (typeof window.ethereum === 'undefined') {
    // Handle case where user hasn't installed Dapper.
    self.errMsg = "oops! it seems like you don't have dapper installed";
    return;
  }

  try {
    // If a user is logged in to Dapper and has previously approved the dapp,
    // `ethereum.enable` will return the result of `eth_accounts`.
    const accounts = await window.ethereum.enable();
    const ownerAddress = accounts[0];
    console.log(ownerAddress);

    var queryObj = { "owner" : ownerAddress };
    self.getWizards(queryObj);


  } catch (error) {
    // Handle error. If the user rejects the request for access, then
    console.log("user rejected permission to access dapper wallet");
    console.log(error);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang = "scss" scoped>
</style>
