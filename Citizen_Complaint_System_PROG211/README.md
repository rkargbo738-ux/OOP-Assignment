# Citizen Complaint System

**Course:** PROG211 – Object-Oriented Programming 1  
**Domain:** Government  
**Problem:** Citizen Complaint System  
**Language:** Python 3

## Project purpose
This project demonstrates Object-Oriented Programming (OOP) by modelling a small government service desk that receives, stores and updates citizen complaints.

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

## Python data structure requirement
Only **one Python data structure** is used for storing multiple complaint objects: a **dictionary**.

```text
complaints = {
    "CMP-301": Complaint object,
    "CMP-302": Complaint object
}
```

The complaint ID is the unique dictionary key. This makes it easy to retrieve a complaint and update its status.

## Demonstrated object interaction
`ComplaintSystem` accepts `Complaint` objects. Each `Complaint` contains a `Citizen` object. This demonstrates interaction between objects rather than treating the program as a collection of unrelated functions.

## Run the program

```bash
python3 main.py
```

The default execution runs a demonstration.

For the interactive version:

```bash
python3 -c "from main import interactive_mode; interactive_mode()"
```

## Run tests

```bash
python3 -m unittest -v
```

## Example output

```text
--- Community Services Desk: Complaint Register ---
CMP-301 | Waste | Under Review | Aminata Koroma (CIT-104) | Collection point near the market has not been cleared.
CMP-302 | Roads | Submitted | Daniel Bangura (CIT-219) | A damaged street section is affecting access to the community clinic.
```

## Digital Public Goods (DPG) alignment
- **Open-source:** suitable for publication in a public GitHub repository.
- **Inclusive and accessible:** simple text-based interface, clear commands and readable output.
- **Privacy-respecting:** the project avoids sensitive personal data and uses fictional demonstration records.
- **Modular and reusable:** the `Citizen`, `Complaint` and `ComplaintSystem` classes have separate responsibilities and can be reused in a larger system.

## Suggested GitHub files
- `main.py` – application source code
- `test_main.py` – automated tests
- `README.md` – explanation, DPG alignment and usage instructions
- `sample_output.txt` – captured execution output
- `screenshots/` – screenshots of program execution
- `DOCUMENTATION.docx` or PDF – the written assignment documentation

## Academic integrity
Understand the code before submission and adapt the explanation and demonstration to your own work. Keep the fictional sample data and replace it only if your lecturer requires different examples.
