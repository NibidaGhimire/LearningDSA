# collection of operators
operators = set(['+', '*'])  

# dictionary with operators and its precedence
precedence = {'+':1, '*':2} 
 
def infix_to_postfix(infix): 
    stack=[]
    postfix=""

    for c in infix:
        if c not in operators:
            postfix+=(c)
        else:
            while stack and precedence[c]<=precedence[stack[-1]]:
                postfix+=(stack.pop())

            stack.append(c)

    while stack:
        postfix+=(stack.pop())

    return postfix


expression = input()
print(infix_to_postfix(expression))