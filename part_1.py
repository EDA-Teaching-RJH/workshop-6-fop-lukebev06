sample_bay = ["Basalt","Silica","Iron","Dust"]
new_findings = []


print(sample_bay[0])
print(sample_bay[len(sample_bay)-1])

print(len(sample_bay))

for i in range(len(sample_bay)):
    print(f"Transmitting data for: {sample_bay[i]}")

rock_1  = input("enter rock type 1: ")
new_findings.append(rock_1)

rock_2  = input("enter rock type 2: ")
new_findings.append(rock_2)

rock_3  = input("enter rock type 3: ")
new_findings.append(rock_3)

print(new_findings)

if "dust" in sample_bay:
    is_dust = sample_bay.index("dust")
    sample_bay.pop(is_dust)
    print("Dust is gone")
else:
    print("there was no dust")


