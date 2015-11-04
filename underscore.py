class underscore(object):
    def map(self, myList, myLambda): #callback
        returnList = []
        for element in myList:
            returnList.append(myLambda(element))
        return returnList

    def find(self):
        pass
    def reduce(self):
        pass
    def reject(self):
        pass
    def filter(self):
        pass

print "working"
# var myFunction = function(){do something};// javascript anonymous function
# function myFunction(){}
# def myFunction():
#   do something
# myFunction = lambda x: do something
# lambda x,y,z : x + y + z

_ = underscore()
print _.map([1,2,3],lambda x : x*x)
