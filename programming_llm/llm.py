from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.agents import initialize_agent

from llama_index import GPTSimpleVectorIndex

index = GPTSimpleVectorIndex.load_from_disk('./indices/programming_index.json')

tools = [
    Tool(
        name="GPT index",
        func=lambda q: str(index.query(q)),
        description="useful for when you want generate code for your application. The input to this tool should be a complete english sentence with code",
        return_direct=True 
    )
]

memory = ConversationBufferMemory(memory_key="chat_history")

llm=OpenAI(
        temperature=1,
        model_name="gpt-3.5-turbo",
        presence_penalty=0,
        frequency_penalty=0
    )
agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", memory=memory)

def run(query):
    try:
        return agent_chain.run(input=query) 
    except Exception as e:
        print(e)
        return "Error occured."

