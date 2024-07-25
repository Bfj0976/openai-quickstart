import gradio as gr

from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain import PromptTemplate
from openai import OpenAI



def initialize_sales_bot(vector_store_dir: str="real_estates_sale"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global SALES_BOT    
    SALES_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.8}))
    # 返回向量数据库的检索结果
    SALES_BOT.return_source_documents = True

    return SALES_BOT

def sales_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")
    # TODO: 从命令行参数中获取
    enable_chat = True

    ans = SALES_BOT({"query": message})
    # 如果检索出结果
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"]:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 如果未检索到相关文档，但大模型聊天模式已启用
    elif enable_chat:
        # 使用一个prompt来引导AI生成一个自然而非机器人式的回答
        prompt_template = PromptTemplate.from_template(
            "请以人类日常聊天的语气回答：{information}。注意：不要暴露自己是人工智能。当你不知道答案的时候，可以根据该问题自己杜撰一些答案，不要说不知道。回答的语言根据问题来，比如问题是英文，则用英文回答。"
        )
        full_prompt = prompt_template.format(information=message)
        print(full_prompt)
        dynamic_response = generate_ai_response(full_prompt)
        return dynamic_response
    # 否则输出套路话术
    else:
        return "这个问题我要问问领导"

def generate_ai_response(prompt):
    # 这里实现与AI模型的交互，根据prompt生成回答
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ],
            }
        ],
        max_tokens=300
    )
    ai_response = "这个问题我要问问领导"
    if response.choices:
        ai_response = response.choices[0].message.content
    return ai_response

def launch_gradio():
    demo = gr.ChatInterface(
        fn=sales_chat,
        title="比亚迪汽车销售",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    # 初始化比亚迪销售机器人
    initialize_sales_bot()
    # 启动 Gradio 服务
    launch_gradio()
