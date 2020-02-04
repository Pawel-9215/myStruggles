

input_data = open("input.txt")
mass = []
all_the_mass = 0

for line in input_data:
    mass.append(int(line))

#print(mass)



def calculate_fuel(mass):

    total_fuel = int(mass/3) - 2
    
    if total_fuel <= 0:
        return 0
    else:
        total_fuel = total_fuel + calculate_fuel(total_fuel)
        return total_fuel


#print(calculate_fuel(14))

for i in range(len(mass)):

    all_the_mass = all_the_mass + calculate_fuel(mass[i])

print(all_the_mass)

