import random

def data(size, datatype):
    # Asumsi: karena perbandingannya dengan counting sort berarti range angkanya sampai sebesar size arraynya
    # Asumsi: menggunakan choices agar ada pengulangan angka
    numbers = random.choices(range(0, size), k=size)
    if(datatype == 'sorted'):
        numbers.sort()
    elif(datatype == 'reversed'):
        numbers.sort()
        numbers.reverse()

    return numbers

datatypes = ['sorted', 'random', 'reversed']
sizes = [500, 5000, 50000]

print(data(10, 'random'))

for type in datatypes:
    for size in sizes:
        new_data = data(size, type)
        with open(f'{type}_{size}.txt', 'w') as file:
            for num in new_data:
                file.write("%i\n" % num)
