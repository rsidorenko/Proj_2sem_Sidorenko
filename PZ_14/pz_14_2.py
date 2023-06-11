import re

file1 = open('hotline1.txt', 'r', encoding='UTF-8').read()
file = re.findall(r"(8?.\(\d{3}\)?.\d{3}-\d{2}-\d{2})", file1)
result = list(set(file))
print('Номера телефонов: ', ', '.join(result))
print('Количество элементов:', len(result))
print('\n')

old_file = open('hotline1.txt', encoding='UTF-8')
read = old_file.readlines()
old_file.close()
new_file = open('upd_hotline1.txt', 'w', encoding='UTF-8')
for x in read:
    string = re.sub('«Горячая линия»', '«Горячая линия Министерства образования Ростовской области»', x)
    new_file.writelines(string)
new_file.close()