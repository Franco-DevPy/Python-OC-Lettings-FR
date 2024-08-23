Testing
=======

Overview
--------

Testing is an essential part of ensuring that your Django application functions correctly and maintains its integrity as it evolves. This guide covers how to run unit tests, integration tests, and manage test coverage for Python-OC-Lettings-FR.

Running Tests
-------------

To ensure that your application is working correctly, you need to run tests regularly. Python-OC-Lettings-FR uses pytest for running tests.

Prerequisites
-------------

Make sure you have the necessary dependencies installed. You should have already set up your environment and installed dependencies as described in the Installation guide.

Running Tests with pytest
-------------------------

Activate Your Virtual Environment

If you have not already activated your virtual environment, do so with:

.. code-block:: bash

    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\Activate.ps1  # Windows

Run Tests

Use pytest to run your tests:

.. code-block:: bash

    pytest

This command will discover and run all the tests in your project. By default, pytest will look for files named test_*.py or *_test.py and execute any functions within those files that are prefixed with test_.

Test Coverage
-------------

To ensure that your tests cover a significant portion of your codebase, you can use the coverage tool.

Install Coverage

If you haven’t installed coverage, you can add it to your project:

.. code-block:: bash

    pip install coverage

Run Coverage

To measure coverage, run:

.. code-block:: bash

    coverage run -m pytest

This command will run your tests and measure code coverage.

Generate Coverage Report

After running tests, you can generate a report:

.. code-block:: bash

    coverage report

For a more detailed HTML report, you can run:

.. code-block:: bash

    coverage html

This will create an htmlcov directory with an HTML report. You can open htmlcov/index.html in your browser to view the coverage report.

Integration Tests
-----------------

Integration tests are designed to verify that different parts of the application work together as expected.

Running Integration Tests

Integration tests should be defined similarly to unit tests but focus on testing interactions between components. Ensure that any additional setup required for integration tests is included in your test suite.

Testing Best Practices
----------------------

- Write Tests for New Features: Always write tests for new features or bug fixes.
- Automate Tests: Use CI/CD pipelines to automate the running of tests on every commit or pull request.
- Keep Tests Fast: Write tests that run quickly to ensure you get feedback promptly.
- Test Edge Cases: Ensure that your tests cover not only typical use cases but also edge cases and error conditions.

Troubleshooting
---------------

If you encounter issues while running tests:

- Check Test Output: Review the output from pytest or coverage for details on what failed.
- Verify Dependencies: Ensure all required dependencies are installed and up-to-date.
- Consult Documentation: Refer to the documentation for pytest and coverage for additional help.

For more detailed information on pytest, visit the pytest documentation.