from typing import Any
from mcp.server.fastmcp import FastMCP
import json
from datetime import datetime
import math

# Initialize FastMCP server
mcp = FastMCP("learning-basics")

# Simple in-memory data storage for learning
NOTES = []
COUNTER = 0

@mcp.tool()
async def say_hello(name: str = "World") -> str:
    """Say hello to someone. This is the simplest possible tool!
    
    Args:
        name: The name of the person to greet (optional, defaults to "World")
    """
    return f"Hello, {name}! Welcome to your first MCP server! 🎉"

@mcp.tool()
async def add_numbers(a: float, b: float) -> str:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    """
    result = a + b
    return f"{a} + {b} = {result}"

@mcp.tool()
async def multiply_numbers(a: float, b: float) -> str:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    """
    result = a * b
    return f"{a} × {b} = {result}"

@mcp.tool()
async def calculate_square_root(number: float) -> str:
    """Calculate the square root of a number.
    
    Args:
        number: The number to find the square root of
    """
    if number < 0:
        return "Error: Cannot calculate square root of negative numbers!"
    
    result = math.sqrt(number)
    return f"√{number} = {result:.2f}"

@mcp.tool()
async def get_current_time() -> str:
    """Get the current date and time."""
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    day_name = now.strftime("%A")
    return f"Current time: {formatted_time} ({day_name})"

@mcp.tool()
async def count_characters(text: str) -> str:
    """Count characters, words, and lines in text.
    
    Args:
        text: The text to analyze
    """
    char_count = len(text)
    word_count = len(text.split())
    line_count = len(text.split('\n'))
    
    return f"""Text Analysis:
📝 Characters: {char_count}
📖 Words: {word_count}
📄 Lines: {line_count}

Text: "{text}" """

@mcp.tool()
async def flip_coin() -> str:
    """Flip a coin and get heads or tails."""
    import random
    result = random.choice(["Heads", "Tails"])
    coin_emoji = "🪙" if result == "Heads" else "🎯"
    return f"Coin flip result: {result} {coin_emoji}"

@mcp.tool()
async def roll_dice(sides: int = 6) -> str:
    """Roll a dice with specified number of sides.
    
    Args:
        sides: Number of sides on the dice (default: 6)
    """
    import random
    if sides < 2:
        return "Error: Dice must have at least 2 sides!"
    
    result = random.randint(1, sides)
    return f"🎲 Rolled a {sides}-sided dice: {result}"

@mcp.tool()
async def add_note(note: str) -> str:
    """Add a note to your personal note collection.
    
    Args:
        note: The note text to save
    """
    global NOTES
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    note_entry = {
        "id": len(NOTES) + 1,
        "text": note,
        "timestamp": timestamp
    }
    NOTES.append(note_entry)
    return f"✅ Note saved! (ID: {note_entry['id']}) - {note}"

@mcp.tool()
async def list_notes() -> str:
    """List all your saved notes."""
    if not NOTES:
        return "📝 No notes saved yet. Use 'add_note' to create your first note!"
    
    notes_list = "📋 Your Notes:\n\n"
    for note in NOTES:
        notes_list += f"#{note['id']} - {note['timestamp']}\n{note['text']}\n\n"
    
    return notes_list.strip()

@mcp.tool()
async def clear_notes() -> str:
    """Clear all saved notes."""
    global NOTES
    count = len(NOTES)
    NOTES.clear()
    return f"🗑️ Cleared {count} notes. Your note collection is now empty."

@mcp.tool()
async def increment_counter() -> str:
    """Increment a simple counter by 1."""
    global COUNTER
    COUNTER += 1
    return f"🔢 Counter incremented! Current value: {COUNTER}"

@mcp.tool()
async def get_counter() -> str:
    """Get the current counter value."""
    return f"🔢 Current counter value: {COUNTER}"

@mcp.tool()
async def reset_counter() -> str:
    """Reset the counter to 0."""
    global COUNTER
    old_value = COUNTER
    COUNTER = 0
    return f"🔄 Counter reset! Changed from {old_value} to 0"

@mcp.tool()
async def generate_password(length: int = 12) -> str:
    """Generate a random password.
    
    Args:
        length: Length of the password (default: 12, min: 4, max: 50)
    """
    import random
    import string
    
    if length < 4:
        return "Error: Password must be at least 4 characters long!"
    if length > 50:
        return "Error: Password cannot be longer than 50 characters!"
    
    # Use letters, digits, and some safe special characters
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return f"🔐 Generated password ({length} characters): {password}"

@mcp.tool()
async def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> str:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
    Args:
        temperature: The temperature value to convert
        from_unit: Source unit (C, F, or K)
        to_unit: Target unit (C, F, or K)
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    
    # Convert to Celsius first
    if from_unit == "F":
        celsius = (temperature - 32) * 5/9
    elif from_unit == "K":
        celsius = temperature - 273.15
    elif from_unit == "C":
        celsius = temperature
    else:
        return "Error: Use C (Celsius), F (Fahrenheit), or K (Kelvin)"
    
    # Convert from Celsius to target
    if to_unit == "F":
        result = celsius * 9/5 + 32
    elif to_unit == "K":
        result = celsius + 273.15
    elif to_unit == "C":
        result = celsius
    else:
        return "Error: Use C (Celsius), F (Fahrenheit), or K (Kelvin)"
    
    return f"🌡️ {temperature}°{from_unit} = {result:.2f}°{to_unit}"

@mcp.tool()
async def get_help() -> str:
    """Get help information about all available tools."""
    help_text = """
🎓 Learning MCP Server - Available Tools:

📞 Basic Functions:
• say_hello(name) - Greet someone
• get_current_time() - Get current date/time
• get_help() - Show this help message

🧮 Math Tools:
• add_numbers(a, b) - Add two numbers
• multiply_numbers(a, b) - Multiply two numbers  
• calculate_square_root(number) - Find square root

📝 Text Tools:
• count_characters(text) - Analyze text

📋 Note Management:
• add_note(note) - Save a note
• list_notes() - Show all notes
• clear_notes() - Delete all notes

🔢 Counter:
• increment_counter() - Add 1 to counter
• get_counter() - Show counter value
• reset_counter() - Reset to 0

🎲 Fun Tools:
• flip_coin() - Flip a coin
• roll_dice(sides) - Roll dice
• generate_password(length) - Create password

🌡️ Utilities:
• convert_temperature(temp, from, to) - Convert temperature units

This is a beginner-friendly MCP server to learn the basics! 🚀
"""
    return help_text

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting Learning MCP server... 🎓")
    print("This server has basic tools perfect for beginners!")
    mcp.run(transport='stdio')
