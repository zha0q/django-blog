<template>

    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="0"><i :class="timeIcon"></i> </el-menu-item>
      <el-menu-item index="1" @click="jumpTo('Home')">
        <router-link :to="{name: 'Home'}" class="link">首页</router-link>
      </el-menu-item>
      <el-menu-item index="2" @click="jumpTo('ArticleCreate')">
        <router-link :to="{name: 'ArticleCreate'}" class="link">发表文章</router-link>
      </el-menu-item>
      <el-menu-item v-if="!username" index="3" style="float: right"  @click="jumpTo('Login')">
        <router-link :to="{name: 'Login'}" class="link">登录</router-link>
      </el-menu-item>
      <el-menu-item v-if="!username"  index="4" style="float: right" @click="jumpTo('Register')">
        <router-link :to="{name: 'Register'}" class="link">注册</router-link>
      </el-menu-item>
      <el-menu-item v-if="username" index="5" style="float: right" @click="jumpTo('UserView')">
        <div class="link">{{username}}</div>
      </el-menu-item>
      <el-menu-item v-if="username" index="6" style="float: right" @click="jumpTo('Logout')">
        <div class="link" @click="logout">登出</div>
      </el-menu-item>
    </el-menu>

</template>

<script>

export default {
  name: "BlogHeader",
  props: {
    activeIndex: '',
  },

  data() {
    return({
      username: '',
      timeIcon: 'el-icon-moon',
    })
  },

  mounted() {
    this.username = localStorage.getItem('username');
    console.log(localStorage.getItem('username'))

    const curDate = new Date();
    const hours = curDate.getHours();
    if(hours <= 5 || hours >= 19)
      this.timeIcon = 'el-icon-moon';
    else if(hours > 5 && hours <= 8)
      this.timeIcon = 'el-icon-sunrise-1';
    else if(hours > 8 && hours <= 16)
      this.timeIcon = 'el-icon-sunny';
    else
      this.timeIcon = 'el-icon-sunset';
  },

  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    logout() {
      localStorage.clear();
      location.reload()
      console.log("out")
    },
    jumpTo(rut) {
      if(rut === 'UserView') {
        this.$router.push({name: rut, params: {username: this.username}})
        location.reload()
      }
      else
        this.$router.push({name: rut})
    }
  },

}
</script>

<style scoped>

  .link{
    text-decoration: none;
  }

</style>
