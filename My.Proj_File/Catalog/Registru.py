with open("Catalog.txt", "r") as fp:
    lines = fp.readlines()
    print(*lines, sep = "\n")
with open("Catalog.txt", "w") as fp:
    name_index = input("Write name for delete >>>>: ")
    for line in lines:
        if name_index not in line.strip("\n"):            
            fp.write(line)