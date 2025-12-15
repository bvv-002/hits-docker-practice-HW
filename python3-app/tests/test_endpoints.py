import unittest
import requests

BASE_URL = "http://127.0.0.1:8888"

class TestAPI(unittest.TestCase):

    def test_hospital_post(self):
        data = {
            'name': 'Central Hospital',
            'address': '123 Main St',
            'beds_number': '100',
            'phone': '555-1234'
        }
        response = requests.post(f"{BASE_URL}/hospital", data=data)
        self.assertIn("ok", response.text.lower())

    def test_patient_post(self):
        data = {
            'surname': 'Petrov',
            'born_date': '1990-01-01',
            'sex': 'M',
            'mpn': '1234567890'
        }
        response = requests.post(f"{BASE_URL}/patient", data=data)
        self.assertIn("ok", response.text.lower())

    def test_doctor_post(self):
        data = {
            'surname': 'Ivanov',
            'profession': 'Therapist',
            'hospital_ID': '1'
        }
        response = requests.post(f"{BASE_URL}/doctor", data=data)
        self.assertIn("ok", response.text.lower())

    def test_diagnosis_post(self):
        data = {
            'patient_ID': '1',
            'type': 'Flu',
            'information': 'Mild symptoms'
        }
        response = requests.post(f"{BASE_URL}/diagnosis", data=data)
        self.assertIn("ok", response.text.lower())

    def test_doctor_patient_post(self):
        data = {
            'doctor_ID': '1',
            'patient_ID': '1',
            'date': '2025-12-14'
        }
        response = requests.post(f"{BASE_URL}/doctor-patient", data=data)
        self.assertIn("ok", response.text.lower())

if __name__ == "__main__":
    unittest.main()

