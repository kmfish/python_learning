# 如果用户输入不能转换为int，则会发生异常
# x = int(input("Enter a num: "))

# 我们可以使用try来处理异常
while True:
    try:
        x = int(input("Enter a num: "))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('\nNo input taken')
    except ZeroDivisionError as e:  # 访问错误的信息
        print('ZeroDivisionError ocurred: {}'.format(e))
    finally:
        print('\nAttempted Input\n')
