# Langchain Custom Chatbot

This project is a custom chatbot built using **Langchain**, **Flask**, and **Hugging Face models**. It extracts data from a website, creates embeddings, and provides a RESTful API for conversation.

## Features
- Extracts data from a website using Langchain's `WebBaseLoader`.
- Creates embeddings using Hugging Face's `sentence-transformers`.
- Stores embeddings in a FAISS vector store.
- Provides a Flask API to handle user queries.

## Requirements
- Python 3.8+
- Libraries: `langchain`, `flask`, `flask-restful`, `requests`, `beautifulsoup4`, `sentence-transformers`, `faiss-cpu`, `langchain-community`, `langchain-huggingface`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/langchain-chatbot.git
   cd langchain-chatbot
Create a virtual environment:

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install the required libraries:

pip install -r requirements.txt
Usage
Extract data from the website:

python extract_data.py
Create embeddings and store them in a vector store:

python create_embeddings.py
Run the Flask API:
python app.py

Test the API using Postman or curl:
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "What courses are available?"}'

API Endpoint
POST /chat: Send a JSON payload with {"message": "Your question here"}.
Example Response
{
  "response": "The available courses are: 1. Python for Beginners, 2. Advanced Python Programming, 3. Data Science with Python."
}
