"""
Chat API endpoints for the LangGraph agent.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ai.chat_agent import LangGraphChatAgent

# Initialize the chat agent
try:
    chat_agent = LangGraphChatAgent()
except Exception as e:
    print(f"Warning: Could not initialize chat agent: {e}")
    chat_agent = None


# Define request/response models
class ChatMessage(BaseModel):
    """A single chat message."""

    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    """Request body for chat endpoint."""

    message: str
    history: Optional[List[ChatMessage]] = None


class ChatResponse(BaseModel):
    """Response body for chat endpoint."""

    response: str
    success: bool


# Create router
router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("/send", response_model=ChatResponse)
async def send_message(request: ChatRequest) -> ChatResponse:
    """
    Send a message to the chat agent and get a response.

    Args:
        request: ChatRequest with message and optional history

    Returns:
        ChatResponse with the agent's response
    """
    if not chat_agent:
        raise HTTPException(status_code=500, detail="Chat agent not initialized")

    try:
        # Process message with or without history
        if request.history:
            # Convert to list of dicts
            history_list = [
                {"role": msg.role, "content": msg.content} for msg in request.history
            ]
            response = chat_agent.chat_with_context(request.message, history_list)
        else:
            response = chat_agent.chat(request.message)

        return ChatResponse(response=response, success=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


@router.post("/search", response_model=ChatResponse)
async def search_query(query: str) -> ChatResponse:
    """
    Perform a web search through the agent.

    Args:
        query: Search query string

    Returns:
        ChatResponse with search results
    """
    if not chat_agent:
        raise HTTPException(status_code=500, detail="Chat agent not initialized")

    try:
        from ai.search_tool import web_search

        results = web_search.invoke({"query": query})
        return ChatResponse(response=results, success=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")


@router.get("/services/{service_type}", response_model=ChatResponse)
async def get_service_info(service_type: str) -> ChatResponse:
    """
    Get information about SeedStudio services.

    Args:
        service_type: Type of service (education, healthcare, agriculture, industry)

    Returns:
        ChatResponse with service information
    """
    if not chat_agent:
        raise HTTPException(status_code=500, detail="Chat agent not initialized")

    try:
        from ai.search_tool import seedstudio_services

        results = seedstudio_services.invoke({"service_type": service_type})
        return ChatResponse(response=results, success=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Service lookup error: {str(e)}")
