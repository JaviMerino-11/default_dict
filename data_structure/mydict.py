class MyDict(dict):
    def __init__(self, default_value_msg: str):
        super().__init__()
        self.__default_value = default_value_msg

    def __getitem__(self, key_target):
        result = self.get(key_target, self.__default_value)
        self[key_target] = result
        return result
