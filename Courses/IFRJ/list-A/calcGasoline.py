litroGasolina=5.46 # average price of gasoline in Brazil 2023
valorPago=float(input("Informe o valor pago:"))
litrosAbastecidos = (valorPago/litroGasolina)
print("litrosAbastecidos: " + str(litrosAbastecidos))