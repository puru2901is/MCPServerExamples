#!/usr/bin/env python3

from customer_service import mcp

def main():
    """Main entry point for the customer service MCP server."""
    print("Starting customer service MCP server...")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
