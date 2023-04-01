class Auto:

    subclass = 'city cars'

    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption):

        self.car_classes = car_classes
        self.year = year
        self.model = model
        self.color = color
        self.weight = weight
        self.top_speed = top_speed
        self.engine_type = engine_type
        self.fuel_consumption = fuel_consumption

    def brief_information(self):
        return f'{self.car_classes}: {self.year} {self.model} {self.color}'
    def full_information(self):
        return f'{self.car_classes}: {self.year} {self.model} {self.color} {self.weight} {self.top_speed} {self.engine_type} {self.fuel_consumption}'

class Mini(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)

    def class_assignment_Mini(self):
        return 'Мини-автомобили: это самый маленький класс автомобилей, который обычно предназначен для использования в городе.\nОни имеют компактный размер, легкий вес и маленький двигатель. Они часто используются как городские автомобили для кратких поездок в городе.'

mini_1 = Mini('Mini cars', 2019, 'Smart EQ ForTwo Coupe', 'silver color', 'weight 1,085 kg', 'top speed 130 km/h', 'electric drive', 'average fuel consumption 15.7 kWh')


class Compact(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, price,fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)
        self.price = price

    def class_assignment_Compact(self):
        return 'Компактные автомобили: это более крупный класс автомобилей, чем мини-автомобили, но все еще довольно компактный по сравнению с другими классами.\nОни часто предназначены для использования в городе и имеют более мощные двигатели, чем мини-автомобили.'


compact_1 = Compact('Compact cars', 2021, 'Honda Civic', 'blue color', 'weight 1,315 kg', 'top speed 180 km/h', 'front-wheel drive', 'average price $22,000', 'average fuel consumption 7.4 L/100 km')


class Midsize(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, price,fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)
        self.price = price

    def class_assignment_Midsize(self):
        return 'Среднеразмерные автомобили: это класс автомобилей, который обычно используется как семейный автомобиль.\n Они больше, чем компактные автомобили, но все еще достаточно компактные, чтобы использовать в городе. Они могут быть как седанами, так и хэтчбеками.'


Mid_1 = Midsize('Midsize cars', 2022, 'Toyota Camry', 'black color', 'weight 1,545 kg', 'top speed 220 km/h', 'front-wheel drive', 'average price $25,000', 'average fuel consumption 7.2 L/100 km')


class Business(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, price,fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)
        self.price = price

    def class_assignment_Business(self):
        return 'Бизнес-автомобили: это класс автомобилей, который обычно используется в деловых целях.\n Они имеют высокую комфортность и оснащены различными дополнительными функциями и технологиями. Они могут быть как седанами, так и универсалами.'


business_1 = Business('Business cars', 2021, 'BMW 5 Series', 'white color', 'weight 1,765 kg', 'top speed 250 km/h', 'all-wheel drive', 'average price $53,000', 'average fuel consumption 8.7 L/100 km')


class SUV(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, price,fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)
        self.price = price

    def class_assignment_SUV(self):
        return 'Внедорожники: это класс автомобилей, которые предназначены для езды в сложных условиях и по бездорожью.\n Они имеют более высокую проходимость и вместительность, чем другие классы автомобилей.'

suv_1 = SUV('SUVs', 2021, 'Jeep Wrangler', 'green color', 'weight 2,076 kg', 'top speed 180 km/h', 'all-wheel drive', 'average price $34,000', 'average fuel consumption 12.4 L/100 km')


class Sports(Auto):
    def __init__(self, car_classes, year, model, color, weight, top_speed, engine_type, _price,fuel_consumption):
        super().__init__(car_classes, year, model, color, weight, top_speed, engine_type, fuel_consumption)
        self._price = _price

    def class_assignment_Sports(self):
        return 'Спортивные автомобили: это класс автомобилей, которые обычно используются для гоночных мероприятий и для быстрой езды по шоссе.\nОни обычно имеют более мощные двигатели, лучшую маневренность и динамические характеристики, чем другие классы автомобилей.'

sports_1 = Sports('Sports cars', 2022, 'Porsche 911 Carrera', 'red color', 'weight 1,480 kg', 'top speed 291 km/h', 'rear-wheel drive', 'average price $99,000', 'average fuel consumption 10.8 L/100 km')


# print(mini_1.class_assignment_Mini())
# print(mini_1.brief_information())
# print(compact_1.price)
# print(compact_1.full_information())
# print(compact_1.class_assignment_Compact())
print(sports_1.full_information())
print(sports_1._price)
print(sports_1.full_information())
print(sports_1.__dict__)