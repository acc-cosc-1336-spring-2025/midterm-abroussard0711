#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import test_case
from src.question_b.question_b import is_prime
from src.question_c.question_c import change_global
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_test_case(self):       # test for question_a 
        self.assertEqual(test_case(), 100)

    def test_is_prime(self):        # test for question_b
        self.assertEqual (is_prime(4), False)
        self.assertEqual (is_prime(5), True)
        self.assertEqual (is_prime(11), True)

    def test_change_global(self):   # test for question_c
        self.assertEqual (change_global(), 25) 

    def test_get_day_of_week(self): # test for question_d
        self.assertEqual (get_day_of_week(0), 'Invalid number')
        self.assertEqual (get_day_of_week(1), 'Monday')
        self.assertEqual (get_day_of_week(2), 'Tuesday')
        self.assertEqual (get_day_of_week(3), 'Wednesday')
        self.assertEqual (get_day_of_week(8), 'Invalid number')

