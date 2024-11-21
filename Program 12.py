import numpy as np
import csv

def write_grades():
    # Ask the user for the number of students
    num_students = int(input("Enter the number of students: "))

    # Open the grades.csv file in write mode
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        
        # Collect data for each student
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))
            
            # Write the student's data as a new row in the CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Data has been written to grades.csv.")

def read_grades():
    # Load the data from grades.csv into a NumPy array
    data = []
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append([row[2], row[3], row[4]])  # Only grades columns

    # Convert the data into a numpy array
    grades = np.array(data, dtype=int)

    # Print the first few rows of the dataset
    print("First few rows of the dataset (grades):")
    print(grades[:5])  # Print first 5 rows for reference

    return grades

def calculate_statistics(grades):
    # Calculate and print statistics for each exam (columns)
    for i in range(grades.shape[1]):
        print(f"\nStatistics for Exam {i + 1}:")
        print(f"Mean: {np.mean(grades[:, i]):.2f}")
        print(f"Median: {np.median(grades[:, i]):.2f}")
        print(f"Standard Deviation: {np.std(grades[:, i]):.2f}")
        print(f"Minimum: {np.min(grades[:, i])}")
        print(f"Maximum: {np.max(grades[:, i])}")

    # Calculate overall statistics for the entire dataset (all exams combined)
    all_grades = grades.flatten()

    print("\nOverall Statistics for all Exams:")
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")

def pass_fail_statistics(grades):
    # Calculate number of students passing and failing each exam (grade >= 60 is passing)
    passing_grades = grades >= 60

    for i in range(grades.shape[1]):
        passed = np.sum(passing_grades[:, i])
        failed = grades.shape[0] - passed
        print(f"\nExam {i + 1} - Passed: {passed}, Failed: {failed}")

    # Calculate overall pass percentage across all exams
    total_passed = np.sum(passing_grades)
    total = grades.shape[0] * grades.shape[1]  # Total grades in all exams
    pass_percentage = (total_passed / total) * 100
    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")

def main():
    write_grades()  # Write the grades to the file
    grades = read_grades()  # Read and store grades in NumPy array
    calculate_statistics(grades)  # Calculate and display statistics for each exam
    pass_fail_statistics(grades)  # Display pass/fail statistics

if __name__ == "__main__":
    main()
