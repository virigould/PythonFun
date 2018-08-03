

with open("FillDateOffsets.txt") as f:
    count = 0
    for line in f:
        if count < 83:
            lists = line.split()
            print(lists[1])
            count += 1
