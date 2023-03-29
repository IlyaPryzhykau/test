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
        return 'Мини-автомобили: это самый маленький класс автомобилей, который обычно предназначен для использования в городе.\n Они имеют компактный размер, легкий вес и маленький двигатель. Они часто используются как городские автомобили для кратких поездок в городе.'

mini_1 = Mini('Mini cars', 2019, 'Smart EQ ForTwo Coupe', 'silver color', 'weight 1,085 kg', 'top speed 130 km/h', 'electric drive', 'average fuel consumption 15.7 kWh')


print(mini_1.class_assignment_Mini())
print(mini_1.class_assignment_Mini())
print(mini_1.class_assignment_Mini())