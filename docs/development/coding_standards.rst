Coding Standards
================

Overview
--------

Adhering to consistent coding standards is essential for maintaining a high-quality codebase in Python-OC-Lettings-FR. This guide outlines the conventions and best practices to follow when contributing to the project.

General Guidelines
------------------

- **Consistency:** Follow the existing style of the codebase. Consistency across the project is more important than following any single style guide.
- **Readability:** Write code that is easy to read and understand. Prioritize clarity over cleverness.
- **Comments:** Use comments to explain the purpose of the code, especially for complex logic. Avoid obvious comments that do not add value.

Python Style Guide
------------------

Python-OC-Lettings-FR follows the PEP 8 style guide, which is the de facto standard for Python code. Key points include:

- **Indentation:** Use 4 spaces per indentation level.
- **Line Length:** Limit all lines to a maximum of 79 characters.
- **Blank Lines:** Use blank lines to separate functions and classes, and to separate logical sections within a function.
- **Imports:**
  - Imports should be grouped in the following order: standard library imports, related third-party imports, and local application imports.
  - Each group of imports should be separated by a blank line.

Example:

.. code-block:: python

   import os
   import sys

   from django.conf import settings
   from django.core.exceptions import ValidationError

   from .models import Profile

- **Naming Conventions:**
  - Use snake_case for function and variable names.
  - Use CamelCase for class names.
  - Constants should be written in UPPERCASE.

- **Docstrings:** Use PEP 257 conventions for docstrings. Every module, class, and function should have a docstring.

Example:

.. code-block:: python

   def fetch_data():
       """
       Fetch data from the API.

       Returns:
           dict: The data retrieved from the API.
       """
       pass

Django-Specific Conventions
---------------------------

- **Models:**
  - Model classes should inherit from django.db.models.Model.
  - Use descriptive names for fields and related attributes.
  - Define __str__() methods for models to provide meaningful string representations.

Example:

.. code-block:: python

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField()

       def __str__(self):
           return self.user.username

- **Views:**
  - Use class-based views (CBVs) where appropriate for better reusability and organization.
  - If a view is simple and does not require class-based functionality, function-based views (FBVs) are acceptable.

- **Templates:**
  - Follow Django’s template language conventions.
  - Organize templates in a clear directory structure, typically under an app's templates directory.

Linting
-------

To enforce coding standards, Python-OC-Lettings-FR uses flake8 for linting. It checks the code for compliance with PEP 8 and other coding standards.

Running Linting
---------------

Activate Your Virtual Environment

If not already activated:

.. code-block:: bash

   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\Activate.ps1  # Windows

Run flake8

Use flake8 to check your code:

.. code-block:: bash

   flake8

This command will scan your codebase and output any violations of the coding standards.

flake8 Configuration
---------------------

You can configure flake8 to match project-specific needs by modifying the .flake8 configuration file in the root of the project.

Example .flake8:

.. code-block:: ini

   [flake8]
   max-line-length = 79
   exclude = migrations,venv

Best Practices
--------------

- **DRY (Don’t Repeat Yourself):** Avoid duplication in your code by abstracting common functionality into functions or classes.
- **KISS (Keep It Simple, Stupid):** Write simple and straightforward code that is easy to understand and maintain.
- **YAGNI (You Aren’t Gonna Need It):** Avoid adding functionality until it is necessary.

Reviewing Code
--------------

Before merging any changes, ensure that:

- The code adheres to the standards outlined in this guide.
- All tests pass successfully.
- The code is well-documented, with meaningful comments and docstrings.

Conclusion
----------

Consistently following these coding standards helps maintain a high-quality, readable, and maintainable codebase. All contributors are expected to adhere to these guidelines to ensure that Python-OC-Lettings-FR remains robust and easy to work on.