"""
Defines the get_project_path tool for retrieving the Unity project path.
"""
import asyncio
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP, Context
from unity_connection import get_unity_connection


def register_get_project_path_tool(mcp: FastMCP):
    """Registers the get_project_path tool with the MCP server."""

    @mcp.tool()
    async def get_project_path(ctx: Context) -> Dict[str, Any]:
        """Retrieves the current Unity project path.

        Args:
            ctx: The MCP context.

        Returns:
            A dictionary containing the project asset folder path (project
             path, data path, persistent data path, streaming assets path,
             temporary cache path).
        """
        # Get the current asyncio event loop
        loop = asyncio.get_running_loop()
        # Get the Unity connection instance
        connection = get_unity_connection()
        
        # Run the synchronous send_command in the default executor
        result = await loop.run_in_executor(
            None,  # Use default executor
            connection.send_command,  # The function to call
            "get_project_path",  # First argument for send_command
            {}  # Empty params dict since no parameters needed
        )
        # Return the result obtained from Unity
        return result 