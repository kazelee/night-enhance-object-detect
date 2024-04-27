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
							<li>ExDark 论文：<el-link type="primary" href="https://arxiv.org/pdf/1808.04560v1.pdf">Getting to Know Low-light Images with The Exclusively Dark Dataset</el-link></li>
							<li>收集了 7,363 张从极低光照环境到黄昏（即 10 种不同条件）的低光图像</li>
							<li>其中 12 个对象类别（类似于 PASCAL VOC）在图像类别级别和局部对象边界框中进行了注释</li>
							<li>包括:自行车、船只、瓶子、公交车、汽车、猫、椅子、杯子、狗、摩托车、人和桌子等对象</li>
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
				<el-card shadow="hover" class="mgb20" style="height: 450px">
					<div style="margin-bottom: 20px;"><center><b>以往的模型 与 我们的模型 在部分目标上的检测率比较</b></center></div>
					<div class="zhexianWrap">
						<div ref="ec-bar" id="ec-bar"></div>
					</div>
					
				</el-card>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="height: 850px">
					<template #header>
						<div class="clearfix">
							<span>数据集展示</span>
						</div>
					</template>
					<div>
						<ul>
							<li>ExDark：针对目标检测方向，在暗光条件下拍摄的多种对象数据集</li>
						</ul>
						<el-image width= 400px height=200px :src="img_exdark1" fit="contain" title="ExDark 数据集示例"/>
						<el-image width= 400px height=200px :src="img_exdark2" fit="contain" title="ExDark 数据集示例"/>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import img_exdark1 from '../../assets/img/exdark1.png'
import img_exdark2 from '../../assets/img/exdark2.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'ExDark',
    count: '7363',
    split: 'none',
    size: '不规则',
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
			subtext: 'PR',
			left: 48,
			top: 0
		},
		tooltip: {
			trigger: "axis",
			confine: true,
		},
		legend: {
			data:['Bicycle', 'Boat', 'Car', 'Cat', 'People']
		},
		xAxis: {
			type: "category",
			data: ["RetinexNet","MIRNet","SNR-Net","Restromer","Retinexformer"],
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
			min: 0, // 最大值和最小值要从后端获取，或者写死数值，或者不去自定义最大最小值
            max: 100,
            splitNumber: 5, //设置坐标轴的分割段数
            axisLabel: {
              formatter: function (v: number) {
                return v.toFixed(1); //0表示保留小数为0位，1表示1位，2表示2位
              },
            },
            axisLine: {
              //y轴线的颜色以及宽度
              show: true,
              lineStyle: {
                // color: "#BDBDBD",
                width: 1,
                type: "solid",
              },
            },
		},
		// data: ["RetinexNet","MIRNet","SNR-Net","Restromer","Retinexformer"],
		series: [
			{
			name: 'Bicycle',
			type: 'bar',
			data: [73.8, 71.8, 75.3, 76.2, 76.3]
		},
		{
			name: 'Boat',
			type: 'bar',
			data: [62.8, 63.8, 64.4, 65.1, 66.7]
		},
		{
			name: 'Car',
			type: 'bar',
			data: [80.8, 71.1, 77.5, 76.3, 77.6]
		},
		{
			name: 'Cat',
			type: 'bar',
			data: [53.4, 58.8, 59.1, 59.2, 61.2]
		},
		{
			name: 'People',
			type: 'bar',
			data: [65.9, 68.8, 69.1, 68.6, 69.5]
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
  height: 350px;
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
