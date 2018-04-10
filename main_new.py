import json

#ToDos
#   1.Limit the grades
#   2.Order the list
#   3.Grade should be a number
#   4.

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]["grade_breakdown"]
    return grades

def askForAssignmentMarks(grades, points, student_id):
    #current_grades = {student_id: {}}

    for key in grades:
        try:
            if points[ID][key] >= -1:
                print "Your Grade from " + key + " is " + str(points[student_id][key])
                #points[ID][key] = points[student_id][key]
                answer=raw_input("Do you want to update your score y/n")
                if answer=="y":
                    points[ID][key]=input("your new score")
                    if points>=100 or (points<=0 and points!=-1):
                        points = input ("please insert grade between 0 and 100")
            #else:
                #points[student_id][key] = input(
                #"What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
        except:
            points[ID][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

    return points

def saveGrades(existing):

    print (json.dumps(existing))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(existing))
    file.close()

def printCurrentGrade(grades,existing, ID):
    curr_grade = 0
    for key in existing[ID]:
        if existing[ID][key] != -1:
            calc_grade = int(existing[ID][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print (curr_grade)

def main():
    ID=raw_input("id?")
    grades = loadSetupData(ID)
    existing = askForAssignmentMarks(grades)
    saveGrades(existing)
    printCurrentGrade(grades, existing)

main()