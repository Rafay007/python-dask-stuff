class animal:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        print('getting name')
        return self._name

    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name


obj = animal("rafay")

print(obj.name)
