# Intermediate Software Development Automated Teller Project
This project will be developed through several assignments, each building on the previous ones. Ultimately, an entire system will be created to manage bank transactions for clients with one or more bank accounts.

## Author
Lovedeep Singh Sidhu

## Assignment 01: Classes, Encapsulation, and Unit Test Planning
In Assignment 01, the focus is on creating foundational classes that implement encapsulation through private variables and public methods. The `BankAccount` class safeguards sensitive information like `account_number`, `client_number`, and `balance`, allowing modifications only through controlled methods such as `deposit` and `withdraw`. The `Client` class similarly protects personal details, providing access via getter methods while preventing direct changes. This approach enhances data integrity and ensures proper usage of the classes. Thorough documentation and meaningful naming conventions improve readability and maintainability, laying the groundwork for future assignments.

## Assignment 02: Banking System Implementation
In the second assignment, the banking system is implemented by extending the `BankAccount` class into specialized subclasses: `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount`. Each subclass has distinct attributes and methods that define its behavior, further applying the principles of encapsulation. Polymorphism is utilized through the `get_service_charges` method, which each account type implements according to its specific rules. For instance, `ChequingAccount` incorporates its overdraft limit, while `SavingsAccount` imposes fees if the balance dips below a minimum. This design enables a unified interface for service charge calculation while allowing for tailored behaviors based on account type. Overall, the structure enhances code flexibility and maintainability.

## Assignment 03: Strategy and Observer Patterns
The third assignment enhances the banking application by implementing the Strategy and Observer design patterns. The Strategy Pattern is utilized to manage the calculation of service charges for various bank account types, allowing for the selection of algorithms at runtime and promoting flexibility and maintainability. The Observer Pattern is employed to keep clients informed of important account updates, such as balance changes or significant transactions, ensuring that they remain up-to-date with their account activities. This automatic notification system streamlines client engagement and enhances the overall user experience.

## Assignment 04: Event-Driven Programming Paradigm
By utilizing signal-slot , which allows user actions (such as button clicks or table selections) to trigger particular methods (slots), this application uses the event-driven programming model. The event loop of the Application handles events asynchronously to maintain the app's responsiveness. Signals are used to control UI changes and interactions, enabling communication between many components without obstructing the main thread. Event responses are used to dynamically provide error handling and user feedback.
