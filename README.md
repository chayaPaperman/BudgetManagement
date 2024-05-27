# BudgetManagement
# Balance - Backend Development for Expense and Income Management Application

Welcome to the backend project for the "Balance" expense and income management application. This project develops the crucial infrastructure for an application designed to help users wisely manage their monthly budget.

## System Specification

### Server-Side
A server-side development written in Python

### Database
Data management in the application handled using MongoDB, an innovative and popular database system.

### Quality Assurance
Writen tests to assess system performance

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
        

# Routing
The application offer the following routing functionalities:

## User Router
Including registration, login, and profile updates.


| HTTP Method | Route                    | Function          | Description                              |
|-------------|--------------------------|-------------------|------------------------------------------|
| POST        | /signup                  | signup            | Register a new user                      |
| POST        | /login                   | login             | User login                               |
| PUT         | /update_details/{user_id} | update_details    | Update user details by user ID           |
| GET         | /all_users               | get_all_users     | Retrieve all users                       |


## Operation Router
Including creation, update, deletion, and retrieval of data related to user transactions.


| HTTP Method | Route                  | Function        | Description                                     |
|-------------|------------------------|-----------------|-------------------------------------------------|
| GET         | /getBalance/{user_id} | get_balance     | Retrieve balance of a specific user             |
| GET         | /getAllRevenues/{user_id} | get_all_revenues | Retrieve all revenues of a specific user      |
| GET         | /getAllSpending/{user_id} | get_all_spending | Retrieve all spending of a specific user      |
| POST        | /add                   | add             | Add a new operation                            |
| PUT         | /update/{operation_id} | update          | Update an existing operation by unique ID       |
| DELETE      | /delete/{operation_id} | delete          | Delete an existing operation by unique ID       |

## Statistics Router
 Option to retrieve data in a format suitable for visualization using the matplotlib library.


| HTTP Method | Route            | Function             | Description                               |
|-------------|------------------|----------------------|-------------------------------------------|
| GET         | /users_balance   | balance_statistics   | Retrieve statistics for users' balance    |

## Installation and Execution

1. Install all the required dependencies for the project.
2. Run the command `pip install -r requirements.txt` to install all necessary packages.
3. Run the command `python main.py` to start the server.








