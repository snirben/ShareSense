import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('./components/loginPage.vue')
    },
    {
      path: '/logout',
      name: 'Logout',
      component: () => import('./components/loginPage.vue')
    },
    {
      path: '/alertcenter',
      name: 'alertcenter',
      component: () => import('./components/AlertCenter.vue')
    },
    {
      path: '/panicbutton',
      name: 'panicbutton',
      component: () => import('./components/panicButton.vue')
    },
  ]
})

export default router