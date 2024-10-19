# OneDigital Assignment

## Features

- **Metrics Calculation**: 
  - Total spend
  - Average purchase value
  - Maximum purchase value
  - Median purchase value
  - Number of unique products purchased
- **Data Validation**: Validates that the input data contains valid types and values for critical fields such as `price`, `quantity`, and `product_name`.
- **Console Export**: Exports the calculated metrics to the console.

## Requirements

- Python 3.12.3
- Polars (for data manipulation)
- Click (for CLI)
- Pytest (for testing)

## Project Structure

```bash
.
├── Dockerfile               # Dockerfile to build the container
├── main.py                  # Main file with the CLI entry point
├── requirements.txt         # Project dependencies
├── input_file.json          # Sample input data. Add more files here and pass them as arguments to main.py
│   ├── purchases_v1.json   # Sample input data     
├── src
│   ├── console_exporter.py  # Console exporter implementation
│   ├── data_fetcher.py      # Data fetcher to load JSON data from file
│   ├── data_validator.py    # Data validator for ensuring input validity
│   ├── metrics_calculator.py# Metrics calculation logic
│   └── utils
│       └── logger.py        # Logger setup
└── tests                    # Unit tests for the application
```

## Running the Project

To run the project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ujjwalbatra/OneDigitalAssignment.git
    cd OneDigitalAssignment
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the CLI**:
    ```bash
    python main.py input_file/purchases_v1.json
    ```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Running the Project with Docker

To run the project using Docker, follow these steps:

1. **Build the Docker Image**:
    ```bash
    docker build -t onedigital-assignment .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -it onedigital-assignment input_file/purchases_v1.json  
    ```

This will build the Docker image and run the container, processing the default file `input_file/purchases_v1.json`. Make sure the `input_file` directory contains the `purchases_v1.json` file.
