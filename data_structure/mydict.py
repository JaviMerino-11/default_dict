class my_Dict(dict):
    def __init__(self, default_msg=None):
        super().__init__()
        self.__default_msg = default_msg

    def __getitem__(self, key_target):
        if key_target not in self:
            return self.__default_msg
        else:
            return self.get(key_target)