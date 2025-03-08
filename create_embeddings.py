from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load the extracted data
with open("extracted_data.txt", "r", encoding="utf-8") as file:
    text_data = file.read()

# Split the text into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_text(text_data)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(texts, embeddings)

# Save the vector store
vector_store.save_local("faiss_index")

print("Embeddings created and saved to faiss_index")