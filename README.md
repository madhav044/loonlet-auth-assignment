# Loonlet Auth Assignment

A FastAPI-based authentication system with JWT Authentication and Role-Based Access Control (RBAC) developed as part of the Loonlet Innovations Pvt. Ltd. coding assessment.

---

## Features

### Authentication
* **User Registration API** - Secure account creation with automated role assignment.
* **User Login API** - Validates credentials and returns a secure session token.
* **JWT Token Authentication** - Stateless, secure session management.
* **Password Hashing** - Secure password storage utilizing strong one-way hashing algorithms.
* **Secure Authentication Flow** - Built following industry-standard OAuth2 security protocols.

### Role-Based Access Control (RBAC)
Supported System Roles:
* **Admin**
* **Therapist**
* **Parent**

### Protected Endpoints
* **Admin Portal** - Accessible exclusively by Admin users to view all registered users.
* **Therapist Portal** - Accessible exclusively by Therapist users for clinical endpoints.
* **Parent Portal** - Accessible exclusively by Parent users to view individual profile information.

---

## Tech Stack

* **Language:** Python
* **Core Framework:** FastAPI
* **Object-Relational Mapper:** SQLAlchemy
* **Database Engine:** SQLite
* **Token Handler:** JWT Authentication
* **Password Hashing Utility:** Passlib (with bcrypt backend)
* **Asynchronous Server:** Uvicorn

---

## Project Structure

```text
loonlet-auth-assignment/
│
├── app/
│   ├── main.py          # Application entry point & route definitions
│   ├── database.py      # SQLAlchemy configuration & engine setup
│   ├── core/            # Security configurations (JWT, hashing, secret keys)
│   ├── models/          # Database entities (SQLAlchemy Models)
│   ├── routers/         # Main application API endpoints split by logic
│   └── schemas/         # Input/Output data validation models (Pydantic)
│
├── requirements.txt     # Complete project dependencies list
├── README.md            # System documentation
└── loonlet_auth.db      # Local relational SQLite database

Installation & Setup
Step 1: Clone the Repository
git clone [https://github.com/madhav044/loonlet-auth-assignment.git](https://github.com/madhav044/loonlet-auth-assignment.git)
cd loonlet-auth-assignment

Step 2: Create and Activate Virtual Environment
On Windows:
python -m venv venv
venv\Scripts\activate

On macOS / Linux:
python -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Run the Project
To start the local development server, run:
python -m uvicorn app.main:app --reload

Local Server URL: http://127.0.0.1:8000

Interactive Swagger UI Documentation: http://127.0.0.1:8000/docs

API Endpoints Blueprint
Public Endpoints
1. Register User
Route: POST /register

Request Body (JSON):
{
  "name": "Madhav",
  "email": "madhav@example.com",
  "password": "password123",
  "role": "parent"
}

2. Login User
Route: POST /login

Request Body (JSON):

{
  "email": "madhav@example.com",
  "password": "password123"
}
API Response (JSON):
{
  "access_token": "jwt_token",
  "token_type": "bearer",
  "role": "parent"
}

Protected Endpoints (RBAC Enforced)
Admin Portal (GET / POST) : Accessible exclusively by verified Admin roles (e.g., View all registered users).

Therapist Portal (GET / POST) : Accessible exclusively by verified Therapist roles.

Parent Portal (GET / POST) : Accessible exclusively by verified Parent roles (e.g., View profile information).

Security Features
Stateless JWT Validation - Intercepts and verifies incoming authorization headers safely.

Cryptographic Hashing - Secures application records against credential breach vulnerabilities.

Granular RBAC Guards - Uses dependency injection to handle role filtering inline.

Strict Input Validation - Leverages Pydantic schemas to block malformed requests.

Secure Local Database Storage - Structured schema isolation for user profiles.

Database Schema Details (SQLite)
The core database model maps the following structured properties:

ID : Integer (Primary Key, Auto-Increment)

Name : String (User Identification)

Email : String (Unique Constraint, Indexed)

Password : String (Securely Salted Cryptographic Hash)

Role : String (Defines RBAC mapping permissions)

Repository
GitHub Project Link: https://github.com/madhav044/loonlet-auth-assignment

Author Profile
Developer Name: Madhav Chand

Email Contact: 2200032610cseh@gmail.com