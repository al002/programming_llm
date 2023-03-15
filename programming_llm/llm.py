from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

template = """
I want you to act as a {role}. I will describe a project details you will code project with thouse tools: {tech_stacks}. You should output different filename and content for its functionality. Do not write explanations. My frist request is "{query}".
"""

prompt = PromptTemplate.from_template(template)

ROLE = "Senior Frontend developer"
TECHS = "React, pnpm, Ant Design, Redux Toolkit, axios"
QUERY = "Create Pokemon App that lists pokemons with images that come from PokeAPI sprites endpoint"

# chat mode instance
chat = ChatOpenAI(temperature=0.7)

chatgpt_chain = LLMChain(
    llm=chat, 
    prompt=prompt, 
    verbose=True, 
)

output = chatgpt_chain.predict(role=ROLE, tech_stacks=TECHS, query=QUERY)
print(output)

def run(query, template):
    try:
        # prompt = ""
        # match template:
        #     case llm_pb2.TERMINAL:
        #         prompt = load_prompt(str(Path("programming_llm/prompt/terminal/prompt.json").resolve())).format()
        #     case _:
        #         prompt = query
        # logging.info(prompt)
        # return agent_chain.run(input=query)
        pass
    except Exception as e:
        print(e)
        return "Error occured."

