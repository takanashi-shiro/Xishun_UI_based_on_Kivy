from funcs.kb.in_course import in_course
from funcs.kb.in_week import in_week

def get_course_data(week,day,course,class_ls):
    for i in class_ls:
        if in_week(week, i['weeks']) and day == i['day'] and in_course(course,i['class']):
            if i['week_flag'] == '单周' and int(week) % 2 == 1:
                return i
            elif i['week_flag'] == '双周' and int(week) % 2 == 0:
                return i
            elif i['week_flag'] == '每周':
                return i
    return None