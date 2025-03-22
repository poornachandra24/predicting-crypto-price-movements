# Predicting Crypto Price Movements

This project focuses on developing and deploying a machine learning model to predict cryptocurrency price movements. It utilizes a fully serverless architecture for ease of deployment and maintenance.

## Project Structure

The project is organized as follows:

```
.
├── src/ # Source code
│ ├── baseline_model.py # Baseline model implementation
│ ├── data.py # Data loading utilities
│ ├── hyperparams.py # Hyperparameter tuning logic
│ ├── logger.py # Logging setup
│ ├── model_registry_api.py # Model registry integration (CometML)
│ ├── paths.py # Directory path management
│ ├── predict.py # Prediction API endpoint
│ ├── preprocessing.py # Data preprocessing and feature engineering
│ └── train.py # Model training logic
├── deployment-dir/ # Deployment-specific files
│ ├── cerebrium.toml # Cerebrium configuration
│ ├── main.py # Deployment entry point
│ └── src/ # Deployment source code (likely a subset of ../src)
├── LICENSE # License information
├── Makefile # Build and automation commands
├── pyproject.toml # Project dependencies and configuration (Poetry)
├── poetry.lock # Dependency lock file (Poetry)
├── README.md # Project documentation (this file)
└── set_environment_variables_template.sh # Environment variable template
```
**Directory Explanations:**

*   **`src/`**:  Contains the core logic of the project, separated into modules for maintainability.
*   **`deployment-dir/`**:  Holds files specifically needed for deploying the model as a service.  The `src/` subdirectory here likely contains a streamlined version of the code from the main `src/` directory, optimized for deployment.
*   **`LICENSE`**: Specifies the license under which the project is released (e.g., MIT, Apache 2.0).
*   **`Makefile`**:  Provides convenient commands for common tasks (building, training, deploying). This improves developer experience and ensures consistency.
*   **`pyproject.toml` and `poetry.lock`**: Manage project dependencies using [Poetry](https://python-poetry.org/), ensuring reproducible environments.
*   **`set_environment_variables_template.sh`**: A template for setting required environment variables (API keys, etc.).  This is crucial for security and configuration management.

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/predicting_crypto_price_movements.git
    cd predicting_crypto_price_movements
    ```

    **(Important: Replace `your-username` with the actual repository owner.)**

2.  **Install Dependencies (using Poetry):**

    ```bash
    poetry install
    ```

    This command creates a virtual environment and installs all project dependencies defined in `pyproject.toml`.  Using a virtual environment is critical for isolating project dependencies and avoiding conflicts.

## Tools

This project leverages a serverless stack:

*   **CometML:**  Used for experiment tracking (tracking model training runs, metrics, etc.) and as a model registry (storing and versioning trained models).
*   **Cerebrium:**  The deployment platform.  Provides a serverless environment for hosting the prediction API.
*   **GitHub Actions:**  Automates workflows such as data fetching, model training, and deployment.  This ensures consistency and reproducibility.

## Quick Start (5-Minute Demo)

To quickly see the system in action, follow these steps:

1.  **Initialize the Project:**

    ```bash
    make init
    ```
    This likely sets up the virtual environment and performs other initial setup tasks.

2.  **Set Environment Variables:**

    *   Edit `set_environment_variables_template.sh` and add your API keys for CometML and Cerebrium.
    *   Rename the file to `set_environment_variables.sh`.
    *   Source the file to set the environment variables:

        ```bash
        . ./set_environment_variables.sh
        ```
    **(Important: Never commit API keys or other secrets to version control.  `.gitignore` should include `set_environment_variables.sh`.)**

3.  **Download Data:**

    ```bash
    make data
    ```
    This fetches historical cryptocurrency data from Coinbase and saves it locally.

4.  **Train the Model:**

    ```bash
    make train
    ```
    This trains the machine learning model using the downloaded data.  Training progress and metrics will likely be logged to CometML.

5.  **Deploy the Model:**

    ```bash
    make deploy
    ```
    This deploys the trained model to Cerebrium, making it accessible as an API endpoint.

6.  **Set Endpoint URL and Re-run Environment Variables:**

    *   Obtain the endpoint URL from the Cerebrium deployment output.
    *   Add the `CEREBRIUM_ENDPOINT_URL` variable to your `set_environment_variables.sh` file.
    *   Re-source the file:

        ```bash
        . ./set_environment_variables.sh
        ```
    This ensures that any scripts or tools that need to interact with the deployed model know its location.

## Acknowledgments
Special thanks to [@Paulescu](https://github.com/Paulescu) for his contributions and insights that inspired this project. 