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
							<li>FiveK 来源：<el-link type="primary" href="https://data.csail.mit.edu/graphics/fivek/">MIT-Adobe FiveK Dataset</el-link></li>
							<li>由一组不同的摄影师用单反相机拍摄的 5,000 张照片组成</li>
							<li>都是 RAW 格式，即，相机传感器记录的所有信息都会被保留下来</li>
							<li>这些照片涵盖了广泛的场景、主题和照明条件</li>
							<li>目标结果图像由五名摄影专业的学生调整照片的色调得到</li>
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
					<div style="margin-bottom: 20px;"><center><b>以往的模型 与 我们的模型 在 FiveK 上的 PSNR 值和 FLOPS 值比较</b></center></div>
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
							<li>FiveK：对暗光图像进行拍摄，并由 5 名专业人员调整至正常效果</li>
						</ul>
						<el-image width= 400px height=200px :src="img_fivek1" fit="contain" title="FiveK 官方样例展示"/>
                        <ul>
							<li>补充：实际选用的数据集展示，其中白天暗光场景居多</li>
						</ul>
						<el-image width= 400px height=200px :src="img_fivek2" fit="contain" title="训练测试使用的 FiveK 数据集示例"/>
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
import img_fivek1 from '../../assets/img/fivek1.png'
import img_fivek2 from '../../assets/img/fivek2.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'FiveK',
    count: '5000',
    split: '4500 / 500',
    size: '无规则',
  },
]

onMounted(() => {
    drawEcharts();
})

const drawEcharts = () => {
    var newChart = echarts.init(document.getElementById('ec-bar'));
    var new_option = {
		title: [
			// {
			// 	text: '在暗光增强典型数据集 LOL-v1 上的处理结果'
			// },
          // 因为是两个y轴，所以title写成数组的形式，进行配置
          {
            // title为标题部分，有一级标题text，二级标题subtext。这里我们使用二级标题，再修改一下这个二级标题的位置即可出现我们想要的效果了，当然样式也可以通过title.subtextStyle去配置
            subtext: "PSNR",
            left: 48, // 距离左边位置
            top: 0, // 距离上面位置
            // subtextStyle: {
            //   // 设置二级标题的样式
            //   color: "#BFBFBF",
            // },
          },
          {
            // title为标题部分，有一级标题text，二级标题subtext。这里我们使用二级标题，再修改一下这个二级标题的位置即可出现我们想要的效果了，当然样式也可以通过title.subtextStyle去配置
            subtext: "FLOPS",
            right: 48, // 距离左边位置
            top: -8, // 距离上面位置
            // subtextStyle: {
            //   // 设置二级标题的样式
            //   color: "#BFBFBF",
            // },
          },
        ],
		tooltip: {
			trigger: "axis",
			confine: true,
		},
		legend: {
			data:['PSNR', 'FLOPS']
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
		yAxis: [
          {
            type: "value",
            splitNumber: 6, //设置坐标轴的分割段数
            // splitLine: {
            //   //去除网格线
            //   show: false,
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
          {
            type: "value",
            splitLine: {
              //去除网格线
              show: false,
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
            splitNumber: 6, //设置坐标轴的分割段数
            axisLabel: {
			// 设置y轴的文字的样式
			textStyle: {
                show: true,
                // color: "#BDBDBD",
                fontSize: "12",
              },
            },
          },
        ],
		series: [
			{
			name: 'PSNR',
			yAxisIndex: 0, // 默认使用的是左侧的y轴 左侧的y轴yAxisIndex值为0
			type: 'bar',
			data: [23.04, 23.73, 23.81, 24.13, 24.94]
		},
		{
			name: 'FLOPS',
			yAxisIndex: 1, // 指定使用右侧的y轴，也就是yAxisIndex为1即可
			type: 'bar',
			data: [21.10, 785.0, 26.35, 144.3, 15.57]
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
