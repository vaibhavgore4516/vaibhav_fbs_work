feet=int(input("enter distance in feet"))
inches=int(input("enter distance in inches"))
total_inches=feet*12+inches
total_centimeters=total_inches*2.54
meters=int(total_centimeters//100)
centimeters=total_centimeters%100
print("distance in meters",meters)
print("distance in centimeters",centimeters)