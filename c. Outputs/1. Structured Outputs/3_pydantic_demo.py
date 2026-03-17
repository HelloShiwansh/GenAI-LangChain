from pydantic import BaseModel, EmailStr, Field
# its like type dict + validation

from typing import Optional


class Student(BaseModel):
    name: str = 'sms'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='marks scaled to 1-10')

new_student = {
    'name' : 'Shiwansh',
    'age' : 21,
    'email' : 'sms@gmail.com'
}

student = Student(**new_student)

print(student)
student_dict = dict(student)

print(student_dict['name'])