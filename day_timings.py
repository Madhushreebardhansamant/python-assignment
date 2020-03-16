# 6)Write a function
# input_data=[
#  ['9:00', '5:00'], # Monday
#  ['9:00', '5:00'], # Tuesday
#  ['5:00', '10:00'], # ...
#  ['9:00', '5:00'],
#  ['9:00', '6:00'],
#  ['5:00', '10:00'],
#  ['5:00', '10:00'],
#  ]
#
# output_data=
# ['Monday-Tuesday,Thursday:9:00-5:00',
#  'Wednesday,Saturday-Sunday:5:00-10:00',
#  'Friday:9:00-6:00']

inputt = [['9:00', '5:00', 'Mon'], ['9:00', '5:00', 'Tue'], ['5:00', '10:00', 'Wed'], ['9:00', '5:00', 'Thu'],
          ['9:00', '6:00', 'Fri'], ['5:00', '10:00', 'Sat'], ['5:00', '10:00', 'Sun']]
weeks = {'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7}
week = {1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
d = {}
for inp in inputt:
    key = inp[0] + '-' + inp[1]
    if key in d:
        d[key].append(weeks[inp[-1]])
    else:
        d[key] = [weeks[inp[-1]]]
for key, value in d.items():
    new_list = []
    value = sorted(value)
    temp = [value[0]]
    for i in range(len(value) - 1):
        if value[i] == value[i + 1] - 1:
            temp.append(value[i + 1])
        else:
            new_list.append(temp)
            temp = [value[i + 1]]
    new_list.append(temp)
    d[key] = new_list
for key, value in d.items():
    temp = ''
    for i in value:
        if len(i) > 1:
            if temp:
                temp += ', ' + week[i[0]] + '-' + week[i[-1]]
            else:
                temp = week[i[0]] + '-' + week[i[-1]]
        else:
            if temp:
                temp += ', ' + week[i[0]]
            else:
                temp = week[i[0]]
    d[key] = temp
print(d)