# Citizen Complaint System
# PROG211 - Object Oriented Programming 1

class Citizen:
    def __init__(self, citizen_id, alias):
        self.citizen_id = citizen_id
        self.alias = alias

    def identify(self):
        return f"{self.alias} ({self.citizen_id})"

    @classmethod
    def from_alias(cls, alias):
        return cls("CIT-104", alias)

class Complaint:
    def __init__(self, complaint_id, category, description, citizen, status="Submitted"):
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.citizen = citizen
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def summary(self):
        return f"{self.complaint_id} | {self.category} | {self.status} | {self.citizen.identify()} | {self.description}"

class ComplaintSystem:
    def __init__(self, office_name):
        self.office_name = office_name
        self.complaints = []

    def submit_complaint(self, complaint):
        if self.valid_category(complaint.category):
            self.complaints.append(complaint)
            print("Complaint submitted:", complaint.complaint_id)
        else:
            print("Invalid category")

    def update_complaint(self, complaint_id, new_status):
        for c in self.complaints:
            if c.complaint_id == complaint_id:
                c.update_status(new_status)
                print("Updated:", c.summary())
                return
        print("Complaint not found")

    def display_complaints(self):
        print(f"--- {self.office_name}: Complaint Register ---")
        for c in self.complaints:
            print(c.summary())

    @staticmethod
    def valid_category(category):
        allowed = ["Waste", "Roads", "Water", "Electricity", "Sanitation"]
        return category in allowed

    @classmethod
    def create_demo_system(cls):
        system = cls("Community Services Desk")
        citizen1 = Citizen("CIT-104", "Aminata Koroma")
        citizen2 = Citizen("CIT-219", "Daniel Bangura")

        comp1 = Complaint("CMP-301", "Waste", "Collection point near the market has not been cleared.", citizen1, "Under Review")
        comp2 = Complaint("CMP-302", "Roads", "A damaged street section is affecting access to the community clinic.", citizen2, "Submitted")

        system.complaints.append(comp1)
        system.complaints.append(comp2)
        return system

if __name__ == "__main__":
    my_system = ComplaintSystem.create_demo_system()
    my_system.display_complaints()
