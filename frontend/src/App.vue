<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background-color: #f6f6f6;
  margin-top: 4px;
}

.main {
  font: 13px Small;
  margin-left: 10em;
  margin-right: 10em;
}

.article {

  height: 10em;
  padding: 10px;
  overflow: hidden;
  background-color: #ffffff;

  border: 2px solid #eee;
  border-radius: 4px;
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

.ttitle {

  color: #121212;
  font-size:  24px;
  text-decoration: none;
}

</style>
