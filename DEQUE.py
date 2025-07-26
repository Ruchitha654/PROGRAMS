stack=[]
info={'a':1,'b':2,'c':3}
stack.append('a')
stack.append('b')
if info[stack[-1]]%2==0:
    stack.pop()
stack.append('c')
if info[stack[0]]+info[stack[-1]]>3:
    stack.append('d')
print(stack)