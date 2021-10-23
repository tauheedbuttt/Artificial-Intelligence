def show_matrix(matrix):
    for i in range(len(matrix)):
        print(f"{i+1}: ", end=' ')
        for j in range(len(matrix[i])):
            print(f"{letters[i][j]} ", end=' ')
        print()

letters = [
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L'],
    ['M','N','O','P'],
    ['Q','R','S','T'],
    ['U','V','W','X'],
    ['Y','Z',' ',' '],
]

# display matrix
show_matrix(letters)

choice = 1
l = 0
rows = []
while(choice!=0):
    choice = int(input(f"Row Number of {l+1} Letter: "))
    if(choice==0): break
    if choice < 0 or choice > 7 :
        raise ValueError(f"{choice} out of bounds")
    rows.append(letters[choice])
    l += 1

transpose = []
for i in range(len(rows)):
    transpose.append([])
    for j in range(len(rows[i])):
        transpose[i].append(rows[j][i])

show_matrix(transpose)
