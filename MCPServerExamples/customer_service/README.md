# Customer Service MCP Server

A Model Context Protocol (MCP) server that provides comprehensive customer service functionality including:

## Features

### Order Management
- **Get Order Status**: Retrieve detailed information about any order including status, tracking, and delivery estimates
- **Cancel Orders**: Cancel orders that haven't shipped yet with proper validation
- **Update Shipping Address**: Modify shipping addresses for unshipped orders
- **Process Refunds**: Handle full or partial refunds for delivered/cancelled orders

### Customer Support
- **Customer Search**: Find customers by email, customer ID, or phone number
- **Support Tickets**: Create and track customer support tickets with priority levels
- **Customer Order History**: View complete order history for any customer

### Available Tools

1. `get_order_status(order_id)` - Get current order status and details
2. `cancel_order(order_id, reason)` - Cancel an eligible order
3. `search_customer(email, customer_id, phone)` - Find customer information
4. `create_support_ticket(customer_id, subject, description, priority, order_id)` - Create support tickets
5. `get_ticket_status(ticket_id)` - Check support ticket status
6. `process_refund(order_id, amount, reason)` - Process order refunds
7. `update_shipping_address(order_id, new_address)` - Update shipping information
8. `get_customer_orders(customer_id, limit)` - Get customer's order history

## Installation

```bash
cd customer_service
uv sync
```

## Usage

The server runs as an MCP server and can be integrated with any MCP-compatible client.

## Sample Data

The server includes sample customers and orders for testing:
- Customer: John Doe (CUST-123) with orders ORD-001
- Customer: Jane Smith (CUST-456) with order ORD-002

## Configuration

Add to your MCP client configuration:

```json
{
  "customer-service": {
    "type": "stdio",
    "command": "uv",
    "args": ["--directory", "/path/to/customer_service", "run", "customer_service.py"]
  }
}
```
