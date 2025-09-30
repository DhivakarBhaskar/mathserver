from django.shortcuts import render

def calculate_power(request):
    power = None
    error = None
    if request.method == 'POST':
        print("POST method is used")
        print(f"request = {request}")
        try:
            intensity = float(request.POST.get('intensity', ''))
            resistance = float(request.POST.get('resistance', ''))
            print(f"Intensity = {intensity}")
            print(f"Resistance = {resistance}")
            if intensity <= 0 or resistance <= 0:
                error = "Please enter positive values for intensity and resistance."
            else:
                power = intensity ** 2 * resistance
                print(f"Power = {power} Watts")
        except ValueError:
            error = "Invalid input. Please enter numeric values."
            print("Input error: Non-numeric value entered.")
    else:
        print(f"{request.method} method is used")

    return render(request, 'calculate_power.html', {'power': power, 'error': error})
