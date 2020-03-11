# 4)Create a class factory with following properties
#
# 	If input is a list then should return an instance of list
# 	else should return a string instance with value 'Input should be list'
# example:-
# 	a = A([1,2,3])
# 	type(a) is a list
# 	a = A()
# 	type(a) is a string


class A:
    def __init__(self, num = ' '):
        self.num = num
a = A([1,2,3])
dtype = type((a.num))
if dtype == list or str or int:
    print('type(a) is a' + str(dtype))