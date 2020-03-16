# 4)Create a class factory with following properties
#
# 	If input is a list then should return an instance of list
# 	else should return a string instance with value 'Input should be list'
# example:-
# 	a = A([1,2,3])
# 	type(a) is a list
# 	a = A()
# 	type(a) is a string


class frc:
    def __init__(self,a=''):
        self.a=a
    def show(self):
        return self.a
a = frc([1,2,3]).show()

print(type(a))