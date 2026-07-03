Installation & Setup
====================

Prerequisites
-------------

- Python 3.12+
- Git
- Docker (optional, for containerized deployment)

Local Development
-----------------

1. Clone the repository::

    git clone https://github.com/Franco-DevPy/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

2. Create and activate a virtual environment::

    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/Mac

3. Install dependencies::

    pip install -r requirements.txt

4. Create a ``.env`` file with the required environment variables::

    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    SENTRY_DSN=your-sentry-dsn  # optional

5. Run the development server::

    python manage.py runserver

The site will be available at http://localhost:8000.

Running Tests
-------------

::

    pytest --cov=. --cov-fail-under=80

Docker Deployment
-----------------

Build and run with Docker::

    docker build -t oc-lettings .
    docker run -p 8000:8000 --env-file .env oc-lettings

Required environment variables for production:

- ``SECRET_KEY`` — Django secret key
- ``DEBUG`` — set to ``False`` in production
- ``ALLOWED_HOSTS`` — comma-separated list of allowed hostnames
- ``SENTRY_DSN`` — Sentry DSN for error monitoring (optional)
