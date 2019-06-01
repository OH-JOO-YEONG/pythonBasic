# def return_false():
#     print("함수 return_false")
#     return False
#
# def return_true():
#     print("함수 return_true")
#     return True
# print("테스트 1")
# a = return_false()
# b = return_true()
#
# if a and b:
#     print(True)
# else:
#     print(False)
#
# print("테스트 2")
# if return_false() and return_true():
#     print(True)
# else:
#     print(False)

dic = {'key2' : 'Value1'}

if "key1" in dic and dic["key1"] == "Value1": #앞에 조건이 false라 else부분으로 넘어감
    print("Key1도 있고 그 값은 Value1이네")
else:
    print("아니네")