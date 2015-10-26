#!/bin/python2.7

def add_scalar_to_list(my_scalar, my_list=[]):
    '''Given a scalar and a list, append the scalar to the list.

    If no list is provided, return a new list containing just the scalar value.
    '''
    return my_list.append(my_scalar)

extra_credit = 0

# DO NOT CHANGE ANYTHING BELOW THIS LINE
# Test section. All these tests should pass when run as follows.
#
# pip install mock unittest2
# ./example_code.py
#
# If you want to go for extra credit, free to set the extra_credit to 1, or 2

import mock
import unittest2

class TestExample(unittest2.TestCase):

    def setUp(self):
        self._input_list = [mock.sentinel.first, mock.sentinel.second, mock.sentinel.third]

    @property
    def input_list(self):
        return list(self._input_list)

    def test_returns_an_array(self):
        'The method should return a list'
        r = add_scalar_to_list(mock.sentinel.test_returns_an_array, self.input_list)
        self.assertIsInstance(r, list)

    def test_returns_same_array_it_was_given(self):
        'The method should modify the input_list in place'
        input_list_copy = self.input_list
        r = add_scalar_to_list(mock.sentinel.junk, input_list_copy)
        self.assertIs(r, input_list_copy)

    def test_append_value_is_last_entry(self):
        'The value passed should be added to the end of the list.'
        v = mock.sentinel.should_be_last_entry
        r = add_scalar_to_list(v, self.input_list)
        self.assertIs(r[-1], v)

    def test_appending_value_to_default_generates_new_list(self):
        'Distinct calls should not have any side-effects.'
        r1 = add_scalar_to_list(mock.sentinel.first_run)
        r2 = add_scalar_to_list(mock.sentinel.second_run)
        self.assertListEqual(r1, [mock.sentinel.first_run])
        self.assertListEqual(r2, [mock.sentinel.second_run])

    @unittest2.skipIf(extra_credit < 1, 'Not trying for 1st tier of extra credit')
    def test_scalarization_of_list(self):
        'If thing is not a scalar, flatten it into a scalar'
        v = [mock.sentinel.a, mock.sentinel.b]
        r = add_scalar_to_list(v, self.input_list)
        self.assertListEqual(r, self.input_list.extend([mock.sentinel.a, mock.sentinel.b]))

    @unittest2.skipIf(extra_credit < 2, 'Not trying for 2nd tier of extra credit')
    def test_scalarization_of_dict(self):
        'If thing is not a scalar, flatten it into a scalar'
        v = {mock.sentinel.a: mock.sentinel.b}
        r = add_scalar_to_list(v, self.input_list)
        self.assertListEqual(r, self.input_list.extend([mock.sentinel.a, mock.sentinel.b]))

if __name__ == '__main__':
    unittest2.main()
