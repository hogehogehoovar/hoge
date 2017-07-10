data=[ ]
with open('users.csv', 'r') as file:
    for line in file:
        line = line.rstrip()
        data.append(line.split(","))
    file.close()
output=[ ]
for line in data:
    lst=list(line[14])
    lst[0]=""
    lst[-1]=""
    line[14]=str("".join(lst))
    output.append(line)

with open('users1.csv', 'w') as f:
    for line in output:
        for str in line:
            f.write(str)
            f.write(",")
        f.write('\n')
