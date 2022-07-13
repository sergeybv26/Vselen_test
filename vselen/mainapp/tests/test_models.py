from unittest import TestCase

from mainapp.models import Student


class StudentModelTest(TestCase):

    def setUp(self) -> None:
        self.student = Student.objects.create(
            firstname='Иван',
            lastname='Иванов',
            university='МГУ',
            email='test@test.com',
            birthday='1990-01-01',
            comment='Текст примечания'
        )

    def test_firstname_label(self):
        field_label = self.student._meta.get_field('firstname').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_lastname_label(self):
        field_label = self.student._meta.get_field('lastname').verbose_name
        self.assertEqual(field_label, 'Фамилия')

    def test_university_label(self):
        field_label = self.student._meta.get_field('university').verbose_name
        self.assertEqual(field_label, 'Образование')

    def test_email_label(self):
        field_label = self.student._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Адрес электронной почты')

    def test_birthday_label(self):
        field_label = self.student._meta.get_field('birthday').verbose_name
        self.assertEqual(field_label, 'Дата рождения')

    def test_comment_label(self):
        field_label = self.student._meta.get_field('comment').verbose_name
        self.assertEqual(field_label, 'Примечание')

    def test_is_active_label(self):
        field_label = self.student._meta.get_field('is_active').verbose_name
        self.assertEqual(field_label, 'Пользователь активен?')

    def tearDown(self) -> None:
        self.student.delete()
