canh1 = int(input('nhập chiều ngang '))
canh2 = int(input('nhập chiều cao '))
i = 0
while i <= canh2:
    if i==1 :
        print('*'+('*'*(canh1-2))+'*')
    elif i > 1 and i < canh2:
        print('*'+(' '*(canh1-2))+'*')
    elif i == canh2 :
        print('*' + ('*' * (canh1 - 2)) + '*')
    i = i + 1
exit()