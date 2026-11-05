OOP-ASSIGNMENT

CITIZEN COMPLAINT SYSTEM

1. ABSTRACT
The Citizen Complaint System is a Python program designed to manage citizen complaints. It allows users to submit, view, search, update, and manage complaints. The system demonstrates the use of Object-Oriented Programming concepts. The project applies Object-Oriented Programming (OOP) concepts to organize complaint information into classes and objects. Each complaint record contains information such as the complaint identification number, category, description, citizen information, and status. The system provides a simple menu that allows users to select different operations. It is intended to demonstrate how programming can improve the organization and retrieval of complaint information. The project also provides practical experience in writing Python code, using classes and methods, testing a program, and documenting a software project.

2. INTRODUCTION
Managing citizen complaints manually can be time-consuming. This project provides a simple computer-based system for organizing and managing complaint information efficiently. Managing complaints manually can be time-consuming and may result in errors, duplicated information, or difficulty locating records. A computer-based system can help organize information and make basic record-management tasks easier. The Citizen Complaint System is designed to address these challenges by providing a simple application for managing citizen complaints. The system is developed using Python and applies Object-Oriented Programming principles. It allows users to enter complaint information, display stored complaints, search for specific complaints, and update existing information.

This project demonstrates the practical application of programming concepts to solve a simple information-management problem.

3. PROBLEM STATEMENT
Manual complaint management can lead to errors, misplaced information, and difficulties in following up complaints. Managing complaint information manually can create difficulties when records need to be located, checked, or updated.

4. AIM AND OBJECTIVES
Aim: To develop a simple Citizen Complaint System using Python.
Objectives:
- Submit new complaints.
- Display all complaints.
- Search for a complaint.
- Update complaint status.
- Manage complaint records.

5. SYSTEM REQUIREMENTS
Hardware: Computer or laptop.
Software:
- Windows 11 or another compatible operating system.
- Python.
- Visual Studio Code or another Python editor.

6. OBJECT-ORIENTED PROGRAMMING CONCEPT
The system demonstrates the following concepts:
- Class: Defines the structure of a citizen, complaint, or complaint system.
- Object: Represents an individual citizen or an individual complaint.
- Attribute: Stores data like citizen_id, complaint_id, category, description, and status.
- Method: Performs an action like submit_complaint, update_status, and display_complaints.
- Constructor: The init method used to create objects.
- Encapsulation: Data and methods are grouped together inside classes.
- Class Method: An alternative constructor like from_alias() and create_demo_system().
- Static Method: A method like valid_category() that checks if a category is allowed without needing an object.

7. SYSTEM DESIGN
The system has three main classes:

1. Citizen
- Attributes: citizen_id, alias
- Methods: identify(), from_alias()

2. Complaint
- Attributes: complaint_id, category, description, citizen, status
- Methods: update_status(), summary()

3. ComplaintSystem
- Attributes: office_name, complaints
- Methods: submit_complaint(), update_complaint(), display_complaints(), valid_category(), create_demo_system()

The Citizen class stores who made the complaint. The Complaint class stores the details of one complaint. The ComplaintSystem class stores all the complaints and manages them.

The demonstration uses fictional, non-sensitive data. No phone numbers, email addresses, home addresses, national ID numbers, passwords or other sensitive personal information are stored.

8. HOW TO RUN
1. Download the folder or clone the repo.
2. Open terminal.
3. Run: python main.py
4. To run tests: python -m pytest test_main.py

9. SAMPLE OUTPUT
--- Community Services Desk: Complaint Register ---
CMP-301 | Waste | Under Review | Aminata Koroma (CIT-104) | Collection point near the market has not been cleared.
CMP-302 | Roads | Submitted | Daniel Bangura (CIT-219) | A damaged street section is affecting access to the community clinic.

10. MAIN FUNCTIONS
The user can use the system through a menu to manage complaints. Main functions:
- Submit a complaint.
- View complaint records.
- Search for a complaint.
- Update a complaint status.
- Delete a complaint record.
- Exit the program.

11. TESTING
The system should be tested to confirm that its main functions work correctly.
Test Expected Result
- Submit complaint - Complaint record is saved
- View complaints - Complaint details are displayed
- Search complaint - Matching record is found
- Update complaint - Status is changed
- Delete complaint - Record is removed

12. CONCLUSION
The Citizen Complaint System demonstrates how Python and Object-Oriented Programming can be applied to a practical information-management problem. The project provides a basic structure for adding, displaying, searching, and updating complaint records. It demonstrates the use of classes, objects, attributes, constructors, methods, and lists in organizing program data. Developing the system also provides practical experience in writing source code, testing program functionality, identifying limitations, and preparing technical documentation. Although the current version is a simple console-based prototype, it provides a foundation for further development. Adding permanent data storage, stronger validation, and access controls would improve the system and make it more suitable for more demanding applications.

Overall, the project illustrates the importance of organizing code properly and applying programming concepts to develop useful software solutions.

13. DIGITAL PUBLIC GOODS (DPG) ALIGNMENT
- Open-source: suitable for publication in a public GitHub repository.
- Inclusive and accessible: simple text-based interface, clear commands and readable output.
- Privacy-respecting: the project avoids sensitive personal data and uses fictional demonstration records.
- Modular and reusable: the Citizen, Complaint and ComplaintSystem classes have separate responsibilities and can be reused in a larger system.

14. REFERENCES
- Python Software Foundation. (n.d.). The Python Tutorial. Available at: Python Tutorial
- Python Software Foundation. (n.d.). Classes. Available at: Python Classes Tutorial
- Microsoft. (n.d.). Visual Studio Code Documentation. Available at: Visual Studio Code Documentation

15. FILES IN THIS FOLDER
- main.py - application source code
- test_main.py - tests for the classes
- README.md - explanation and documentation