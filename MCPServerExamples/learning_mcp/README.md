# Learning MCP Server 🎓

A beginner-friendly Model Context Protocol (MCP) server designed to help you learn MCP concepts with simple, easy-to-understand tools.

## What is this? 🤔

This MCP server provides basic tools that demonstrate core MCP concepts:
- Simple function calls
- Data persistence (in-memory)
- Different data types
- Error handling
- User interaction

Perfect for beginners who want to understand how MCP servers work!

## Available Tools 🛠️

### 📞 Basic Functions
- `say_hello(name)` - Your first MCP tool! Greets someone
- `get_current_time()` - Shows current date and time
- `get_help()` - Lists all available tools

### 🧮 Math Tools
- `add_numbers(a, b)` - Add two numbers
- `multiply_numbers(a, b)` - Multiply two numbers  
- `calculate_square_root(number)` - Find square root

### 📝 Text Analysis
- `count_characters(text)` - Count characters, words, and lines

### 📋 Note Management
- `add_note(note)` - Save a note to memory
- `list_notes()` - Show all saved notes
- `clear_notes()` - Delete all notes

### 🔢 Simple Counter
- `increment_counter()` - Add 1 to counter
- `get_counter()` - Show current counter value
- `reset_counter()` - Reset counter to 0

### 🎲 Fun Tools
- `flip_coin()` - Random heads or tails
- `roll_dice(sides)` - Roll a dice with custom sides
- `generate_password(length)` - Create random password

### 🌡️ Utilities
- `convert_temperature(temp, from, to)` - Convert between C, F, K

## Installation

```bash
cd learning_mcp
uv sync
```

## Usage

Once added to your MCP client, you can try:

```
"Say hello to me"
"Add 5 and 3"
"Add a note: Remember to practice MCP daily"
"What time is it?"
"Flip a coin"
"Roll a 20-sided dice"
```

## Learning Goals 📚

This server demonstrates:

1. **Basic Tool Structure** - See how MCP tools are defined
2. **Parameter Handling** - Required vs optional parameters
3. **Data Types** - Strings, numbers, booleans
4. **State Management** - Simple in-memory storage
5. **Error Handling** - Input validation
6. **Documentation** - How to document tools properly

## Configuration

Add to your MCP client settings:

```json
{
  "learning-mcp": {
    "type": "stdio",
    "command": "uv",
    "args": ["--directory", "/path/to/learning_mcp", "run", "learning_mcp.py"]
  }
}
```

## Perfect for Beginners! 🌟

- Simple, clear function names
- Helpful error messages
- Easy to understand code
- Well-documented tools
- No complex dependencies
- Instant feedback

Start your MCP journey here! 🚀
