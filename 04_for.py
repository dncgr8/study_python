#　for文　list
point_list = [75, 80, 91]
total = 0
for point in point_list:
    total = total + point

number_of_subject = len(point_list)
average = total/number_of_subject

print('合計点は{},平均点は{}です。'.format(total, average))
# range
for number in range(10):
    print(number)

for number in range(1, 100):
    print(number)

#enumerate

for index, color in enumerate(['red', 'blue', 'green']):
    print("No.{} is {}".format(index, color))
