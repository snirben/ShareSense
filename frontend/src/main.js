import Vue from 'vue';
import App from './App.vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
library.add(faRightFromBracket);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.config.productionTip = false;
import router from './routers';

new Vue({
	render : (h) => h(App),
	router
}).$mount('#app');
