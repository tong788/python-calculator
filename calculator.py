class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            a = -a
            b = -b

        for i in range(b):  # Loop with the now-positive b
            result = self.add(result, a)

        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")

        is_negative = (a < 0) ^ (b < 0)  

        a = -a if a < 0 else a
        b = -b if b < 0 else b

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        return -result if is_negative else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")

        if a < 0 and b > 0:
            while a < 0:
                a += b
        elif a > 0 and b < 0:
            while a >= -b:
                a += b
        elif a < 0 and b < 0:
            while a <= b:
                a -= b
        else:
            while a >= b:
                a -= b

        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))