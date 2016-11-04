class DataStruct(object):
    """This class demonstrates how to protect class attributes from beeing
    overwritten with new values. __slots__ makes dynamic addition of
    attributes not possible."""

    __slots__ = ['__x', 'x', '__y', 'y']

    def __init__(self):
        pass
        #self.x = x
 
    def __msg(self,attr):
        print "Attribute \'" + attr + "\' is already set"

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if hasattr(self,'x'):
            self.__msg('x')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if hasattr(self,'y'):
            self.__msg('y')
        else:
            self.__y = y
