# WebCalc
Simple Web Calculator App

This Flask application provides a simple web interface for performing arithmetic calculations. It safely evaluates arithmetic expressions entered by the user, using Abstract Syntax Trees (AST) to prevent the execution of unauthorized code.

## Features

- **Safe Evaluation**: Utilizes AST for the safe evaluation of arithmetic expressions, preventing the execution of potentially harmful code.
- **Support for Basic Operations**: Supports addition, subtraction, multiplication, division, exponentiation, and negation.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Gunicorn (for production deployment)

### Installation

1. Clone the repository: git clone https://github.com/RadLud/WebCalc/
2. Navigate to the project directory
3. Install the required Python packages: pip install -r requirements.txt

### Running the Application

1. Start the Flask application: 'flask run' or 'python -m flask run'
2. Access the application in your web browser at `http://127.0.0.1:5000/`.

### Deployment

For production environments, it is recommended to use Gunicorn as the WSGI HTTP Server: 'gunicorn app:app'

## Usage

- The application presents a simple form where users can input arithmetic expressions.
- After submitting the form, the application displays the result of the evaluated expression.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

