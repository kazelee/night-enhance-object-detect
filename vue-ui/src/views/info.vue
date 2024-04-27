<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 410px">
					<template #header>
						<div class="clearfix">
							<span>强光分离模型</span>
						</div>
					</template>
					<div>
						<ul>
							<li>主要参考：<el-link type="primary" href="https://arxiv.org/pdf/2207.10564.pdf">Unsupervised Night Image Enhancement</el-link></li>
							<li>其他工作：优化数据缓存 GC 机制，使得大量图像数据在 CPU 上测试也可行</li>
						</ul>
						<el-image width= 400px height=200px :src="img_model1" fit="contain" title="强光分离模型结构图"/>
					</div>
				</el-card>
				<el-card shadow="hover" class="mgb20" style="height: 500px">
					<div style="margin-bottom: 10px;"><center><b>对光效应图像进行强光分离后的处理结果示例</b></center></div>
					<el-image width= 400px height=200px :src="img_demo1" fit="contain" title="强光分离效果展示"/>
					<el-image width= 400px height=200px :src="img_demo2" fit="contain" title="强光分离效果展示"/>
					
				</el-card>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 520px">
					<template #header>
						<div class="clearfix">
							<span>暗光增强模型</span>
						</div>
					</template>
					<div>
						<ul>
							<li>主要参考：<el-link type="primary" href="https://arxiv.org/abs/2303.06705">Retinexformer</el-link></li>
							<li>其他工作：使用更多的数据集进行训练测试，记录模型的结果</li>
						</ul>
						<el-image width= 400px height=200px :src="img_model2" fit="contain" title="暗光增强模型结构图"/>
					</div>
				</el-card>
				<el-card shadow="hover" class="mgb20" style="height: 390px">
					<div style="margin-bottom: 10px;"><center><b>不同数据权重下的暗光增强效果比较</b></center></div>
					<el-image width= 400px height=200px :src="img_demo3" fit="contain" title="暗光增强效果展示"/>
					
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import img_model1 from '../assets/img/model1.png'
import img_model2 from '../assets/img/model2.png'
import img_demo1 from '../assets/img/light-free-demo1.png'
import img_demo2 from '../assets/img/light-free-demo2.png'
import img_demo3 from '../assets/img/night-demo.png'

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

</script>

<style scoped>
ul {
	padding: 14px;
	/* margin: 10px; */
}
ul li {
	/* background-position: 0px 5px; */
	padding-left: 10px; 
	margin: 5px;
}

.el-link {
  margin-right: 8px;
  font-size: 16px;
}
.el-link .el-icon--right.el-icon {
  vertical-align: text-bottom;
}

.el-row {
	margin-bottom: 20px;
}

.grid-content {
	display: flex;
	align-items: center;
	height: 100px;
}

.grid-cont-right {
	flex: 1;
	text-align: center;
	font-size: 14px;
	color: #999;
}

.grid-num {
	font-size: 30px;
	font-weight: bold;
}

.grid-con-icon {
	font-size: 50px;
	width: 100px;
	height: 100px;
	text-align: center;
	line-height: 100px;
	color: #fff;
}

.grid-con-1 .grid-con-icon {
	background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
	color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
	background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
	color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
	background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
	color: rgb(242, 94, 67);
}

.user-info {
	display: flex;
	align-items: center;
	padding-bottom: 20px;
	border-bottom: 2px solid #ccc;
	margin-bottom: 20px;
}

.user-info-cont {
	padding-left: 50px;
	flex: 1;
	font-size: 14px;
	color: #999;
}

.user-info-cont div:first-child {
	font-size: 30px;
	color: #222;
}

.user-info-list {
	font-size: 14px;
	color: #999;
	line-height: 25px;
}

.user-info-list span {
	margin-left: 70px;
}

.mgb20 {
	margin-bottom: 20px;
}

.todo-item {
	font-size: 14px;
}

.todo-item-del {
	text-decoration: line-through;
	color: #999;
}

.schart {
	width: 100%;
	height: 300px;
}
</style>
