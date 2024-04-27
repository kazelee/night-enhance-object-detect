<template>
    <div class="zhexianWrap">
      <div id="echartsBox"></div>
    </div>
  </template>
  
  <script>
  import Echarts from "echarts";
  export default {
    data() {
      return {
        myChart: null, // 定义变量用来存放echarts实例
        minData: 1,
        maxData: 10,
      };
    },
    mounted() {
      this.drawEcharts();
    },
    methods: {
      // 画图方法
      drawEcharts() {
        this.myChart = Echarts.init(document.getElementById("echartsBox"));
        this.myChart.setOption({
          tooltip: {
            trigger: "axis",
            confine: true, // 解决悬浮提示被遮住的问题
            formatter: function (params) {
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
                    ${params[i].data} ${i == 0 ? "km" : "min"}
                  </div>`;
              }
              return res; // 经过这么一加工，最终返回出去并渲染，最终就出现了我们所看的效果
            },
          },
          xAxis: {
            type: "category",
            data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
            axisLabel: {
              // 设置x轴下方文字的样式
              textStyle: {
                show: true,
                color: "#BDBDBD",
                fontSize: "12",
              },
            },
            axisLine: {
              show: true,
              lineStyle: {
                // 设置x轴线条的样式
                color: "#BDBDBD",
                width: 1,
                type: "solid",
              },
            },
          },
          yAxis: [
            {
              type: "value",
              splitNumber: 4, //设置坐标轴的分割段数
              splitLine: {
                //去除网格线
                show: false,
              },
              axisLine: {
                //y轴线的颜色以及宽度
                show: true,
                lineStyle: {
                  color: "#BDBDBD",
                  width: 1,
                  type: "solid",
                },
              },
              axisLabel: {
                // 设置y轴的文字的样式
                textStyle: {
                  show: true,
                  color: "#BDBDBD",
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
                  color: "#BDBDBD",
                  width: 1,
                  type: "solid",
                },
              },
              min: this.minData, // 最大值和最小值要从后端获取，或者写死数值，或者不去自定义最大最小值
              max: this.maxData,
              splitNumber: 6, //设置坐标轴的分割段数
              axisLabel: {
                formatter: function (v) {
                  return v.toFixed(1); //0表示保留小数为0位，1表示1位，2表示2位
                },
              },
            },
          ],
          legend: {
            data: ["跑步", "平板支撑"],
          },
          series: [
            {
              name: "跑步",
              yAxisIndex: 0, // 默认使用的是左侧的y轴 左侧的y轴yAxisIndex值为0
              data: [8.5, 7.2, 10, 9.5, 4, 6.6, 10],
              type: "line",
            },
            {
              name: "平板支撑",
              yAxisIndex: 1, // 指定使用右侧的y轴，也就是yAxisIndex为1即可
              data: [3.5, 4, 2.5, 5, 9.4, 1, 5],
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
            // 因为是两个y轴，所以title写成数组的形式，进行配置
            {
              // title为标题部分，有一级标题text，二级标题subtext。这里我们使用二级标题，再修改一下这个二级标题的位置即可出现我们想要的效果了，当然样式也可以通过title.subtextStyle去配置
              subtext: "公里数（km）",
              left: 48, // 距离左边位置
              top: 0, // 距离上面位置
              subtextStyle: {
                // 设置二级标题的样式
                color: "#BFBFBF",
              },
            },
            {
              // title为标题部分，有一级标题text，二级标题subtext。这里我们使用二级标题，再修改一下这个二级标题的位置即可出现我们想要的效果了，当然样式也可以通过title.subtextStyle去配置
              subtext: "分钟（min）",
              right: 48, // 距离左边位置
              top: -8, // 距离上面位置
              subtextStyle: {
                // 设置二级标题的样式
                color: "#BFBFBF",
              },
            },
          ],
          color: ["#ED837C", "#E8D095"], // 控制折线图的颜色
        });
        // 自适应
        window.addEventListener("resize", () => {
          this.myChart.resize();
        });
      },
    },
  };
  </script>
  <style lang="less" scoped>
  .zhexianWrap {
    width: 100%;
    height: 300px;
    overflow: hidden; // 解决鼠标移除echarts图以后出现滚动条问题
    #echartsBox {
      width: 100%;
      height: 100%;
    }
  }
  </style>