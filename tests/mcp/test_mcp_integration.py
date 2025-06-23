import sys

import pytest

from app.agent.mcp import MCPAgent


@pytest.mark.asyncio
async def test_mcp_integration_basic():
    agent = MCPAgent()
    await agent.initialize(
        connection_type="stdio",
        command=sys.executable,
        args=["-m", "app.mcp.server"],
    )
    try:
        tools = await agent.mcp_clients.list_tools()
        assert any(tool.name == "bash" for tool in tools.tools)
    finally:
        await agent.cleanup()
