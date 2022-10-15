import math

try:
    List_odd = []
    List_even = []
    List_9 = []
    begin = int(input('begin - '))
    end = int(input('end - '))
    for item in range(begin, end):
        if item %2 ==0:
            List_even.append(item)
        if item %2 !=0:
            List_odd.append(item)
        if item %9 ==0:
            List_9.append(item)
    print(f'Even numbers: {List_even}\n Sum of even: {sum(List_even)}\n Avg of even {sum(List_even)/len(List_even)}\n')
    print(f'Odd numbers: {List_odd}\n Sum of odd: {sum(List_odd)}\n Avg of odd {sum(List_odd)/len(List_odd)}\n')
    print(f'Nine numbers: {List_9}\n Sum of nine: {sum(List_9)}\n Avg of nine {sum(List_9) / len(List_9)}\n')

except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')