'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase


class TestStudentLists(TestCase):

    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

    def test_cant_create_class_with_zero_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(0)

    def test_can_create_class_with_positive_number_of_students(self):
        test_class = ClassList(1)

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    def test_student_not_in_clas_list(self):
        test_class = ClassList(3)
        test_class.add_student('Student A')
        test_class.add_student('Student B')
        test_class.add_student('Student C')
        with self.assertRaises(StudentError):
            test_class.remove_student('Student D')

    def test_remove_student_from_empty_list(self):
        test_class = ClassList(1)
        with self.assertRaises(StudentError):
            test_class.remove_student("Student")

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_check_for_student_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Student A')
        test_class.add_student('Student B')
        self.assertFalse(test_class.is_enrolled('Student C'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_student_is_none_if_class_list_is_empty(self):
        test_class = ClassList(2)
        index = test_class.index_of_student("Test Student")
        self.assertIsNone(index)

    def test_index_of_student_is_none_in_populated_class_list(self):
        test_class = ClassList(1)
        test_class.add_student('Student A')
        self.assertIsNone(test_class.index_of_student('Student B'))

    def test_return_true_if_class_list_full(self):
        test_class = ClassList(1)
        test_class.add_student('Student A')
        self.assertTrue(test_class.is_class_full())

    def test_return_is_false_for_empty_class_list(self):
        test_class = ClassList(3)
        self.assertFalse(test_class.is_class_full())