<template>
  <div class="content">
    <el-tabs type="border-card">
      <el-tab-pane
        v-for="item in table"
        :key="item.origin"
        :label="item.origin"
        class="tab"
      >
        <div class="left">
          <el-image :src="getImageUrl(item.origin)" fit="contain" />
          <el-divider />
          <el-image :src="getImageUrl(item.translated)" fit="contain" />
        </div>
        <div class="right">
          <pre>{{ item.text }}</pre>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "ListView",
  data() {
    return {
      table: [],
      timer: null,
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      this.axios.get("/api/img").then((res) => {
        this.table = res.data.data;
      });
    },
    getImageUrl(origin) {
      return "http://127.0.0.1:8888/" + origin;
    },
  },
};
</script>
<style>
.tab {
  display: flex;
  flex-direction: row;
}
.left {
  display: flex;
  flex-direction: column;
}
.left img {
  height: 42vh;
}
.right {
  max-width: 30%;
  margin-left: 30px;
  font-size: 20px;
  line-height: 36px;
}
</style>
