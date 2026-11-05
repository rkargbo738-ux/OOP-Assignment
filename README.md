# Citizen Complaint System

**Course:** PROG211 - Object-Oriented Programming 1
**Domain:** Government
**Problem:** Citizen Complaint System
**Language:** Python 3

## Project purpose
This project shows Object-Oriented Programming (OOP) by modelling a small government service desk that receives, stores and updates citizen complaints.

The demonstration uses fictional, non-sensitive data. No phone numbers, email addresses, home addresses, national ID numbers, passwords or other sensitive personal information are stored.

## OOP design

### 1. `Citizen`
- **Attributes:** `citizen_id`, `alias`
- **Instance method:** `identify()`
- **Class method:** `from_alias()` as an alternative constructor

### 2. `Complaint`
- **Attributes:** `complaint_id`, `category`, `description`, `citizen`, `status`
- **Instance methods:** `update_status()`, `summary()`

### 3. `ComplaintSystem`
- **Attributes:** `office_name`, `complaints`
- **Instance methods:** `submit_complaint()`, `update_complaint()`, `display_complaints()`
- **Class method:** `create_demo_system()`
- **Static method:** `valid_category()`

## How to run
1. Download the folder or clone the repo
2. Open terminal
3. Run: `python main.py`
4. To run tests: `python -m pytest test_main.py` or `python test_main.py`

## Sample output