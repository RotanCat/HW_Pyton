bracket_list = []
bracket_type = {'{': '}', '[':']', '<':'>', '(':')'}


def check(bracket_list): #saving the last open brackets in list, the next closing bracket compared with the last open, if not ==, False, if ==, removed from list.
    try:
        with open("input.txt") as text:
            text = text.read()
            for i in text:
                if i in "{[<(":
                    bracket_list.append(i)
                elif i in "}]>)":
                    try:
                        if i == bracket_type[bracket_list[-1]]:
                            bracket_list.pop(-1)
                        else:
                            return False
                    except:
                        return False
            if len(bracket_list) == 0:
                return True
            else:
                return False
    except FileNotFoundError:
        print("File not found")

with open("output.txt", "w") as text:
    text.write(str(check(bracket_list)))