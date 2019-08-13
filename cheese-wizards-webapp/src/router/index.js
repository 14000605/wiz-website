import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/Login';
import BootstrapVue from 'bootstrap-vue';

Vue.use(Router);
Vue.use(BootstrapVue);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    }
  ]
});
