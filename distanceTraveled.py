#distance=speed *time

def main():
    speed=int(input("Enter speed traveled: "))
    time=int(input("Enter hours traveled: "))
    distance_Traveled(speed, time)

def distance_Traveled(speed, time):
    distance=speed*time
    print(f"At the speed of {speed} mph and the time traveled for {time} hours the distance is {distance} miles")
    
main()


