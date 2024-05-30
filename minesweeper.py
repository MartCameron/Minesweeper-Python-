# Resubmitting this after not completing it properly first time around. The first time 
# worked by I didn't do it as a function that uses the minesweeper board as a parameter. 
# I have now done this.


# Define a function that takes in the minesweeper 2D list board (b) as a parameter

def scores(b):

# Get the number of rows & columns of the input board so you can create an equivalent 
# sized scoreboard. Also you'll need to know these 'lengths' so that you know within  
# what parameters to be searching for mines.

    rows = len(b)
    cols = rows

# Create a new 2D list of equal size to the minefield 2D list. Populate
# with 0s.
    scoreboard = [[0 for i in range(rows)] for j in range(cols)]

# Iterate through each position on the grids. First check if there's a mine
# in that position. If so, add a '#' to the scoreboard 2D list.

# If not, check every position on the 8 touching cells to add 1 whenever a 
# neighbouring cell contains a mine.
# While checking each position, start by ensuring it only checks rows/columns
# that are within the board (eg if you are in the top row, don't check a row
# above as that doesn't exist)
 
    for row in range(rows):
        for col in range(cols):
            if minefield[row][col] == "#":
                scoreboard[row][col] = "#"
            else:
               
                if (row-1)>=0 and (col-1)>=0:
                    if b[row-1][col-1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0

                if (row-1)>=0:
                    if b[row-1][col] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0

                if (row-1)>=0 and (col+1)<cols:
                    if b[row-1][col+1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0     

                if (col+1) < cols:
                    if b[row][col+1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0  


                if (row+1) < rows and (col+1) < cols:
                    if b[row+1][col+1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0  

                if row+1 < rows:
                    if b[row+1][col] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0  

                if row+1 < rows and (col-1)>=0:
                    if b[row+1][col-1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0    

                if (col-1)>=0:
                    if b[row][col-1] == "#":
                        scoreboard[row][col] += 1
                    else:
                        scoreboard[row][col] += 0    
                         

# Print out the minefield so the user can see the original board

    print(b[0])
    print(b[1])
    print(b[2])
    print(b[3])
    print(b[4])

    print()

# Print out the output board so the number of neighbouring mines can be 
# seen in each cell. 

    print(scoreboard[0])
    print(scoreboard[1])
    print(scoreboard[2])
    print(scoreboard[3])
    print(scoreboard[4])       
        
        
        
# Create a minefield.
    
minefield = [["-","-","#","#","-"],
        ["-","#","-","-","#"],
        ["-","-","#","#","-"],
        ["#","-","-","-","-"],
        ["-","#","-","-","-"]]        




# Call the function using the board "minefield" as the parameter

scores(minefield)
        
       