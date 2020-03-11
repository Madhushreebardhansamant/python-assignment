# 1) week_list = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
# input = {day: 'mon', 'number': 2}
# output = 'wed'
#
# input = {'day': 'fri', 'number': 28}
# output = ?

def finding(i,week_list,inputt):
    if inputt['num']>(len(week_list)-1):
        n=inputt['num']%7
        i=i+n
    else:
        i=i+inputt['num']
    if i>6:
        i=i-7
    return week_list[i]
week_list = ['mon', 'tues', 'wed', 'thurs','fri', 'sat', 'sun']
inputt = {'day' :'fri', 'num':6}
for i in range(len(week_list)):
    if week_list[i]==inputt['day']:
         day=finding(i,week_list,inputt)
print(day)