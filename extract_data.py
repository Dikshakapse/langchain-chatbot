from langchain_community.document_loaders import WebBaseLoader

# Set a User Agent string (optional but recommended)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Load data from the URL using WebBaseLoader
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
data = loader.load()

# Save the extracted data to a text file
with open("extracted_data.txt", "w", encoding="utf-8") as file:
    file.write(data[0].page_content)

print("Data extracted and saved to extracted_data.txt")