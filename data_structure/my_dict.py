class my_Dict(dict):
    def __getitem__(self, key_target):
        if key_target not in self:
            default_msg = 'Not found in dictionary'
            return default_msg
        else:
            return key_target in self
