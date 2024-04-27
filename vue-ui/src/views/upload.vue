<template>
    <div class="container">
        <!-- <el-row :gutter="20">
			<el-col :span="8">
                <div class="content-title">上传图像</div> -->
                <!-- <div class="plugins-tips">
                    Element Plus自带上传组件。 访问地址：
                    <a href="https://element-plus.org/zh-CN/component/upload.html" target="_blank">Element Plus Upload</a>
                </div> -->
                <!-- <el-upload
                    class="upload-demo"
                    drag
                    action="http://jsonplaceholder.typicode.com/api/posts/"
                    multiple
                    :on-change="handle"
                >
                    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                    <div class="el-upload__text">
                        将文件拖到此处，或
                        <em>点击上传</em>
                    </div>
                </el-upload>
            </el-col> -->
        
            <!-- <el-col :span="12"> -->
        <div class="content-title">图像列表</div>
        <el-upload
            v-model:file-list="fileList"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
        >
            <el-icon><Plus /></el-icon>
        </el-upload>
            <!-- </el-col> -->
        <!-- </el-row> -->
    </div>

    <el-dialog v-model="dialogVisible">
        <img w-full :src="dialogImageUrl" alt="Preview Image" />
    </el-dialog>
</template>

<script setup lang="ts">
// const handle = (rawFile: any) => {
//     console.log(rawFile);
// };

import { ref } from 'vue'
import { Plus } from '@element-plus/icons-vue'

import type { UploadProps, UploadUserFile } from 'element-plus'

const fileList = ref<UploadUserFile[]>([
  {
    name: 'food.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
  {
    name: 'plant-1.png',
    url: '/images/plant-1.png',
  },
  {
    name: 'food.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
  {
    name: 'plant-2.png',
    url: '/images/plant-2.png',
  },
  {
    name: 'food.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
  {
    name: 'figure-1.png',
    url: '/images/figure-1.png',
  },
  {
    name: 'food.jpeg',
    url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
  },
  {
    name: 'figure-2.png',
    url: '/images/figure-2.png',
  },
])

const dialogImageUrl = ref('')
const dialogVisible = ref(false)


const handleRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
  console.log(uploadFile, uploadFiles)
}

const handlePictureCardPreview: UploadProps['onPreview'] = (uploadFile) => {
  dialogImageUrl.value = uploadFile.url!
  dialogVisible.value = true
}

</script>

<style scoped>
.content-title {
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
.upload-demo {
    width: 360px;
}
</style>
