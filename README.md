# AI Chatbot Agent

This project is an AI chatbot built using FastAPI, LangGraph and Streamlit.

It supports:
- Groq models
- OpenAI models
- Optional web search using Tavily

The backend handles the AI agent logic and API routes.
The frontend provides an interactive UI using Streamlit.

---

# Project Structure

ai_agent.py → LangGraph agent logic  
backend.py → FastAPI backend server  
frontend.py → Streamlit frontend  
requirements.txt → Dependencies  

---

# Setup Instructions

## Step 1: Create Virtual Environment

```
python -m venv venv
```

## Step 2: Activate Environment

Windows:
```
venv\Scripts\activate
```

## Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root folder and add:

```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# Running the Application

## 1. Start Backend

```
python backend.py
```

Backend runs at:

```
http://127.0.0.1:9999
```

Swagger documentation:

```
http://127.0.0.1:9999/docs
```

---

## 2. Start Frontend

Open a new terminal and run:

```
streamlit run frontend.py
```

Frontend runs at:

```
http://localhost:8501
```

---

# Important

- Backend must be running before starting frontend.
- API keys are required for model responses.
- Use separate terminals for backend and frontend.

---

# What I Implemented

- Integrated LangGraph agent with tool support
- Added support for Groq and OpenAI models
- Built FastAPI backend with dynamic model selection
- Built Streamlit frontend with chat interface
- Added optional web search toggle
- Connected frontend and backend using REST API

---

Author  
Nagendra Babu Karra
