<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 380px">
					<template #header>
						<div class="clearfix">
							<span>数据集介绍</span>
						</div>
					</template>
					<div>
						<ul>
							<li>BDD100K 论文：<el-link type="primary" href="https://arxiv.org/pdf/1805.04687v2">A Diverse Driving Dataset for Heterogeneous Multitask Learning</el-link></li>
							<li>一个大规模、多样化的驾驶视频数据集</li>
							<li>伯克利大学AI实验室（BAIR）发布的目前最大规模、内容最具多样性的公开驾驶数据集，同时设计了一个图片标注系统</li>
							<li>包含10万段高清视频，每个视频约40秒，720p，30 fps 。每个视频的第10秒对关键帧进行采样，得到10万张图片（图片尺寸：1280 * 720 ），并进行标注</li>
						</ul>
                        <!-- <template> -->
                            <el-table :data="tableData" stripe > 
                                <el-table-column prop="date" label="名称" />
                                <el-table-column prop="count" label="数量" />
                                <el-table-column prop="split" label="训练 / 测试" />
                                <el-table-column prop="size" label="尺寸" />
                            </el-table>
                        <!-- </template> -->
						
					</div>
				</el-card>
				<el-card shadow="hover" class="mgb20" style="height: 570px">
					<div style="margin-bottom: 20px;"><center><b>在白天图像上的训练权重结果（用于暗光增强效果的评估）</b></center></div>
					<!-- <div class="zhexianWrap">
						<div ref="ec-bar" id="ec-bar"></div>
					</div> -->
					<el-image width= 400px height=200px :src="img_pr" fit="contain" title="由 40K 张白天图像训练出的目标检测权重 PR 曲线"/>
					<ul>
						<li>此外，使用该权重在 1K 张暗光图像测试集上的准确率达到 63%(car)</li>
					</ul>
				</el-card>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 970px">
					<template #header>
						<div class="clearfix">
							<span>数据集展示</span>
						</div>
					</template>
					<div>
						<ul>
							<li>BDD100K：官方给出的数据集展示，包含各种应用场景</li>
						</ul>
						<el-image width= 400px height=200px :src="img_bdd100k" fit="contain" title="BDD100K 数据集官方展示"/>
                        <ul>
							<li>用于目标检测的数据（白天）及其标注 label</li>
						</ul>
						<el-image width= 400px height=200px :src="img_label" fit="contain" title="用于目标检测的数据和标签"/>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import img_bdd100k from '../../assets/img/teaser.gif'
import img_label from '../../assets/img/bdd_label.jpg'
import img_pr from '../../assets/img/PR_curve.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'BDD100K',
    count: '100K',
    split: '80K(labeled) train:val:test=8:1:1',
    size: '1280x720',
  }
]

onMounted(() => {
    // drawEcharts();
})

const drawEcharts = () => {
    var newChart = echarts.init(document.getElementById('ec-bar'));
    var new_option = {
		title: {
			// text: 'ECharts 入门示例'
			subtext: 'PSNR',
			left: 48,
			top: 0
		},
		tooltip: {
			trigger: "axis",
			confine: true,
		},
		legend: {
			data:['LOL_v1', 'LOL_v2_real', 'LOL_v2_synthetic']
		},
		xAxis: {
			type: "category",
			data: ["DeepUPE","MIRNet","SNR-Net","Restromer","Retinexformer"],
			axisLabel: {
            // 设置x轴下方文字的样式
            textStyle: {
              show: true,
            //   color: "#BDBDBD",
              fontSize: "12",
            },
          },
		  axisLine: {
            show: true,
            lineStyle: {
              // 设置x轴线条的样式
            //   color: "#BDBDBD",
              width: 1,
              type: "solid",
            },
          },
		},
		yAxis: {
			type: "value",
			splitNumber: 6, //设置坐标轴的分割段数
            // splitLine: {
            //   //去除网格线
            //   show: true,
            // },
            axisLine: {
              //y轴线的颜色以及宽度
              show: true,
              lineStyle: {
                // color: "#BDBDBD",
                width: 1,
                type: "solid",
              },
            },
            axisLabel: {
              // 设置y轴的文字的样式
              textStyle: {
                show: true,
                // color: "#BDBDBD",
                fontSize: "12",
              },
            },
		},
		series: [
			{
			name: 'LOL_v1',
			type: 'bar',
			data: [14.38, 24.14, 24.61, 22.43, 25.16]
		},
		{
			name: 'LOL_v2_real',
			type: 'bar',
			data: [13.27, 20.02, 21.48, 19.94, 22.80]
		},
		{
			name: 'LOL_v2_synthetic',
			type: 'bar',
			data: [15.08, 21.94, 24.14, 21.41, 25.67]
		}
	],
		grid: {
          // 位置
          show: true,
          x: 48,
          y: 24,
          x2: 48,
          y2: 26, // 6
          borderWidth: 0, // 去除图表的边框
        },
	};

	// 使用刚指定的配置项和数据显示图表。
	newChart.setOption(new_option);
}

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

.zhexianWrap {
  width: 100%;
  height: 300px;
  overflow: hidden; /*解决鼠标移除echarts图以后出现滚动条问题*/
  #ec-line {
    width: 100%;
    height: 100%;
  }
  #ec-bar {
	width: 100%;
	height: 100%;
  }
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
