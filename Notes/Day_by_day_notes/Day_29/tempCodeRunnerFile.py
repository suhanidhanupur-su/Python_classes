def find_average_of_all_subject_marks(number_of_sub):

    maths_marks = int(input("enter the maths marks: "))
    science_marks = int(input("enter the science marks: "))
    english_marks = int(input("enter your english marks: "))

    total = maths_marks + science_marks + english_marks
    average = total / number_of_sub

    print(average)

find_average_of_all_subject_marks(3)