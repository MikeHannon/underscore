class underscore(object):
    def map(self, myLambda): #callback
        #_.map(lambda x: x + " world") if we invoke _.map as seen on the left
        #1) myLambda becomes lambda x: x + " world"
        print (myLambda("hello"))
        #2) myLambda expects a variable to replace x
        #3) we invoke myLamda passing it "hello"
        #4) x becomes hello and myLambda at this point looks like: lambda "hello": "hello" + " world"
        #5) closing of the ) finalizes the invocation of the function.  print ('hello world')

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

_ = underscore()
