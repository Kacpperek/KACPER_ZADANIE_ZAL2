import random

# Wygeneruj losowy zbiór danych
data = [random.randint(1, 100) for _ in range(10)]

# Wykonaj obliczenia na zbiorze danych
suma = sum(data)
srednia = sum(data) / len(data)
najwieksza = max(data)
najmniejsza = min(data)

# Wyświetl wyniki
print("Zbiór danych:", data)
print("Suma:", suma)
print("Średnia:", srednia)
print("Największa wartość:", najwieksza)
print("Najmniejsza wartość:", najmniejsza)
