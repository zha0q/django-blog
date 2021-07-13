import Vue from 'vue'
import Router from 'vue-router'

//引入组件
import Home from '../views/Home'
import ArticleDetail from "../views/ArticleDetail";
import Register from "../views/Register";
import Login from "../views/Login";
import ArticleCreate from "../views/ArticleCreate";
import UserView from "../views/UserView";


Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },

    {
      path: '/article/:id',
      name: 'ArticleDetail',
      component: ArticleDetail
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/articlecreate',
      name: 'ArticleCreate',
      component: ArticleCreate
    },
    {
      path: '/userview/:username',
      name: 'UserView',
      component: UserView
    },
  ]
})


const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

