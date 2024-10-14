#Список: оценки = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: ученики = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
grades_1 = {students[0]:sum(grades[0])/len(grades[0]),
            students[1]:sum(grades[1])/len(grades[1]),
            students[2]:sum(grades[2])/len(grades[2]),
            students[3]:sum(grades[3])/len(grades[3]),
            students[4]:sum(grades[4])/len(grades[4])}
print(grades_1)
print('Bilbo:',grades_1['Bilbo'])


