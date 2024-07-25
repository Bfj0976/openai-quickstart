# 作业
### Day1: 总结：[7-22 homework.json](7-22%20homework.json)

### Day2：
#### 1. GPT-4V的使用   代码：[gpt-4v.ipynb](openai_api/gpt-4v.ipynb)
##### 1.1 上传自己手写的图片到images文件夹，可命名为gpt-4v.jpg；![gpt-4v.jpg](openai_api/images/gpt-4v.jpg)
##### 1.2 修改query_base64_image_description的方法描述，分析gpt-4v.jpg图片；![img.png](homework_images/1.1.png)
##### 1.3 输出分析结果，并使用函数对输出进行渲染，渲染成Markdown格式使结果更易读；![img.png](homework_images/1.3.png)
#### 2. ai translator的使用   代码：[main.py](openai-translator/ai_translator/main.py) [argument_parser.py](openai-translator/ai_translator/utils/argument_parser.py)
##### 2.1 ai translator中，添加2种以上的其他语言对翻译
![img.png](homework_images/korean.png)
![img.png](homework_images/japanese.png)
#### 3. 扩展langchain chains 
##### 3.1 扩展chains，使其支持生物、计算机和汉语文学老师等学科的提示词模板及对应 Chains问答。
代码：[router_chain.ipynb](langchain/jupyter/chains/router_chain.ipynb)

### Day3：
#### 1. 实战sales chatbot
##### 1.1 自行生成一个新的产品介绍知识库，可搜索使用一个产品的行业数据，也可自建一个产品的真实数据。参考“房产销售聊天机器人”，开发一个“**销售聊天机器人”；
知识库：[real_estate_sales_data.txt](langchain/byd_sales_chatbot/real_estate_sales_data.txt)
##### 1.2 在"**销售聊天机器人"中，使用向量数据库进行检索回答，如果向量数据库检索不到问题答案时，能够通过一个prompt来回答这个问题，而不是直接告诉用户我是一个AI机器人。
代码： [sales_chatbot.py](langchain/byd_sales_chatbot/sales_chatbot.py)
##### 1.3 请在openai-quickstart/langchain/sales_chatbot同级目录，新建一个"**_sales_chatbot"文件夹，并以这个文件夹作为该实战项目的目录。
代码： [byd_sales_chatbot](langchain/byd_sales_chatbot)
![img.png](homework_images/sales.png)