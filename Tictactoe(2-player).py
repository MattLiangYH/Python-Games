grid1 = [" "," "," "]
grid2 = [" "," "," "]
grid3 = [" "," "," "]

print("      "+"c1","c2","c3")
print("r1",grid1)
print("r2",grid2)
print("r3",grid3)
tracker = 0
print("First person = O, Second person's marker is X")

while True:
    spot = input("<")
    if spot == "r1c1" and grid1[0] == " ":
        if tracker%2 == 0:
            grid1[0] = "O"
        else:
            grid1[0] = "X"
    elif spot == "r2c1" and grid2[0] == " ":
        if tracker%2 == 0:
            grid2[0] = "O"
        else:
            grid2[0] = "X"
    elif spot == "r3c1" and grid3[0] == " ":
        if tracker%2 == 0:
            grid3[0] = "O"
        else:
            grid3[0] = "X"
    elif spot == "r1c2" and grid1[1] == " ":
        if tracker%2 == 0:
            grid1[1] = "O"
        else:
            grid1[1] = "X"
    elif spot == "r2c2" and grid2[1] == " ":
        if tracker%2 == 0:
            grid2[1] = "O"
        else:
            grid2[1] = "X"
    elif spot == "r3c2" and grid3[1] == " ":
        if tracker%2 == 0:
            grid3[1] = "O"
        else:
            grid3[1] = "X"
    elif spot == "r1c3" and grid1[2] == " ":
        if tracker%2 == 0:
            grid1[2] = "O"
        else:
            grid1[2] = "X"
    elif spot == "r2c3" and grid2[2] == " ":
        if tracker%2 == 0:
            grid2[2] = "O"
        else:
            grid2[2] = "X"
    elif spot == "r3c3" and grid3[2] == " ":
        if tracker%2 == 0:
            grid3[2] = "O"
        else:
            grid3[2] = "X"
    else:
        print("Error")
        continue
    tracker += 1
    
    #player 2
    if grid1[0] == "X" and grid2[0] =="X" and grid3[0] == "X": #c1's vertical
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[0] == "X" and grid1[1] =="X" and grid1[2] == "X": #top horizontal
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid2[0] == "X" and grid2[1] =="X" and grid2[2] == "X": #middle horizontal
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid3[0] == "X" and grid3[1] =="X" and grid3[2] == "X": #bottom horizontal
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[1] == "X" and grid2[1] =="X" and grid3[1] == "X": #c2's vertical
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[2] == "X" and grid2[2] =="X" and grid3[2] == "X": #c3's vertical
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[0] == "X" and grid2[1] =="X" and grid3[2] == "X": #diagonal left-right
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[2] == "X" and grid2[1] =="X" and grid3[0] == "X": #diagonal right-left
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    
    #player 1
    
    elif grid1[0] == "O" and grid2[0] =="O" and grid3[0] == "O": #c1's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[0] == "O" and grid1[1] =="O" and grid1[2] == "O": #top horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid2[0] == "O" and grid2[1] =="O" and grid2[2] == "O": #middle horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid3[0] == "O" and grid3[1] =="O" and grid3[2] == "O": #bottom horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[1] == "O" and grid2[1] =="O" and grid3[1] == "O": #c2's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[2] == "O" and grid2[2] =="O" and grid3[2] == "O": #c3's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[0] == "O" and grid2[1] =="O" and grid3[2] == "O": #diagonal left-right
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif grid1[2] == "O" and grid2[1] =="O" and grid3[0] == "O": #diagonal right-left
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    
    elif " " not in grid1 and " " not in grid2 and " " not in grid3:
        print("It's a tie")
        break
    else:
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        if tracker%2 == 0:
            print("Player one's turn"+"\n")
        else:
            print("Player two's turn"+"\n")
        continue

