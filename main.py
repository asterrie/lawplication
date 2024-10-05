from llama_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain_core import BaseCache, OpenAI
import sys
import os

os.environ["OPENAI_API_KEY"] = ""

def creativeVectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size )

    #define LLM
    llmpredictor = LLMPredictor(llm = OpenAI(temperature = 0, model_name = "gpt-4o-mini", max_tokens = tokens))

    #loading data
    docs = SimpleDirectoryReader(path).load_data()

    #create vector index
    vectorIndex = GPTSimpleVectorIndex(documents = docs, llmpredictor = LLMPredictor, prompt_helper = prompt_helper)
    vectorIndex.save_to_disk(vectorIndex.json)
    return vectorIndex

    vectorIndex = creativeVectorIndex('knowledge')

def answerME(vectorIndex):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    while True:
        prompt = input('Please ask: ')
        response = vIndex.query(prompt, response_mode = "compact")
        print(f"Response: {response} \n")

    answerME(vectorIndex.json)
