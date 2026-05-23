monto_cordobas = float(input("Ingrese la cantidad en Córdobas (C$): "))
tipo_cambio = float(input("Ingrese el tipo de cambio oficial del dólar: "))

equivalencia_dolares = monto_cordobas / tipo_cambio

print(f"La equivalencia es: US$ {equivalencia_dolares:.2f}")
