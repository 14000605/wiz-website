<template>
  <div class="login">
    <div class="container">
      <b-alert :show="errMsg" variant="warning" dismissible fade>
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
                    v-model="userAddress"
                    id="inputAddress"
                    class="form-control"
                    placeholder="Wallet address"
                    required
                    autofocus
                  />
                </div>
                <br />
                <b-button
                  variant="primary"
                  class="w-100"
                  @click="onGoButtonClicked"
                  :disabled="!userAddress"
                >Let's Go!!</b-button>
                <hr class="my-4" />
                <b-button class="w-100 mb-2" @click="useDapperWallet">Dapper</b-button>
                <b-button class="w-100 mb-2">Use Metamask</b-button>
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
      errMsg: null,
      userAddress: null
    };
  },
  methods: {
    isAddressValid: function() {
      // try {
      //   const address = web3.utils.toChecksumAddress(address);
      //   return address;
      // } catch(e) {
      //   return e.message;
      // }
      var address = this.userAddress;
      return address != null || address != "";
    },
    onGoButtonClicked: function() {
      // this.validateEthereumAddress(this.userAddress);
      // We still need to validate owner address
      this.$router.push({
        name: "Progress",
        params: { address: this.userAddress }
      });
    },
    useDapperWallet: function() {
      this.retrieveDapperWalletAddress(this);
    },
    retrieveDapperWalletAddress: async self => {
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
        console.log("found owner address: " + ownerAddress);
        self.userAddress = ownerAddress;
      } catch (error) {
        // Handle error. If the user rejects the request for access, then
        console.log("user rejected permission to access dapper wallet");
        console.log(error);
      }
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

.wiz-login-card {
  margin-top: 200px;
}

.login {
  font-family: code saver;
}
</style>
