from enum import Enum

# Diagnostic #3
# Complete the implementation of the CalculatorPacket class; specifically the perform_calcluation method

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

#A silly class to hold the calculator packet information
class CalculatorPacket:
    def __init__(self, _operator, _operand_A, _operand_B):
       self.operator=_operator
       self.A=_operand_A
       self.B=_operand_B

    #Perform the calculation inputting into the object. If the calculation is invalid, return None
    def perform_calculation(self):
        ans = 0
        if self.operator == Operation.ADD:
            ans = self.A + self.B
        elif self.operator == Operation.SUBTRACT:
            ans = self.A - self.B
        elif self.operator == Operation.MULTIPLY:
            ans = self.A * self.B
        elif self.operator == Operation.DIVIDE:
            ans = self.A / self.B
        else:
            ans = "None"

        return ans





if __name__=="__main__":

    print('We are going to perform some calculations')

    calcA = CalculatorPacket(Operation.ADD,3,5)
    print('Result should be 8. You calculated: '+ str(calcA.perform_calculation()))

    calcB = CalculatorPacket(Operation.SUBTRACT, -7, 52)
    print('Result should be -59. You calculated: ' + str(calcB.perform_calculation()))

    calcC = CalculatorPacket(Operation.MULTIPLY, -10, -7)
    print('Result should be 70. You calculated: ' + str(calcC.perform_calculation()))

    calcD = CalculatorPacket(-1, 3, 5)
    print('Result should be None. You calculated: ' + str(calcD.perform_calculation()))
