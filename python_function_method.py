number1 = int('10')
number2 = int('2017')
number3 = int('-100')

eto_list = ['子', '丑', '寅']
eto_list.append('卯')
eto_list.remove('丑')
print(eto_list)
# append, removeは　戻り値がない。
eto_str = '子丑寅卯辰巳午未申酉戌亥'
index = eto_str.find('辰')
#index print
print(index)
replaced = eto_str.replace('子', '猫')
#replaced eto_str
print(replaced)
