medium = 0


with open("input.txt", "r") as file_in:
    file_in = file_in.readlines()
    for i in file_in:
        medium += int((i.strip().split(","))[-1])
    medium = medium / len(file_in)
    with open("output.txt", "w") as file_out:
        for i in file_in:
            if int((i.strip().split(","))[-1]) > medium:
                file_out.write(f"{(i.strip().split(","))[0]}\n")


