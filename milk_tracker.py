import time
import random
from datetime import datetime


class DiaryLogisticsTruck:
    def __init__(self, truck_id, route_name, initial_temp):
        self.truck_id = truck_id
        self.route_name = route_name
        self.milk_temperature = initial_temp  # Celsius
        self.max_safe_temp = 4.0  # milk must stay under 4°C
        self.is_spoiled = False

    def update_sensor_data(self):
        # Simulate temperature fluctuations during transit
        # randomly simulates a stable cooler or a sudden cooling malfunction
        temp_change = random.choice([-0.2, 0.1, 0.3, 0.8])
        self.milk_temperature = round(self.milk_temperature + temp_change, 2)

        if self.milk_temperature > self.max_safe_temp:
            self.is_spoiled = True

    def check_status(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "⚠ CRITICAL STATUS: Cargo At Risk (Spoilage Hazard)" if self.is_spoiled else "✅ Stable"

        print(f"[{timestamp}] Truck {self.truck_id} ({self.route_name}) | Temp: {self.milk_temperature}°C | Status: {status}")


# Simulate a real-time fleet management dashboard
print("--- STARTING HERDLOGIX MEAT AND DIARY COLD-CHAIN DISPATCH ---")

fleet = [
    DiaryLogisticsTruck("TK-01", "Farm Route A (High Yield)", 1.5),
    DiaryLogisticsTruck("TK-02", "Farm Route B (Regional Diary)", 2.1),
    DiaryLogisticsTruck("TK-03", "Farm Route C (Divisional Meat)", 3.4)
]

# Run a live simulation loop for 5 operational ticks
for tick in range(15):
    time.sleep(1)  # Simulates data packets coming in overtime
    for truck in fleet:
        truck.update_sensor_data()
        truck.check_status()
