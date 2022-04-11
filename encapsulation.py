
class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
