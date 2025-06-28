from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
import json
from mcp.server.fastmcp import FastMCP
from enum import Enum

# Initialize FastMCP server
mcp = FastMCP("customer-service")

# Enums for order and ticket status
class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

# Mock database - In a real implementation, this would be a proper database
ORDERS_DB = {
    "ORD-001": {
        "order_id": "ORD-001",
        "customer_id": "CUST-123",
        "customer_email": "john.doe@email.com",
        "customer_name": "John Doe",
        "items": [
            {"product": "Laptop", "quantity": 1, "price": 999.99},
            {"product": "Mouse", "quantity": 1, "price": 29.99}
        ],
        "total": 1029.98,
        "status": OrderStatus.SHIPPED,
        "order_date": "2025-06-20",
        "tracking_number": "TRK123456789",
        "estimated_delivery": "2025-06-28",
        "shipping_address": "123 Main St, Anytown, ST 12345"
    },
    "ORD-002": {
        "order_id": "ORD-002",
        "customer_id": "CUST-456",
        "customer_email": "jane.smith@email.com",
        "customer_name": "Jane Smith",
        "items": [
            {"product": "Smartphone", "quantity": 1, "price": 699.99}
        ],
        "total": 699.99,
        "status": OrderStatus.PROCESSING,
        "order_date": "2025-06-25",
        "tracking_number": None,
        "estimated_delivery": "2025-06-30",
        "shipping_address": "456 Oak Ave, Another City, ST 67890"
    }
}

TICKETS_DB = {
    "TKT-001": {
        "ticket_id": "TKT-001",
        "customer_id": "CUST-123",
        "customer_email": "john.doe@email.com",
        "customer_name": "John Doe",
        "subject": "Damaged item received",
        "description": "The laptop I received has a crack on the screen",
        "status": TicketStatus.OPEN,
        "priority": Priority.HIGH,
        "created_date": "2025-06-26",
        "last_updated": "2025-06-26",
        "agent_assigned": None,
        "order_id": "ORD-001"
    }
}

CUSTOMERS_DB = {
    "CUST-123": {
        "customer_id": "CUST-123",
        "name": "John Doe",
        "email": "john.doe@email.com",
        "phone": "+1-555-0123",
        "registration_date": "2024-01-15",
        "loyalty_tier": "Gold",
        "total_orders": 15,
        "total_spent": 5999.85
    },
    "CUST-456": {
        "customer_id": "CUST-456",
        "name": "Jane Smith",
        "email": "jane.smith@email.com",
        "phone": "+1-555-0456",
        "registration_date": "2024-03-22",
        "loyalty_tier": "Silver",
        "total_orders": 8,
        "total_spent": 2799.92
    }
}

@mcp.tool()
async def get_order_status(order_id: str) -> str:
    """Get the current status and details of an order.
    
    Args:
        order_id: The order ID to look up (e.g., ORD-001)
    """
    if order_id not in ORDERS_DB:
        return f"Order {order_id} not found. Please check the order ID and try again."
    
    order = ORDERS_DB[order_id]
    
    items_list = "\n".join([
        f"  - {item['product']} (Qty: {item['quantity']}) - ${item['price']:.2f}"
        for item in order['items']
    ])
    
    tracking_info = f"Tracking Number: {order['tracking_number']}" if order['tracking_number'] else "Tracking not yet available"
    
    return f"""
Order Status for {order_id}:

Customer: {order['customer_name']} ({order['customer_email']})
Order Date: {order['order_date']}
Status: {order['status'].upper()}
{tracking_info}
Estimated Delivery: {order['estimated_delivery']}

Items Ordered:
{items_list}

Total: ${order['total']:.2f}
Shipping Address: {order['shipping_address']}
"""

@mcp.tool()
async def cancel_order(order_id: str, reason: str = "Customer request") -> str:
    """Cancel an order if it's eligible for cancellation.
    
    Args:
        order_id: The order ID to cancel
        reason: Reason for cancellation (optional)
    """
    if order_id not in ORDERS_DB:
        return f"Order {order_id} not found. Please check the order ID and try again."
    
    order = ORDERS_DB[order_id]
    current_status = order['status']
    
    # Check if order can be cancelled
    if current_status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
        return f"Cannot cancel order {order_id}. Order is already {current_status}. Please contact customer service for returns."
    
    if current_status == OrderStatus.CANCELLED:
        return f"Order {order_id} is already cancelled."
    
    # Cancel the order
    ORDERS_DB[order_id]['status'] = OrderStatus.CANCELLED
    ORDERS_DB[order_id]['cancellation_reason'] = reason
    ORDERS_DB[order_id]['cancellation_date'] = datetime.now().strftime("%Y-%m-%d")
    
    return f"""
Order {order_id} has been successfully cancelled.

Customer: {order['customer_name']}
Original Total: ${order['total']:.2f}
Cancellation Reason: {reason}
Refund Status: Refund will be processed within 3-5 business days

A confirmation email has been sent to {order['customer_email']}.
"""

