"""
Author: Fernando Molano

Program to ask a student how many courses is s/he taking this semester, 
save each course into a list and then print every course name
"""

def getCoursesNames(number_of_courses, list_of_classes):
    # get the name of each course student is taking this semester
    for course in range(number_of_courses):
        course_name = input('Enter the name of the course: ')
        list_of_classes.append(course_name)  # add course to the list
    

    return list_of_classes  # return the list with the courses names


# read the items on the list, and show each course name capitalized
def readListOfCourses(list):
    print('Here is the list of Courses you are currently enrolled in: ')
    for course in list:
        print(f'{course.title()}')  # capitalize each word


def main():
    # empty array to store list of courses
    list_of_classes = []

    number_of_courses = int(input('How many classes are you taking this semester? '))

    fill_list = getCoursesNames(number_of_courses, list_of_classes)
    print('')
    
    readListOfCourses(fill_list)
    


main()