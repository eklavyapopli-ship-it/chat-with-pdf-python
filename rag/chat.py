from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
# vector embedding
embedding_model= GoogleGenerativeAIEmbeddings(
      model="gemini-embedding-001",
)

vector_db = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)