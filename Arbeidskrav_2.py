#!/usr/bin/env python3

# Arbeidskrav 2
# PY1010-1 24H Grunnleggende programmering med Python
# Abubakr Iqbal - abiqb8651

# Oppgave 1
year_born = int(input('Hvilket år er du født? '))
age_particular_year = 2024
age = age_particular_year - year_born
print(f'Du er eller blir {age} år i løpet av dette året.')


# Oppgave 2
num_students = int(input('Skriv inn antall elever:' ))
pizza_per_student = 1 / 4  
total_pizzas = num_students * pizza_per_student
pizzas_to_buy = int(total_pizzas) + 1
print(f'Det må handles inn {pizzas_to_buy} pizzaer til festen.')


# Oppgave 3
import numpy as np
v_grad = float(input('Skriv inn gradtallet: '))
v_rad = v_grad * np.pi / 180
print(f'Vinkelen {v_grad} grader tilsvarer {v_rad:.4f} radianer.')


# Oppgave 4a)
data = {
	"Norge": ["Oslo", 0.634],
	"England": ["London", 8.982],
	"Frankrike": ["Paris", 2.161],
	"Italia": ["Roma", 2.873]
}


# Oppgave 4b og 4c)
country = input("Skriv inn ett land: ").strip().capitalize()

if country in data:
	capital = data[country][0]
	population = data[country][1]
	print(f"{capital} er hovedstaden i {country} og det er {population} mill. innbyggere i {capital}.")
else:
	print(f"Det finnes ikke data om landet {country}.")
	add_new = input(f"Vil du legge til {country} i dictionaryen? (ja/nei): ").strip().lower()
	if add_new == "ja":
		capital = input(f"Skriv inn hovedstaden i {country}: ").strip().capitalize()
		population = float(input(f"Skriv inn antall millioner innbyggere i {capital}: "))
		data[country] = [capital, population]
		print(f"{country} med hovedstaden {capital} og {population} mill. innbyggere er lagt til i dictionaryen.")
	else:
		print(f"{country} ble ikke lagt til i dictionaryen.")
		
print("\nOppdatert dictionary:")
for country, info in data.items():
	print(f"{country}: Hovedstad: {info[0]}, Innbyggere: {info[1]} mill.")
	
	
# Oppgave 5)
a = float(input("Skriv inn lengden til a: "))
b = float(input("Skriv inn lengden til b: "))

hypotenuse = (a**2 + b**2)**0.5 
radius = hypotenuse / 2 
triangle_area = (a * b) / 2 
semicircle_area = (3.1415 * radius**2) / 2  
semicircle_pem = 3.1415 * radius  
total_pem = a + b + semicircle_pem 
total_area = triangle_area + semicircle_area  

print(f"Arealet til figuren er: {total_area:.2f}")
print(f"Den ytre omkretsen til figuren er: {total_pem:.2f}")


# Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y, color='green', label=r"$f(x) = -x^2 - 5$")
plt.title("Oppgave 6 - Graf av funksjonen $f(x) = -x^2 - 5$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
