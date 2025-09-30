# Ex.05 Design a Website for Server Side Processing
# Date:30/09/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
calculate_power.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Lamp Filament Power Calculator</title>
    <style>
        body 
        {
            font-family:Arial, sans-serif;
            margin:20px;
            background-color: #495280ff;
        }
        label 
        {
            display: inline-block;
            width: 150px;
            font-size:19px;
        }
        input[type="number"] 
        {
            width: 250px;
        }
        button
        {
            margin-top:10px;
            width:100px;
            cursor: pointer;
    transition: background-color 0.3s ease; 
}

button:hover {
    background-color:silver;
}
        
        h3
        {
            color: green;
        }  
        .container
        {
            max-width:700px;
            margin: auto;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            margin-top:20%;
            background-color: #f9f9f9;
            height:300px;
        } 


    </style>
</head>
<body>
    <center>
    <div class="container">
    <h1>Lamp Filament Power Calculator</h1>
    <form method="post">
        {% csrf_token %}
        <label for="intensity">Intensity: </label>
        <input type="number" id="intensity" name="intensity" step="any" min="0" required><br><br>
<br>
        <label for="resistance">Resistance: </label>
        <input type="number" id="resistance" name="resistance" step="any" min="0" required><br><br>
<br>
        <button type="submit">Calculate Power</button>
    </form>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}

    {% if power %}
        <h3>Power (P) = {{ power|floatformat:2 }} Watts</h3>
    {% endif %}
</div>
</center>
</body>
</html>

views.py
from django.shortcuts import render

def calculate_power(request):
    power = None
    error = None
    if request.method == "POST":
        try:
            intensity = float(request.POST.get('intensity', ''))
            resistance = float(request.POST.get('resistance', ''))
            if intensity <= 0 or resistance <= 0:
                error = "Please enter positive numbers for intensity and resistance."
            else:
                power = intensity ** 2 * resistance  # P = I^2 * R
        except ValueError:
            error = "Invalid input. Please enter numeric values."

    return render(request, 'calculate_power.html', {'power': power, 'error': error})

```
# SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-09-30 152343.png>)

# HOMEPAGE:

![alt text](<Screenshot 2025-09-30 152309.png>)

# RESULT:
The program for performing server side processing is completed successfully.
