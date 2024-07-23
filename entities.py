class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)
        print(f"asasasa  {len(self.value)}")
        self.validate_name()

    def validate_name(self):
        if len(self.value) < 1:
            raise ValueError("Name can't be empty")


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
        print(f"asasasa  {len(self.value)}")
        self.validate_phone()

    def validate_phone(self):
        print(len(self.value))
        if len(self.value) != 10:
            raise ValueError("Phone number must be 10 digits long")
