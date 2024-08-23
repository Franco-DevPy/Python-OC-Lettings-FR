Automated Heroku Deployment
===========================

This section explains how the **Python-OC-Lettings-FR** application is automatically deployed to Heroku using GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

Overview
--------

The deployment process is fully automated using a CI/CD pipeline. Whenever changes are pushed to specific branches (`deploy-test` or `deploy-prod`), the pipeline is triggered. The CI/CD pipeline handles:

- Running tests and linting the code.
- Building a Docker image.
- Pushing the Docker image to Docker Hub.
- Deploying the application to Heroku.

Pipeline Structure
------------------

The CI/CD pipeline is defined in the `.github/workflows/ci.yml` file and consists of three main jobs:

1. **CI for Django Application (ci-django):**
   - **Checkout code:** Retrieves the code from the GitHub repository.
   - **Set up Python:** Configures Python 3.9 on the runner.
   - **Install dependencies:** Installs the required Python packages.
   - **Run database migrations:** Applies any pending migrations.
   - **Run flake8:** Checks the code for PEP8 compliance.
   - **Run tests:** Executes the Django tests and generates a coverage report.

2. **Build and Push Docker Image (build-and-push-docker-image):**
   - **Checkout code:** Retrieves the code from the GitHub repository.
   - **Set up Docker Buildx:** Prepares Docker Buildx for multi-platform builds.
   - **Login to DockerHub:** Logs in to Docker Hub using credentials stored in GitHub Secrets.
   - **Build and push Docker image:** Builds the Docker image and pushes it to Docker Hub.

3. **Deploy to Heroku (deploy-test and deploy-prod):**
   - **Pull Docker image:** Retrieves the Docker image from Docker Hub.
   - **Run Docker container:** Starts a Docker container on Heroku.
   - **Wait for Docker container:** Pauses to ensure the container is ready.
   - **Collect static files:** Collects static files using Django’s `collectstatic` command.
   - **Run database migrations:** Applies any pending migrations.

Branch-Specific Deployment
---------------------------

- **Test Environment Deployment (deploy-test):**
    - Triggered by pushing to the `deploy-test` branch.
    - Deploys the application to the test environment.

- **Production Environment Deployment (deploy-prod):**
    - Triggered by pushing to the `deploy-prod` branch.
    - Deploys the application to the production environment.

Environment Configuration
--------------------------

- **GitHub Secrets:** The pipeline relies on several secrets stored in the GitHub repository:
    - `DOCKER_USERNAME`: Docker Hub username.
    - `DOCKER_PASSWORD`: Docker Hub password.
    - `HEROKU_API_KEY`: Heroku API key.
    - `HEROKU_APP_NAME`: Heroku app name.

Ensure these secrets are configured in your GitHub repository before running the pipeline.

Running the Pipeline
--------------------

To trigger the deployment pipeline, simply push your changes to one of the deployment branches:

- For testing: `git push origin deploy-test`
- For production: `git push origin deploy-prod`

The pipeline will automatically run, and you can monitor its progress in the "Actions" tab of your GitHub repository.

Troubleshooting
---------------

- **Pipeline Failures:** If the pipeline fails at any stage, check the logs in the GitHub Actions interface for details.
- **Deployment Issues:** If the deployment fails, ensure that the Heroku app and Docker image are correctly configured. Use the Heroku CLI to inspect logs:

    .. code-block:: bash

        heroku logs --tail --app your-heroku-app-name

Additional Resources
---------------

- `Heroku Documentation <https://devcenter.heroku.com/>`
- `GitHub Actions Documentation <https://docs.github.com/en/actions>`
- `Docker Documentation <https://docs.docker.com/>`

---

### Explanation

- **Overview**: Summarizes the automated deployment process.
- **Pipeline Structure**: Breaks down the steps involved in the CI/CD pipeline.
- **Branch-Specific Deployment**: Explains how deployments are tied to specific branches.
- **Environment Configuration**: Details the necessary secrets and their purpose.
- **Running the Pipeline**: Instructions on how to trigger the deployment.
- **Troubleshooting**: Offers solutions to common issues during deployment.

This guide will help users and developers understand how the application is deployed to Heroku and what steps are involved in the CI/CD pipeline.