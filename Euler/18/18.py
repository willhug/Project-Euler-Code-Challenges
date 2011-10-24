import io

tri = []
def createTriangle():
    triangle = []
    file = open("triangle67.txt", "r")
    triangle = file.read().split("\n")
    triangle.pop(-1)
    for i in triangle:
         tri.append(i.split(" "))
    return tri

def maximizeTriangle():
  for j in range(len(tri) - 2, -1, -1):
    print tri[j]
    for i in range(len(tri[j])):
      tri[j][i] = int(tri[j][i]) + max(int(tri[j+1][i]), int(tri[j+1][i+1]))
  return tri[0][0]


createTriangle()
print maximizeTriangle()
        
