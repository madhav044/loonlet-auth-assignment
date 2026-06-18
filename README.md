# Loonlet Auth Assignment

A secure authentication and Role-Based Access Control (RBAC) system developed using Django and Django REST Framework.

## Features

### Authentication

* User Registration API
* User Login API
* JWT Token Authentication
* Password Hashing using Django's secure password system
* Protected API Endpoints

### Role-Based Access Control (RBAC)

Supported Roles:

* Admin
* Therapist
* Parent

### Role Permissions

#### Admin

* View all registered users

#### Therapist

* Access therapist-specific protected endpoints

#### Parent

* View parent profile information

## Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* SQLite Database

## Installation

Clone the repository:

```bash
git clone https://github.com/madhav044/loonlet-auth-assignment.git
cd loonlet-auth-assignment
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

The application will be available at:

http://127.0.0.1:8000/

## API Endpoints

### Authentication

#### Register User

POST /register/

Required Fields:

* Name
* Email
* Password
* Role

#### Login User

POST /login/

Required Fields:

* Email
* Password

Response:

* JWT Access Token
* User Role

### Protected APIs

#### Admin Endpoint

Accessible only by Admin users.

#### Therapist Endpoint

Accessible only by Therapist users.

#### Parent Endpoint

Accessible only by Parent users.

## Security Features

* Password Hashing
* JWT Authentication
* Role-Based Authorization
* Input Validation
* Protected Routes

## Repository

GitHub Repository:
https://github.com/madhav044/loonlet-auth-assignment
