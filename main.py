"""
main.py
"""

from hello_world import hello 
from string_compare import diff_count

print(hello())
print(diff_count('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
# print(diff_count('GAGCCTACTAACGGGAT', ''))

'''
hello_world.py

Every time this is called it should return the string: Hello World!
'''

def hello():
    return 'Hello World!'

'''
string_compare.py

Given two sets of string data of equal length, calculate the positional difference between them
eg:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

differences = 7
'''

def diff_count(string_a, string_b):
    validate(string_a, string_b)
    return len([[x,y] for x, y in zip(string_a, string_b) if x != y])

def validate(string_a, string_b):
    if len(string_a) != len(string_b):
        raise ValueError('Length of both string_a and string_b must be equal')

"""
test.py
"""

import unittest

from hello_world import hello
from string_compare import diff_count

class HelloWorldTest(unittest.TestCase):
    def test_say_hello(self):
        expected = 'Hello World!'
        self.assertEqual(hello(), expected)

class StringCompareTest(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(diff_count('GAGCCTACTAACGGGAT', 'GAGCCTACTAACGGGAT'), 0)
    
    def test_different_long_strings(self):
        self.assertEqual(diff_count('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)
    
    def test_single_identical_strings(self):
        self.assertEqual(diff_count('A', 'A'), 0)
    
    def test_single_different_strings(self):
        self.assertEqual(diff_count('A', 'G'), 1)

    def test_empty_strings(self):
        self.assertEqual(diff_count('', ''), 0)

    def test_different_length_strings(self):
        with self.assertRaises(ValueError):
            diff_count('AG', 'GAGCC')
    
    def test_one_empty_string(self):
        with self.assertRaises(ValueError):
            diff_count('', 'GAGCC')
    


if __name__ == "__main__":
    unittest.main()