class AttributePrinterMixin:
    def __str__(self):
        return self._format_attributes(self.__class__, self.__dict__)

    @staticmethod
    def _format_attributes(cls, attributes):
        output = f"{cls.__name__}: {{\n"
        for key, value in attributes.items():
            if key.startswith("__") and key.endswith("__"):  # Skip built-in attributes
                continue
            if key.startswith("_"):
                if key.startswith(f"_{cls.__name__}__"):  # Private attribute
                    key = key[len(cls.__name__) + 2:]
                else:  # Protected attribute
                    key = key[1:]
            output += f"\t{key}: {value}\n"
        output += "}"
        return output
class MyClass(AttributePrinterMixin):
    def __init__(self):
        self.public_field = 42
        self._protected_field = "protected"
        self.__private_field = [1, 2, 3]


obj = MyClass()
print(obj)
