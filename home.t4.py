import math
try:
    list = []
    while True:
        num = int(input('Введіть число - '))
        if num !=7:
            list.append(num)
        else:
            print(f' Sum: {sum(list)}\n Max: {max(list)}\n Min: {min(list)}\n Good bye!')
            break
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')