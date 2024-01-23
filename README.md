# Python Template Repository

This repository serves as a template for starting Python projects with integrated logging, notification features, and more. It utilizes the `loguru` library for comprehensive logging and demonstrates the implementation of a notification feature using the `notifiers` library. Additionally, it showcases the use of decorators and wrappers for function logging, including entry, exit, and execution time tracking.

## Features

- **Logging Levels:** The template code demonstrates the use of different logging levels to control the verbosity of the output. The following levels are showcased:

  - `DEBUG`
  - `INFO`
  - `ERROR`

- **Logging Decorator:** A `logger_wraps` decorator is provided, offering the capability to wrap functions for logging their entry, exit, and execution time. The decorator supports the following parameters:

  - `entry`: If `True`, logs the function entry.
  - `exit`: If `True`, logs the function exit and result.
  - `level`: The logging level to use.

- **Slack Notification (Optional):** The template includes commented-out code to send Slack notifications in case of errors. To enable this feature, follow these steps:
  1. Uncomment the lines related to Slack notification in the script.
  2. Ensure you've filled in the required Slack webhook URL in the `.env` file.

## Getting Started

Follow these steps to create a new Python project using this template:

1. Click the "Use this template" button at the top of the repository page to create a new repository based on this template.

2. Clone your newly created repository to your local machine:

   ```bash
        git clone https://github.com/yourusername/your-repo-name.git
        cd your-repo-name
        poetry install
   ```

Rename the .env.example file to .env and fill in the necessary values.

## Usage

Run the main script using the following command:

To test the logging example

    ```bash
        poetry run python log_example.py
    ```

The script will output logs of different levels and demonstrate the decorator's impact on the test_timeit function. The output will be displayed in the console.
