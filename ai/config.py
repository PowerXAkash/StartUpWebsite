"""
Configuration file for API keys and URLs.
Store your API credentials here.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1")

# Search Tool Configuration (e.g., Google Search, DuckDuckGo, or custom API)
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "your-search-api-key-here")
SEARCH_API_URL = os.getenv("SEARCH_API_URL", "https://api.search.example.com")

# Model Configuration
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))

# Agent Configuration
AGENT_NAME = "SeedStudio AI Assistant"
AGENT_DESCRIPTION = "An intelligent AI agent for SeedStudio with web search capabilities"
