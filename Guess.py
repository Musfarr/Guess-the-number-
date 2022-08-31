


n = 73
i = 0
while(i < 10):

    gs = int(input("guess the number\n"))
    i = i + 1

    if (gs == n):
        print("congrats you won")
        break
    elif (gs<n):
        print("increase your number\n")
    elif (gs > n):
        print("decrease your nmbr\n")

    print("number of guess left",10 - i)
    continue
print("game over ")
