# Tabla de multiplicar
num = int(input("¿tabla del? "))

print(f"\n--- Tabla del{num}---")
for i in range(1,13):
    resultado = num * i
    print(f"{num} x {i:2d} = {resultado:3d}")

  
    