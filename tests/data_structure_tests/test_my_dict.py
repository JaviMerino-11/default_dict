import unittest
from data_structure.my_dict import my_Dict


class TestDefaultDictRunner(unittest.TestCase):

    def test_default_dict_runner_key_OK(self):
        expected_key = 'some_key'
        expected_value = 'some_value'

        test_dict = my_Dict()
        test_dict[expected_key] = expected_value

        self.assertEqual(test_dict[expected_key], expected_value)

    def test_default_dict_runner_key_not_OK(self):
        expected_key = 'some_key'
        expected_value = 'some_value'
        not_expected_key = 'some_invalid_key'
        expected_msg = 'Not found in current dictionary'

        test_dict = my_Dict(default_msg=expected_msg)
        test_dict[expected_key] = expected_value

        self.assertEqual(test_dict[not_expected_key], expected_msg)

    def test_default_dict_runner_SAMUEL_1(self):
        expected_key = 'key_a'
        expected_value = 'value_a'
        invalid_key_expected_msg = 'Not found in current dictionary'

        test_dict = my_Dict(default_msg=invalid_key_expected_msg)
        test_dict2 = my_Dict(default_msg=invalid_key_expected_msg)
        test_dict3 = my_Dict(default_msg=invalid_key_expected_msg)
        test_dict2[expected_key] = expected_value
        test_dict3[expected_key] = expected_value
        del test_dict3[expected_key]

        self.assertEqual(test_dict[expected_key], invalid_key_expected_msg)
        self.assertEqual(test_dict2[expected_key], expected_value)
        self.assertEqual(test_dict3[expected_key], invalid_key_expected_msg)

    def test_default_dict_runner_SAMUEL_2(self):
        expected_key = 'key_a'
        unexpected_key = 'key_b'
        expected_value = 'value_a'
        invalid_key_expected_msg = 'Not found in current dictionary'

        test_dict = my_Dict(default_msg=invalid_key_expected_msg)
        test_dict[expected_key] = expected_value
        test_dict2 = my_Dict(default_msg=invalid_key_expected_msg)
        test_dict2.update(
            {
                'key_a': 'value_a',
                'key_b': 'value_b'
            }
        )

        key_results_list = list(test_dict2.keys())
        value_results_list = list(test_dict2.values())
        expected_key_results_list = ['key_a', 'key_b']
        expected_value_results_list = ['value_a', 'value_b']

        self.assertEqual(test_dict[expected_key], expected_value)
        self.assertEqual(test_dict[unexpected_key], invalid_key_expected_msg)
        self.assertEqual(key_results_list, expected_key_results_list)
        self.assertEqual(value_results_list, expected_value_results_list)


if __name__ == '__main__':
    unittest.main()
