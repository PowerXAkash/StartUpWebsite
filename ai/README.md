# SeedStudio AI Chat Agent

A LangGraph-based intelligent chat agent with web search capabilities, integrated with OpenAI's GPT models.

## Features

- **LangGraph Integration**: State-based conversational AI using LangGraph
- **Web Search Tool**: Integrated search capabilities via DuckDuckGo (free, no API key required)
- **SeedStudio Services Lookup**: Quick access to information about SeedStudio AI solutions
- **Conversation History**: Maintains context across multiple message exchanges
- **FastAPI Integration**: Easy REST API endpoints for chat functionality

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Edit `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your-actual-openai-api-key
CHAT_MODEL=gpt-4  # or gpt-3.5-turbo
```

Get your OpenAI API key from: https://platform.openai.com/api-keys

### 3. File Structure

```
ai/
├── __init__.py           # Package initialization
├── config.py            # API configuration and environment variables
├── search_tool.py       # Search functionality (web search, SeedStudio services)
├── chat_agent.py        # LangGraph-based chat agent
└── README.md            # This file
```

## Usage

### Option 1: Use FastAPI Endpoints

Start the server:
```bash
python -m uvicorn main:app --reload
```

#### Chat Endpoint
```bash
curl -X POST "http://localhost:8000/api/chat/send" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me about your education AI solutions",
    "history": []
  }'
```

#### Search Endpoint
```bash
curl -X POST "http://localhost:8000/api/chat/search?query=artificial%20intelligence"
```

#### Services Lookup
```bash
curl -X GET "http://localhost:8000/api/chat/services/education"
```

### Option 2: Use Agent Directly

```python
from ai.chat_agent import LangGraphChatAgent

# Initialize agent
agent = LangGraphChatAgent()

# Single message
response = agent.chat("What AI solutions do you offer for healthcare?")
print(response)

# With conversation history
history = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"}
]
response = agent.chat_with_context("Tell me more", history)
print(response)
```

## Components

### config.py
Manages all API configuration through environment variables:
- OpenAI API key and model selection
- Search API configuration
- Agent settings (name, description, token limits)

### search_tool.py
Provides search capabilities:
- **web_search()**: General web search using DuckDuckGo
- **seedstudio_services()**: Information about SeedStudio's AI services
- Fallback knowledge base for offline functionality

### chat_agent.py
LangGraph-based agent with:
- State management (messages, search results, tool selection)
- Tool binding (web_search, seedstudio_services)
- Multi-turn conversation support
- Automatic tool invocation based on query needs

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/chat/send` | Send message to chat agent |
| POST | `/api/chat/search` | Perform web search |
| GET | `/api/chat/services/{type}` | Get service information |

## Environment Variables

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_API_URL=https://api.openai.com/v1
CHAT_MODEL=gpt-4

# Search Configuration (optional)
SEARCH_API_KEY=your-key
SEARCH_API_URL=https://api.search.example.com

# Agent Settings
MAX_TOKENS=2048
```

## Extending the Agent

### Add a New Tool

```python
from langchain_core.tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """Description of what the tool does."""
    return f"Result for {param}"

# In chat_agent.py, add to tools list:
tools = [web_search, seedstudio_services, my_custom_tool]
```

### Connect to Frontend Chatbot

Update the frontend chat to call the API:

```javascript
async function sendMessage(message) {
  const response = await fetch('/api/chat/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: message,
      history: conversationHistory
    })
  });
  return await response.json();
}
```

## Troubleshooting

**Issue**: "Chat agent not initialized"
- Ensure `OPENAI_API_KEY` is set in `.env`
- Check that langchain and openai packages are installed

**Issue**: Search results not working
- DuckDuckGo search is free and doesn't require API keys
- For custom search, configure `SEARCH_API_KEY` and `SEARCH_API_URL`

**Issue**: Slow responses
- Using `gpt-4` may have rate limits; try `gpt-3.5-turbo` for faster responses
- Adjust `MAX_TOKENS` to reduce response size

## Future Enhancements

- [ ] Add database for conversation persistence
- [ ] Implement RAG (Retrieval-Augmented Generation) for company knowledge base
- [ ] Add multi-language support
- [ ] Implement conversation caching for faster responses
- [ ] Add sentiment analysis
- [ ] Create admin dashboard for monitoring chat metrics
