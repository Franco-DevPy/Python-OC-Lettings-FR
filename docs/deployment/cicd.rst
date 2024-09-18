CI/CD Deployment Guide
======================

This section outlines how to set up Continuous Integration (CI) and Continuous Deployment (CD) for the **Python-OC-Lettings-FR** application using GitHub Actions. CI/CD helps automate the process of building, testing, and deploying the application, ensuring that changes are integrated and deployed efficiently.

Overview
--------

CI/CD involves automating the following stages:

1. **Continuous Integration (CI)**: Automatically build and test the application whenever changes are made to the codebase.
2. **Continuous Deployment (CD)**: Automatically deploy the application to a production or staging environment once the code passes all tests.

In this guide, we'll use GitHub Actions to configure CI/CD workflows for the Django application.

Setting Up GitHub Actions
--------------------------

1. **Configure Secrets**:
    - Go to the repository settings on GitHub and navigate to `Secrets and variables` > `Actions`.
    - Add the following secrets:
        - `DOCKER_USERNAME`: Your Docker Hub username.
        - `DOCKER_PASSWORD`: Your Docker Hub password.
        - `HEROKU_API_KEY`: Your Heroku API key.
        - `HEROKU_APP_NAME`: Your Heroku application name.

2. **Push Changes**:
    - Commit and push the `.github/workflows/ci-cd-pipeline.yml` file to the repository. The CI/CD pipeline will automatically run based on the configuration.

Using the CI/CD Pipeline
------------------------

1. **Automatic Deployment**:
    - When you push changes to the `deploy-prod` branch, the CI/CD pipeline will automatically build the Docker image, push it to Docker Hub, and deploy it to the production environment on Heroku.
    - When you push changes to the `deploy-test` branch, the pipeline will deploy the Docker image to a test environment.

2. **Manual Triggers**:
    - You can manually trigger the pipeline using the GitHub Actions interface under the `Actions` tab of your repository.

3. **Monitoring and Debugging**:
    - Monitor the progress of your workflows and check logs for each step in the GitHub Actions tab.
    - If a workflow fails, review the logs to identify and resolve the issue.

Deploying to Production
-----------------------

1. **Branch Setup**:
    - Ensure that your production-ready code is pushed to the `deploy-prod` branch.

2. **Pipeline Execution**:
    - The pipeline will automatically trigger when changes are pushed to the `deploy-prod` branch. The steps involved are:
        - **Checkout code**: Retrieves the code from the GitHub repository.
        - **Set up Python**: Configures Python 3.9 on the runner.
        - **Install dependencies**: Installs the required Python packages.
        - **Run database migrations**: Applies any pending migrations.
        - **Run flake8**: Checks the code for PEP8 compliance.
        - **Run tests**: Executes the Django tests and generates a coverage report.
        - **Build Docker image**: Builds the Docker image for the application.
        - **Push Docker image**: Pushes the Docker image to Docker Hub.
        - **Log in to Heroku Container Registry**: Authenticates with Heroku.
        - **Pull Docker image from Docker Hub**: Retrieves the Docker image from Docker Hub.
        - **Tag Docker image for Heroku**: Tags the Docker image for Heroku deployment.
        - **Push Docker image to Heroku**: Pushes the Docker image to Heroku.
        - **Release the app on Heroku**: Deploys the Docker image to the Heroku application.
        - **Run database migrations on Heroku**: Applies any pending migrations on the Heroku database.

3. **Post-Deployment**:
    - After the deployment is complete, monitor the application on Heroku to ensure it is running correctly.
    - Use the Heroku CLI to check logs and troubleshoot any issues:

      ```bash
      heroku logs --tail --app your-heroku-app-name
      ```

Troubleshooting
---------------

- **Workflow Failures**: Ensure all secrets are correctly configured and that the Dockerfile is correctly set up.
- **Build Issues**: Verify that the Dockerfile and application dependencies are correct.
- **Deployment Issues**: Check deployment logs and ensure that Docker containers are correctly configured.

Additional Resources
---------------------

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Heroku Documentation](https://devcenter.heroku.com/)

---

### Explanation

- **Overview**: Describes the purpose and benefits of CI/CD.
- **Setting Up GitHub Actions**: Guides users through configuring secrets and pushing changes to trigger the pipeline.
- **Using the CI/CD Pipeline**: Explains how automatic and manual triggers work and how to monitor the pipeline.
- **Deploying to Production**: Provides detailed steps for deploying to the production environment.
- **Troubleshooting**: Provides guidance on resolving common issues that may arise during the CI/CD process.