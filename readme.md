# API Client and Data Parser

## Project Overview

This project is a simple Python application that demonstrates how to fetch data from a REST API, parse and validate the response, and test the application using Python's `unittest` framework.

The project follows an object-oriented approach by organizing the API client and data parser into separate classes.

## Features

- **API Client:** Fetches user information from a REST API using the `requests` library.
- **Data Parser:** Validates user data and cleans text fields.
- **Error Handling:** Handles HTTP errors and invalid or missing data.
- **Unit Testing:** Tests API client functionality and data parsing using `unittest` and mock objects.
- **Modular Structure:** Separates API communication, data parsing, application execution, and testing.

## Project Structure

```text
api_client_project/
├── api_client.py
├── data_parser.py
├── main.py
├── test_api_client.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- Requests
- REST API
- JSON
- Object-Oriented Programming (OOP)
- Unit Testing (`unittest`)
- Mocking (`unittest.mock`)
- Git and GitHub

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd api_client_project
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not yet configured, add the following line:

```text
requests
```

## Running the Application

Run the main Python file:

```bash
python main.py
```

The application uses the API client to fetch user data and the parser to validate and clean the response.

## Running Unit Tests

Run all unit tests using:

```bash
python -m unittest -v test_api_client.py
```

The tests cover:

- Parsing valid user data.
- Removing unnecessary whitespace.
- Converting email addresses to lowercase.
- Detecting missing fields.
- Rejecting empty names.
- Fetching user data successfully.
- Handling HTTP errors.

Mock objects are used to test API behavior without making actual HTTP requests.

## Learning Objectives

This project demonstrates how to:

1. Create reusable Python classes.
2. Make HTTP requests to a REST API.
3. Process JSON responses.
4. Validate and clean data.
5. Write unit tests for different scenarios.
6. Use mocks to isolate external API dependencies.
7. Organize a Python project into separate modules.

## Future Improvements

- Add stronger email and data-type validation.
- Handle network timeouts and connection errors.
- Add logging for debugging.
- Support fetching multiple users.
- Expand unit test coverage.

## Author

Sidharth Pramod PP
