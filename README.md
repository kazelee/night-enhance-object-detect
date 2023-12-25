# 强光分离/暗光增强目标检测系统

HFUT 领域方向设计 & 毕设选题：
- 基于暗光增强的夜间车辆识别系统设计与实现
- 基于光照分量分离的暗光增强系统设计与实现

## 参考项目

整合了以下项目（其中第一个项目只使用到了强光分离的部分）：
- [jinyeying/night-enhancement: [ECCV2022] "Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression", https://arxiv.org/abs/2207.10564](https://github.com/jinyeying/night-enhancement)
- [caiyuanhao1998/Retinexformer: "Retinexformer: One-stage Retinex-based Transformer for Low-light Image Enhancement" (ICCV 2023)](https://github.com/caiyuanhao1998/Retinexformer)
- [ultralytics/ultralytics: NEW - YOLOv8 🚀 in PyTorch > ONNX > OpenVINO > CoreML > TFLite](https://github.com/ultralytics/ultralytics)

注：本项目只保留了测试部分，训练部分请参考上述项目链接自行训练

## 环境部署

通过 `requirements.txt` 文件安装必要包（没有测试效果，可能会有遗漏）

从 `ClearLightEffect/results/delighteffects/model/` 下的文件 `delighteffects_params_0600000.pt.txt` 中的链接，下载模型并移动到同路径，参考下面的文件结构。

确保文件结构如下（必要文件已列出）：

```
├─basicsr
├─basicsr.egg-info     
├─ClearLightEffects
│  │  dataset.py
│  │  ENHANCENET.py
│  │  main_delighteffects.py
│  │  networks.py
│  │  utils.py
│  ├─light-effects // 1.1 强光分离数据集的临时位置
│  ├─output // 1.2 强光分离结果的临时位置
│  └─results
│     └─delighteffects
│         └─model
│                 delighteffects_params_0600000.pt
│                 delighteffects_params_0600000.pt.txt
├─data
│  └─Test
│      └─input // 2.1 暗光增强数据的临时位置
├─Enhancement
│     test_from_dataset.py
│     test_my_dataset.py
│     utils.py   
├─input // 0 输入的测试集
├─object_test // 3.1 目标检测数据的临时位置
├─object_weights
│      car_day_40k.pt
│      yolov8n.pt     
├─Options
│      RetinexFormer_Test.yml
├─output // 4 最终结果存储的位置，文件夹名称为测试的时间戳
├─pretrained_weights
│      FiveK.pth
│      LOL_v1.pth
│      LOL_v2_real.pth
│      LOL_v2_synthetic.pth
│      SDSD_indoor.pth
│      SDSD_outdoor.pth
│      SID.pth
│      SMID.pth
├─results
│  └─Test
│      └─RetinexFormer_Test // 2.2 暗光增强的结果临时位置
└─runs
   └─detect // 3.2 目标检测的结果临时位置：runs/detect/predict
```

## 测试运行

运行 `main_ui.py` 文件，通过用户界面操作。

注：可以直接将文件直接拖入文件列表框中，然后选择测试参数后，点击运行按钮测试
