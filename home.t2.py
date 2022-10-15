try:
    num = int(input('число -> '))
    sym = input('символ -> ')
    var = input('Положення [Вертикально - v | Горизонтально - h] -> ')
    for x in range (0, num):
        if var =='v':
            print(sym)
        elif var == 'h':
            print(sym, end='')
        else:
            raise Exception ('Incorrect choose of var')

except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('\nExit')