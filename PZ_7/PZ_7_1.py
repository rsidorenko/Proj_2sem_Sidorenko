# Дан символ C и строки S, S0. После каждого вхождения символа C в строку S
# вставить строку S0.
S = "ctVdysiCxKuclRBXOEvUyRcKxkcqkCqgR"
S0 = "Swag"
S_new = S.replace('C', 'C' + S0).replace('c' , 'c' + S0)
print('Первоначальная строка:', S)
print('Конечный список:', S_new)