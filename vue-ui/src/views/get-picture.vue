<template>
    <div>
      <el-upload v-model="fileList" ref="uploadref" action="#" :auto-upload="false" list-type="picture-card" :file-list="fileList" :limit="1" :on-preview="handlePictureCardPreview" :on-remove="handleRemove">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog v-model="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt="" />
      </el-dialog>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        fileList: [],
        dialogImageUrl: "",
        dialogVisible: false,
        fileParam: "",
      };
    },
    created() {
      axios
        .get("http://127.0.0.1:5000/get-picture/")
        .then((response) => {
          console.log(response.data);
          this.fileList.push(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
      handleRemove(file, fileList) {
        this.fileList.pop();
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
    },
  };
  </script>
  