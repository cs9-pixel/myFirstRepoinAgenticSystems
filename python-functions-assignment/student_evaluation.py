
def greet_student(name):
    return f"Hello, {name}"



def calculate_results(scores):
    num_subjects = len(scores)
    average = sum(scores) / num_subjects
    return num_subjects, average



def evaluate_performance(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"



def main():
    name = input("Enter student name: ")

    n = int(input("Enter number of subjects: "))
    scores = []

    for i in range(n):
        mark = float(input(f"Enter score for subject {i+1}: "))
        scores.append(mark)

    greeting = greet_student(name)
    subjects, average = calculate_results(scores)
    result = evaluate_performance(average)

    print("\n--- Final Result ---")
    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)



main()
