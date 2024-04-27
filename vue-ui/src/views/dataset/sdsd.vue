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
							<li>SDSD 论文：<el-link type="primary" href="https://paperswithcode.com/paper/seeing-dynamic-scene-in-the-dark-a-high">Seeing Dynamic Scene in the Dark</el-link></li>
							<li>通过无 ND 滤色板和有 ND 滤色板两种情况，分别拍摄同一个场景，前者作为正常光情况，后者作为暗光情况，拍摄得到视频，然后再采样帧作为图像</li>
							<li>对室内和室外两种场景分开，构造两个数据集 SDSD-indoor 和 SDSD-outdoor</li>
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
							<li>SDSD：对有无滤镜片拍摄的两组视频进行采样，包括室内和室外</li>
						</ul>
						<el-image width= 400px height=200px :src="img_sdsd" fit="contain" title="SDSD 数据集示例"/>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import img_sdsd from '../../assets/img/sdsd.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'SDSD-indoor',
    count: '70(video)',
    split: '12x30(train)',
    size: '1920x1080',
  },
  {
    date: 'SDSD-outdoor',
    count: '80(video)',
    split: '13x30(train)',
    size: '1920x1080',
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
			data:['SDSD-indoor', 'SDSD-outdoor']
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
			name: 'SDSD-indoor',
			type: 'bar',
			data: [21.70, 24.38, 29.44, 25.67, 29.77]
		},
		{
			name: 'SDSD-outdoor',
			type: 'bar',
			data: [21.94, 27.13, 28.66, 24.79, 29.84]
		},
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
