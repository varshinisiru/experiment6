a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    return a * (time ** 2) + b * time + c

t = 6
print(f"Predicted temperature at t={t}: {quadratic_weather_model(t):.2f}°C")
