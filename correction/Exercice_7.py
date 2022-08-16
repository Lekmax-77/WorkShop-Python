import inspect
from tabnanny import check

class MetaCheck(type):
    def __new__(cls, clsname, bases, attrs):
        print("NEW")
        assert 'process' in attrs
        # print(inspect.signature(attrs['process']).parameters, len(inspect.signature(attrs['process']).parameters))
        assert len(inspect.signature(attrs['process']).parameters) == 4
        print("Sucess")
        return type(clsname, bases, attrs)

class Test(metaclass=MetaCheck):
    def process(self, data, test, test2):
        pass

class Test1(metaclass=MetaCheck):
    def process(self, data, test, test2, test3):
        pass