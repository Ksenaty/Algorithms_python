# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
sym1 = str(input('Введите первую букву <<< '))
sym2 = str(input('Введите вторую <<< '))
sym1_index = alphabet.find(sym1)
sym2_index = alphabet.find(sym2)
if sym2_index > sym1_index:
    print(f'Индекс первой буквы {sym1_index}\n'
          f'Индекс второй буквы {sym2_index}\n'
          f'Букв между ними {len(alphabet[sym1_index + 1:sym2_index])}\n')
else:
    print(f'Индекс первой буквы {sym1_index}\n'
          f'Индекс второй буквы {sym2_index}\n'
          f'Букв между ними {sym1_index - (sym2_index + 1)}\n')
