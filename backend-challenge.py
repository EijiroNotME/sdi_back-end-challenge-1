def find_optimized_cost(required_seats):
    cars = [
        {"size": "S", "capacity": 5, "cost": 5000},
        {"size": "M", "capacity": 10, "cost": 8000},
        {"size": "L", "capacity": 15, "cost": 12000}
    ]
    
    dp = [float('inf')] * (required_seats + 1)
    dp[0] = 0
    
    car_used = [-1] * (required_seats + 1)
    
    for i in range(1, required_seats + 1):
        for car in cars:
            if i >= car['capacity']:
                if dp[i - car['capacity']] + car['cost'] < dp[i]:
                    dp[i] = dp[i - car['capacity']] + car['cost']
                    car_used[i] = car
    
    if dp[required_seats] == float('inf'):
        return "No valid combination found."
    
    result = []
    seats_left = required_seats
    while seats_left > 0:
        car = car_used[seats_left]
        result.append(car)
        seats_left -= car['capacity']
    
    from collections import Counter
    counter = Counter([car['size'] for car in result])
    
    output = []
    total_cost = dp[required_seats]
    output.append(f"Total = PHP {total_cost}")
    
    for size, count in counter.items():
        output.append(f"{size} x {count}")
    
    return "\n".join(output)

if __name__ == "__main__":
    try:
        seat_number = int(input("Please input number (seat): "))
        if seat_number < 0:
            raise ValueError("Number of seats must be non-negative.")
        
        result = find_optimized_cost(seat_number)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
