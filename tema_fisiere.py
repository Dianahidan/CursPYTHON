import csv

csvreader = csv.DictReader(open('input.csv'))
cars_list = []
for row in csvreader:
    cars_list.append(row)
# # print(cars_list)

slow_cars = list(filter(lambda car: int(car['hp']) < 120, cars_list))
fast_cars = list(filter(lambda car: 120 <= int(car['hp']) < 180, cars_list))
sport_cars = list(filter(lambda car: int(car['hp']) >= 180 , cars_list))
cheap_cars = list(filter(lambda car: int(car['price']) < 1000, cars_list))
medium_cars = filter(lambda car: 1000 <= int(car['price']) < 5000, cars_list)
expensive_cars = filter(lambda car: int(car['price']) >= 5000, cars_list)
# print(slow_cars)
# print(fast_cars)
# print(sport_cars)
# print(cheap_cars)
# print(list(medium_cars))
# print(list(expensive_cars))

import os
if not os.path.exists('output_data'):
    os.makedirs('output_data')

with open('./output_data/slow_cars.csv', 'w') as slow_cars_file:
    csv_writer = csv.writer(slow_cars_file, delimiter =',')
    for new_car in slow_cars:
        csv_writer.writerow(new_car)

with open('./output_data/fast_cars.csv', 'w') as fast_cars_file:
    csv_writer = csv.writer(fast_cars_file, delimiter =',')
    for new_car in fast_cars:
        csv_writer.writerow(new_car)

with open('./output_data/sport_cars.csv', 'w') as sport_cars_file:
    csv_writer = csv.writer(sport_cars_file, delimiter =',')
    for new_car in sport_cars:
        csv_writer.writerow(new_car)

with open('./output_data/cheap_cars.csv', 'w') as cheap_cars_file:
    csv_writer = csv.writer(cheap_cars_file, delimiter =',')
    for new_car in cheap_cars:
        csv_writer.writerow(new_car)

with open('./output_data/medium_cars.csv', 'w') as medium_cars_file:
     csv_writer = csv.writer(medium_cars_file, delimiter=',')
     for new_car in medium_cars:
         csv_writer.writerow(new_car)

with open('./output_data/expensive_cars.csv', 'w') as expensive_cars_file:
    csv_writer = csv.writer(expensive_cars_file, delimiter =',')
    for new_car in expensive_cars:
        csv_writer.writerow(new_car)
