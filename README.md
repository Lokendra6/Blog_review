# Django Blog Application

## Overview
This is a simple blog application built using Django. It allows users to sign up, log in, create, update, and delete blog posts. Users can also view a list of all posts and see post details.

## Features
- User authentication (Signup, Login, Logout)
- Create, update, and delete posts (only by the author)
- View all blog posts
- View individual post details

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Django
- Virtual environment (optional but recommended)

### Installation Steps
1. **Clone the repository**:
  
   git clone <repository-url>
   cd <repository-folder>
   

2. **Create and activate a virtual environment (optional but recommended)**:
   
   python -m venv C:\Users\admin\venv
   C:\Users\admin\venv\Scripts\activate  # On Windows
   

3. **Generate `requirements.txt`** (if not already created):
  
   pip freeze > requirements.txt
   

4. **Install dependencies**:
   
   pip install -r requirements.txt
  

5. **Run database migrations**:
   
   python manage.py migrate
   

6. **Create a superuser (optional for admin access)**:
   
   python manage.py createsuperuser
   

7. **Run the development server**:
  
   python manage.py runserver
   

8. **Access the application**:
   Open your browser and visit `http://127.0.0.1:8000/`

## Usage
- **Sign Up/Login**: Users need to sign up or log in to create, update, or delete posts.
- **Create a Post**: Navigate to the create post page and fill in the required details.
- **Edit/Delete a Post**: Only the author of a post can edit or delete it.
- **View Posts**: Anyone can view the list of posts and their details.




