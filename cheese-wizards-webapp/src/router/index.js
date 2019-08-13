import Vue from 'vue';
import Router from 'vue-router';
import Main from '@/components/Main';
import BootstrapVue from 'bootstrap-vue';

Vue.use(Router);
Vue.use(BootstrapVue);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    }
  ]
});
