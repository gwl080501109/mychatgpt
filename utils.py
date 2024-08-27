from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 设置API密钥
WENXIN_APP_Key = "oackgbiAt0I2PXRUzpaJP9E5"
WENXIN_APP_SECRET = "HTIF206MaMZFIXKTlm6JbhtDfmSCosjD"
DASHSCOPE_API_KEY = "sk-7cb7535b25a54d5a8f3af0066af95fd3"
model = Tongyi(
        model_name="qwen-turbo",
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        api_key=DASHSCOPE_API_KEY
    )

def get_chat_response(prompt, memory):
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input":prompt})
    print(response)
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("比尔盖茨是谁", memory))
# print(get_chat_response("我上一个问题问的是啥", memory))


