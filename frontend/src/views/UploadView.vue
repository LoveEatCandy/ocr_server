<template>
  <div class="content">
    <el-upload class="upload" drag name="file_content" action="/api/upload">
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
    </el-upload>
  </div>
</template>

<script>
import { UploadFilled } from "@element-plus/icons-vue";
export default {
  components: {
    UploadFilled,
  },
};
</script>

<style scoped>
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
}
.upload {
  width: 50%;
}
</style>
