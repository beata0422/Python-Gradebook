last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#Create a list called subjects and fill it with the classes you are taking:
subjects = ['physics', 'calculus','poetry','history']
#Create a list called grades and fill it with your scores:
grades = [98, 97, 85, 88]
#use append to add "computer science" to subjects and 100 to grades.
subjects.append('computer science')
grades.append(100)
#Save this zip object as a list into a variable called gradebook.
gradebook = list(zip(subjects, grades))
#use append to add ("visual arts", 93) to gradebook.
gradebook.append(('visual arts',93))
full_gradebook = last_semester_gradebook + gradebook
print(gradebook)


