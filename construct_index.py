from langchain.llms import OpenAI
from llama_index import GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, SimpleDirectoryReader, download_loader

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()

# doc1 = SimpleDirectoryReader('data').load_data()
doc2 = loader.load_data(file='data/pdf/sicp.pdf')

max_input_size = 4096
num_outputs = 1024
max_chunk_overlap = 20
chunk_size_limit = 600

prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=num_outputs))

# index1 = GPTSimpleVectorIndex(doc1, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

index = GPTSimpleVectorIndex(doc2, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

# index1.set_text("Paul graham essay")
# index2.set_text("Structure and Interpretation of Computer Programs 2nd Edition")

# index = GPTListIndex([index1, index2])

index.save_to_disk("./indices/programming_index.json")
