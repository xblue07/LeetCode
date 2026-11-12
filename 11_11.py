class Solution:
    def isValid(self, s: str) -> bool:
        myStack=[]
        for symbol in s: 
            if symbol is '(' or symbol is '[' or symbol is '{':
                myStack.append(symbol)
            else:
                if symbol is ')'and myStack.peek() is '(':
                 