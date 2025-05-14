# Nutrition RAG Chatbot

An interactive chatbot built on RAG principle that provides nutrition information and answers questions about food and dietary requirements. The chatbot uses LangChain and HuggingFace open-source models to process and respond to user queries about nutrition, which are free of charge.

## Features

- Interactive chat interface
- Document-based question answering
- Support for uploading nutrition-related documents
- Acceptable responses with source citations
- Temporary storage management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/NutritionChatbot.git
cd NutritionChatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root (if needed for API keys or configuration)

## Usage

1. Run the main application:
```bash
python main.py
```

2. Use the interface to:
   - Upload nutrition-related documents
   - Ask questions about nutrition
   - Get detailed answers with source citations
   - Clear the conversation history when needed

## Project Structure

- `main.py` - Main application entry point
- `ui.py` - User interface components
- `model.py` - LLM model configuration
- `vector_store.py` - Document storage and retrieval
- `documents.py` - Document processing utilities
- `config.py` - Configuration settings
- `text_utils.py` - Text processing utilities
- `file_utils.py` - File handling utilities

## Dependencies

- LangChain
- HuggingFace Transformers
- FAISS for vector storage
- IPython widgets for the interface
- Python-dotenv for environment management

## Contributing

Feel free to submit issues and enhancement requests!