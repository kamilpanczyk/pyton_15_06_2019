import random
tip = random.randint(0, 4)
skarbx, skarby = random.randint(0, 10), random.randint(0, 10)
graczx, graczy = random.randint(0, 10), random.randint(0, 10)
skarbx
moves = 0
graczynew = 0
graczxnew = 0
print(skarbx, skarby, graczx, graczy, moves)
while True:
    odx = graczx - skarbx
    ody = graczy - skarby
    move = input("Gdzie chcesz pójść? W S A D ")


    if move == "W":
        graczynew = graczy + 1;
    elif move == "S":
        graczynew = graczy - 1;
    elif move == "A":
        graczxnew = graczx - 1;
    elif move == "D":
        graczxnew = graczx + 1;
    if graczynew < 0 or graczynew > 10 or graczxnew < 0 or graczxnew > 10:
        print("Przegrałeś ")
        break;
    moves = moves + 1
    if odx == 0 and ody == 0:
        print("Wygrałeś")
    if graczynew - skarby > ody:
        print("Oddalasz się od skarbu")


print(skarbx, skarby, graczx, graczy, moves)



