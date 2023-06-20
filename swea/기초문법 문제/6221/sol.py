man1 = input()
man2 = input()

if man1 == man2:
    print('Result : Draw')
elif man1 == '가위':
    if man2 == '바위':
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
elif man1 == '바위':
    if man2 == '가위':
        print('Result : Man1 Win!')
    else:
        print('Result : Man2 Win!')
elif man1 == '보':
    if man2 == '가위':
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
