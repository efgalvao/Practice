from math import ceil

def gradingStudents(grades):
    for n in grades:
        if n < 38:
            print(n)
        elif (ceil(n/5)*5) - n < 3:
            print(ceil(n/5)*5)
        else:
            print(n)
    return n


grades = [73, 67, 38, 33]
gradingStudents(grades)
resposta = [75, 67, 40, 33]