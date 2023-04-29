content = ""
with open("./test/test_code.txt", "r") as f:
    content = f.read()

lines = content.splitlines()
row = 0
for line in lines:
    words = line.split()
    print(row, "-" , words)
    row += 1
