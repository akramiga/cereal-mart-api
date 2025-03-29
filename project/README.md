 Cereal Crop Store Inventory Management API

# Overview

This project implements a RESTful API using Django REST Framework (DRF) for managing inventory and tracking transactions in a cereal crop store.  It allows store managers to track inventory levels, manage crop information, and record inventory transactions.

## Features

   **Crop Management:**
    *   Add, update, and delete cereal crop items (name, description, category, unit price)
  **Inventory Level Management:**
    *   View current inventory levels in kilograms.
    *   Record stock-in and stock-out transactions.
    *   Automatic stock level updates based on transactions.
    *   Provides a summary of total quantities of each crop in stock.
  **User Authentication and Authorization:**
    *   Secure API endpoints with user authentication.
    *   Role-based access control (Admin, Store Manager).
  **API Endpoints:**
  **Filtering and Sorting:**  List endpoints support filtering and sorting.

## Technologies Used

*   Python3
*   Django
*   Django REST Framework
