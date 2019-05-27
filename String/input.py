# mine = input('가위 바위 보 가운데 하나를 내주세요> ')
# print('mine :', mine)
def shut_down():
    a = input("write your choice: ")
    if a == "yes":
         return "Shutdown"
    elif a == "no":
         return "Shutdown aborted"
    else :
         return "Sorry"

b = shut_down()
print(b)