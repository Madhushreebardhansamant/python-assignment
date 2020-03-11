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

def funct(inputt):
    dict1 = {}
    for line in inputt:

        key = line[0] + '-' + line[1]
        value = line[-1]
        if key in dict1:
            dict1[key].append(value)
        else:

            dict1[key] = [value]
    return dict1


inputt = [
    ['9:00', '7:00', 'Mon'],
    ['9:00', '7:00', 'Tue'],
    ['9:00', '7:00', 'Wed'],
    ['9:00', '7:00', 'Thu'],
    ['1:00', '7:00', 'Fri'],
    ['2:00', '7:00', 'Sat'],
    ['1:00', '10:00', 'Sun'],
]
print(funct(inputt))