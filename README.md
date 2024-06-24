# Automation-UI

## Overview

This project is an automation framework for UI testing using Python, BDD (Behavior Driven Development) with Gherkin syntax, and Allure for reporting. It is designed to be scalable and maintainable, supporting automated UI tests for a booking application.

## Project Structure

Automation-UI/
├── Actions/
│ ├── pycache/
│ └── bookingAction.py
├── features/
│ └── booking.feature
├── pages/
│ ├── pycache/
│ └── booking_page.py
├── reports/
├── screenshots/
├── steps/
├── utils/
├── venv/
├── .env
├── .gitignore
├── environment.py
├── pytest.ini
├── README.md
└── requirements.txt


- **Actions**: Contains action classes that perform the actual steps described in the feature files.
- **features**: Contains feature files written in Gherkin syntax describing the test scenarios.
- **pages**: Contains page object classes representing the web pages of the application.
- **reports**: Directory for storing test reports.
- **screenshots**: Directory for storing screenshots taken during test execution.
- **steps**: Contains step definition classes where Gherkin steps are implemented.
- **utils**: Contains utility classes and functions.
- **venv**: Python virtual environment directory.
- **.env**: Environment variable configurations.
- **.gitignore**: Git ignore file.
- **environment.py**: Environment configuration file.
- **pytest.ini**: Pytest configuration file.
- **README.md**: Project documentation.
- **requirements.txt**: List of Python dependencies.

## Getting Started

### Prerequisites

- Python 3.8+
- Chrome browser
- ChromeDriver

### Setup

1. **Clone the repository**:
   ```bash
    git clone https://github.com/nanthakannan/Automation-UI.git
    cd Automation-UI

2. **Create and activate virtual environment**:  
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
    pip install -r requirements.txt

4. **Set up environment variables**:
    Create a .env file in the project root and add any required environment variables.

**Running Tests**

    behave -f allure_behave.formatter:AllureFormatter -o reports/ .\features - Run all Feature Files

    behave -f allure_behave.formatter:AllureFormatter -o reports/ --tags=@regression .\features - Runs all the feature files which has the tag name "regression" (change the tag name which needs to be executed)

**Generate Allure report**:

    allure serve reports/



This `README.md` provides a comprehensive overview of the project, including setup instructions, running tests, and generating reports. Make sure to update the `https://github.com/nanthakannan/Automation-UI.git` placeholder with your actual repository URL.




