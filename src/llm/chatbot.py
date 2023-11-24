from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import  RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from item_re_return import item_feedback
import os

from log import getSysResponse, getUserPrompt

# load the document and split it into chunks
loader = TextLoader("./items.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="joseentregas")


chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)
text = ""
userInput = input()
for s in chain.stream("Torata onde está?"):
    # print(text, end="", flush=True)
    text+=s
    if "<|im_end|>" in text:
        break

#print(text.removesuffix("<|im_end|>"))

print(item_feedback(text))
print(text.removesuffix("<|im_end|>"))

with open('output.txt', 'w') as f:
    f.write(text.removesuffix("<|im_end|>"))


getUserPrompt(userInput)
#log de resposta do llm
getSysResponse(text.removesuffix("<|im_end|>"))
