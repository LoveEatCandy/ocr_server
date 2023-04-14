<template>
  <div class="content"></div>
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

    if (this.timer) {
      clearInterval(this.timer);
    } else {
      this.timer = setInterval(() => {
        this.getData();
      }, 1000);
    }
  },
  destroyed() {
    if (this.timer) {
      clearInterval(this.timer);
    }
  },
  methods: {
    getData() {
      this.axios.get("/api/img").then((res) => {
        this.table = res.data;
      });
    },
  },
};
</script>
<style></style>
