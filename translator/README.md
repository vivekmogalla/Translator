# Translation Application

## Overview

Translation Application is a Python-based web application that provides translation service. It allows users to translate text and documents between different languages using various translation pipelines.

## Features
- **Translate text between multiple languages**
- **Translate word documents using different translation pipelines.**
- **Support various content types and target languages**

### Prerequisites

- Python 3.6+
- Django 3.0+

### Installation Steps

1. Clone the repository:

        git clone https://github.com/your-username/translation-app.git3

2. Navigate to the Project directory
 
        cd translation-app

3. Install the required Python packages

        pip install -r requirements.txt

4. Set up your database (e.g SQLite, MYSQL, PostGresql) and configure the database settings in 'settings.py'


5. Run database migrations

        python manage.py migrate

6. Create a superuser account (for admin access)

        python manage.py createsuperuser
7. Start the development server:

        python manage.py runserver

8. Access the Application at 'http://localhost:8000' in your web browser

