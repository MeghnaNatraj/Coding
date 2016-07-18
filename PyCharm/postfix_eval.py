__author__ = 'Meghna'

class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True

    def calc(op1,item,op2):
        if item == '/':
            return op1 / op2
        elif item == '*':
            return op1 * op2
        elif item == '-':
            return op1 - op2
        elif item == '+':
            return op1 + op2
        elif item == '%':
            return op1 % op2

def postfix_evaluation(exp):
    operators = ['/','*','-','+','%']
    s = Stack()
    for item in exp:
        print(item)
        if item not in operators:
            s.push(item)
        else:
            op1 = s.pop()
            op2 = s.pop()
            print("Here")
            s.push(s.calc(op1,item,op2))
    print("Done")
    return s.pop()

print(postfix_evaluation('345*-'))

