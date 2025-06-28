# MCP Server Examples 🚀

A comprehensive collection of **Model Context Protocol (MCP) servers** demonstrating various use cases and implementation patterns. These examples showcase how to build powerful, AI-friendly tools that can be integrated with Claude and other AI assistants.

## 📋 Table of Contents

- [What is MCP?](#what-is-mcp)
- [Available Servers](#available-servers)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)

## 🤖 What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables seamless integration between AI assistants and external data sources and tools. It allows AI models to:

- Access real-time data
- Perform actions on behalf of users
- Integrate with existing workflows and systems
- Maintain context across interactions

## 🛠️ Available Servers

### 1. 🎓 Learning MCP Server
**Perfect for beginners!**
- **Location**: `learning_mcp/`
- **Purpose**: Educational MCP server with simple, easy-to-understand tools
- **Features**:
  - Basic function calls (`say_hello`, `get_current_time`)
  - Simple math operations (`add_numbers`, `multiply_numbers`, `square_root`)
  - Data persistence (`notes` system with add/list/clear)
  - Fun utilities (`flip_coin`, `roll_dice`, `generate_password`)
  - Text analysis (`count_characters`)
  - Temperature conversion
  - Counter functionality

### 2. 🎧 Customer Service MCP Server
**Enterprise-ready customer support tools**
- **Location**: `customer_service/`
- **Purpose**: Comprehensive customer service and order management
- **Features**:
  - **Order Management**: Status tracking, cancellations, refunds
  - **Customer Support**: Search customers, create tickets, track issues
  - **Address Updates**: Modify shipping addresses for unshipped orders
  - **Customer History**: Complete order history and account details

### 3. 🌤️ Weather MCP Server
**Real-time weather information**
- **Location**: `weather/`
- **Purpose**: Weather forecasts and alerts using National Weather Service API
- **Features**:
  - Current weather conditions
  - Detailed forecasts
  - Weather alerts for US states
  - Location-based weather data

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) package manager

### 1. Clone the Repository
```bash
git clone https://github.com/puru2901is/MCPServerExamples.git
cd MCPServerExamples
```

### 2. Choose a Server and Navigate to Its Directory
```bash
# For learning (recommended for beginners)
cd learning_mcp

# For customer service
cd customer_service

# For weather
cd weather
```

### 3. Install Dependencies
```bash
uv sync
```

### 4. Run the Server
```bash
uv run main.py
```

## 📦 Installation

Each server is self-contained with its own dependencies managed by `uv`.

### System Requirements
- macOS, Linux, or Windows
- Python 3.8 or higher
- uv package manager

### Installing uv
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

## 🔧 Configuration

### VS Code Settings
If you're using VS Code with MCP integration, add this to your `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "learning-mcp": {
        "type": "stdio",
        "command": "/path/to/uv",
        "args": [
          "--directory",
          "/path/to/MCPServerExamples/learning_mcp",
          "run",
          "learning_mcp.py"
        ]
      },
      "customer-service": {
        "type": "stdio", 
        "command": "/path/to/uv",
        "args": [
          "--directory",
          "/path/to/MCPServerExamples/customer_service",
          "run",
          "customer_service.py"
        ]
      },
      "weather": {
        "type": "stdio",
        "command": "/path/to/uv", 
        "args": [
          "--directory",
          "/path/to/MCPServerExamples/weather",
          "run",
          "weather.py"
        ]
      }
    }
  }
}
```

### Claude Desktop Configuration
For Claude Desktop, add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "learning-mcp": {
      "command": "uv",
      "args": [
        "--directory", 
        "/path/to/MCPServerExamples/learning_mcp",
        "run",
        "learning_mcp.py"
      ]
    }
  }
}
```

## 🎯 Usage Examples

### Learning MCP Server
```python
# Basic greeting
say_hello("World")  # Returns: "Hello, World!"

# Math operations
add_numbers(5, 3)    # Returns: 8
calculate_square_root(16)  # Returns: 4.0

# Note-taking
add_note("Remember to test the MCP server")
list_notes()  # Shows all saved notes

# Fun utilities
flip_coin()  # Returns: "heads" or "tails"
roll_dice(20)  # Rolls a 20-sided die
```

### Customer Service Server
```python
# Search for a customer
search_customer(email="john@example.com")

# Get order status
get_order_status("ORD-001")

# Create support ticket
create_support_ticket(
    customer_id="CUST-123",
    subject="Billing Question", 
    description="Question about recent charge",
    priority="medium"
)
```

### Weather Server
```python
# Get weather forecast
get_forecast(latitude=40.7128, longitude=-74.0060)  # NYC

# Get weather alerts
get_alerts("NY")  # New York state alerts
```

## 🧪 Development

### Project Structure
```
MCPServerExamples/
├── .gitignore              # Comprehensive Python .gitignore
├── README.md               # This file
├── learning_mcp/           # Beginner-friendly MCP server
│   ├── learning_mcp.py     # Main server implementation
│   ├── main.py             # Entry point
│   ├── pyproject.toml      # Dependencies and config
│   └── README.md           # Detailed usage guide
├── customer_service/       # Customer service tools
│   ├── customer_service.py # Server implementation
│   ├── main.py             # Entry point
│   ├── pyproject.toml      # Dependencies and config
│   └── README.md           # Usage documentation
└── weather/                # Weather information server
    ├── weather.py          # Server implementation
    ├── main.py             # Entry point
    ├── pyproject.toml      # Dependencies and config
    └── README.md           # Usage guide
```

### Adding New Servers
1. Create a new directory for your server
2. Add `pyproject.toml` with dependencies
3. Implement your server following MCP patterns
4. Add a `main.py` entry point
5. Document your server with a README.md

### Testing
Each server can be tested individually:

```bash
cd server_directory
uv run main.py
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-server`
3. **Add your MCP server** following the existing patterns
4. **Update documentation** including README files
5. **Test thoroughly** with different MCP clients
6. **Submit a pull request**

### Contribution Guidelines
- Follow the existing code style and patterns
- Include comprehensive documentation
- Add examples and usage guides
- Test with multiple MCP clients
- Keep dependencies minimal and well-documented

## 📚 Learning Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude MCP Integration](https://docs.anthropic.com/en/docs/build-with-claude/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.mcp)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

- **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/puru2901is/MCPServerExamples/issues)
- **Discussions**: Join conversations in [GitHub Discussions](https://github.com/puru2901is/MCPServerExamples/discussions)
- **Documentation**: Each server has detailed README files with usage examples

## 🏷️ Tags

`mcp` `model-context-protocol` `ai` `claude` `python` `servers` `examples` `tutorial` `customer-service` `weather` `learning`

---

**Happy coding!** 🎉 Start with the `learning_mcp` server if you're new to MCP, then explore the more advanced examples.
