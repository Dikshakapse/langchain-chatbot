from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import os

app = Flask(__name__)
api = Api(app)

# Load the vector store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Initializing the LLM 
huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not huggingfacehub_api_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable is not set.")

llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    huggingfacehub_api_token=huggingfacehub_api_token,
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

class Chatbot(Resource):
    def post(self):
        data = request.get_json()
        user_input = data.get("message")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400
        
        response = qa_chain.run(user_input)
        return jsonify({"response": response})

api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)