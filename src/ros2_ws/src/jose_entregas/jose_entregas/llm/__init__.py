from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import  RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from item_re_return import item_feedback

load_dotenv()

# load the document and split it into chunks
try:
    loader = TextLoader("./items.txt")
    documents = loader.load()

except:
    print("Arquivo não encontrado")

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

llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=512)
prompt = ChatPromptTemplate.from_template(template)


chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)
text = ""
for s in chain.stream("fazo?"):
    # print(text, end="", flush=True)
    text+=s
    if "<|im_end|>" in text:
        break

#print(text.removesuffix("<|im_end|>"))

print(item_feedback(text))