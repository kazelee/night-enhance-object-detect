<template>
    <div>
        <div class="container" style="margin-bottom: 20px;">
            <div class="content-title">图像列表</div>
            <el-upload
                v-model="fileList"
                ref="uploadref"
                action="#"
                :auto-upload="false"
                list-type="picture-card"
                :file-list="fileList"
                
                :on-change="handleChange"
                :on-preview="handlePictureCardPreview"
                :on-remove="handleRemove"
            >
                <!-- :limit="1" -->
                <!-- :before-remove="beforeRemove" -->

                <!-- 使用 drag 会导致添加图像只有最后一张存到本地，这里不考虑了 -->

                <!-- <i class="el-icon-plus"></i> -->
                <el-icon><Plus /></el-icon>
                <!-- <template #tip>
                    <div class="el-upload__tip">
                        jpg/png files with a size less than 500kb
                    </div>
                </template> -->
            </el-upload>
            <!-- <div class="handle-row">
                <el-button type="primary" @click="handleClick">保存到本地</el-button>
            </div> -->
        </div>
        
        <div class="container" style="margin-bottom: 20px;">
            <div class="content-title">参数设置</div>
            <el-form ref="formRef" :rules="rules" :model="form" label-width="80px">
                <el-form-item label="强光分离" prop="delivery">
                    <el-col :span="2">
                        <el-switch v-model="form.delivery"></el-switch>
                    </el-col>
                    <el-col :span="1">尺寸：</el-col>
                    <el-col :span="2">
                        <el-select v-model="form.region" placeholder="请选择">
                            <el-option key="512" label="512" value=512></el-option>
                            <el-option key="1024" label="1024" value=1024></el-option>
                        </el-select>
                    </el-col>
                    
                </el-form-item>
                <el-form-item label="暗光增强" prop="delivery2">
                    <el-col :span="2">
                        <el-switch v-model="form.delivery2"></el-switch>
                    </el-col>
                    <el-col :span="1">模型：</el-col>
                    <el-col :span="3">
                        <el-select v-model="form.region2" placeholder="请选择">
                            <el-option key="LOL_v1" label="LOL_v1" value="LOL_v1"></el-option>
                            <el-option key="LOL_v2_real" label="LOL_v2_real" value="LOL_v2_real"></el-option>
                            <el-option key="LOL_v2_synthetic" label="LOL_v2_synthetic" value="LOL_v2_synthetic"></el-option>
                            <el-option key="SDSD_indoor" label="SDSD_indoor" value="SDSD_indoor"></el-option>
                            <el-option key="SDSD_outdoor" label="SDSD_outdoor" value="SDSD_outdoor"></el-option>
                            <el-option key="SID" label="SID" value="SID"></el-option>
                            <el-option key="SMID" label="SMID" value="SMID"></el-option>
                            <el-option key="FiveK" label="FiveK" value="FiveK"></el-option>
                        </el-select>
                    </el-col>
                </el-form-item>
                <el-form-item label="目标检测" prop="delivery3">
                    <el-col :span="2">
                        <el-switch v-model="form.delivery3"></el-switch>
                    </el-col>
                    <el-col :span="1">模型：</el-col>
                    <el-col :span="3">
                        <el-select v-model="form.region3" placeholder="请选择">
                            <el-option key="yolov8n.pt" label="yolov8n.pt" value="yolov8n.pt"></el-option>
                            <el-option key="bdd_day40k.pt" label="bdd_day40k.pt" value="bdd_day40k.pt"></el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="1">&nbsp;&nbsp;尺寸：  </el-col>
                    <el-col :span="2">
                        <el-input type="textarea" rows="1" v-model="form.desc"></el-input>
                    </el-col>
                    <el-col :span="1">&nbsp;&nbsp;阈值：  </el-col>
                    <el-col :span="2">
                        <el-input type="textarea2" rows="1" v-model="form.desc2"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item label="模型对比" prop="delivery4">
                    <el-col :span="2">
                        <el-switch v-model="form.delivery4"></el-switch>
                    </el-col>
                    <el-col :span="2">目标检测对比  </el-col>
                    <el-col :span="2">
                        <el-switch v-model="form.delivery5"></el-switch>
                    </el-col>
                    <el-col :span="2">检测原图  </el-col>
                    <el-col :span="2">
                        <el-switch v-model="form.delivery6"></el-switch>
                    </el-col>
                </el-form-item>
                
            </el-form>
            <el-form-item>
                <el-button type="primary" @click="submitForm">确认</el-button>
                <el-button @click="resetForm">重置</el-button>
            </el-form-item>
        </div>

        <div class="container">
            <div class="content-title">结果展示</div>
            <el-form-item>
                    <el-button type="primary" @click="refreshImage">刷新</el-button>
                    <el-button @click="openExplorer">在文件管理器中打开</el-button>
                </el-form-item>
            <div class="demo-image__preview">
                <el-image
                v-loading="loading"
                style="width: 1000px; height: 800px"
                :src="currentImage"
                :preview-src-list="srcList"
                :initial-index="0"
                fit="contain"
                />
            </div>
        </div>

        <!-- style="width: 1000px; height: 1000px" -->

        <el-dialog v-model="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="" />
        </el-dialog>
    </div>
