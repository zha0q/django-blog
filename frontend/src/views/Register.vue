<template>
  <div>
    <BlogHeader :active-index="'4'"></BlogHeader>
    <el-form ref="form" :model="form" label-width="80px" class="main">
      <el-form-item label="昵称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.psw"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click.prevent="onsubmit">注册</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
import BlogHeader from "../components/BlogHeader";
import {postUser} from "../api/api";

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
      postUser(this.form.name, this.form.psw)
        .then(response => {
          this.rps = response.data
          alert('注册成功！')
          setTimeout(() => {
            this.$router.push({name: 'Login'});
          }, 1000)
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
  width: 30em;
}

</style>
