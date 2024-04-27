<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="8">
				<el-card shadow="hover" class="mgb20" style="height: 252px">
					<div class="user-info">
						<el-avatar :size="120" :src="imgurl" />
						<div class="user-info-cont">
							<div class="user-info-name">{{ name }}</div>
							<div>{{ role }}</div>
						</div>
					</div>
					<div class="user-info-list">
						当前日期：
						<span>{{currentDate}}</span>
					</div>
					<div class="user-info-list">
						当前地点：
						<span>合肥</span>
					</div>
				</el-card>
				<el-card shadow="hover" style="height: 302px">
					<template #header>
						<div class="clearfix">
							<span>项目详情</span>
						</div>
					</template>
					<div>
						<ul>
							<li>模型架构主要参考了 ECCV 2022 论文 <el-link type="primary" href="https://arxiv.org/pdf/2207.10564.pdf">Unsupervised Night Image Enhancement</el-link>与 ICCV 2023 论文 <el-link type="primary" href="https://arxiv.org/abs/2303.06705">Retinexformer</el-link>架构</li>
							<li>项目基于 <el-link type="primary" href="https://pytorch.org/">PyTorch</el-link>和 <el-link type="primary" href="https://github.com/XPixelGroup/BasicSR">BasicSR</el-link>等工具库</li>
							<li>系统引入 <el-link type="primary" href="https://docs.ultralytics.com/">YOLOv8</el-link>目标检测作为测试结果评估参考</li>
							<li>后端基于 <el-link type="primary" href="https://flask.palletsprojects.com/en/3.0.x/">Flask</el-link>，前端基于 <el-link type="primary" href="https://cn.vuejs.org/">Vue</el-link>和 <el-link type="primary" href="https://element-plus.org/zh-CN/">Element Plus</el-link>实现界面交互和可视化</li>
							<!-- <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask</a> -->
						</ul>
					</div>
				</el-card>
			</el-col>
			<el-col :span="16">
				<el-card shadow="hover" style="height: 574px">
					<template #header>
						<div class="clearfix">
							<span>系统介绍</span>
							<!-- <el-button style="float: right; padding: 3px 0" text>添加</el-button> -->
						</div>
					</template>
					<div>
						<ul>
							<li><b>核心功能：</b>消除暗光图像过曝、光晕等光效应，同时增强暗光图像的亮度</li>
							<li><b>“项目介绍”标签页：</b>展示项目的模型构造，以及在此之上的优化工作</li>
							<li><b>“数据集介绍”标签页：</b>展示使用到的数据集，以及训练和测试的结果</li>
							<li><b>“测试运行”标签页：</b>用于用户上传暗光图像测试，得到处理后的结果</li>
						</ul>
						<!-- <img src="../assets/img/demo.png"/> -->
						<el-image width= 800px height=400px :src="demo_url" :fit="demo_fit" title="暗光图像增强前后效果对比示例"/>
					</div>
				
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="20">
			<el-col :span="12">
				<el-card shadow="hover">
					<!-- <div> -->
					<!-- <schart ref="bar" class="schart" canvasId="bar" :options="options"></schart> -->
					<div><center><b>以往的模型 与 我们的模型 在不同数据集上的 PSNR 值比较</b></center></div>
					<div class="zhexianWrap">
						<div ref="ec-bar" id="ec-bar"></div>
					</div>
					<!-- </div> -->
				</el-card>
				
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover">
					<div><center><b>近年来不同模型在暗光增强典型数据集 LOL_v2_real 上的处理结果</b></center></div>
					<div class="zhexianWrap">
						<div ref="ec-line" id="ec-line"></div>
					</div>
				</el-card>
				<!-- <el-card shadow="hover">
					<schart ref="line" class="schart" canvasId="line" :options="options2"></schart>
				</el-card> -->
				
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import Schart from 'vue-schart';
// import Echarts from 'echarts';
import { VueElement, defineComponent, onMounted, reactive, inject } from 'vue';
import imgurl from '../assets/img/img.jpg';
import demo_url from '../assets/img/demo.png';

let echarts = inject<any>('echarts');

const demo_fit = "contain";

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const date = new Date();
const year = date.getFullYear();
const month = date.getMonth() + 1;
const day = date.getDate();
const currentDate = `${year}-${month}-${day}`;

// var myChart = null;
// var minData = 1;
// var maxData = 10;

