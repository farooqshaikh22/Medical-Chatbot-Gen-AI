![Screenshot (4)](https://github.com/farooqshaikh22/Medical-Chatbot-Gen-AI/assets/127769353/4ca80cee-ff29-4641-8662-2a3b7771ffe3)

# Overview
The *Medical Chatbot Gen AI* project leverages advanced natural language processing and vector embedding technologies to provide intelligent responses to medical-related queries. Built using cutting-edge tools such as Hugging Face's Sentence Transformers and Pinecone's vector database, this chatbot is designed to offer accurate and context-aware information to users.

## Features
- **Robust PDF Data Extraction**: The chatbot extracts valuable medical information from PDF documents, enabling a comprehensive knowledge base.

- **Efficient Text Chunking**: Utilizing recursive character-based text splitting, the extracted data is organized into manageable chunks, facilitating efficient processing.

- **Powerful Embeddings with Sentence Transformers**: The chatbot employs Hugging Face's Sentence Transformers for embeddings, ensuring nuanced and contextually rich representations of textual content.

- **Intelligent Retrieval with Pinecone**: Leveraging Pinecone's vector database, the chatbot creates embeddings for text chunks and performs similarity searches to provide relevant and accurate responses.

- **Interactive User Interface**: Users can engage with the chatbot by inputting medical queries, receiving informative responses based on the embedded knowledge base.

## How to Use
1. **Installation**: Clone the repository and set up the required dependencies using the provided `requirements.txt` file.

2. **Run the Chatbot**: Execute the main script, and the chatbot will be ready to respond to medical queries.

3. **Ask Questions**: Input medical questions, and the chatbot will provide informative answers based on the embedded knowledge.

## Project Structure
- **data/**: Contains PDF documents with medical information.
- **model/**: Holds the pre-trained language model for contextual understanding.
- **src/**: Main source code files for the chatbot implementation.
