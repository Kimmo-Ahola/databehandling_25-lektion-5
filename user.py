from datetime import date
class User():
    def __init__(self, id, first_name, last_name, birth_date) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date


    def __repr__(self) -> str:
        return f"{self.id} {self.first_name} {self.last_name} {self.birth_date}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def calculate_age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    
    @staticmethod
    def is_valid_birth_date(birth_date: date) -> bool:
        return birth_date <= date.today()
    
    @classmethod
    def from_age(cls, id, first_name, last_name, age):
        birth_year = date.today().year - age
        birth_date = date(birth_year, date.today().month, date.today().day)
        return cls(id, first_name, last_name, birth_date)


class AdminUser(User):
    def __init__(self, id, first_name, last_name, birth_date) -> None:
        super().__init__(id, first_name, last_name, birth_date)


admin_user = AdminUser(1, 'Kimmo', 'Ahola', date(1991,8,4))