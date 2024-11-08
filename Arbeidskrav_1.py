#!/usr/bin/env python3

# Arbeidskrav 1
# PY1010-1 24H Grunnleggende programmering med Python
# Abubakr Iqbal - abiqb8651

# Km driven
yearly_driven_km = 16000

# Insurance
insurance_electric_vehicle = 5000
insurance_gas_vehicle = 7500
insurance_fee_car = 8.38
insurance_year = 365
insurance_fee_yearly = insurance_fee_car * insurance_year

# Electricity cost for electric vehicle
kwh_one_km = 0.2
price_per_kwh = 2.0
electric_car_price = kwh_one_km * price_per_kwh * yearly_driven_km

# Fuel cost for bensin 
gasoline_price = 1.0
gasoline_car_price = gasoline_price * yearly_driven_km

# Toll cost
toll_price_electric_car = 0.1 * yearly_driven_km
toll_price_gasoline_car = 0.3 * yearly_driven_km

# Total cost electric / bensin
total_cost_electric_vehicle = insurance_electric_vehicle + electric_car_price + toll_price_electric_car + insurance_fee_yearly
total_cost_gasoline_vehicle = insurance_gas_vehicle + gasoline_car_price + toll_price_gasoline_car + insurance_fee_yearly
diff = total_cost_gasoline_vehicle - total_cost_electric_vehicle

# Svar og beregninger
print("Årlige totalkostnader:\n")

# Elbil
print(f"Elbil:")
print(f"  Forsikring: {insurance_electric_vehicle} kr")
print(f"  Strøm: {electric_car_price} kr")
print(f"  Bom: {toll_price_electric_car} kr")
print(f"  Total: {total_cost_electric_vehicle} kr\n")

# Bensin
print(f"Bensinbil:")
print(f"  Forsikring: {insurance_gas_vehicle} kr")
print(f"  Bensin: {gasoline_car_price} kr")
print(f"  Bom: {toll_price_gasoline_car} kr")
print(f"  Total: {total_cost_gasoline_vehicle} kr\n")

# Utskrift av differanse basert verdier
if diff > 0:
	print(f"Differanse: Bensinbil koster {diff} kr mer enn elbil per år.")
elif diff < 0:
	print(f"Differanse: Elbil koster {diff} kr mer enn bensinbil per år.")
else:
	print("Ingen differanse: Elbil og bensinbil koster det samme per år.")
