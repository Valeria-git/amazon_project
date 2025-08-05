# Amazon Project (UI Automation with Selenium and PyTest)

## Note

You shoul have your own account in Amazon to run tests

## How to Run Tests

Make sure you are in the root directory of the project. Then run the following command:

```bash
python3 -m pytest -s -v
```

## Path Warning: sys.path.append(...)

In some modules, the following line is used to manually set the import path:

```python
import sys
sys.path.append("/Users/your_name/Desktop/amazon_project")
```

This was added during development to enable local imports.

**Important:** You should change the path to reflect the location of the project on your machine. For example:

```python
sys.path.append("/home/your_username/projects/amazon_project")
```

## Requirements

- Python 3.12 or higher
- Selenium
- PyTest



## Project Structure

```
amazon_project/
│
├── base/          
├── pages/          # Page Object Model classes
├── tests/          # PyTest test cases
├── screens/        # Screens as results of tests
├── utils/          # Utility modules (ignored via .gitignore)
└── README.md
```


## Credentials File

The project uses a `credentials.json` file located in the `utils/` directory to store login credentials such as email and password.

**Note:** This file is excluded from version control using `.gitignore`.

You must create your own `credentials.json` file with the following structure:

```json
{
  "email": "your_email@example.com",
  "password": "your_password"
}