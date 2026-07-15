class Customer:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            password=data["password"],
        )    