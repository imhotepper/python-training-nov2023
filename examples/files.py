def grep(text, file):
    my_list = []
    with open(file, 'r') as file:
        for line in file:
            if text in line:
                my_list.append(line)
    return my_list


if __name__ == "__main__":
    with open("functions.py", "r") as f:  # f.__enter__()
        for line in f:
            if line.strip() and not line.startswith(" "):
                print(line.strip())
        # f.__exit__()  will close the file

    with open("test.txt", "x+") as f:
        f.write("hello world\n")
        f.write("hello again\n")
        print(f.tell())
        f.seek(0)
        print(f.read(10))
