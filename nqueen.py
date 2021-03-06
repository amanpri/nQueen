import random
def get_h_cost(board):
  h = 0
  for i in range(len(board)):
    #Check every column we haven't already checked
    for j in range(i + 1,len(board)):  # i=0 1-3,2-3,3-3
      #Queens are in the same row
      if board[i] == board[j]:
        h += 1
      #Get the difference between the current column and the check column
      offset = j - i
      #To be a diagonal, the check column value has to be 
      #equal to the current column value +/- the offset
      if board[i] == board[j] - offset or board[i] == board[j] + offset:
        h += 1
  return h

#main
n=4 # 4 queen problem
i=0
board=[random.randint(0,n-1) for i in range(n)]
print(board)
for i in range(n):
  for j in range(n):
    print(get_h_cost(board),end=' ')
    board[i]=j
  print()