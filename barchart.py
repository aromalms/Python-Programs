#barchart example
import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D', 'E']	
avg_marks = [50, 49, 30, 45, 60]

plt.figure(figsize=(7,5))
plt.bar(students, avg_marks, color=["red", "green", "orange", "blue", "black"])  
plt.ylabel("Average Marks")
plt.title("Students Average Marks")
plt.show()
