# 전역변수, 지역변수
a = 1
print(a)

def vartest():
    global a
    print(a)
    a = a + 10
    return a

a = vartest()
print(a)
