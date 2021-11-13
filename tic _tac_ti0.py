a={
    'T1', ' ','T2',' ','T3',' ',
    'M1', ' ','M2',' ','M3',' ',
    'D1',' ', 'D2', ' ','D3', ' '
}

player=1
total_moves=0
print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print('**************************')
while True:
    print(a['T1']+'|'+a['T2']+'|'+a['T3'])
    print('-+-+-')
    print(a['M1']+'|'+a['M2']+'|'+a['M3'])
    print('-+-+-')
    print(a['D1']+'|'+a['D2']+'|'+a['D3'])
    if total_moves == 9:
        break
    while True:
        if player==1:
            p1_input=input('player one')
            if p1_input.upper() in a and a [p1_input.upper()] == ' ':
                a[p1_input.upper()] = 'x'
                player=2
                break
            else:
                print ('invalid input, please try again')
                continue
        else:
            p2_input=input ('player two')
            if p2_input.upper()in a and a [p2_input.upper()]==' ':
                a[p2_input.upper()]= 'o'
                player=1
                break
            else:
                print('invalid input, please try again')
                continue
total_moves += 1
print('**************************')
print()
