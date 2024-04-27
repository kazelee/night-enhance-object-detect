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
							<li>SID 论文：<el-link type="primary" href="https://paperswithcode.com/paper/learning-to-see-in-the-dark">Learning to See in the Dark</el-link></li>
							<li>SMID 论文：<el-link type="primary" href="https://paperswithcode.com/paper/seeing-motion-in-the-dark">Seeing Motion in the Dark</el-link></li>
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
							<li>SID：拍摄日间场景，通过不同曝光时长获取不同暗度的图像</li>
						</ul>
						<el-image width= 400px height=200px :src="img_sid" fit="contain" title="SID 数据集示例"/>
                        <ul>
							<li>SMID：在暗光场景下使用长短曝光拍摄一批视频，并采样成图片</li>
						</ul>
						<el-image width= 400px height=200px :src="img_smid" fit="contain" title="SMID 数据集示例"/>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import img_sid from '../../assets/img/sid.png'
import img_smid from '../../assets/img/smid.png'

let echarts = inject<any>('echarts');

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const tableData = [
  {
    date: 'SID',
    count: '5094',
    split: '70%(train) 20%(test) 10%(val)',
    size: '4200x2832(Sony) 6000x4000(Fuji)',
  },
  {
    date: 'SMID',
    count: '202x101',
    split: '64%(train) 12%(val) 24%(test)',
    size: '5456x3672',
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
			data:['SID', 'SMID']
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
			name: 'SID',
			type: 'bar',
			data: [17.01, 20.84, 22.87, 22.27, 24.44]
		},
		{
			name: 'SMID',
			type: 'bar',
			data: [23.91, 25.66, 28.49, 26.97, 29.15]
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
