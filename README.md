# BudgetManagement
# Balance - Backend Development for Expense and Income Management Application

Welcome to the backend project for the "Balance" expense and income management application. This project develops the crucial infrastructure for an application designed to help users wisely manage their monthly budget.

## System Specification

### Database
Data management in the application will be handled using MongoDB, an innovative and popular database system.

### Server-Side
Server-side development will be done in Python, a popular and efficient programming language.

### Routing
The application offer the following routing functionalities:

- **User Routes**: Including registration, login, and profile updates.
- **Transaction Routes**: Including creation, update, deletion, and retrieval of data related to user transactions.
- **Visualization Route**: Option to retrieve data in a format suitable for visualization using the matplotlib library.

### Quality Assurance
Developers will write tests to assess system performance, as per their understanding.

## File Summary
    
    ├─ app\                             
    │  ├─ db_managment\                 Database management
    │  │  └─ config_db.py               Database connection code
    │  ├─ models\                       
    │  │  ├─ operation_model.py         Model for transaction operation
    │  │  ├─ userDetails_model.py       Model for user name & password
    │  │  └─ user_model.py              Model for user
    │  ├─ routers\                      
    │  │  ├─ operation_router.py        Routes for transaction operations
    │  │  ├─ statistics_router.py       Routes for data statistics
    │  │  └─ user_router.py             Routes for user operations
    │  ├─ services\                     
    │  │  ├─ operation_service.py       Logic for transaction operations
    │  │  ├─ statistics_service.py      Logic for data statistics
    │  │  └─ user_service.py            Logic for user operations
    ├─ tests\                           
    │  ├─ test_operation.py             tests for operation_router page
    │  ├─ test_statistics.py            tests for statistics_router page
    │  └─ test_user.py                  tests for user_router page
    ├─ utils\                           
    │  └─ logger.py                     Decorator for logs
    ├─ .gitignore                       Project gitignore file  
    ├─ README.md                        Project README file
    ├─ main.py                          Main application logic
    └─ requirements.txt                 Dependencies for the project
        
## Installation and Execution

1. Install all the required dependencies for the project.
2. Run the command `pip install -r requirements.txt` to install all necessary packages.
3. Run the command `python main.py` to start the server.