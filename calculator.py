result=int(input("type any number you want: "))
cal=input("choose one between 'add', 'subtract', 'multiply', 'divide' or 'stop': ")
while cal!='stop':
    if cal=="add":
        num=int(input("choose number: "))
        result+=num
    elif cal=="subtract":
        num=int(input("choose number: "))
        result-=num
    elif cal=="multiply":
        num=int(input("choose number: "))
        result*=num
    else:
        num=int(input("choose number: "))
        result/=num
        
    cal=input("choose one between 'add', 'subtract', 'multiply', 'divide' or 'stop': ")


print(result)