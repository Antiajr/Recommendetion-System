from db_student import db, science_courses, engineering_courses, questions,christian_university,muslim_university,neutral_university
import random
import string


def fullName():
    name = input('| *Enter Your Fullname: ').strip().lower()

    for letter in name:
        if letter == ' ':
            continue
        elif letter not in string.ascii_letters:
            print(message(status='404', msg="Enter your fullname that contains only letters %s" %name))
            return fullName()

    if name == '':
        print(message(status='404', msg="Enter your fullname"))
        return fullName()

    elif len(name.strip()) < 3:
        print(message(status='404', msg="Fullname must be greater than 3 letters"))
        return fullName()
    elif len(name.strip()) > 40:
        print(message(status='404', msg="Fullname is too long"))
        return fullName()
    print('----------------------------------------')
    return name


def Age():
    try:
        age = int(input('| *Enter Your Age:'))
        if age < 17 or age > 50:
            print(message(status='202', msg="Your age must be within 18 - 50"))
            return Age()
        else:
            print('----------------------------------------')
            return age
    except:
        print(message(status='404', msg="Enter a proper age"))
        return Age()


def Gender():
    try:
        gender = int(input('| *Choose gender from these option below\n| 1. Male\n| 2. Female\n| *Enter Option:  '))
        if gender == 1:
            gender = 'male'
            print('----------------------------------------')
            return gender
        elif gender == 2:
            gender = 'female'
            print('----------------------------------------')
            return gender
        else:
            print(message(status='404', msg="Enter a correct option above"))
            return Gender()
    except:
        print(message(status='404', msg="Invalid Option. Enter An Option Above"))
        return Gender()


def Religion():
    try:
        religion = int(input('| *Choose your religion from these option below\n| 1. Muslim\n| 2. Christian\n| 3. Other\n| *Enter Option:  '))
        if religion == 1:
            religion = 'muslim'
            print('----------------------------------------')
            return religion
        elif religion == 2:
            religion = 'christian'
            print('----------------------------------------')
            return religion
        elif religion == 3:
            religion = 'other'
            print('----------------------------------------')
            return religion
        else:
            print(message(status='404', msg="Enter a correct option above"))
            return Religion()
    except:
        print(message(status='404', msg="Invalid Option. Enter An Option Above"))
        return Religion()


db.update({'jamb_subjects_and_scores': {}})


def SubjectAndScore(subjects):
    for total_jambSubject in range(6):
        jamb_subject = input("| *Enter your jamb subject or type done when you are done: ").strip().lower()

        if jamb_subject == 'done':
            break
        elif jamb_subject == '':
            print(message(status='404', msg="Enter a subject"))
            return SubjectAndScore(subjects)

        elif jamb_subject in db['jamb_subjects_and_scores']:
            print(message(status='202', msg="Subject %s already submitted." % jamb_subject))
            return SubjectAndScore(subjects)

        elif jamb_subject in subjects:
            try:
                jamb_score = int(input("| *Enter your jamb score for %s : " % jamb_subject))
                if jamb_score > 100 or jamb_score < 0:
                    print(message(status='404', msg="%s score must be between 0 - 100..\n| Info: %s data have been cancelled please re-enter again" % (jamb_subject, jamb_subject)))
                    return SubjectAndScore(subjects)
                else:
                    db['jamb_subjects_and_scores'].update({jamb_subject: jamb_score})
                    return SubjectAndScore(subjects)
            except:
                print(message(status='404', msg="Enter your correct score for %s" % jamb_subject))
                return SubjectAndScore(subjects)

        else:
            for subject in subjects:
                if jamb_subject[:3] in subject:
                    print(message(status='202', msg="Do you mean %s" % subject))
                    return SubjectAndScore(subjects)
                elif jamb_subject[0] in subject[0]:
                    print(message(status='202', msg="Do you mean %s" % subject))
                    return SubjectAndScore(subjects)
            else:
                print(message(status='404', msg="Subject %s does not exist type in correct subject e.g %s..." % (
                jamb_subject, subjects[0:4])))
                return SubjectAndScore(subjects)


db.update({'question_answer': {}})
def qaSection():
    print('\t\t *Question And Answer')
    for question in range(len(questions)):
        print('----------------------------------------')
        answer = input('| *%s: ' % questions[question]).strip().lower()
        if answer not in ['yes', 'no', 'y', 'n']:
            answer = 'Null'
        db['question_answer'].update({questions[question]: answer})
    print('----------------------------------------')

def recomender():
    print(db)
    university = None
    if db['religion'] == 'christian':
        university = random.choice(christian_university)
    elif db['religion'] == 'muslim':
        university = random.choice(muslim_university)
    elif db['religion'] == 'other':
        university = random.choice(neutral_university)
    else:
        print('| *Error: Something went wrong...try again')
        print('----------------------------------------')

    jamb_subject_high_score = max(db['jamb_subjects_and_scores'], key=db['jamb_subjects_and_scores'].get)
    print('|')
    print('----------------------------------------')
    all_courses = science_courses + engineering_courses
    print()
    for course in all_courses:
        if str(jamb_subject_high_score).lower() == all_courses and int(
                db['jamb_subjects_and_scores'].get(jamb_subject_high_score)) > 65 or str(
            jamb_subject_high_score).lower() in course.lower():
            print('| *Your course is %s and your university is %s' %(course, university))
            print('----------------------------------------')
            break
        elif str(jamb_subject_high_score).lower() in ['maths', 'biology', 'chemistry', 'physics']:
            for additional_course in engineering_courses:
                if jamb_subject_high_score[:5] in additional_course:
                    science_courses.append(additional_course)
            print('| *Your course is %s and your university is %s ' %(random.choice(science_courses) , university))
            print('----------------------------------------')
            break
        elif str(jamb_subject_high_score).lower() in ['english', 'geography', 'physics']:
            print('| *Your course is %s and your university is %s' %(random.choice(engineering_courses), university))
            print('----------------------------------------')
            break
        else:
            print('| *Error: Something went wrong...try again')
            print('----------------------------------------')



def message(status, msg):
    mode = None
    if status == '404':
        mode = 'Error'
    elif status == '202':
        mode = 'Info'
    else:
        mode = ''
    return ("""----------------------------------------
| %s: %s
----------------------------------------""" % (mode, msg))
