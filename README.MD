# Product Management System

## Description

This repository contains a Django web application designed for a django project.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Ajin28/bcg_backend.git
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   # Or
   venv\Scripts\activate  # For Windows

   ```

3. Navigate to the project directory:

   ```bash
   cd bcg_backend

   ```



4. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Update .env with Database configs:



6. Apply migrations:

   ```bash
   python manage.py migrate
   ```
   

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://127.0.0.1:8000/`.

9. Access Admin Protal at - `http://localhost:8000/admin/login`

10. Postman Collection File - bkc backend.postman_collection.json