// const dom = document.getElementById('ec-line')!;
// const myChart = Echarts.init(dom);

const options = {
	type: 'bar',
	title: {
		text: '最近一周各品类销售图'
	},
	xRorate: 25,
	labels: ['周一', '周二', '周三', '周四', '周五'],
	datasets: [
		{
			label: '家电',
			data: [234, 278, 270, 190, 230]
		},
		{
			label: '百货',
			data: [164, 178, 190, 135, 160]
		},
		{
			label: '食品',
			data: [144, 198, 150, 235, 120]
		}
	]
};
const options2 = {
	type: 'line',
	title: {
		text: '在暗光增强典型数据集 LOL_v2_real 上的处理结果'
	},
	labels: ['6月', '7月', '8月', '9月', '10月'],
	datasets: [
		{
			label: 'PSNR',
			data: [234, 278, 270, 190, 230]
		},
		{
			label: '百货',
			data: [164, 178, 150, 135, 160]
		},
		{
			label: '食品',
			data: [74, 118, 200, 235, 90]
		}
	]
};

onMounted(() => {
	drawEcharts();
})

const drawEcharts = () => {
	// myChart = Echarts.init(document.getElementById("echartsBox"));
	var myChart = echarts.init(document.getElementById('ec-line'));
	var newChart = echarts.init(document.getElementById('ec-bar'));

    myChart.setOption({
        tooltip: {
          trigger: "axis",
          confine: true, // 解决悬浮提示被遮住的问题
          formatter: function (params: string | any[]) {
            var res =
              "<div style='padding:0 12px;height:24px;line-height:24px;'><p>" +
              params[0].name +
              " </p></div>";
            for (var i = 0; i < params.length; i++) {
              //因为是个数组，所以要遍历拿到里面的数据，并加入到tooltip的数据内容部分里面去
              res += `<div style="padding:0 12px;">
                  <span style="display:inline-block;margin-right:4px;border-radius:2px;width:10px;height:10px;background-color:${[
                    params[i].color, // 默认是小圆点，我们将其修改成有圆角的正方形，这里用的是模板字符串。并拿到对应颜色、名字、数据
                  ]};"></span>
                  ${params[i].seriesName}
                  ${params[i].data}
                </div>`;
				// ${i == 0 ? "km" : "min"}
            }
            return res; // 经过这么一加工，最终返回出去并渲染，最终就出现了我们所看的效果
          },
        },
        xAxis: {
          type: "category",
          data: ["input", "SID", "RetinexNet", "Restromer", "SNR-Net", "UL-ResNet", "Retinexformer"],
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
            min: 0, // 最大值和最小值要从后端获取，或者写死数值，或者不去自定义最大最小值
            max: 1,
            splitNumber: 5, //设置坐标轴的分割段数
            axisLabel: {
              formatter: function (v: number) {
                return v.toFixed(1); //0表示保留小数为0位，1表示1位，2表示2位
              },
            },
          },
        ],
        legend: {
          data: ["PSNR", "SSIM"],
        },
        series: [
          {
            name: "PSNR",
            yAxisIndex: 0, // 默认使用的是左侧的y轴 左侧的y轴yAxisIndex值为0
            data: [9.72, 13.24, 15.47, 19.94, 21.48, 25.51, 22.80],
            type: "line",
          },
          {
            name: "SSIM",
            yAxisIndex: 1, // 指定使用右侧的y轴，也就是yAxisIndex为1即可
            data: [0.18, 0.442, 0.567, 0.827, 0.849, 0.80, 0.840
			],
            type: "line",
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
            subtext: "SSIM",
            right: 48, // 距离左边位置
            top: -8, // 距离上面位置
            // subtextStyle: {
            //   // 设置二级标题的样式
            //   color: "#BFBFBF",
            // },
          },
        ],
        color: ["#ED837C", "#E8D095"], // 控制折线图的颜色
    });

	

	// 指定图表的配置项和数据
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
			data:['LOL_v1', 'LOL_v2_real', 'SID', 'FiveK']
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
			name: 'SID',
			type: 'bar',
			data: [17.01, 20.84, 22.87, 22.27, 24.44]
		},
		{
			name: 'FiveK',
			type: 'bar',
			data: [23.04, 23.73, 23.81, 24.13, 24.94]
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

	    // 自适应
		window.addEventListener("resize", () => {
        myChart.resize();
		newChart.resize();
      });
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
