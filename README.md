# Django Blog Post App

This is a simple Django app for managing blog posts on your website.

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/django-blog-post-app.git
cd blog_post
```

2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt
```

3. Apply Migration:
```python manage.py migrate```

4. Create a superuser account:
```python manage.py createsuperuser```

5. Run the development server:
```python manage.py runserver```

## Features

1. **User Authentication:** Utilizes Django's built-in authentication system for managing authors and administrators.

2. **Crud Operations:** Create, Read, Update, and Delete blog posts seamlessly through the admin interface.




