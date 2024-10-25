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
    # Open the grades.csv file in read mode
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        
        # Read the header
        header = next(reader)
        
        # Print the header
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")
        print("-" * 60)
        
        # Read and print each row
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

def main():
    write_grades()  # Write the grades to the file
    read_grades()   # Read and display the grades from the file

if __name__ == "__main__":
    main()
