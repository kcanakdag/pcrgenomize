import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')

export default {
  setup() {
    const usersPromise = ref(fetchUsers())
    const promised = usePromise(usersPromise)

    return {
      ...promised,
      // spreads the following properties:
      // data, isPending, isDelayElapsed, error
    }
  },
}