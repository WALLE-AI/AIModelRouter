# AIModelRouter
AI Lagrge models Router
# Feature
* 开发者集成 SDK包 支持Python TypeScript等主流的编程语言
* frontend
  * 登录与注册页面
  * 用户管理：
    * 模型管理
      * api_key创建、删除、隐藏、显示与复制等
      * 模型服务上key设置等
      * 默认模型与服务商设置
    * 模型可观测性：模型调度次数、tokens、模型趋势柱状图等
    * 用户画像
  * Model Hub
    * 左侧页面显示内容
      * 模型类别：embedding text audio 文生图、图生图等等
      * 右侧：模型卡片，主要介绍模型服务商、类型、体验按钮等
      * 点击模型卡片弹框：显示模型名称、服务商、toKens计费情况等
  * 模型体验页面：chat、audio和文本图/视频页面
* backend
  * 模型服务商配置，包括对应图表：参考dify model provider模块
  * OpenAI-Like接口统一，参考 AI getway 策略
  * 接口文档服务，前期参考fastapi做
* Python SDK 开发
  * 参考Ai getway,
* 开发周期
  * 一个月
# 参考
* https://github.com/Portkey-AI/gateway.git
* https://github.com/langgenius/dify.git  dify中模型路由
* https://openrouter.ai/
