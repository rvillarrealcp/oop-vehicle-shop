class CarManager:
    all_cars:list = list()
    total_cars:int = int
    past_ids:set = set()
    past_services:set = set()

    def __init__(self, make:str, model:str, year:int, mileage:int):
        self._car_id:int = self.create_id()
        self._make:str = make
        self._model:str = model
        self._year:int = year
        self._mileage:int = mileage
        self._services:list = self.create_services()

    def __str__(self):
        return f"ID: {self.car_id} | Make: {self.make} | Model: {self.model} Year: {self.year} | Mileage: {self.mileage}"

    @property
    def car_id(self) -> int:
        return self._car_id
    
    @car_id.setter
    def car_id(self, new_id:int):
        if hasattr(self, '_car_id'):
            raise Exception("ID has already been set")
        if type(new_id) != int:
            raise Exception("ID must be an int")
        else:
            self._car_id = new_id
    
    @property
    def make(self) -> str:
        return self._make
    @make.setter
    def make(self, new_make:str):
        if type(new_make) != str:
            raise Exception("Make must be a str")
        else:
            self._make = new_make

    @property
    def model(self) -> str:
        return self._model
    @model.setter
    def model(self, new_model:str):
        if type(new_model) != str:
            raise Exception("Model must be a str")
        else:
            self._model = new_model

    @property
    def year(self) -> int:
        return self._year
    @year.setter
    def year(self, new_year:int):
        if type(new_year) != int:
            raise Exception("Year must be an int")
        else:
            self._year = new_year

    @property
    def mileage(self) -> int:
        return self._mileage
    @mileage.setter
    def mileage(self, new_milage:int):
        if type(new_milage) != int:
            raise Exception("Mileage must be an int")
        else:
            self._mileage = new_milage

    @property
    def services(self) -> list:
        return self._services
    @services.setter
    def services(self, new_service):
        if hasattr(self, '_services'):
            return
        if type(new_service) != list:
            raise Exception("Services must be a list")

    def create_id(self) -> int:
        if len(self.past_ids):
            new_id = max(list(self.past_ids))+1
        else:
            new_id = 1
        self.past_ids.add(new_id)
        return new_id
    
    def create_services(self) -> list:
        return []   
    @classmethod
    def run_menu(cls):
        run = True
        menu = """
        1. Add a car
        2. View all cars
        3. View total number of cars
        4. See a car's details
        5. Service a car
        6. Update mileage
        7. Quit
        """
        while run:
            user_inp = input(menu)
            if user_inp == '1':
                user_make = input("Enter the make: ")
                user_model = input("Enter the model: ")
                user_year = int(input("Enter the year: "))
                user_mileage = int(input("Enter mileage: "))
                new_car = cls(user_make, user_model, user_year, user_mileage)
                cls.all_cars.append(new_car)
                print(f"Successfully added {user_make} {user_model}!")
            elif user_inp == '2':
                for car in cls.all_cars:
                    print(car)
            elif user_inp == '3':
                print(f"Total number of cars is {len(cls.all_cars)}")
            elif user_inp == '4':
                if not cls.all_cars:
                    print("No cars available to view")
                else:
                    print("\nAvailable cars:")
                    for i, car in enumerate(cls.all_cars, 1):
                        print(f"{i}. {car.make} | {car.model} | {car.year} | (ID: {car.car_id})")
                    choice = input("\nEnter car number to view details: ")
                    idx = int(choice) - 1
                    if choice.isdigit():
                        if 0 <= idx <len(cls.all_cars):
                            car = cls.all_cars[idx]
                            print(f"\n ID: {car.car_id} | Make: {car.make} | Model: {car.model} |Year: {car.year} | Mileage: {car.mileage}")
                        else:
                            print("Invalid car number.")
                    else:
                        print("Please enter a valid selection from the list of options.")
            elif user_inp == '5':
                if not cls.all_cars:
                    print("No cars available to view")
                else:
                    print("\nAvailable cars:")
                    for i, car in enumerate(cls.all_cars, 1):
                        print(f"{i}. {car.make} | {car.model} | {car.year} | (ID: {car.car_id})")
                    choice = input("\nEnter car number to view details: ")
                    idx = int(choice) - 1
                    if choice.isdigit():
                        if 0 <= idx <len(cls.all_cars):
                            car = cls.all_cars[idx]
                            serv_msg = input("Enter name of service performed: ")
                            serv_date = input('Enter date service was performed: ')
                            car.services.append({"Service": serv_msg, "Date": serv_date})
                            print(f"{serv_msg} was successfully added to service record on {serv_date}")
                        else:
                            print("Invalid car number.")
                    else:
                        ("Please enter a valid selection from the list of options.")
            elif user_inp == '6':
                if not cls.all_cars:
                        print("No cars available to view")
                else:
                    print("\nAvailable cars:")
                    for i, car in enumerate(cls.all_cars, 1):
                        print(f"{i}. {car.make} | {car.model} | {car.year} | (ID: {car.car_id})")
                    choice = input("\nEnter car number to view details: ")
                    idx = int(choice) - 1
                    if choice.isdigit():
                        if 0 <= idx <len(cls.all_cars):
                            car = cls.all_cars[idx]
                            new_mileage = int(input("Enter new mileage for vehicle: "))
                            car.mileage = new_mileage
                            print(f"Mileage has successfully been updated to {new_mileage}")
                        else:
                            print("Invalid car number.")
                    else:
                            print("Please enter a valid selection from the list of options")
            elif user_inp == '7':
                print("Thank you for using Car Manager. See you next Time!!!")
                break

CarManager.run_menu()