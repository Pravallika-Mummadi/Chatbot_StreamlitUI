# Import necessary modules and classes
from langchain.llms import CTransformers
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from typing import Any, Dict, List, Union
import sys

# Define the model ID and configuration parameters
model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
config = {'temperature':0.00, 'context_length':8000,}

# Initialize the CTransformers object with the specified model and configuration
llm = CTransformers(model=model_id, 
                    model_type='mistral',
                    config=config,
                    )

prompt = PromptTemplate.from_template("you are an assistant answer the following : {query}")
chain = LLMChain(llm=llm,prompt=prompt)

# Define a function to generate AI responses based on the given query
def genai_engine(query):
    response = chain.run(query)
    return response