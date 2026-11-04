import unittest
from main import Citizen, Complaint, ComplaintSystem

class CitizenComplaintSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = ComplaintSystem.create_demo_system()
        self.citizen = Citizen.from_alias("CIT-900", "Test Citizen")
        self.complaint = Complaint(
            "CMP-900", "Water", "Sample water service complaint.", self.citizen
        )

    def test_objects_and_interaction(self):
        self.system.submit_complaint(self.complaint)
        self.assertIn("CMP-900", self.system.complaints)
        self.assertIs(self.system.complaints["CMP-900"].citizen, self.citizen)

    def test_dictionary_is_used_as_single_collection(self):
        self.system.submit_complaint(self.complaint)
        self.assertIsInstance(self.system.complaints, dict)
        self.assertEqual(len(self.system.complaints), 1)

    def test_status_update(self):
        self.system.submit_complaint(self.complaint)
        self.system.update_complaint("CMP-900", "Resolved")
        self.assertEqual(self.complaint.status, "Resolved")

    def test_invalid_category(self):
        bad = Complaint("CMP-901", "Housing", "Unsupported category.", self.citizen)
        with self.assertRaises(ValueError):
            self.system.submit_complaint(bad)

    def test_duplicate_id(self):
        self.system.submit_complaint(self.complaint)
        duplicate = Complaint("CMP-900", "Roads", "Another complaint.", self.citizen)
        with self.assertRaises(ValueError):
            self.system.submit_complaint(duplicate)

if __name__ == "__main__":
    unittest.main()
