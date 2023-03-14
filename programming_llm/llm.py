import logging
from pathlib import Path
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.prompts import load_prompt

from llama_index import GPTSimpleVectorIndex
import llm_pb2

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

def run(query, template):
    try:
        # prompt = ""
        # match template:
        #     case llm_pb2.TERMINAL:
        #         prompt = load_prompt(str(Path("programming_llm/prompt/terminal/prompt.json").resolve())).format()
        #     case _:
        #         prompt = query
        # logging.info(prompt)
        return agent_chain.run(input=query)
    except Exception as e:
        print(e)
        logging.error(e)
        return "Error occured."

