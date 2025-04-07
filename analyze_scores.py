import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('student_scores.csv')

# Calculate average score for each student
data['Average'] = data[['Math', 'Science', 'English']].mean(axis=1)

# Display the data
print("Student Scores with Averages:")
print(data)

# Find the top performer
top_student = data.loc[data['Average'].idxmax()]
print("\nTop Performer:")
print(f"{top_student['Name']} with an average of {top_student['Average']}")

# Create a bar chart
plt.bar(data['Name'], data['Average'], color='skyblue')
plt.title('Average Scores by Student')
plt.xlabel('Student Name')
plt.ylabel('Average Score')
plt.show()