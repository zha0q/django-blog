<template>
  <div>
    <el-header>
      <BlogHeader :active-index="'2'"></BlogHeader>
    </el-header>

    <el-form :model="form" label-width="80px" class="main">


      <el-form-item label="标题">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="图片">
        <img v-if="image" :src="image" class="avatar">
        <input type="file" @change="imgSubmit"></input>
      </el-form-item>
      <div class="toolbar">
        <el-button-group>
          <el-button size="mini" @click="addContent('****')">加粗</el-button>
          <el-button size="mini" @click="addContent('----------')">分割</el-button>
          <el-button size="mini" @click="addContent('#')">标题</el-button>
          <el-button size="mini" @click="addContent('``')">文本</el-button>
          <el-button size="mini" @click="addContent('``````')">代码</el-button>
          <el-button size="mini" @click="addContent('*')">无序列表</el-button>
          <el-button size="mini" @click="addContent('1. ')">有序列表</el-button>
        </el-button-group>
      </div>

      <el-form-item label="文章">
        <el-input
          type="textarea"
          :autosize="{minRows: 23, maxRows: 40}"
          resize="none"
          placeholder="请输入内容"
          v-model="form.content">
        </el-input>
        <el-button round style="margin-top: 20px" icon="el-icon-edit" @click="onSubmit">发表</el-button>
      </el-form-item>

  </el-form>
  </div>




</template>

<script>
import BlogHeader from "../components/BlogHeader";
import {postBlog, postImg} from "../api/api";
const token = localStorage.getItem('token')
// import authorization from '@/utils/authorization'
export default {
name: "ArticleCreate",
  components: {BlogHeader},

  mounted() {
    this.username = localStorage.getItem('username')
  },

  data() {
    return({
      form: {
        title: '',
        content: '',
      },
      username: '',
      image: '',
      imageId: '',
    })
  },

  methods: {
    imgSubmit(e) {
      if(!this.username)
      {
        alert('请登录！');
        setTimeout(() => {
          this.$router.push({name: 'Login'});
        }, 500)
      }
      else
      {

        let formData = new FormData();
        formData.append('content', e.target.files[0])
        postImg(formData)
        .then(response => {
          if(response.status >= 200 && response.status < 300)
          {
            alert("图片上传成功")
            this.image = response.data.content
            this.imageId = response.data.id
          }
        })
      }
    },

    onSubmit() {
      if(!this.username)
      {
        alert('请登录！');
        setTimeout(() => {
          this.$router.push({name: 'Login'});
        }, 500)
      }
      else
      {

        postBlog(this.form.title, this.imageId, this.form.content, token)
          .then(response => {
            if(response.status >= 200 && response.status < 300) {
              alert("发表成功!")
              setTimeout(() => {
                console.log(response)
                this.$router.push("/article/" + response.data.id)
              }, 500)

            }
          })
      }
    },
    addContent(txt) {
      this.form.content = this.form.content + txt
      console.log(this.form.content)
    }
  }

}
</script>

<style scoped>

.main {
  font: 13px Small;
  padding-right: 4em;
  margin-left: 20em;
  margin-right: 20em;
  text-align: center;
  background-color: white;
}

.avatar {
  height: 178px;
  width: 178px;
  display: block;
}

.toolbar {
  padding-left: 9em;
  padding-right: 9em;
  padding-bottom: 2em;
}

</style>
