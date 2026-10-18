with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])

    if area_km2 > 9:
        size = 'Large'
    else:
        size = 'Small'
    print(ward, 'is', size)

