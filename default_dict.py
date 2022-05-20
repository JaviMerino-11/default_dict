from data_structure.my_dict import my_Dict


def main() -> None:
    test_dict = my_Dict()
    test_dict['key1'] = 'value1'
    print(test_dict['key1'])
    print(test_dict['b'])
    test_dict['b'] = 'hola'
    print(test_dict['b'])


if __name__ == '__main__':
    main()
