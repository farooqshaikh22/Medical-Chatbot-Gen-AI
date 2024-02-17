from src.helper import load_pdf,text_split,download_huggingface_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

documents = load_pdf("data/")
text_chunks = text_split(documents)
embeddings = download_huggingface_embeddings()

#initializing pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)

index_name="medical-chatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks],
                                embeddings,
                                index_name=index_name)
