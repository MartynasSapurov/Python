from libnum import nroot


class MyException(Exception):
    def __str__(self):
        return 'MyException'


class MyOtherException(Exception):
    def __str__(self):
        return 'MyOtherException'


class MyLastException(Exception):
    def __str__(self):
        return 'MyLastException'


class Calc:
    def add(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            result = self + other
        except MyException:
            result = "MyException"
        finally:
            return result

    def sub(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            result = self - other
        except MyException:
            result = "MyException"
        finally:
            return result

    def mul(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            result = self * other
        except MyException:
            result = "MyException"
        finally:
            return result

    def div(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            result = self / other
        except MyException:
            result = "MyException"
        except ZeroDivisionError:
            result = "ZeroDivisionError"
        finally:
            return result

    def exp(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            elif other < 0:
                raise MyOtherException()
            result = self ** other
        except MyException:
            result = "MyException"
        except MyOtherException:
            result = "MyOtherException"
        finally:
            return result

    def root(self, other):
        try:
            if not (isinstance(self, int or float) and isinstance(other, int or float)):
                raise MyException()
            elif self < 0 and not other % 2:
                raise MyLastException()
            result = nroot(self, other)
        except MyException:
            result = "MyException"
        except MyLastException:
            result = "MyLastException"
        finally:
            return result


print('-'*50)
MyCalc = Calc

print(MyCalc.add(9, 2))
print(MyCalc.sub(-1, 2))
print(MyCalc.mul(9, 2))
print(MyCalc.div(9, 2))
print(MyCalc.exp(9, 2))
print(MyCalc.root(-1, 3))


