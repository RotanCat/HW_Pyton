lines = []
strip_switch = 0

with open("input1.txt", "r") as file_in:
    file_in = (file_in.readlines())
    for i in file_in:
        if strip_switch:
            lines.append(f"{i.strip()}\n")
        else:
            lines.append(i)

with open("input2.txt", "r") as file_in:
    file_in = (file_in.readlines())
    for i in file_in:
        if strip_switch:
            lines.append(f"{i.strip()}\n")
        else:
            lines.append(i)

lines.sort()

with open("output.txt", "w") as file_out:
    for i in lines:
        file_out.write(i)

#The programm accounts for spaces and other special symbols as legit. For stripping the special symbols toggle the strip_switch = True