def vowelFunction(r):
    if (r == 'a') or (r == 'e') or (r == 'i') or (r == 'o') or (r == 'u') or (r == 'A') or (r == 'E') or (r == 'I') or (r == 'O') or (r == 'U'):
        return True
    else:
        return False
u=0
while True:
    ip = input("Enter the single Character  ")
    if(len(ip)==1):
        print(vowelFunction(ip))
        break
    else:
        print("Try Again for it")