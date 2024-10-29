# Intermediate Software Development Automated Teller Project
This project will be developed through several assignments, each building on the previous ones. Ultimately, an entire system will be created to manage bank transactions for clients with one or more bank accounts.

## Author
Lovedeep Singh Sidhu

## Assignment 01: Classes, Encapsulation, and Unit Test Planning
In the first assignment, the focus is on creating foundational classes that utilize private variables and public methods for accessing and modifying those variables. The goal is to establish a well-structured framework that will be built upon in future assignments. Each class will be thoroughly documented with clear, meaningful names to enhance readability and maintainability.

## Encapsulation
Encapsulation is a core principle of object-oriented programming that involves hiding a class's internal workings from the outside world. This is achieved through private attributes and public methods. In the `BankAccount` class, important details such as `account_number`, `client_number`, and `balance` are kept private, and modifications to the balance are controlled via public methods like `deposit` and `withdraw`. Similarly, the `Client` class protects personal details, allowing access through getter methods while preventing direct changes to the internal data. This practice safeguards the integrity of the data and ensures correct usage of the classes.

## Assignment 02: Banking System Implementation
The second assignment introduces the implementation of the banking system, where the concepts of encapsulation are further applied. Each account type—such as `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount`—is implemented as a subclass of `BankAccount`, with specific attributes and methods that dictate their behavior.

## Polymorphism
Polymorphism is leveraged in the banking system through the `get_service_charges` method, which is defined in each subclass of `BankAccount`. Each account type provides its own implementation for calculating service charges based on its unique attributes and rules. For example, `ChequingAccount` considers its overdraft limit, while `SavingsAccount` applies fees if the balance falls below a minimum threshold. This allows for a unified interface while retaining the flexibility to handle specific behaviors of different account types.

## Assignment 03: Strategy and Observer Patterns
The third assignment enhances the banking application by implementing the Strategy and Observer design patterns. The Strategy Pattern is utilized to manage the calculation of service charges for various bank account types, allowing for the selection of algorithms at runtime and promoting flexibility and maintainability. The Observer Pattern is employed to keep clients informed of important account updates, such as balance changes or significant transactions, ensuring that they remain up-to-date with their account activities. This automatic notification system streamlines client engagement and enhances the overall user experience.
