num_tickets = 237
bus_capacity = 48

bus_quantity = num_tickets // bus_capacity
num_tickets_left = num_tickets % bus_capacity

has_partial_bus = False
empty_seats = 0

if num_tickets_left:
    if num_tickets_left >= bus_capacity / 2:
        bus_quantity += 1
        has_partial_bus = True
        empty_seats = bus_capacity - num_tickets_left
        num_tickets_left = 0

print(bus_quantity, num_tickets_left, has_partial_bus, empty_seats)