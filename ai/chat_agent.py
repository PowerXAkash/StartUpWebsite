"""
LangGraph-based chat agent with search capabilities.
This agent can process user queries, search for information, and provide responses.
"""

from typing import Any, Dict, List, TypedDict, Optional
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
import json

from ai.config import OPENAI_API_KEY, CHAT_MODEL, MAX_TOKENS, AGENT_NAME
from ai.search_tool import SearchTool


# Define the state structure for the agent
class AgentState(TypedDict):
    """State dictionary for the LangGraph agent."""

    messages: List[BaseMessage]
    search_results: Optional[List[Dict[str, str]]]
    current_tool: Optional[str]


# Initialize the search tool
search_tool = SearchTool()


@tool
def web_search(query: str) -> str:
    """
    Search the web for information.

    Args:
        query: The search query string

    Returns:
        Formatted search results as a string
    """
    results = search_tool.search(query)
    if not results or "error" in results[0]:
        return "Unable to search. Using local knowledge base."

    formatted_results = "\n".join(
        [f"- {r.get('title', '')}: {r.get('snippet', '')}" for r in results[:3]]
    )
    return f"Search results for '{query}':\n{formatted_results}"


@tool
def seedstudio_services(service_type: str) -> str:
    """
    Get information about SeedStudio services.

    Args:
        service_type: Type of service (education, healthcare, agriculture, industry)

    Returns:
        Formatted service information
    """
    service_info = search_tool.search_seedstudio_services(service_type)
    return json.dumps(service_info, indent=2)


class LangGraphChatAgent:
    """
    A LangGraph-based chat agent with search capabilities.
    Integrates with OpenAI LLM and search tools.
    """

    def __init__(self, model_name: str = CHAT_MODEL, api_key: str = OPENAI_API_KEY):
        """Initialize the chat agent."""
        self.model_name = model_name
        self.api_key = api_key

        # Initialize the LLM
        self.llm = ChatOpenAI(
            model=model_name,
            api_key=api_key,
            temperature=0.7,
            max_tokens=MAX_TOKENS,
        )

        # Bind tools to the LLM
        tools = [web_search, seedstudio_services]
        self.llm_with_tools = self.llm.bind_tools(tools)

        # Initialize the graph
        self.graph = self._build_graph()
        self.compiled_graph = self.graph.compile()

    def _build_graph(self) -> StateGraph:
        """Build the LangGraph state machine."""
        graph = StateGraph(AgentState)

        # Define nodes
        graph.add_node("chatbot", self._chatbot_node)
        graph.add_node("tools", self._tools_node)

        # Define edges
        graph.add_edge(START, "chatbot")
        graph.add_conditional_edges(
            "chatbot",
            self._should_use_tools,
            {
                "tools": "tools",
                "end": END,
            },
        )
        graph.add_edge("tools", "chatbot")

        return graph

    def _chatbot_node(self, state: AgentState) -> Dict[str, Any]:
        """Process messages and generate responses."""
        messages = state.get("messages", [])

        # Get response from LLM
        response = self.llm_with_tools.invoke(messages)

        # Add the assistant's response to messages
        messages.append(response)

        return {
            "messages": messages,
            "current_tool": None,
        }

    def _tools_node(self, state: AgentState) -> Dict[str, Any]:
        """Execute tool calls."""
        messages = state.get("messages", [])
        last_message = messages[-1]

        # Process tool calls
        if hasattr(last_message, "tool_calls"):
            for tool_call in last_message.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]

                # Execute the tool
                if tool_name == "web_search":
                    result = web_search.invoke(tool_args)
                elif tool_name == "seedstudio_services":
                    result = seedstudio_services.invoke(tool_args)
                else:
                    result = f"Unknown tool: {tool_name}"

                # Add tool result to messages
                messages.append(
                    ToolMessage(
                        content=result,
                        tool_call_id=tool_call["id"],
                    )
                )

        return {
            "messages": messages,
            "current_tool": None,
        }

    def _should_use_tools(self, state: AgentState) -> str:
        """Determine if tools should be used."""
        messages = state.get("messages", [])
        last_message = messages[-1]

        # Check if the last message contains tool calls
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return "end"

    def chat(self, user_message: str) -> str:
        """
        Process a user message and return the agent's response.

        Args:
            user_message: The user's input message

        Returns:
            The agent's response string
        """
        # Initialize state with the user message
        initial_state = {
            "messages": [HumanMessage(content=user_message)],
            "search_results": None,
            "current_tool": None,
        }

        # Run the compiled graph
        result = self.compiled_graph.invoke(initial_state)

        # Extract the last message (should be from assistant)
        final_messages = result.get("messages", [])
        if final_messages:
            last_message = final_messages[-1]
            if isinstance(last_message, AIMessage):
                return last_message.content
            elif isinstance(last_message, ToolMessage):
                # If last is tool result, get the previous AI message
                for msg in reversed(final_messages[:-1]):
                    if isinstance(msg, AIMessage):
                        return msg.content
        return "No response generated"

    def chat_with_context(
        self, user_message: str, history: List[Dict[str, str]]
    ) -> str:
        """
        Process a user message with conversation history.

        Args:
            user_message: The user's current input
            history: Previous messages in conversation

        Returns:
            The agent's response string
        """
        # Build message list from history
        messages = []
        for msg in history:
            if msg.get("role") == "user":
                messages.append(HumanMessage(content=msg.get("content", "")))
            elif msg.get("role") == "assistant":
                messages.append(AIMessage(content=msg.get("content", "")))

        # Add the current user message
        messages.append(HumanMessage(content=user_message))

        # Initialize state
        initial_state = {
            "messages": messages,
            "search_results": None,
            "current_tool": None,
        }

        # Run the compiled graph
        result = self.compiled_graph.invoke(initial_state)

        # Extract response
        final_messages = result.get("messages", [])
        if final_messages:
            last_message = final_messages[-1]
            if isinstance(last_message, AIMessage):
                return last_message.content
            elif isinstance(last_message, ToolMessage):
                for msg in reversed(final_messages[:-1]):
                    if isinstance(msg, AIMessage):
                        return msg.content

        return "No response generated"
