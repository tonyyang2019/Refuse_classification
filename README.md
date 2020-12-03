# Refuse_classification
各大城市开始执行垃圾分类，但垃圾分类过于复杂，所以用机器来代替人们分类。

## 运行环境
+ python3.7
+ requests
+ base64
+ tkinter
+ 保持网络连接

## 项目介绍
这个项目不需要使用本地神经网络，所以并没有训练模型这个步骤，我们使用的是百度API和天行数据API，进行两个重要步骤的处理
百度API用来做物体识别
天行数据API用来做垃圾分类

## 项目文件
这个项目有两个文件，refuse_classification.py和UI.py
refuse_classification.py是主要处理程序
UI.py是窗口可视化程序

## 如果运行（默认你网络已经通了）
1. 下载这个网页的内容（refuse_classification.py和UI.py）
2. 注册百度账号，登录百度智能云，打开图像识别，在控制器中添加应获取应用id和key（>>https://ai.baidu.com/tech/imagerecognition/general）
3. 注册天行数据账号，登录，获取id（>>https://www.tianapi.com/apiview/97#viewerrorcode）
4. 把百度的id和key放进refuse_classification.py的19行，天行数据的放进47行
5. 运行UI.py点击识别，选择图片就可以看见结果了
