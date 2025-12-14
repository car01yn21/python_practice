# for practice only

age = int(input("How old are you? "))

bus_fare = 4.25
fare_type = "standard"

# kids ride for free
is_kid = age < 5
if is_kid:
    bus_fare = 0
    fare_type = "kids"

# seniors gets a dallor off
if age >= 60:
    bus_fare = bus_fare -1
    fare_type = "senior"

print("The " 
      + fare_type + " bus fare is $" + str(bus_fare) + ".")