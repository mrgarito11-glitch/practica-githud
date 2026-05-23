precio_original = float(input("Ingrese el precio original de la prenda: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (ej. 20): "))

monto_deducido = precio_original * (porcentaje_descuento / 100)
precio_final = precio_original - monto_deducido

print(f"Monto deducido: {monto_deducido:.2f}")
print(f"Precio final con descuento: {precio_final:.2f}")
