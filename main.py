import random
from adminsion import message, fullName, Age, Gender,Religion, SubjectAndScore,qaSection,recomender
from  db_student import db,subjects




def University_Recommender():
    print('\t\t\tUNIVERSITY RECOMMENDER\n----------------------------------------')
    fullname = fullName()
    db.update({'fullname': fullname})

    age = Age()
    db.update({'age': age})

    gender = Gender()
    db.update({'gender': gender})

    religion = Religion()
    db.update({'religion': religion})

    subjects_and_score = SubjectAndScore(subjects)

    print('----------------------------------------')

    qasection = qaSection()
    recomender()



University_Recommender()
