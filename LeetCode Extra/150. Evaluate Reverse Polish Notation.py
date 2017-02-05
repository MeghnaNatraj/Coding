class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
                continue
            except ValueError:
                pass

            right = int(stack.pop())
            left = int(stack.pop())
            if i == "+":
                stack.append(left+right)
            elif i == "-":
                stack.append(left-right)
            elif i == "*":
                stack.append(left*right)
            elif i == "/":
                if left<=0 and right<0 or left>=0 and right>0:
                    stack.append(left/right)
                else:
                    stack.append((-1)*(abs(left)/abs(right)))
            else:
                stack.append(left**right)

        return int(stack[0])

        """
        :type tokens: List[str]
        :rtype: int
        """

# Solution 2 using Stack
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

