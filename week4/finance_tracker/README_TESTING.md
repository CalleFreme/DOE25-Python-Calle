# Finance Tracker Testing

This directory contains comprehensive tests for the Finance Tracker application.

## Test Structure

- `test_transaction_class.py` - Tests for the Transaction class
- `test_finance_tracker.py` - Tests for the main finance tracker functions
- `pytest.ini` - Pytest configuration
- `requirements-test.txt` - Testing dependencies

## Running Tests Locally

### Prerequisites

Make sure you have Python installed, then install the test dependencies:

```bash
pip install -r requirements-test.txt
```

### Run All Tests

```bash
# Run all tests with coverage
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=term-missing
```

### Run Specific Tests

```bash
# Run only Transaction class tests
pytest test_transaction_class.py

# Run only finance tracker function tests
pytest test_finance_tracker.py

# Run specific test method
pytest test_transaction_class.py::TestTransaction::test_init_with_all_parameters
```

### Test Coverage

The tests aim for high coverage of critical functionality:

- **Transaction Class**: 100% coverage of all methods
- **Core Functions**: Comprehensive testing of business logic
- **File Operations**: Mocking file I/O for reliable testing
- **Error Handling**: Testing error conditions and edge cases

Current coverage target: **80%** minimum

### What's Tested

#### Transaction Class Tests
- ✅ Initialization with all parameters
- ✅ Default parameter handling
- ✅ String representations (`__str__`, `__repr__`)
- ✅ Comparison methods (`__lt__`, `__eq__`)
- ✅ Sign calculation for income/expense
- ✅ Sorting functionality

#### Finance Tracker Function Tests
- ✅ Adding transactions to lists
- ✅ Balance calculation (income, expense, mixed)
- ✅ File reading and writing operations
- ✅ Error handling for invalid data
- ✅ Menu display functionality
- ✅ Integration between functions

#### Edge Cases Covered
- Empty transaction lists
- Invalid amount data
- File I/O errors
- Missing files
- Malformed data

## GitHub Actions CI/CD

The project includes automated testing via GitHub Actions:

- **Multi-Python Version Testing**: Tests run on Python 3.8, 3.9, 3.10, 3.11
- **Code Quality Checks**: Black formatting, isort import sorting
- **Security Scanning**: Bandit security analysis  
- **Coverage Reporting**: Codecov integration
- **Linting**: Flake8 code style checks

### Workflow Triggers

Tests run automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches
- Changes to files in `week4/finance_tracker/` directory

## Bug Fixes Applied

The following bugs were identified and fixed in the original code:

1. **Function Parameter Order**: Fixed `add_transaction(transaction, transactions)` call order
2. **Missing Parameter**: Added missing `transactions` parameter to `write_financial_data_to_file()` call

## Code Quality Standards

Tests follow these standards:
- Descriptive test names explaining what's being tested
- Comprehensive docstrings for test classes and methods
- Proper use of pytest fixtures and mocking
- Clear assertions with meaningful error messages
- Separation of unit tests, integration tests, and edge cases

## Running Code Quality Tools

```bash
# Format code with Black
black .

# Sort imports with isort  
isort .

# Run linting
flake8 .

# Security scan
bandit -r .
```

## Test Maintenance

- Add tests for any new functionality
- Update tests when modifying existing functions
- Maintain high coverage (80%+ target)
- Test both positive and negative scenarios
- Include integration tests for critical workflows