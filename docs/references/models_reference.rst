Models Reference
=================

Overview
--------

This section provides detailed information about the Django models used in the Python-OC-Lettings-FR project. Each model represents a table in the database and contains the fields and relationships that define the data structure of the application.

Models
------

1. Profile
~~~~~~~~~~

**Description:** The Profile model extends the default Django User model to include additional information specific to users within the Orange County Lettings system.

**Fields:**

- **user:** A one-to-one relationship with Django’s built-in User model.
- **favorite_city:** A CharField to store the user’s favorite city.

**Example:**

.. code-block:: python

   from django.db import models
   from django.contrib.auth.models import User

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

**Relationships:**

- **User:** Each Profile is associated with one User.

2. Letting
~~~~~~~~~~

**Description:** The Letting model represents a property letting (rental) in the system. Each letting includes details about the property and is linked to an address.

**Fields:**

- **title:** A CharField that holds the title of the letting (e.g., "Beach House").
- **address:** A foreign key to the Address model.

**Example:**

.. code-block:: python

   from django.db import models

   class Letting(models.Model):
       title = models.CharField(max_length=255)
       address = models.ForeignKey('Address', on_delete=models.CASCADE)

**Relationships:**

- **Address:** Each Letting is associated with one Address.

3. Address
~~~~~~~~~~

**Description:** The Address model stores details about a property’s address, including the street name, city, state, and ZIP code.

**Fields:**

- **number:** A CharField to store the house number.
- **street:** A CharField for the street name.
- **city:** A CharField for the city.
- **state:** A CharField for the state.
- **zip_code:** A CharField for the ZIP code.
- **country_iso_code:** A CharField for the ISO country code.

**Example:**

.. code-block:: python

   from django.db import models

   class Address(models.Model):
       number = models.CharField(max_length=10)
       street = models.CharField(max_length=255)
       city = models.CharField(max_length=255)
       state = models.CharField(max_length=2)
       zip_code = models.CharField(max_length=10)
       country_iso_code = models.CharField(max_length=2)

**Relationships:**

- **Letting:** An Address can be linked to multiple Letting instances.

Using the Models
----------------

For more information on how to use these models, refer to the Django documentation on models. You can also generate diagrams of your models using tools like Django Extensions.