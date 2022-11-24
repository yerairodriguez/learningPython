q1 = int(input("Q1:"))
q2 = int(input("Q2:"))
q3 = int(input("Q3:"))
finalTest = int(input("Final test:"))
final_project = int(input("Final project:"))

qGrades = ((q1+q2+q2)/3)*0.55
finalGrades = finalTest*0.3
finalProjectGrades = final_project*0.15

defFinalGrades = qGrades+finalGrades+finalProjectGrades

print("Final grades: %"%defFinalGrades)
