<template>
  <div class="hello">
    <div class = "container">
      <b-alert :show = "errMsg" variant = "warning" dismissible fade>
        <small>{{ errMsg }}</small>
      </b-alert>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
          <div class="card card-signin my-5">
            <div class="card-body">
              <h5 class="card-title text-center">Sign In</h5>
              <form class="form-signin">
                <div class="form-label-group container">
                  <input
                    id="inputAddress"
                    class="form-control"
                    placeholder="Wallet address"
                    required
                    autofocus
                  />
                </div>
                <br />
                <b-button variant = "primary" class = "w-100">Let's Go!!</b-button>
                <hr class="my-4" />
                <b-button variant = "primary" class = "w-100 mb-2">Use Dapper</b-button>
                <b-button variant = "primary" class = "w-100 mb-2">Usse Metamask</b-button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
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
      errMsg: null
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
        success: data => {
          // Listen for this event to retrieve wizards data
          this.$emit("logged-in", data);
          console.log(data);
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  },
  created: function(){
    onDapperWalletLogIn(this);
  }
};

async function onDapperWalletLogIn(self) {
  if (typeof window.ethereum === "undefined") {
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

    var queryObj = { owner: ownerAddress };
    self.getWizards(queryObj);
  } catch (error) {
    // Handle error. If the user rejects the request for access, then
    console.log("user rejected permission to access dapper wallet");
    console.log(error);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: exocet;
  src: url(/staticfiles/font/exocet.ttf);
}

.wiz-login-card {
  margin-top: 200px;
}

.wiz-login-card-title {
  font-family: exocet, sans-serif;
}
</style>
