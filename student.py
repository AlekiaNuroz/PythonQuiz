from pprint import pprint

def invert_student_course_dict(student_course_dict: dict[str, list[str]]) -> dict[str, list[str]]:
  """
  Creates a new dictionary mapping courses to the students enrolled in them.

  This function takes a dictionary where keys are student names (strings) 
  and values are lists of courses (strings) the student is enrolled in. 
  It returns a new dictionary where keys are courses (strings) and 
  values are lists of students (strings) enrolled in that course. 
  The returned dictionary is sorted in ascending order by course name.

  Args:
    student_course_dict: A dictionary of student names (strings) and their 
                         corresponding lists of courses (strings).

  Returns:
    A dictionary of courses (strings) and the lists of students (strings) 
    enrolled in them, sorted in ascending order by course name.
  """
  inverted_dict = {}
  for student, courses in student_course_dict.items():
    for course in courses:
      inverted_dict.setdefault(course, []).append(student)
  return dict(sorted(inverted_dict.items()))

# Sample input
student_course_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Create an inverted dictionary 
inverted_dict = invert_student_course_dict(student_course_dict)

# Print the original and inverted dictionaries
print("Original Dictionary:")
pprint(student_course_dict)

print("\nInverted Dictionary:")
pprint(inverted_dict)