</template>

<script>
import axios from "axios";
import { ElMessage } from "element-plus";

export default {
    data() {
        return {
            loading: false,
            url: '',
            srcList: [
                // 'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
                // 'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
                // 'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
                // 'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
                // 'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
                // 'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
                // 'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg',
            ],
            fileList: [],
            dialogImageUrl: "",
            dialogVisible: false,
            fileParam: "",
            form: {
                delivery: true,
                delivery2: true,
                delivery3: true,
                delivery4: false,
                delivery5: false,
                delivery6: false,

                region: 1024,
                region2: "LOL_v2_synthetic",
                region3: "yolov8n.pt",

                desc: 640,
                desc2: 0.5,
            },
        };
    },
    created() {
        axios
            .get("http://127.0.0.1:5000/get-picture/")
            .then((response) => {
                response.data.forEach(element => {
                    console.log(element)
                    this.fileList.push(element)
                });
                // console.log(response.data);
                // this.fileList.push(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
        axios
            .get("http://127.0.0.1:5000/get-last-result/")
            .then((response) => {
                this.srcList = []

                response.data.forEach(element => {
                    console.log(element)
                    this.srcList.push(element)
                })
                url = srcList[0]
            })
            .catch((error) => {
                console.log(error)
            })
    },
    mounted() {
        // 运行时再启用
        setInterval(this.getSignal, 3000)
    },
    computed: {
        currentImage() {
            return this.srcList[0]
        }
    },
    methods: {
        getSignal() {
            axios
            .get("http://127.0.0.1:5000/get-signal/")
            .then((response) => {
                response.data.forEach(element => {
                    // console.log(element)
                    switch (element) {
                        case 'none':
                            break;
                        case 'start':
                            this.loading = true;
                            ElMessage.success('正在处理……');
                            break;
                        case 'end':
                            this.loading = false;
                            ElMessage.success('处理完成！');
                            this.refreshImage();
                            // url = this.srcList[0];
                            break;
                        case 'running':
                            break;
                    }
                })
            })
            .catch((error) => {
                console.log(error)
            })
        },
        openExplorer() {
            var tmp_data = {
                todo: 'open-last'
            }
            axios
                .post("http://127.0.0.1:5000/do-sth/", tmp_data)
                .then((response) => {
                    console.log(response);
                    // this.fileList = [];
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        refreshImage() {
            axios
            .get("http://127.0.0.1:5000/get-last-result/")
            .then((response) => {
                this.srcList = []

                response.data.forEach(element => {
                    console.log(element)
                    this.srcList.push(element)
                })
                url = srcList[0]
            })
            .catch((error) => {
                console.log(error)
            })
        },
        beforeRemove(file, fileList) {
            console.log(file["file_name"])
            var imageInfo = {
                filename: file["file_name"],
                // 其他图像信息...
            };

            // 发送图像信息到后端
            this.sendImageInfoToBackend(imageInfo);
        },
        handleRemove(file, fileList) {
            console.log(file["file_name"])
            var imageInfo = {
                filename: file["file_name"],
                // 其他图像信息...
            };

            // 发送图像信息到后端
            this.sendImageInfoToBackend(imageInfo);

            // console.log(file, fileList);
        },
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },
        handleChange(file, fileList) {
            this.fileParam = new FormData(); // 创建form对象
            this.fileParam.append("file", file["raw"]);
            this.fileParam.append("fileName", file["name"]);

            // 尝试直接 change 时插入
            axios
                .post("http://127.0.0.1:5000/save-picture/", this.fileParam)
                .then((response) => {
                    console.log(response);
                    // this.fileList = [];
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        sendImageInfoToBackend(imageInfo) {
            console.log(imageInfo)
            // 使用 axios 或其他 HTTP 请求库发送 POST 请求到后端
            // 例如：
            axios.post('http://127.0.0.1:5000/del-picture/', imageInfo)
              .then(response => {
                console.log('图像信息已发送到后端');
              })
              .catch(error => {
                console.error('发送图像信息时出错：', error);
              });
        },
        submitForm() {
        // 表单提交逻辑
        this.$refs.formRef.validate(valid => {
            if (valid) {
                // 表单验证通过，执行提交操作
                axios.post('http://127.0.0.1:5000/set-args/', this.form)
                console.log('表单数据：', this.form);
            } else {
                console.log('表单验证失败');
            }
        });
        },
        resetForm() {
        // 重置表单
            this.$refs.formRef.resetFields();
        },

    },
};
</script>

<style scoped>
/* .mgb20 {
	margin-bottom: 20px;
} */

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

.demo-image__error .image-slot {
  font-size: 30px;
}
.demo-image__error .image-slot .el-icon {
  font-size: 30px;
}
.demo-image__error .el-image {
  width: 100%;
  height: 200px;
}
</style>
