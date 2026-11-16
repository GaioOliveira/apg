soma_pares = 0
for n in range(1, 11):
    if n % 2 == 0:
        soma_pares += n
        # OU soma_pares = soma_pares + n
print(f"A soma dos números pares de 1 a 10 é --> {soma_pares}")