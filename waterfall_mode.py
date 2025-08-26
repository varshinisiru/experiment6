from weather_model import quadratic_weather_model

print("=== WATERFALL MODE ===")
for hour in range(0, 25, 6):
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

