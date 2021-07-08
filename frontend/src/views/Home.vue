<template>
  <el-container class="hello">

    <el-header>
      <BlogHeader :active-index="'1'"></BlogHeader>
    </el-header>
    <el-main class="main">
      <ArticleList></ArticleList>
    </el-main>




  </el-container>
</template>



<script>
import {getBlogs, postBlog} from "../api/api";
import ArticleList from "../components/ArticleList";
import BlogHeader from "../components/BlogHeader";

export default {
  name: 'Home',
  components: {BlogHeader, ArticleList},



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

.main {

  margin-left: 10em;
  margin-right: 10em;
}


</style>
