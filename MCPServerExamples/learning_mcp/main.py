#!/usr/bin/env python3

from learning_mcp import mcp

def main():
    """Main entry point for the learning MCP server."""
    print("Starting Learning MCP server... 🎓")
    print("Perfect for beginners to learn MCP concepts!")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
