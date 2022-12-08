#Emily Rusch

class Ambulance:
    """priority, speed, and capacity of an ambulance"""

emergency = Ambulance()

emergency.priority = 1
emergency.speed = 80
emergency.capacity = 1

def formula(x):
    p = emergency.priority
    s = emergency.speed
    c = emergency.capacity
    controlled_velocity = -10*(1 - p) + 2.37*(s/10)**3.98 + 30(c+1.2)
    return controlled_velocity

print(formula(emergency))
