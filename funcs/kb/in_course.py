def trans_course(course):
    course=course[:-1]
    st,end = course.split('-')
    res = list(range(int(st),int(end)+1))
    return res

def in_course(now_course_time,course_time):
    now_course_time = int(now_course_time.split('-')[0])
    if now_course_time in trans_course(course_time):
        return True
    else:
        return False
