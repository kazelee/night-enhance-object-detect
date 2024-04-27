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
							<li>LOL_v1 论文：<el-link type="primary" href="https://arxiv.org/pdf/1808.04560v1.pdf">Deep Retinex Decomposition for Low-Light Enhancement</el-link></li>
							<li>LOL_v2_real 论文：<el-link type="primary" href="http://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_From_Fidelity_to_Perceptual_Quality_A_Semi-Supervised_Approach_for_Low-Light_CVPR_2020_paper.pdf">From Fidelity to Perceptual Quality</el-link></li>
							<li>LOL_v2_synthetic 论文：<el-link type="primary" href="https://ieeexplore.ieee.org/document/9328179">Sparse Gradient Regularized Deep Retinex Network</el-link></li>
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
				<el-card shadow="hover" class="mgb20" style="height: 410px">
					<div style="margin-bottom: 20px;"><center><b>以往的模型 与 我们的模型 在不同数据集上的 PSNR 值比较</b></center></div>
					<div class="zhexianWrap">
						<div ref="ec-bar" id="ec-bar"></div>
					</div>
					
				</el-card>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 810px">
					<template #header>
						<div class="clearfix">
							<span>数据集展示</span>
						</div>
					</template>
					<div>
						<ul>
							<li>LOL_v1：通过调整相机光圈，在日光场景下拍摄得到暗光图像</li>
						</ul>
						<el-image width= 400px height=200px :src="img_lolv1" fit="contain" title="LOL_v1 数据集示例"/>
                        <ul>
							<li>LOL_v2_real：在LOL_v1的基础上，增加不同色光和暗度</li>
						</ul>
						<el-image width= 400px height=200px :src="img_lolv2real" fit="contain" title="LOL_v2_real 数据集示例"/>
                        <ul>
							<li>LOL_v2_synthetic：通过对正常拍摄照片进行后期处理得到暗光图像</li>
						</ul>
						<el-image width= 400px height=200px :src="img_lolv2syn" fit="contain" title="LOL_v2_synthetic 数据集示例"/>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import img_lolv1 from '../../assets/img/lolv1.png'
import img_lolv2real from '../../assets/img/lolv2real.png'
import img_lolv2syn from '../../assets/img/lolv2syn.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'LOL_v1',
    count: '500',
    split: '485 / 15',
    size: '400x600',
  },
  {
    date: 'LOL_v2_real',
    count: '789',
    split: '689 / 100',
    size: '400x600',
  },
  {
    date: 'LOL_v2_synthetic',
    count: '1000',
    split: '900 / 100',
    size: '384x384',
  },
]

onMounted(() => {
    drawEcharts();
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
