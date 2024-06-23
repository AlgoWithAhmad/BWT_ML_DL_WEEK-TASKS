def get_student_details():
    # Initialize an empty list to store student details
    student_list = []

    # Prompt the user to enter details for 3 students
    for i in range(3):
        name = input(f"Enter name of student {i+1}: ")
        age = int(input(f"Enter age of student {i+1}: "))
        grade = input(f"Enter grade of student {i+1}: ")
        # Append the details as a tuple to the student_list
        student_list.append((name, age, grade))
    
    return student_list

def convert_to_dict(student_list):
    # Convert the list of tuples into a dictionary
    student_dict = {name: (age, grade) for name, age, grade in student_list}
    return student_dict

def display_students(student_dict):
    # Display the student details from the dictionary
    for name, details in student_dict.items():
        age, grade = details
        print(f"Student Name: {name}, Age: {age}, Grade: {grade}")

def main():
    # Get student details
    student_list = get_student_details()
    
    # Convert the list of tuples to a dictionary
    student_dict = convert_to_dict(student_list)
    
    # Display the student details
    display_students(student_dict)

if __name__ == "__main__":
    main()
