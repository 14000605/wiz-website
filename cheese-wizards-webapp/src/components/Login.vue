<template>
  <div class="hello">
    <div class="wiz-login-card">
      <b-card bg-variant="dark" text-variant="white" title="Login">
        <b-card-text
          class="d-flex justify-content-center"
        >With supporting text below as a natural lead-in to additional content.</b-card-text>
        <b-button class="d-flex justify-content-center" href="#" variant="primary">Login</b-button>
      </b-card>
    </div>

    <div class="wiz-login-background">
      <img class="wiz-login-background" src="../assets/cheese.png" />
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
      msg: "Login"
    };
  },
  created: function() {
    // debug()
    init();
  }
};

async function init() {
  if (typeof window.ethereum === "undefined") {
    // Handle case where user hasn't installed Dapper.
    return;
  }

  try {
    // If a user is logged in to Dapper and has previously approved the dapp,
    // `ethereum.enable` will return the result of `eth_accounts`.
    const accounts = await window.ethereum.enable();
    console.log(accounts);
  } catch (error) {
    // Handle error. If the user rejects the request for access, then
  }
}

// const Web3 = require('web3')
// const DappAuth = require('@dapperlabs/dappauth')

// const dappAuth = new DappAuth(new Web3.providers.HttpProvider('http://localhost:8080'))

// async function debug () {
//   const challenge = 'foo'
//   const signature = '0x33838c6f4e621982c2009f9b93ecb854a4b122538159623abc87d2e4c5bd6d2e33591f443b419b3bd2790e455ba6d625f2ca14b822c5cef824ef7e9021443bed1c'
//   const address = '0x86aa354fc865925f945b803ceae0b3f9d856b269'

//   try {
//     const isAuthorizedSigner = await dappAuth.isAuthorizedSigner(
//       challenge,
//       signature,
//       address
//     )

//     console.log(isAuthorizedSigner) // true
//   } catch (e) {
//     console.log(e)
//   }
// }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wiz-login-background {
  position: fixed;
  bottom: 0px;
  right: 0px;
  left: 0px;
  width: 100vw;
  height: 35vh;
}
img {
  object-fit: contain;
}

.wiz-login-card {
  display: flex;
  justify-content: center;
  margin-top: 200px;
}
</style>