@mcp.tool()
async def search_customer(email: str = None, customer_id: str = None, phone: str = None) -> str:
    """Search for customer information by email, customer ID, or phone number.
    
    Args:
        email: Customer's email address
        customer_id: Customer's ID (e.g., CUST-123)
        phone: Customer's phone number
    """
    if not any([email, customer_id, phone]):
        return "Please provide at least one search parameter: email, customer_id, or phone."
    
    # Search by customer_id first (most direct)
    if customer_id and customer_id in CUSTOMERS_DB:
        customer = CUSTOMERS_DB[customer_id]
    else:
        # Search by email or phone
        customer = None
        for cust_id, cust_data in CUSTOMERS_DB.items():
            if (email and cust_data['email'].lower() == email.lower()) or \
               (phone and cust_data['phone'] == phone):
                customer = cust_data
                break
    
    if not customer:
        return "Customer not found. Please check the search parameters and try again."
    
    # Get customer's orders
    customer_orders = [order for order in ORDERS_DB.values() 
                      if order['customer_id'] == customer['customer_id']]
    
    recent_orders = sorted(customer_orders, key=lambda x: x['order_date'], reverse=True)[:3]
    orders_summary = "\n".join([
        f"  - {order['order_id']} ({order['order_date']}) - {order['status'].upper()} - ${order['total']:.2f}"
        for order in recent_orders
    ]) if recent_orders else "  No recent orders"
    
    return f"""
Customer Information:

Name: {customer['name']}
Email: {customer['email']}
Phone: {customer['phone']}
Customer ID: {customer['customer_id']}
Member Since: {customer['registration_date']}
Loyalty Tier: {customer['loyalty_tier']}
Total Orders: {customer['total_orders']}
Total Spent: ${customer['total_spent']:.2f}

Recent Orders:
{orders_summary}
"""

@mcp.tool()
async def create_support_ticket(customer_id: str, subject: str, description: str, 
                              priority: str = "medium", order_id: str = None) -> str:
    """Create a new customer support ticket.
    
    Args:
        customer_id: The customer's ID
        subject: Brief description of the issue
        description: Detailed description of the problem
        priority: Priority level (low, medium, high, urgent)
        order_id: Related order ID if applicable
    """
    if customer_id not in CUSTOMERS_DB:
        return f"Customer {customer_id} not found. Please verify the customer ID."
    
    # Validate priority
    try:
        priority_enum = Priority(priority.lower())
    except ValueError:
        return f"Invalid priority '{priority}'. Must be one of: low, medium, high, urgent"
    
    # Generate new ticket ID
    ticket_count = len(TICKETS_DB) + 1
    ticket_id = f"TKT-{ticket_count:03d}"
    
    customer = CUSTOMERS_DB[customer_id]
    
    # Create ticket
    new_ticket = {
        "ticket_id": ticket_id,
        "customer_id": customer_id,
        "customer_email": customer['email'],
        "customer_name": customer['name'],
        "subject": subject,
        "description": description,
        "status": TicketStatus.OPEN,
        "priority": priority_enum,
        "created_date": datetime.now().strftime("%Y-%m-%d"),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "agent_assigned": None,
        "order_id": order_id
    }
    
    TICKETS_DB[ticket_id] = new_ticket
    
    order_info = f"\nRelated Order: {order_id}" if order_id else ""
    
    return f"""
Support Ticket Created Successfully!

Ticket ID: {ticket_id}
Customer: {customer['name']} ({customer['email']})
Subject: {subject}
Priority: {priority_enum.upper()}
Status: OPEN{order_info}

Description:
{description}

A confirmation email has been sent to the customer. The ticket will be assigned to an agent shortly.
"""

@mcp.tool()
async def get_ticket_status(ticket_id: str) -> str:
    """Get the status and details of a support ticket.
    
    Args:
        ticket_id: The ticket ID to look up (e.g., TKT-001)
    """
    if ticket_id not in TICKETS_DB:
        return f"Ticket {ticket_id} not found. Please check the ticket ID and try again."
    
    ticket = TICKETS_DB[ticket_id]
    
    agent_info = f"Assigned Agent: {ticket['agent_assigned']}" if ticket['agent_assigned'] else "Agent: Not yet assigned"
    order_info = f"\nRelated Order: {ticket['order_id']}" if ticket['order_id'] else ""
    
    return f"""
Support Ticket {ticket_id}:

Customer: {ticket['customer_name']} ({ticket['customer_email']})
Subject: {ticket['subject']}
Status: {ticket['status'].upper()}
Priority: {ticket['priority'].upper()}
Created: {ticket['created_date']}
Last Updated: {ticket['last_updated']}
{agent_info}{order_info}

Description:
{ticket['description']}
"""

