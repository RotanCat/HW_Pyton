result = []

delete = input("Enter the symbols to be deleted: ")

with open("input.txt", "r") as file_in:
    file_in = file_in.readlines()
    for i in file_in:
        result.append(i.strip().strip(delete)[::-1] + ";\n")

with open("output.txt", "w") as file_out:
    file_out.writelines(result)