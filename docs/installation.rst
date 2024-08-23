Installation
============

This section will guide you through the steps needed to install and set up the **Python-OC-Lettings-FR** application on your local machine.

Prerequisites
-------------

Before starting the installation, ensure you have the following:

- A GitHub account with read access to this repository.
- `Git` installed on your machine.
- `Docker` and `Docker Compose` installed.
- (Optional) Python 3.9 or higher for a manual installation without Docker.

Cloning the Repository
-----------------------

Start by cloning the GitHub repository to your local machine:

.. code-block:: bash

    git clone https://github.com/MickaelFioretti/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

Installation with Docker
-----------------------

The application is containerized with Docker, which simplifies installation and execution. Follow these steps to set up and run the application with Docker.

1. Build and Run Docker Containers
    Ensure Docker and Docker Compose are installed on your machine. Then, use the following command to build and start the Docker containers:

        .. code-block:: bash

            docker compose up --build

    This command will:
    - Build the Docker images for the Django application.
    - Create and start the Docker containers.

2. Access the Application
    Once the containers are up and running, access the application by opening your browser and visiting:
    
        `http://localhost:8000`

3. Managing Containers
    To stop the containers, use the following command:

        .. code-block:: bash

            docker compose down

    To restart the containers without rebuilding them:
    
        .. code-block:: bash

            docker compose up

Installation without Docker (Optional)
-----------------------

If you prefer not to use Docker, you can install and run the application directly on your machine.

1. Create a Virtual Environment
    Create a Python virtual environment and activate it:
    
        .. code-block:: bash
        
            python3 -m venv env
            source env/bin/activate # On Windows, use venv\Scripts\activate.ps1

2. Install Dependencies
    Install the required dependencies from the requirements.txt file:
        
        .. code-block:: bash

            pip install -r requirements.txt

3. Run Database Migrations
    Apply the database migrations to set up the database schema:
    
        .. code-block:: bash

            python manage.py migrate

4. Start the Development Server
    Start the Django development server to run the application:
    
        .. code-block:: bash
            
            python manage.py runserver

5. Access the Application
    Open your browser and visit the following URL to access the application:
    
        `http://localhost:8000`



Common Issues
-----------------------

- Docker not starting: Ensure Docker is correctly installed and configured on your machine.
- Python dependency issues: Ensure you are using a virtual environment to isolate your project dependencies.