from dataclasses import dataclass


@dataclass  # dataclass decorator to simplify class definition
class Student:
    # define attributes with data types -> this usually goes on __init__ method along with self
    name: str
    college_id: int
    gpa: float

    # override how info will be printed
    def __str__(self):
        return f'Student: {self.name}\nCollege id: {self.college_id}\nGPA: {self.gpa}\n'


def main():
    # Create Students instances
    alice = Student('Alice Cooper', 12345, 4.0)
    meli = Student('Melissa Cobo', 12124, 3.99)
    ethan = Student('Ethan Ludovick', 99882, 2.001)

    # Print each student data
    print(alice)
    print(meli)
    print(ethan)


main()
