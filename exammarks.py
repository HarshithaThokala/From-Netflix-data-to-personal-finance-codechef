import numpy as np

# Load exam marks
def load_data():
    marks = np.array([78, 85, 33, 66, 15, 88, 90, 59, 29, 70])
    print(marks)   # Required for Test 1
    return marks

# Compute statistics
def compute_statistics(marks):
    average = np.mean(marks)
    median = np.median(marks)
    std_dev = round(np.std(marks), 2)
    return average, median, std_dev

# Analyze performance
def analyze_performance(marks, average):
    above_average = marks[marks > average]
    failed_students = marks[marks < 35]

    print("Number of students above average: ", len(above_average))
    print("Number of failed students: ", len(failed_students))

    return above_average, failed_students

    # Return ONLY these two arrays
    return above_average, failed_students

# Find highest and lowest
def find_extremes(marks):
    highest = marks[np.argmax(marks)]
    lowest = marks[np.argmin(marks)]
    return highest, lowest


# Main Program

print("Exam Marks Statistics Analysis...\n")

marks = load_data()

print("Exam Marks: ", marks)

print("\n--- Class Statistics ---")
average, median, std_dev = compute_statistics(marks)
print("Average Marks: ", average)
print("Median Marks: ", median)
print("Standard Deviation: ", std_dev)

print("\n--- Performance Insights ---")
above_average, failed_students = analyze_performance(marks, average)

print("Students scoring above average: ", above_average)
print("Number of students above average: ", len(above_average))

print("\nStudents who failed (marks < 35): ", failed_students)
print("Number of failed students: ", len(failed_students))

print("\n--- Extremes ---")
highest, lowest = find_extremes(marks)
print("Highest Score: ", highest)
print("Lowest Score: ", lowest)