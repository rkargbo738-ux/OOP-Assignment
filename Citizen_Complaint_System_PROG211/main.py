"""
Citizen Complaint System
PROG211 - Object-Oriented Programming 1

A small, privacy-respecting government complaint management program.
The program stores complaint objects in ONE Python data structure: a dictionary.
All personal data in the demonstration is fictional and non-sensitive.
"""

class Citizen:
    """Represents a citizen who submits a complaint."""

    def __init__(self, citizen_id, alias):
        self.citizen_id = citizen_id
        self.alias = alias

    def identify(self):
        """Return a privacy-friendly citizen reference."""
        return f"{self.alias} ({self.citizen_id})"

    @classmethod
    def from_alias(cls, citizen_id, alias):
        """Alternative constructor using a public-facing alias."""
        return cls(citizen_id, alias)


class Complaint:
    """Represents one complaint submitted to a public office."""

    VALID_STATUSES = ("Submitted", "Under Review", "Resolved")

    def __init__(self, complaint_id, category, description, citizen):
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.citizen = citizen
        self.status = "Submitted"

    def update_status(self, new_status):
        """Update the complaint status if the status is valid."""
        if new_status not in self.VALID_STATUSES:
            raise ValueError("Invalid status. Choose Submitted, Under Review, or Resolved.")
        self.status = new_status

    def summary(self):
        """Return a short, readable complaint summary."""
        return (
            f"{self.complaint_id} | {self.category} | {self.status} | "
            f"{self.citizen.identify()} | {self.description}"
        )


class ComplaintSystem:
    """Manages citizen complaints for a government service desk."""

    ALLOWED_CATEGORIES = ("Roads", "Water", "Waste", "Public Safety", "Other")

    def __init__(self, office_name):
        self.office_name = office_name
        # The ONLY collection/data structure used by the program.
        # Complaint ID is the unique key; each value is a Complaint object.
        self.complaints = {}

    @staticmethod
    def valid_category(category):
        """Check whether a complaint category is supported."""
        return category in ComplaintSystem.ALLOWED_CATEGORIES

    def submit_complaint(self, complaint):
        """Add a Complaint object to the system."""
        if not self.valid_category(complaint.category):
            raise ValueError("Unsupported complaint category.")
        if complaint.complaint_id in self.complaints:
            raise ValueError("Complaint ID already exists.")
        self.complaints[complaint.complaint_id] = complaint

    def update_complaint(self, complaint_id, new_status):
        """Change the status of an existing complaint."""
        if complaint_id not in self.complaints:
            raise KeyError("Complaint ID was not found.")
        self.complaints[complaint_id].update_status(new_status)

    def display_complaints(self):
        """Display every complaint stored in the dictionary."""
        if not self.complaints:
            print("No complaints have been submitted.")
            return

        print(f"\n--- {self.office_name}: Complaint Register ---")
        for complaint in self.complaints.values():
            print(complaint.summary())

    @classmethod
    def create_demo_system(cls):
        """Class method that creates a ready-to-use demonstration system."""
        return cls("Community Services Desk")


def run_demo():
    """Demonstrate object creation and interaction between objects."""
    system = ComplaintSystem.create_demo_system()

    citizen_one = Citizen.from_alias("CIT-104", "Aminata Koroma")
    citizen_two = Citizen.from_alias("CIT-219", "Daniel Bangura")

    complaint_one = Complaint(
        "CMP-301",
        "Waste",
        "Collection point near the market has not been cleared.",
        citizen_one,
    )
    complaint_two = Complaint(
        "CMP-302",
        "Roads",
        "A damaged street section is affecting access to the community clinic.",
        citizen_two,
    )

    system.submit_complaint(complaint_one)
    system.submit_complaint(complaint_two)
    system.update_complaint("CMP-301", "Under Review")
    system.display_complaints()


def interactive_mode():
    """Simple console interface using the same three OOP classes."""
    system = ComplaintSystem.create_demo_system()
    print("\nCitizen Complaint System")
    print("Type 'demo' to view sample records or 'exit' to quit.")

    while True:
        choice = input("\nCommand (demo/add/show/update/exit): ").strip().lower()

        if choice == "demo":
            run_demo()

        elif choice == "add":
            citizen_id = input("Citizen code (e.g., CIT-401): ").strip()
            alias = input("Citizen display name/alias: ").strip()
            category = input("Category (Roads/Water/Waste/Public Safety/Other): ").strip().title()
            description = input("Complaint description: ").strip()
            complaint_id = input("Complaint code (e.g., CMP-401): ").strip()

            citizen = Citizen.from_alias(citizen_id, alias)
            complaint = Complaint(complaint_id, category, description, citizen)

            try:
                system.submit_complaint(complaint)
                print("Complaint submitted successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "show":
            system.display_complaints()

        elif choice == "update":
            complaint_id = input("Complaint code: ").strip()
            new_status = input("New status (Submitted/Under Review/Resolved): ").strip()
            try:
                system.update_complaint(complaint_id, new_status)
                print("Complaint status updated.")
            except (KeyError, ValueError) as error:
                print(f"Error: {error}")

        elif choice == "exit":
            print("Goodbye.")
            break

        else:
            print("Unknown command. Use demo, add, show, update, or exit.")


if __name__ == "__main__":
    run_demo()
