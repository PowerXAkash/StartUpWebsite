"""
Search tool for LangGraph chat agent.
Provides web search and information retrieval capabilities.
"""

import requests
from typing import Optional, List, Dict, Any
from ai.config import SEARCH_API_KEY, SEARCH_API_URL


class SearchTool:
    """
    A search tool that retrieves information from external sources.
    Can be integrated with DuckDuckGo, Google, or custom search APIs.
    """

    def __init__(self, api_key: str = SEARCH_API_KEY, api_url: str = SEARCH_API_URL):
        self.api_key = api_key
        self.api_url = api_url

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Perform a web search for the given query.

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of search results with title, link, and snippet
        """
        try:
            # Example: Using DuckDuckGo (no API key required)
            results = self._search_duckduckgo(query, max_results)
            return results
        except Exception as e:
            return [{"error": f"Search failed: {str(e)}"}]

    def _search_duckduckgo(self, query: str, max_results: int) -> List[Dict[str, str]]:
        """Search using DuckDuckGo API (free, no auth required)."""
        try:
            import requests_html
            from requests_html import HTMLSession

            session = HTMLSession()
            url = f"https://duckduckgo.com/html/?q={query}"
            r = session.get(url, timeout=5)

            results = []
            for result in r.html.find(".result__a")[:max_results]:
                try:
                    title = result.text
                    link = result.attrs.get("href", "")
                    snippet = result.parent.find(".result__snippet", first=True)
                    snippet_text = (
                        snippet.text if snippet else "No snippet available"
                    )

                    results.append(
                        {"title": title, "link": link, "snippet": snippet_text}
                    )
                except:
                    continue

            return results if results else self._search_fallback(query)
        except:
            return self._search_fallback(query)

    def _search_fallback(self, query: str) -> List[Dict[str, str]]:
        """Fallback search using simple local knowledge base."""
        knowledge_base = {
            "education ai": [
                {
                    "title": "SeedStudio Education AI Solutions",
                    "link": "https://seedstudio.example/education-ai",
                    "snippet": "Personalized AI tutoring and teacher analytics for schools.",
                },
            ],
            "healthcare ai": [
                {
                    "title": "SeedStudio Healthcare AI",
                    "link": "https://seedstudio.example/healthcare-ai",
                    "snippet": "Diagnostic support and hospital workflow optimization.",
                },
            ],
            "agriculture ai": [
                {
                    "title": "SeedStudio Agriculture AI",
                    "link": "https://seedstudio.example/agriculture-ai",
                    "snippet": "Crop monitoring, precision farming, and weather intelligence.",
                },
            ],
            "industry ai": [
                {
                    "title": "SeedStudio Industry AI",
                    "link": "https://seedstudio.example/industry-ai",
                    "snippet": "Equipment monitoring and predictive maintenance solutions.",
                },
            ],
        }

        query_lower = query.lower()
        for key in knowledge_base:
            if key in query_lower:
                return knowledge_base[key]

        return [
            {
                "title": "SeedStudio AI Solutions",
                "link": "https://seedstudio.example",
                "snippet": "Explore our AI solutions for education, healthcare, agriculture, and industry.",
            }
        ]

    def search_seedstudio_services(self, service_type: str) -> Dict[str, str]:
        """
        Search for SeedStudio services by category.

        Args:
            service_type: Type of service (education, healthcare, agriculture, industry)

        Returns:
            Dictionary with service information
        """
        services = {
            "education": {
                "name": "Education AI",
                "description": "Personalized learning, teacher dashboards, and parent portals",
                "features": [
                    "Student Learning Agent",
                    "Teacher Dashboard",
                    "Parent Portal",
                ],
            },
            "healthcare": {
                "name": "Healthcare AI",
                "description": "Diagnostic support and hospital workflow optimization",
                "features": ["Diagnosis Support", "Workflow Automation", "Analytics"],
            },
            "agriculture": {
                "name": "Agricultural AI",
                "description": "Crop monitoring, precision farming, and weather intelligence",
                "features": ["Crop Monitoring", "Precision Farming", "Weather Intel"],
            },
            "industry": {
                "name": "Industrial AI",
                "description": "Equipment monitoring and predictive maintenance",
                "features": ["Equipment Monitoring", "Predictive Maintenance", "Automation"],
            },
        }

        return services.get(
            service_type.lower(),
            {
                "name": "Unknown Service",
                "description": "Service not found",
                "features": [],
            },
        )
