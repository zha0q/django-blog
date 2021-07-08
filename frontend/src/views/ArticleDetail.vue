<template>
  <el-container>

    <el-header>
      <BlogHeader :active-index="'1'"></BlogHeader>
    </el-header>
    <el-main class="main">
      <div class="article">
        <h1 class="ttitle">
          {{article.a_title}}
          <div class="aauthor assist">
            {{article.author.username}}<br>发布于
            {{format_time(article.created)}}
          </div>
        </h1>

        <div v-html="article.body_html" class="body"></div>

      </div>


    </el-main>
    <el-main class="main">
      <div class="article">
        <h1>评论</h1><el-button @click="onSubmit" style="float: right; margin-bottom: 10px" icon="el-icon-plus">提交</el-button>
        <el-input
          type="textarea"
          :autosize="{minRows: 3, maxRows: 10}"
          resize="none"
          v-model="comment">

        </el-input>
        <el-card v-for="i in comments" :key="i.c_content">
          <p @click="calls(i.author.username)">@{{i.author.username}}: {{i.c_content}}</p>
          <p style="float:right" class="assist">{{format_time(article.created)}}</p>
        </el-card>


      </div>




    </el-main>




  </el-container>
</template>

<script>
import BlogHeader from "../components/BlogHeader";
import {getBlogs, postComment} from "../api/api";
export default {
  name: "ArticleDetail",
  components: {BlogHeader},

  created() {
    this.load();
  },

  data() {
    return({
      article: {
        author: '',
        created: '',
      },
      comment: '',
      comments: [],
    })
  },

  methods: {
    load() {
      getBlogs('/api/article/' + this.$route.params.id)
      .then(response => {
        this.article = response.data
      })
      getBlogs('/api/comment/')
      .then(response => {
        this.comments = response.data.results.filter(i => {
          return i.article.toString() === this.$route.params.id

        })
      })
    },
    format_time(date) {
      const d = new Date(date);
      return d.toLocaleDateString()
    },
    onSubmit() {
      const token = localStorage.getItem('token')
      postComment(this.comment, this.$route.params.id, token)
      .then(response => {

          alert("评论成功！")
          setTimeout(() => {
            location.reload()
          }, 500)
      })
      .catch(error => {
        alert(error.message)
      })
    },
    calls(uname) {
      this.comment = this.comment + '@' + uname
    },
  },

}
</script>

<style scoped>

.main {
  font: 13px Small;
  margin-left: 10em;
  margin-right: 10em;
}

.article {

  height: auto;
  padding: 10px;

  background-color: #ffffff;

  border: 2px solid #eee;
  border-radius: 4px;
}

.ttitle {
  display: block;
  font: 20px Extra large;
  margin: 30px;
}

.aauthor {
  font: 13px Small;
  float: right;
  line-height: 0.1;
}

.assist {
  color: #bdb4b7;
  font: 10px Extra Small;
}

.body {
  margin-left: 30px;
  margin-right: 30px;
}

</style>
