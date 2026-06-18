Loonlet Auth Assignment

A FastAPI-based authentication system with JWT Authentication and Role-Based Access Control (RBAC) developed as part of the Loonlet Innovations Pvt. Ltd. coding assessment.

Features
Authentication
User Registration API
User Login API
JWT Token Authentication
Password Hashing
Secure Authentication Flow
Role-Based Access Control (RBAC)

Supported Roles:

Admin
Therapist
Parent
Protected APIs
Admin
View all registered users
Therapist
Access therapist-specific protected endpoints
Parent
View profile information
Tech Stack
Python
FastAPI
SQLAlchemy
SQLite
JWT Authentication
Passlib
Uvicorn
Installation
Clone Repository

git clone https://github.com/madhav044/loonlet-auth-assignment.git

cd loonlet-auth-assignment

Create Virtual Environment

python -m venv venv

Activate Virtual Environment (Windows)

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run the Project

python -m uvicorn app.main:app --reload

The application will be available at:

http://127.0.0.1:8000/

API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

API Endpoints
Register User

POST /register

Required Fields:

Name
Email
Password
Role
Login User

POST /login

Required Fields:

Email
Password

Response:

JWT Access Token
User Role
Protected Endpoints
Admin Endpoint

Accessible only by Admin users.

Therapist Endpoint

Accessible only by Therapist users.

Parent Endpoint

Accessible only by Parent users.

Security Features
JWT Authentication
Password Hashing
Role-Based Authorization
Input Validation
Protected Routes
Database

Database Used: SQLite

User Fields:

ID
Name
Email
Password (Hashed)
Role
GitHub Repository

https://github.com/madhav044/loonlet-auth-assignment

Author:
Madhav Chand

Email: 2200032610cseh@gmail.com

Phone: 8074271778
