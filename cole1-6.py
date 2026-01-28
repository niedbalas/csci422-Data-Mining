file_name = input("Enter the filename: ")
with open(file_name, "r") as file:
  print(f"{'Name':<15}{'Hours':>6}{'Total Pay':>15}")

for line in file:
  parts = line.split()
  name = parts[0]
  hours = int(parts[1])
  pay_rate = float(parts[2])
  total_pay = hours * pay_rate

print(f"{name:<15}{hours:>6}{total_pay:>15.2f}")

