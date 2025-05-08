class Stack: 
    def __init__(self): 
        self.items = [] 

    def is_empty(self): 
        return self.items == [] 

    def push(self, data): 
        self.items.append(data) 

    def pop(self): 
        return self.items.pop() 

s = Stack() 
exp = input("Please enter the expression: ") 

is_balanced = True
for c in exp: 
    if c == "(": 
        s.push(1) 
    elif c == ")": 
        if s.is_empty(): 
            is_balanced = False 
            break 
        s.pop() 

if s.is_empty() and is_balanced: 
    print("Expression is correctly parenthesized.") 
else: 
    print("Expression is not correctly parenthesized.")