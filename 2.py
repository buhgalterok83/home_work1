import inspect


class AttributePrinterMixin:
    def __str__(self):
        return self._format_attributes(self.__class__, self.__dict__)

    @staticmethod
    def _format_attributes(cls, attributes):
        output = f"{cls.__name__}: {{\n"
        for key, value in attributes.items():
            classes = [cls] + list(inspect.getmro(cls))[1:-1]
            for c in classes:
                name = f"_{c.__name__}__"
                if key.startswith(name):
                    key = key[len(name):]
                    break
            else:
                if key.startswith("_"):
                    key = key[1:]
            output += f"\t{key}: {value}\n"
        output += "}"
        return output



class A(AttributePrinterMixin):
    def __init__(self):
        self.public_field = 42
        self._protected_field = "protected"
        self.__private_field = [1, 2, 3]
obj = A()
print(obj)


class B:
    def __init__(self):
        self.__private_in_B = "private_in_B"


class A(AttributePrinterMixin, B):
    pass


a = A()
print(a)
