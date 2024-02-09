# Set a dictionary for a price list for different hotel types at
# different cities
hotel_price = {
    "a": { # 1st layer "a" stand for Paris
        "a": 220, # 2nd layer "a" stand for luxury hotel
        "b": 120, # 2nd layer "b" stand for mid-scale hotel
        "c": 80, # 2nd layer "c" stand for economy hotel
        "d": 35 # 2nd layer "d" stand for hostel
        },
    "b": { # 1st layer "b" stand for Madrid
        "a": 200,
        "b": 100,
        "c": 85,
        "d": 30
        },
    "c": { # 1st layer "a" stand for New York
        "a": 300,
        "b": 150,
        "c": 100,
        "d": 40
        },
    "d": { # 1st layer "a" stand for Tokyo
        "a": 250,
        "b": 100,
        "c": 75,
        "d": 40
        }
    }

# Set a dictionary for a price list for different car types at
# different cities
car_rent = {
    "a": { # 1st layer "a" stand for Paris
        "a": 35, # 2nd layer "a" stand for economy car
        "b": 60, # 2nd layer "b" stand for premium car
        "c": 120 # 2nd layer "c" stand for luxury car
        },
    "b": { # 1st layer "b" stand for Madrid
        "a": 20,
        "b": 35,
        "c": 60
        },
    "c": { # 1st layer "c" stand for New York
        "a": 20,
        "b": 40,
        "c": 150
        },
    "d": { # 1st layer "d" stand for Tokyo
        "a": 35,
        "b": 65,
        "c": 150
        }
    }

# Set a dictionary for recalling different destination cities
destination = {
    "a": "Paris",
    "b": "Madrid",
    "c": "New York",
    "d": "Tokyo"
}

# Set a dictionary for recalling different types of rental car
car_type_dict = {
    "a": "economy",
    "b": "premium",
    "c": "luxury"
}

# Set a dictionary for recalling different types of hotel
hotel_type_dict = {
    "a": "luxury",
    "b": "mid-scale",
    "c": "economy",
    "d": "hostel"
}

# Define a function for getting valid integer
def get_valid_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                print("Please input a non-negative integer.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Define a function to check if 1st argument is inside 2nd argument
def check_option(son, mother):
    for factor in mother:
        if son == factor:
            return True
    return False

# Use while loop to ask for user's input on holiday destination
city_flight = ""
while not city_flight.isalpha() or len(city_flight) != 1 or not \
    check_option(city_flight, destination.keys()):
    city_flight = input("""
Hello, where would you like to set your destination for your holiday?
A) Paris
B) Madrid
C) New York
D) Tokyo
(Please input the letter for the option) 
""").lower()

# Ask for user input on nights of staying
num_nights = 0
while num_nights < 1: # Use a while loop to ask for input larger than zero
    num_nights = get_valid_integer("""
How long would you like to stay there?
(Please input the number of nights) 
""")
    if num_nights == 0:
        print("So you are not planning to have a holiday somewhere?")

# Ask for user input on no. of days for car rental
rental_days = 99999999999999999999
while rental_days > num_nights: # use while loop to repeat ask for input
# (it's not possible for car rental days more than staying nights)
    rental_days = get_valid_integer("""
How many days would you need to rent for a car?
(Please input the number of days needed)
(The number could not be more than nights of staying)
""")

# Define function for asking user input on hotel choice
def hotel_choice():
    hotel_type = ""
    while not hotel_type.isalpha() or len(hotel_type) != 1 or not \
        check_option(hotel_type, hotel_type_dict.keys()):
        hotel_type = input("""
Please select the type of accomodation:
A) Luxury Hotel
B) Mid-scale
C) Economy
D) Hostel
(Please input the letter for the option) 
""").lower()
    return hotel_type

# Define function to calculate the sum of hotel cost
def hotel_cost(nights, type): # Total cost will be varied by two factors
# nights of staying and hotel type
    total_cost = nights*hotel_price[city_flight][type]
    return total_cost

# Define function to decide the air fare (as instructed to use if and elif for
# the price reference)
def plane_cost(city_flight):
    if city_flight == "a":
        air_fare = 80
    elif city_flight == "b":
        air_fare = 75
    elif city_flight == "c":
        air_fare = 300
    elif city_flight == "d":
        air_fare = 900
    return air_fare

# Define function for asking user input on rental car choice
def car_choice():
    car_type = ""
    while not car_type.isalpha() or len(car_type) != 1 or not \
        check_option(car_type, car_type_dict.keys()):
        car_type = input("""
Please select the type of car:
A) Economy
B) Premium
C) Luxury
(Please input the letter for the option) 
""").lower()
    return car_type

# Define function to calculate the sum of car rent
def car_rental(days, type): # Total cost will be varied by two factors, rental
# days and car type
    total_cost = days*car_rent[city_flight][type]
    return total_cost

# Define function to summarise all information of the holidays.
# Calling different functions to ask for inputs and calculate, then storing the 
# returns as different vairables
def holiday_cost():
    hotel_type = hotel_choice() 
    hotel = hotel_cost(num_nights,hotel_type)
    plane = plane_cost(city_flight)
    car = 0 # set car rent to 0, will be changed to function return value
    # if the user need to rent a car
    if rental_days > 0:
        car_type = car_choice()
        car = car_rental(rental_days,car_type)
    holiday_total_cost = hotel + plane + car
    # Using the returns to summarise all information for the holidays
    print(f"""
We've summarised your holiday's details.
Here they are:

You will going to {destination[city_flight]} for {num_nights} nights.
Airfare with {plane}.
Staying in {hotel_type_dict[hotel_type]} for {num_nights} nights for {hotel}.\
    """)
    if rental_days > 0: # will only print out details of car rental if users
# need to rent a car
        print(f"Rent a {car_type_dict[car_type]} car for {rental_days} days wi\
th {car}.")
    print(f"""
Total cost at {holiday_total_cost}.

Happy Holiday!!
""")
    return holiday_total_cost


holiday_cost() # calling function to work