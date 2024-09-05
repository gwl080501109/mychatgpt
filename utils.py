from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from http import HTTPStatus
from dashscope import Generation

# 设置API密钥
DASHSCOPE_API_KEY = "sk-7cb7535b25a54d5a8f3af0066af95fd3"
model = Tongyi(
        model_name="qwen-turbo",
        max_tokens=1024,
        top_p=1,
        tempareture=0,
        frequency_penalty=0,
        presence_penalty=0,
        api_key=DASHSCOPE_API_KEY
    )

def get_chat_response(prompt, memory):
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input":prompt})
    print(response)
    return response["response"]

# 修改后的 `get_chat_response_streaming` 函数，支持流式生成
def get_chat_response_streaming(prompt, memory):
    chain = ConversationChain(llm=model, memory=memory, streaming=True)

    # 返回一个生成器，逐步生成响应内容
    response_generator = chain.stream({"input": prompt})
    return response_generator


def call_with_stream(prompt, memory):
    # 获取历史消息
    history_messages = memory.chat_memory.messages  # 通过 chat_memory 获取历史消息
    print("history_messages:", history_messages)
    # 将历史消息中的 'ai' 角色改为 'assistant'

    formatted_messages = []
    for msg in history_messages:
        if msg['role'] == 'ai':
            formatted_messages.append({'role': 'assistant', 'content': msg['content']})
        else:
            formatted_messages.append({'role': msg['role'], 'content': msg['content']})

    # 调用模型，启用流式输出
    responses = Generation.call(
        model='aquilachat-7b',
        api_key='sk-7cb7535b25a54d5a8f3af0066af95fd3',
        temperature=0.1,
        messages=formatted_messages,
        result_format='message',  # 设置结果为 "message" 格式
        stream=True,  # 启用流式输出
        incremental_output=True  # 设置增量输出
    )

    # 返回流式响应的生成器
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            yield response.output.choices[0]['message']['content']
        else:
            print(response)
            yield f"Error: {response.status_code}, {response.message}"
