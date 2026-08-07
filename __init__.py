"""Crawl4AI web-extract provider plugin for Hermes."""

from .provider import Crawl4AIWebSearchProvider

def register(ctx) -> None:
    """Register the Crawl4AI backend for native web extraction."""
    ctx.register_web_search_provider(Crawl4AIWebSearchProvider())