@mcp.tool()
async def process_refund(order_id: str, amount: float = None, reason: str = "Customer request") -> str:
    """Process a refund for an order.
    
    Args:
        order_id: The order ID to refund
        amount: Partial refund amount (optional, defaults to full order total)
        reason: Reason for the refund
    """
    if order_id not in ORDERS_DB:
        return f"Order {order_id} not found. Please check the order ID and try again."
    
    order = ORDERS_DB[order_id]
    
    if order['status'] not in [OrderStatus.DELIVERED, OrderStatus.CANCELLED]:
        return f"Cannot process refund for order {order_id}. Order status is {order['status']}. Order must be delivered or cancelled to process refund."
    
    refund_amount = amount if amount is not None else order['total']
    
    if refund_amount > order['total']:
        return f"Refund amount ${refund_amount:.2f} cannot exceed order total ${order['total']:.2f}."
    
    # Process refund
    ORDERS_DB[order_id]['status'] = OrderStatus.REFUNDED
    ORDERS_DB[order_id]['refund_amount'] = refund_amount
    ORDERS_DB[order_id]['refund_reason'] = reason
    ORDERS_DB[order_id]['refund_date'] = datetime.now().strftime("%Y-%m-%d")
    
    refund_type = "Full" if refund_amount == order['total'] else "Partial"
    
    return f"""
Refund Processed Successfully!

Order ID: {order_id}
Customer: {order['customer_name']} ({order['customer_email']})
{refund_type} Refund Amount: ${refund_amount:.2f}
Original Order Total: ${order['total']:.2f}
Refund Reason: {reason}

The refund will appear on the customer's original payment method within 3-5 business days.
A confirmation email has been sent to {order['customer_email']}.
"""

@mcp.tool()
async def update_shipping_address(order_id: str, new_address: str) -> str:
    """Update the shipping address for an order (if not yet shipped).
    
    Args:
        order_id: The order ID to update
        new_address: The new shipping address
    """
    if order_id not in ORDERS_DB:
        return f"Order {order_id} not found. Please check the order ID and try again."
    
    order = ORDERS_DB[order_id]
    
    if order['status'] in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
        return f"Cannot update shipping address for order {order_id}. Order is already {order['status']}."
    
    old_address = order['shipping_address']
    ORDERS_DB[order_id]['shipping_address'] = new_address
    ORDERS_DB[order_id]['address_updated_date'] = datetime.now().strftime("%Y-%m-%d")
    
    return f"""
Shipping Address Updated Successfully!

Order ID: {order_id}
Customer: {order['customer_name']}

Previous Address: {old_address}
New Address: {new_address}

The customer has been notified of this change via email.
"""

@mcp.tool()
async def get_customer_orders(customer_id: str, limit: int = 10) -> str:
    """Get all orders for a specific customer.
    
    Args:
        customer_id: The customer's ID
        limit: Maximum number of orders to return (default: 10)
    """
    if customer_id not in CUSTOMERS_DB:
        return f"Customer {customer_id} not found. Please check the customer ID and try again."
    
    customer = CUSTOMERS_DB[customer_id]
    customer_orders = [order for order in ORDERS_DB.values() 
                      if order['customer_id'] == customer_id]
    
    if not customer_orders:
        return f"No orders found for customer {customer['name']} ({customer_id})."
    
    # Sort by order date (most recent first) and limit results
    sorted_orders = sorted(customer_orders, key=lambda x: x['order_date'], reverse=True)[:limit]
    
    orders_list = "\n".join([
        f"  {order['order_id']} | {order['order_date']} | {order['status'].upper()} | ${order['total']:.2f}"
        for order in sorted_orders
    ])
    
    return f"""
Orders for {customer['name']} ({customer_id}):

Total Orders Found: {len(customer_orders)}
Showing Most Recent {len(sorted_orders)} Orders:

Order ID | Date | Status | Total
{orders_list}

Customer Summary:
- Member Since: {customer['registration_date']}
- Loyalty Tier: {customer['loyalty_tier']}
- Total Spent: ${customer['total_spent']:.2f}
"""

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting customer service MCP server...")
    mcp.run(transport='stdio')
