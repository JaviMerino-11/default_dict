import unittest
from copy import deepcopy

from data_structure.mydict import MyDict


class TestDefaultDictRunner(unittest.TestCase):

    def test_default_dict_runner_key_OK(self):
        expected_key = 'some_key'
        expected_value = 'some_value'
        expected_msg = 'Not found in current dictionary'

        test_dict = MyDict(default_missing_msg=expected_msg, default_value=11)
        test_dict[expected_key] = expected_value

        self.assertEqual(test_dict[expected_key], expected_value)

    def test_default_dict_runner_key_not_OK(self):
        expected_key = 'some_key'
        expected_value = 'some_value'
        not_expected_key = 'some_invalid_key'
        expected_msg = 'Not found in current dictionary'

        test_dict = MyDict(default_missing_msg=expected_msg, default_value=11)
        test_dict[expected_key] = expected_value

        self.assertEqual(test_dict[not_expected_key], expected_msg)

    def test_default_dict_runner_SAMUEL_1(self):
        expected_key = 'key_a'
        expected_value = 'value_a'
        invalid_key_expected_msg = 'Not found in current dictionary'

        test_dict = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict2 = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict3 = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict2[expected_key] = expected_value
        test_dict3[expected_key] = expected_value
        del test_dict3[expected_key]

        self.assertEqual(test_dict[expected_key], invalid_key_expected_msg)
        self.assertEqual(test_dict2[expected_key], expected_value)
        self.assertEqual(test_dict3[expected_key], invalid_key_expected_msg)

    def test_default_dict_runner_SAMUEL_LOOP(self):
        expected_key = 'key_a'
        unexpected_key = 'key_b'
        expected_value = 'value_a'
        invalid_key_expected_msg = 'Not found in current dictionary'

        test_dict = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict[expected_key] = expected_value
        test_dict2 = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict2.update(
            {
                'key_a': 'value_a',
                'key_b': 'value_b',
            }
        )

        result_loop_dict = deepcopy(test_dict2)
        for keys, values in test_dict2.items():
            print(keys, '->', values)

        self.assertEqual(test_dict[expected_key], expected_value)
        self.assertEqual(test_dict[unexpected_key], invalid_key_expected_msg)
        self.assertDictEqual(test_dict2, result_loop_dict)

    def test_default_dict_runner_SAMUEL_CONDITIONAL(self):
        expected_key = 'key_a'
        expected_value = 'value_a'
        unexpected_key = 'key_c'
        invalid_key_expected_msg = 'Not found in current dictionary'

        test_dict = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        test_dict[expected_key] = expected_value

        if expected_key in test_dict:
            print(list(test_dict.keys()), '->', list(test_dict.values()))
        else:
            print(invalid_key_expected_msg)
        self.assertTrue(expected_key in test_dict)
        self.assertFalse(unexpected_key in test_dict)

    def test_default_dict_runner_SAMUEL_(self):
        expected_key = 'key_a'
        unexpected_key = 'key_c'
        invalid_key_expected_msg = 'Not found in current dictionary'

        d = MyDict(default_missing_msg=invalid_key_expected_msg, default_value=11)
        print(d[expected_key])
        self.assertTrue(expected_key in d)
        self.assertFalse(unexpected_key in d)


if __name__ == '__main__':
    unittest.main()
