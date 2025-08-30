# VibeVault - E-commerce Clothing Store API

Welcome to VibeVault! This project is a robust backend API for an e-commerce clothing store built with Django Rest Framework (DRF). It features secure user authentication with JWT, comprehensive product and category management, shopping cart, wishlist, order processing, email verification, and an admin dashboard for efficient management.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Authentication & Permissions](#authentication--permissions)
- [Email Verification](#email-verification)
- [Admin Dashboard](#admin-dashboard)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User registration with email verification
- Secure authentication using JWT
- CRUD APIs for products and categories
- Shopping cart management
- Wishlist functionality
- Order placement and history
- Role-based permissions
- Admin dashboard for efficient management
- Well-structured serialization and validation
- API documentation for ease of use

---

## Technologies Used

- **Python**
- **Django**
- **Django Rest Framework**
- **djangorestframework-simplejwt** (JWT Authentication)
- **PostgreSQL / SQLite** (choose as per setup)
- **Email backend** (SMTP services for email verification)

---

## Setup & Installation

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vibevault.git
cd vibevault
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

Create a `.env` file and set your environment variables, e.g., database credentials, email settings, secret keys.

Example `.env`:

```ini
SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## API Documentation
Swagger documentation is available at:
```
http://127.0.0.1:8000/swagger/
```

ReDoc documentation is available at:
```
http://127.0.0.1:8000/redoc/
```

---

## Project Structure

```
vibevault/
│
├── api/                  # Core API app containing models, serializers, views
│   ├── migrations/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── models.py
│
├── config/               # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .env
```

---

## API Endpoints

### Authentication

- **Register:** `POST /api/auth/register/`
- **Login:** `POST /api/auth/login/`
- **Email Verification:** `GET /api/auth/verify-email/?token=...`
- **Refresh Token:** `POST /api/auth/refresh/`

### Products & Categories

- **List Products:** `GET /api/products/`
- **Create Product:** `POST /api/products/` *(admin only)*
- **Retrieve Product:** `GET /api/products/<id>/`
- **Update Product:** `PUT /api/products/<id>/` *(admin only)*
- **Delete Product:** `DELETE /api/products/<id>/` *(admin only)*

- **List Categories:** `GET /api/categories/`
- **Create Category:** `POST /api/categories/` *(admin only)*

### Cart

- **View Cart:** `GET /api/cart/`
- **Add to Cart:** `POST /api/cart/`
- **Update Cart Item:** `PUT /api/cart/<item_id>/`
- **Remove from Cart:** `DELETE /api/cart/<item_id>/`

### Wishlist

- **View Wishlist:** `GET /api/wishlist/`
- **Add to Wishlist:** `POST /api/wishlist/`
- **Remove from Wishlist:** `DELETE /api/wishlist/<item_id>/`

### Orders

- **Place Order:** `POST /api/orders/`
- **Order History:** `GET /api/orders/`

---

## Authentication & Permissions

- JWT tokens for secure authentication
- Role-based permissions:
  - Regular users can view and modify their own data
  - Admin users have full access to manage products, categories, and orders

---

## Email Verification

Upon registration, users receive an email with a verification link containing a token. Clicking the link verifies their email address, enabling full access.

---

## Admin Dashboard

The Django admin panel provides an interface for managing products, categories, orders, and users. Accessible at `/admin/`.

---

## Documentation

Comprehensive API documentation is available at `/api/docs/` (using tools like Swagger or Redoc).

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

For questions or support, open an issue or contact [your email].

---

**Happy shopping with VibeVault!** 🚀

---

*Note: Replace placeholder URLs, email addresses, and other details with your actual project info.*