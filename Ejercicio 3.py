precio_neto = float(input("Ingrese el valor neto del producto: "))

iva = precio_neto * 0.15
precio_total = precio_neto + iva

print(f"Monto del IVA (15%): {iva:.2f}")
print(f"Precio final total a pagar: {precio_total:.2f}")
