from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pinecone import Pinecone
from langchain.schema import (
    SystemMessage,
    HumanMessage
)

# Pinecone API Key
pc = Pinecone(api_key=input("Enter your Pinecone API Key: "))

# Pinecone Index Name
index = pc.Index(input("Enter your Pinecone Index Name: "))

# OpenAI Key
OPENAI_API_KEY = input("Enter your OpenAI API Key: ")

# Embedding Model
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# OpenAI Model
chat = ChatOpenAI(
    model="gpt-3.5-turbo-16k-0613"
)

# Get Context from Pinecone
def query_pinecone(query, top_k):
    vector_query = embeddings.embed_query(query)
    results = index.query(
            vector=vector_query,
            top_k=top_k,
            include_values=False,
            include_metadata=True
        )
    
    return results

# Format Prompt for OpenAI
def format_query(query, context, index):
    context = context.matches[index]["metadata"] # You can edit this path to fit your Pinecone record structure
    query = f"question: {query} context: {context}"
    query = f"Please generate an answer to the question by pulling information from the context. Question: {query} Context: {context}"
    return query

# System Message for OpenAI to customize tone and give rules
system = [
    SystemMessage(content="Formatting Guidelines:\n- Length: Maximum of 4 sentences\n- Tone: Professional, polite, clear and concise\n- You cannot add outside information to the answer")
]

# Enter your Question Here
question = input("Enter your Question: ")

retrieval = query_pinecone(question, top_k=3)
query = format_query(question, retrieval, 0)
prompt = HumanMessage(query)
system.append(prompt)

print(chat.invoke(system).content)
