from typing import TypedDict

class Student(TypedDict):
    name: str
    roll_no: int
    age: int

student: Student = {
    'name': 'Zaid',
    'roll_no': 72,
    'age': 19, # str will also work, since TypedDict is guider only
}

print(student)
print(type(student))