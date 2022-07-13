from unittest import TestCase

import requests

from rest_framework import status

from mainapp.models import Student


class TestStudentsView(TestCase):

    def setUp(self) -> None:
        self.domain = 'http://127.0.0.1:8000'
        self.students_url = f'{self.domain}/students/'
        self.data = {
            'firstname': 'Иван',
            'lastname': 'Иванов',
            'university': 'МГУ',
            'email': 'test@test.com',
            'birthday': '1990-01-01',
            'comment': 'Текст примечания'
        }

    def test_get_students(self):
        response = requests.get(url=self.students_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        response = requests.post(url=self.students_url, json=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_negative(self):
        cases = [
            (
                {},
                {
                    "firstname": [
                        "Обязательное поле."
                    ],
                    "lastname": [
                        "Обязательное поле."
                    ],
                    "university": [
                        "Обязательное поле."
                    ],
                    "email": [
                        "Обязательное поле."
                    ]
                }
            ),
            (
                {
                    'firstname': 'Петр',
                    'lastname': 'Петров',
                    'university': 'МГУ',
                    'email': 'asdf'
                },
                {
                    "email": [
                        "Введите правильный адрес электронной почты."
                    ]
                }
            ),
            (
                {
                    'firstname': 'Петр',
                    'lastname': 'Петров',
                    'university': 'МГУ',
                    'email': 'test@test.com'
                },
                {
                    "email": [
                        "Студент с таким Адрес электронной почты уже существует."
                    ]
                }
            )
        ]
        response = requests.post(url=self.students_url, json=self.data)
        for data, expected in cases:
            with self.subTest():
                response = requests.post(url=self.students_url, json=data)
                self.assertEqual(response.json(), expected)

    def tearDown(self) -> None:
        try:
            Student.objects.get(email=self.data['email']).delete()
        except Student.DoesNotExist:
            pass
