students = int(input())

f = 0
c = 0
b = 0
a = 0
grades_sum = 0

for _ in range(students):
    grade = float(input())
    if 2 <= grade <= 2.99:
        f += 1
    elif 3 <= grade <= 3.99:
        c += 1
    elif 4 <= grade <= 4.99:
        b += 1
    elif grade >= 5:
        a += 1
    grades_sum += grade

total_grades = a + b + c + f

a_percentile = a / total_grades * 100
b_percentile = b / total_grades * 100
c_percentile = c / total_grades * 100
f_percentile = f / total_grades * 100

average_grade = grades_sum / total_grades

print(f"Top students: {a_percentile:.2f}%\n"
      f"Between 4.00 and 4.99: {b_percentile:.2f}%\n"
      f"Between 3.00 and 3.99: {c_percentile:.2f}%\n"
      f"Fail: {f_percentile:.2f}%\n"
      f"Average: {average_grade:.2f}")