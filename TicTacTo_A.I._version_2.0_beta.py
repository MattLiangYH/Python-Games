grid1 = [" "," "," "]
grid2 = [" "," "," "]
grid3 = [" "," "," "]
superlst = [grid1,grid2,grid3]
print("      "+"c1","c2","c3")
print("r1",grid1)
print("r2",grid2)
print("r3",grid3)
tracker = 0
print("Human = O, computer's marker is X")
testrand = 0

def move_scanner_bfs(i,j,superlst):
    if superlst[i].count("O") == 2 or superlst[i].count("X") == 2:
        superlst[i][j] = "X"
        count = 1
        return 1
    if i == 0:
        if (superlst[i+1][j] == "O" and superlst[i+2][j] == "O") or (superlst[i+1][j] == "X" and superlst[i+2][j] == "X"):
            superlst[i][j] = "X"
            count = 1
            return 1
        elif j == 0:
            if superlst[i+1][j+1] == "O" and superlst[i+2][j+2] == "O" or superlst[i+1][j+1] == "X" and superlst[i+2][j+2] == "X":
                superlst[i][j] = "X"
                count = 1
                return 1
            else:
                count = 0
                return
    
        elif j == 2:
            if superlst[i+1][j-1] == "O" and superlst[i+2][j-2] == "O" or superlst[i+1][j-1] == "X" and superlst[i+2][j-2] == "X":
                superlst[i][j] = "X"
                count = 1
                return 1
if i == 1:
    if (superlst[i+1][j] == "O" and superlst[i-1][j] == "O") or (superlst[i+1][j] == "X" and superlst[i-1][j] == "X"):
        superlst[i][j] = "X"
        count = 1
            return 1
        elif j == 1:
            if superlst[i-1][j+1] == "O" and superlst[i+1][j-1] == "O" or superlst[i-1][j+1] == "X" and superlst[i-2][j-1] == "X":
                superlst[i][j] = "X"
                count = 1
                return 1
if i == 2:
    if (superlst[1][j] == "O" and superlst[0][j] == "O") or (superlst[i-1][j] == "X" and superlst[i-2][j] == "X"):
        superlst[i][j] = "X"
        count = 1
            return 1
        elif j == 0:
            if superlst[i-1][j+1] == "O" and superlst[i-2][j+2] == "O" or superlst[i-1][j+1] == "X" and superlst[i-2][j+2] == "X":
                superlst[i][j] = "X"
                count = 1
                return 1
    elif j == 2:
        if superlst[i-1][j-1] == "O" and superlst[i-2][j-2] == "O" or superlst[i-1][j-1] == "X" and superlst[i-2][j-2] == "X":
            superlst[i][j] = "X"
            count = int(1)
            return 1
        else:
            count = int(0)
            return


while True:
    if tracker%2 == 0:
        spot = input("<")
        if spot == "r1c1" and superlst[0][0] == " ":
            superlst[0][0] = "O"
        elif spot == "r2c1" and superlst[1][0] == " ":
            superlst[1][0] = "O"
        elif spot == "r3c1" and superlst[2][0] == " ":
            superlst[2][0] = "O"
        elif spot == "r1c2" and superlst[0][1] == " ":
            superlst[0][1] = "O"
        elif spot == "r2c2" and superlst[1][1] == " ":
            superlst[1][1] = "O"
        elif spot == "r3c2" and superlst[2][1] == " ":
            superlst[2][1] = "O"
        elif spot == "r1c3" and superlst[0][2] == " ":
            superlst[0][2] = "O"
        elif spot == "r2c3" and superlst[1][2] == " ":
            superlst[1][2] = "O"
        elif spot == "r3c3" and superlst[2][2] == " ":
            superlst[2][2] = "O"
        else:
            print("Error")
            continue
        tracker += 1
    else:
        sumofblanks = superlst[0].count(" ")+superlst[1].count(" ")+superlst[2].count(" ")
        count = 0
        if tracker == 1 and superlst[1][1] == ' ':
            superlst[1][1] = "X"
        else:
            reservesloti = 0
            reserveslotj = 0
            for i in range(0,3):
                for j in range(0,3):
                    if superlst[i][j] == " ":
                        reservesloti = i
                        reserveslotj = j
                        if count == 0:
                            x = move_scanner_bfs(i,j,superlst)
                            if x == 1:
                                count = 1
            if sumofblanks == superlst[0].count(" ")+superlst[1].count(" ")+superlst[2].count(" "):
                superlst[reservesloti][reserveslotj] = "X"
            count = 0
            tracker += 1

if superlst[0][0] == "X" and superlst[1][0] =="X" and superlst[2][0] == "X": #c1's vertical
    print("Computer wins")
    print("      "+"c1","c2","c3")
    print("r1",grid1)
    print("r2",grid2)
    print("r3",grid3)
    break
    elif superlst[0][0] == "X" and superlst[0][1] =="X" and superlst[0][2] == "X": #top horizontal
        print("Computer wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[1][0] == "X" and superlst[1][1] =="X" and superlst[1][2] == "X": #middle horizontal
        print("Computer wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[2][0] == "X" and superlst[2][1] =="X" and superlst[2][2] == "X": #bottom horizontal
        print("Computer wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][1] == "X" and superlst[1][1] =="X" and superlst[2][1] == "X": #c2's vertical
        print("Player two wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][2] == "X" and superlst[1][2] =="X" and superlst[2][2] == "X": #c3's vertical
        print("Computer wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][0] == "X" and superlst[1][1] =="X" and superlst[2][2] == "X": #diagonal left-right
        print("Computer wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
elif superlst[0][2] == "X" and superlst[1][1] =="X" and superlst[2][0] == "X": #diagonal right-left
    print("Computer wins")
    print("      "+"c1","c2","c3")
    print("r1",grid1)
    print("r2",grid2)
    print("r3",grid3)
    break
    
    #player 1
    
    elif superlst[0][0] == "O" and superlst[1][0] =="O" and superlst[2][0] == "O": #c1's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][0] == "O" and superlst[0][1] =="O" and superlst[0][2] == "O": #top horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[1][0] == "O" and superlst[1][1] =="O" and superlst[1][2] == "O": #middle horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[2][0] == "O" and superlst[2][1] =="O" and superlst[2][2] == "O": #bottom horizontal
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][1] == "O" and superlst[1][1] =="O" and superlst[2][1] == "O": #c2's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][2] == "O" and superlst[1][2] =="O" and superlst[2][2] == "O": #c3's vertical
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][0] == "O" and superlst[1][1] =="O" and superlst[2][2] == "O": #diagonal left-right
        print("Player one wins")
        print("      "+"c1","c2","c3")
        print("r1",grid1)
        print("r2",grid2)
        print("r3",grid3)
        break
    elif superlst[0][2] == "O" and superlst[1][1] =="O" and superlst[2][0] == "O": #diagonal right-left
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
            print("\n")
            print("Player one's turn"+"\n")
        else:
            print("Computer's turn"+"\n")
        
        continue

