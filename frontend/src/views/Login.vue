<template>
  <div >
    <BlogHeader :active-index="'3'"></BlogHeader>
    <el-form ref="form" :model="form" label-width="80px" class="main">
      <el-form-item label="昵称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.psw"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click.prevent="onsubmit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
import BlogHeader from "../components/BlogHeader";
import {postLogin} from "../api/api";

export default {
  name: "Register",
  components: {BlogHeader},

  data() {
    return({
      form: {
        name: '',
        psw: '',
      },
      rps: '',
    })
  },

  methods: {
    onsubmit() {
      postLogin(this.form.name, this.form.psw)
        .then(response => {
          console.log(response)
          if(response.status === 200)
          {
            this.rps = response
            localStorage.setItem("token", response.data.access);
            localStorage.setItem("username", this.form.name);
            alert('登录成功！')
            setTimeout(() => {
            this.$router.push({name: 'Home'});
            }, 500)
          }



          // 路由跳转
          // 登录成功后回到博客首页

        })
        .catch(error => {
          alert(error.message)
        });
      console.log(this.rps);
    },
  },


}
</script>

<style scoped>

.main {
  margin: 6em 20em 0 22em;
  height: 30em;
  width: 30em;}
</style>
