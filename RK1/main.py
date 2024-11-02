import HardDrive, Computer, ComputerHardDrive
hard_drives = [
    HardDrive(1, "Seagate Barracuda", 1000, 1),
    HardDrive(2, "WD Blue", 500, 2),
    HardDrive(3, "Samsung EVO", 2000, 3),
    HardDrive(4, "Toshiba X300", 1500, 1),
]

computers = [
    Computer(1, "Alpha Computer"),
    Computer(2, "Beta Computer"), 
    Computer(3, "Gamma Computer"),
]

computer_hard_drive_relations = [
    ComputerHardDrive(1, 1),
    ComputerHardDrive(2, 2),
    ComputerHardDrive(3, 3),
    ComputerHardDrive(4, 1),
]
result_1 = [
    (hd.model, c.name)
    for hd in hard_drives if hd.model.endswith('a')
    for c in computers if c.computer_id == hd.computer_id
]
print("Запрос 1:", result_1)

from collections import defaultdict

computer_capacity_sum = defaultdict(int)
computer_capacity_count = defaultdict(int)

for hd in hard_drives:
    computer_capacity_sum[hd.computer_id] += hd.capacity
    computer_capacity_count[hd.computer_id] += 1

average_capacity = {
    comp_id: computer_capacity_sum[comp_id] / computer_capacity_count[comp_id]
    for comp_id in computer_capacity_sum
}

result_2 = sorted(
    [(c.name, average_capacity[c.computer_id]) for c in computers],
    key=lambda x: x[1]
)
print("Запрос 2:", result_2)

result_3 = [
    (c.name, [hd.model for hd in hard_drives if hd.computer_id == c.computer_id])
    for c in computers if c.name.startswith('A')
]
print("Запрос 3:", result_3)