import numpy as np

#algorithm for calculating islands horizontally and vertically
class Solution():
   def numIslands(self, grid): #function for calculating the number of  islands
      if len(grid) == 0:
         return 0
      rows,cols = len(grid) , len(grid[0])
      islands=0 #counter for the number of islands
                      
      for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1': #searchinf for islands
                islands+=1 
            self.ocean(i,j,rows,cols,grid) 
      return islands
   def ocean(self,i,j,rows,cols,grid): #function to calculate the area of the ocean
       if i<0 or j<0 or i>=rows or j>=cols: 
           return False
       if grid[i][j]=='0':
           return False
       else:
           grid[i][j]='0'
         
       self.ocean(i+1,j,rows,cols,grid) #directions
       self.ocean(i,j+1,rows,cols,grid)
       self.ocean(i-1,j,rows,cols,grid)
       self.ocean(i,j-1,rows,cols,grid)
    

n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append([])
    for j in range(m):
        array[i].append(str(np.random.randint(0,2))) #creatinf a matrix of random numbers(0,1)
for x in array:
    print(x)
       
res=Solution()
print(res.numIslands(array))
