from random import randint

# Create a list with student's

students = [
    {
        "Student name": "Armen",
        "Russian exam score": randint(50, 101),
        "Math exam score": randint(50, 101),
        "Chemistry exam score": randint(50, 101)
    },
    {
        "Student name": "Artur",
        "Russian exam score": randint(50, 101),
        "Math exam score": randint(50, 101),
        "Chemistry exam score": randint(50, 101)
    },
    {
        "Student name": "Artem",
        "Russian exam score": randint(50, 101),
        "Math exam score": randint(50, 101),
        "Chemistry exam score": randint(50, 101)
    },
    {
        "Student name": "Arnold",
        "Russian exam score": randint(50, 101),
        "Math exam score": randint(50, 101),
        "Chemistry exam score": randint(50, 101)
    },
    {
        "Student name": "Ahmed",
        "Russian exam score": randint(50, 101),
        "Math exam score": randint(50, 101),
        "Chemistry exam score": randint(50, 101)
    }
]
passing_score = 70

# TODO Выведите в консоль все значения. При создании имён переменных используйте подходящие по смыслу слова.

for each_student in students:
    total_score = 0
    # print all key and value from student's dictionary
    for each_item in each_student:
        print(f"{each_item} - {each_student[each_item]}")
        # TODO Рассчитайте сколько всего баллов у каждого ученика, и выведите эти значения.
        if type(each_student[each_item]) != str:
            total_score += each_student[each_item]
    # add new key and value with total score for each student in a dictionary
    each_student["Total student's score"] = total_score
    print(f"Total student's score = {total_score}")
    print("--------------------------------------------")

# TODO Переопределите значение баллов у двух учеников.

for each_student in students:
    # Change value from chosen student's in dictionary
    if each_student["Student name"] == "Ahmed" or each_student["Student name"] == "Arnold":
        new_total_score = 0
        for each_item in each_student:
            if type(each_student[each_item]) != str and each_item != "Total student's score":
                each_student[each_item] = randint(50, 101)
                # Calculate again total score
                new_total_score += each_student[each_item]
            # Replace old value of total score to new value of total score
            each_student["Total student's score"] = new_total_score
        # Print again key and value from student's dictionary where we changed values
        for each_item in each_student:
            print(f"{each_item} - {each_student[each_item]}")
        print("--------------------------------------------")

# TODO Рассчитайте среднее арифметическое значение баллов по ЕГЭ на ученика( с учётом всех трех экзаменов )

for each_student in students:
    # Calculate average score of each student
    average_score = round(each_student["Total student's score"]/3, 0)
    each_student["Average score"] = average_score
    for each_item in each_student:
        print(f"{each_item} - {each_student[each_item]}")
    print("--------------------------------------------")

# TODO Проверьте каждого ученика, проходит ли он по баллам, используя операторы сравнения.

for each_student in students:
    name = each_student["Student name"]
    average_score = each_student["Average score"]
    if each_student["Average score"] >= passing_score:
        print(f"Student - {name} passed exams, because average score is {average_score}")
    else:
        print(f"Student - {name} failed exams, because average score is {average_score}")


