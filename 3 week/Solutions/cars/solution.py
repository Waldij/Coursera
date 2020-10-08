import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        #body whl
        try:
            length, width, height = (float(c) for c in body_whl.split("x", 2))
        except Exception:
            length, width, height = 0.0, 0.0, 0.0
        return length, width, height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row_to_car(row):
                car_list.append(row_to_car(row)) 

    return car_list

def row_to_car(row):

    if len(row) != 7:
        return None

    keys = [
        'car_type',
        'brand',
        'passenger_seats_count',
        'photo_file_name',
        'body_whl',
        'carrying',
        'extra' 
    ]

    car_table = dict(zip(keys, row))
    car_to_return = None

    try:
        float(car_table['carrying'])
    except:
        return None

    if car_table['car_type'] == "car":
        try:
            int(car_table['passenger_seats_count'])
        except:
            return None

        car_to_return = Car(car_table['brand'], car_table['photo_file_name'], car_table['carrying'], car_table['passenger_seats_count']) 
    
    if car_table['car_type'] == "truck":
        car_to_return = Truck(car_table['brand'], car_table['photo_file_name'], car_table['carrying'], car_table['body_whl'])

    if car_table['car_type'] == "spec_machine":
        if car_table['extra'] == '':
            return None

        car_to_return = SpecMachine(car_table['brand'], car_table['photo_file_name'], car_table['carrying'], car_table['extra'])

    return check_car(car_to_return)

def check_car(car_to_return):

    if car_to_return == None:
        return None

    if car_to_return.car_type == '' or car_to_return.brand == '' or car_to_return.photo_file_name == '' or car_to_return.carrying == '':
        return None

    if car_to_return.get_photo_file_ext() == '.jpg':
        pass
    elif car_to_return.get_photo_file_ext() == '.jpeg':
        pass
    elif car_to_return.get_photo_file_ext() == '.png':
        pass
    elif car_to_return.get_photo_file_ext() == '.gif':
        pass
    else:
        return None

    return car_to_return
    
