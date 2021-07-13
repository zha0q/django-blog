<template>

  <div class="infinite-list-wrapper" style="overflow:auto">
    <ul
      class="list"
      v-infinite-scroll="load"
      infinite-scroll-disabled="disabled">
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
    <p v-if="loading"><el-skeleton /></p>
    <p v-if="noMore">没有更多了</p>

  </div>


</template>

<script>
import {getBlogs} from "../api/api";
export default {
  name: "ArticleList",

  data () {
    return {

      blogs: [],
      loading: false,
      nextUrl: 'http://127.0.0.1:8000/api/article/',

    }
  },

  mounted() {
    this.loadBooks()
  },

  computed: {
      noMore () {
        return !this.nextUrl
      },
      disabled () {
        return this.loading || this.noMore
      }
    },

  methods: {
    loadBooks() {
      getBlogs(this.nextUrl).then(response => {
        console.log(response.data)
        this.blogs = this.blogs.concat(response.data.results)
        this.nextUrl = response.data.next
        console.log(this.next)
      })

    },

    load () {
      this.loading = true
        setTimeout(() => {
          if(this.nextUrl != null){
            this.loadBooks()
          }
          this.loading = false
        }, 2000)
      }

  },

}
</script>

<style scoped>

ul {
  margin: 0;
  padding-inline-start: 0;
}

p {
  text-align: center;
}

.article {

  height: 10em;
  padding: 10px;

  background-color: #ffffff;

  border: 2px solid #eee;
  border-radius: 4px;
}

.ttitle {

  color: #121212;
  font-size:  24px;
  text-decoration: none;
}

.content {
  float: left;
  height: 100px;
  overflow: hidden;
  text-overflow-ellipsis: true;
  word-wrap: break-word;
  margin-top: 12px;
  line-height: 1.67;
}

.avatar {
  height: 178px;
  width: auto;
  display: block;
}

</style>
