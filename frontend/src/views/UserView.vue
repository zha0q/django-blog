<template>
  <el-container>
    <el-header>
      <BlogHeader :active-index="'5'"/>
    </el-header>

    <el-main class="main">

      <el-table
        :data="tableData"
        stripe
        style="width: 100%">
        <el-table-column
          prop="id"
          label="ID"
          width="200">
        </el-table-column>
        <el-table-column
          prop="username"
          label="姓名"
          width="200">
        </el-table-column>
        <el-table-column
          prop="last_login"
          label="最后登录"
          width="200">
        </el-table-column>
        <el-table-column
          prop="date_joined"
          label="注册日期"
          width="200">
        </el-table-column>
        <el-table-column
          v-if="username === this.$route.params.username"
          label="修改"
          width="100">
          <el-button size="mini" @click="drawer = !drawer">修改</el-button>
        </el-table-column>
        <el-table-column
          v-if="username !== this.$route.params.username"
          label="订阅"
          width="100">
          <el-button size="mini" @click="onSubscribe">订阅</el-button>
        </el-table-column>
      </el-table>

      <el-collapse>
        <el-collapse-item title="订阅" style="text-align: center">
          <div v-for="i in fans" :key="i.id" @click="visit(i.blogger)">{{ i.blogger }}</div>
        </el-collapse-item>
      </el-collapse>

      <ul>
        <li v-for="i in blogs" :key="i.id" class="article" style="display:block">
          <div style="width: 100%;">
            <router-link :to="{name: 'ArticleDetail', params: {id: i.id}}" class="ttitle">{{i.a_title}}</router-link>
          </div>
          <div class="content">
            <img :src="i.avatar.content" class="avatar">
          </div>
          <div class="content">
            {{i.author.username}}：{{i.a_content}}
          </div>
        </li>
      </ul>

      <el-drawer
        title="我是标题"
        :visible.sync="drawer"
        direction="btt"
        :with-header="false">
        <el-form v-if="username === this.$route.params.username" ref="form" :model="form" label-width="80px" class="main">
          <el-form-item label="昵称">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="form.psw"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click.prevent="onSubmit">修改</el-button>
          </el-form-item>
        </el-form>
      </el-drawer>
    </el-main>

  </el-container>


</template>

<script>
import {getBlogs, postSubscribe, postUserChange} from "../api/api";
import BlogHeader from "../components/BlogHeader";
export default {
  name: "UserView",

  components: {BlogHeader},

  created() {
    this.getInfo()
    this.username = localStorage.getItem('username')
    this.token = localStorage.getItem('token')
    this.loadBlog()
    this.loadFans()
  },

  data() {
    return({
      form: {
        name: '',
        psw: '',
      },
      tableData: [],
      username: '',
      token: '',
      drawer: false,
      nextUrl: '/api/article/',
      blogs: [],
      fans: [],
    })
  },

  methods: {
    getInfo() {
      getBlogs('/api/user/' + this.$route.params.username + '/info')
      .then(response => {
        this.tableData = this.tableData.concat(response.data)
        this.tableData[0].date_joined = new Date(this.tableData[0].date_joined).toLocaleDateString()
      })
    },
    onSubmit() {
      postUserChange('/api/user/' + this.username, this.form.name, this.form.psw, this.token)
      .then(response => {
        if(response.status >= 200 && response.status < 300)
        {
          alert("修改成功!")
          console.log(response)
          localStorage.setItem('username', response.data.username)
          this.$router.push({name: 'UserCenter', params: {username: response.data.username}});
          location.reload()
        }
      })
    },
    onSubscribe() {
      postSubscribe(this.username, this.$route.params.username)
      .then(response => {
        if(response.status >= 200 && response.status < 300)
          alert('订阅成功!')
      })
    },
    loadBlog() {

      getBlogs(this.nextUrl).then(response => {
        this.blogs = this.blogs.concat(response.data.results.filter(i => {
          return i.author.username === this.$route.params.username
        }))
        this.nextUrl = response.data.next
        if(this.nextUrl !== null)
          this.loadBlog()
        console.log(this.nextUrl)
      }).catch(error => {
          console.log(error)
      })
    },
    loadFans() {
      getBlogs('/api/subscribe/')
      .then(response => {
        this.fans = this.fans.concat(response.data.results.filter(i => {
          return i.fans === this.$route.params.username
        }))
        console.log(this.fans)
      })
    },
    visit(author) {
      this.$router.push({name: 'UserView', params: {username: author}})
      location.reload()
    },


  },


}


</script>

<style scoped>

</style>
