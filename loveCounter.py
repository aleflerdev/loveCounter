file = open("charts.csv")
file.readline()
total = 0
love = "love"

for line in file:
    linelist = line.split(",")

    loveIsDumb = linelist[2].lower()

    if love in loveIsDumb:
        total += 1

print(total,"\n\nLooking for love in all the wrong places!\n")
