from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOllama(model="mistral")  # or llama3, gemma, etc.

memory = ConversationBufferMemory()

chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def get_response(user_input):
    return chatbot.run(user_input)
