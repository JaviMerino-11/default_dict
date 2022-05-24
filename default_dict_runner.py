from data_structure.mydict import MyDict


def main() -> None:
    default_value_msg = 'Default Value'
    test_dict = MyDict(default_value_msg=default_value_msg)  # Esto llama al __init__ al __new__...
    test_dict['key1'] = 'value1'  # Esto llama al __setitem__
    test_dict['key2'] = 'value2'
    test_dict['key2'] = 'value3'
    test_dict['key2'] = 'value4'

    print(test_dict['key1'])  # Esto llama al __getitem__
    print(test_dict['key2'])
    print(test_dict['f'])
    print(test_dict['g'])


if __name__ == '__main__':
    main()
