import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import movieStore from './modules/movieStore.js'
import loginStore from './modules/loginStore.js'


Vue.use(Vuex)


export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  modules:{
    movieStore:movieStore,
    loginStore:loginStore,
  }
})
