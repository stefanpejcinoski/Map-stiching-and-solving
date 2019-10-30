import heapq
import numpy as np
from .NodeClass import Node 

def costFunction(point1, point2):
    return np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def Astar(image, start, finish):
    
  
    open_list=[]
    closed_list=[]
    heapq.heapify(open_list)
    startnode=Node(start)
    startnode.gcost=costFunction(start, finish)
    startnode.hcost=0
    startnode.fcost=startnode.gcost+startnode.hcost
    
    heapq.heappush(open_list, startnode)
    
    while open_list:
        current=heapq.heappop(open_list)
      
        closed_list.append(current)
      
        
        if current.position==finish:
            path=[]
            node=closed_list[-1]
            while node!=startnode:
                path.append(node.position)
                node=node.parent
            return path[::-1]        
        
        for ind, neighbor in enumerate([(1, 0), (0, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]):
            if ind>3:
                dirCost=1.42
            else:
                dirCost=1
            
            if current.position[0]+neighbor[0]<0 or current.position[0]+neighbor[0]>image.shape[0]-1 or current.position[1]+neighbor[1]<0 or current.position[1]+neighbor[1]>image.shape[1]-1:
                continue
            
            if image[current.position[0]+neighbor[0]][current.position[1]+neighbor[1]]<250:
                continue
            image[current.position[0]+neighbor[0]][current.position[1]+neighbor[1]]=0
            newnode=Node((current.position[0]+neighbor[0], current.position[1]+neighbor[1]), current)
            newnode.gcost=dirCost*costFunction(newnode.position, finish)
            newnode.hcost=current.hcost+1
            newnode.fcost=newnode.gcost+newnode.hcost
            heapq.heappush(open_list, newnode)
            

            
    return False
