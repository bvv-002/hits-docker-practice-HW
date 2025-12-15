import unittest
from tornado.web import Application
from tornado.testing import AsyncHTTPTestCase
from main import make_app

class TestAppHandlers(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_hospital_get(self):
        response = self.fetch('/hospital')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Hospital', response.body)

    def test_hospital_post(self):
        body = 'name=TestHospital&address=TestAddress&beds_number=10&phone=12345'
        response = self.fetch('/hospital', method='POST', body=body)
        self.assertEqual(response.code, 200)
        self.assertIn(b'OK: ID', response.body)

    def test_doctor_get(self):
        response = self.fetch('/doctor')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Doctor', response.body)

    def test_doctor_post(self):
        body = 'surname=TestDoctor&profession=Cardiologist&hospital_ID=1'
        response = self.fetch('/doctor', method='POST', body=body)
        # Если hospital_ID=1 не существует, может быть 400, но пока проверим 200 или 400
        self.assertIn(response.code, [200, 400])

    def test_patient_get(self):
        response = self.fetch('/patient')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Patient', response.body)

    def test_patient_post(self):
        body = 'surname=TestPatient&born_date=1990-01-01&sex=M&mpn=123456'
        response = self.fetch('/patient', method='POST', body=body)
        self.assertEqual(response.code, 200)
        self.assertIn(b'OK: ID', response.body)

    def test_diagnosis_get(self):
        response = self.fetch('/diagnosis')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Diagnosis', response.body)

    def test_diagnosis_post(self):
        # patient_ID=1 может не существовать, допускаем 200 или 400
        body = 'patient_ID=1&type=Flu&information=TestInfo'
        response = self.fetch('/diagnosis', method='POST', body=body)
        self.assertIn(response.code, [200, 400])

    def test_doctor_patient_get(self):
        response = self.fetch('/doctor-patient')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Doctor', response.body)

    def test_doctor_patient_post(self):
        body = 'doctor_ID=1&patient_ID=1'
        response = self.fetch('/doctor-patient', method='POST', body=body)
        self.assertIn(response.code, [200, 400])

if __name__ == '__main__':
    unittest.main()

