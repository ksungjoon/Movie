import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MovieDetail from '@/views/MovieDetail'
import ProfileView from '@/views/ProfileView'
import MyProfileView from '@/views/MyProfileView'
import SearchView from '@/views/SearchView'
import MainView from '../views/MainView.vue'
import RecommandView from '@/views/RecommandView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MainView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/myprofile/:username',
    name: 'MyProfileView',
    component: MyProfileView
  },
  {
    path: '/search/:keyword',
    name: 'SearchView',
    component: SearchView,
  },
  {
    path: '/recommand/:username',
    name: 'RecommandView',
    component: RecommandView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
