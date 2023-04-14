<template>
  <div class="content">
    <el-card class="box-card" @click="redirect('/upload')">
      <h1>上传</h1>
    </el-card>
    <el-card class="box-card" @click="redirect('/list')">
      <h1>查看</h1>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {};
  },
  created() {},
  methods: {
    redirect(path) {
      this.$router.push({
        path: path,
      });
    },
  },
};
</script>

<style scoped>
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.box-card {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
}
</style>
