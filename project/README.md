 Cereal Crop Store Inventory Management API

# Overview

This project implements a RESTful API using Django REST Framework (DRF) for managing inventory and tracking transactions in a cereal crop store.  It allows store managers to track inventory levels, manage crop information, and record inventory transactions.


## Features

- User authentication using JWT tokens
- CRUD operations for crops
- Tracking inventory transactions (stock in/out)
- Calculating current stock levels
- Filtering, searching, and ordering capabilities
- Role-based access control

## Tech Stack

- Django
- Django REST Framework
- djangorestframework-simplejwt
- django-filter

## API Endpoints

### Authentication

- `POST api/users/register/` - Register a new user
- `POST api/users/token/` - Obtain JWT token
- `POST api/users/token/refresh/` - Refresh JWT token

### Users

- `GET /api/users/` - List all users (admin only)
- `GET /api/users/<id>/` - Get user details (admin only)

### Crops

- `GET /api/inventory/crops/` - List all crops
- `POST /api/inventory/crops/` - Add new crop (authenticated users)
- `GET /api/inventory/crops/<id>/` - Get crop details
- `PUT /api/inventory/crops/<id>/` - Update crop (owner or admin)
- `DELETE /api/inventory/crops/<id>/` - Delete crop (owner or admin)
- `GET /api/inventory/crops/inventory_summary/` - Get inventory summary (authenticated users)

### Inventory Transactions

- `GET /api/inventory/transactions/` - List all transactions (authenticated users)
- `POST /api/inventory/transactions/` - Add new transaction (authenticated users)
- `GET /api/inventory/transactions/<id>/` - Get transaction details (authenticated users)
- `PUT /api/inventory/transactions/<id>/` - Update transaction (authenticated users)
- `DELETE /api/inventory/transactions/<id>/` - Delete transaction (authenticated users)


## API Usage

### Authentication

To authenticate, first register a user:

```
POST /api/users/register/
{
    "username": "john",
    "email": "user1@example.com",
    "password1": "j1234",
    "password2": "secure"
}
```

Then obtain a token:

```
POST /api/users/token/
{
    "username": "john",
    "password": "j1234"
}
```

Use the token in your requests:

```
GET /api/inventory/crops/
Authorization: Bearer <your_token>
```

### Adding a Crop

```
POST /api/inventory/crops/
Authorization: Bearer <your_token>
{
    "name": "millet",
    "category": "millet seeds",
    "unit_price": 650
}
```

### Adding an Inventory Transaction

```
POST /api/inventory/transactions/
Authorization: Bearer <your_token>
{
    "crop": 1,
    "transaction_type": "IN",
    "quantity": 100
}
```
