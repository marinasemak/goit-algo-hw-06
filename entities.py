class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def validate_name(self):
        if len(self.value) < 1:
            print("error")


class Phone(Field):

    def validate_name(self):
        print(len(self.value))
        if len(self.value) != 10:
            raise ValueError("Phone number must be 10 digits long")
