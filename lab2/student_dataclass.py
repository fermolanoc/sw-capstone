from dataclasses import dataclass


@dataclass  # dataclass decorator to simplify class definition
class Student:
    name: str
    college_id: int
    gpa: float


def main():
    alice = Student('Alice Cooper', 12345, 4.0)
    meli = Student('Melissa Cobo', 12124, 3.99)
    ethan = Student('Ethan Ludovick', 99882, 2.001)

    print(alice)
    print(meli)
    print(ethan)


main()
