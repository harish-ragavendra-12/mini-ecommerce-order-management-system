# Mini E-Commerce Order Management System

A console-based Python mini project that simulates a simple e-commerce order management system. Users can add orders, view stored orders, search for orders, and calculate total revenue using JSON file storage.

## Features

- Add new orders
- Add multiple products in a single order
- Automatically calculate total order value
- View all stored orders
- Search orders using Order ID
- Calculate total revenue from all orders
- Menu-driven interface
- Store data in JSON format

## Technologies Used

- Python

## Project Structure

```text
mini-ecommerce-order-management-system/
│
├── e_commerce.py
├── orders.json
└── README.md
```

## Order Data Format

Orders are stored in `orders.json`:

```json
[
    {
        "order_id": 1,
        "customer": "harish",
        "items": [
            {
                "product": "mobile",
                "price": 20000
            }
        ],
        "total": 20000
    }
]
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/harish-ragavendra-12/mini-ecommerce-order-management-system.git
```

2. Move into the project folder:

```bash
cd mini-ecommerce-order-management-system
```

3. Run the program:

```bash
python e_commerce.py
```

## Menu Options

```text
1. Add Order
2. View Orders
3. Search Orders
4. Total Revenue
5. Exit
```

## Concepts Practiced

- CRUD-style logic
- JSON read/write operations
- Search algorithms
- Data storage using files
- Function-based program structure
- Menu-driven application design

## Future Improvements

- Delete Order
- Update Order
- Duplicate Order ID validation
- Exception handling
- Order status tracking
- Invoice generation

## Author

Harish Ragavendra