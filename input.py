def test1():
    # 接受用户输入
    # name = input("Enter a name: ")
    # print("Hello", name.title())

    # eval将输入string认定为是一个python执行语句
    # x = eval(input("Enter a name: "))
    # print(x)

    # 甚至可以接受变量 
    num = 30
    x = eval("num + 42")
    print(x)


test1()