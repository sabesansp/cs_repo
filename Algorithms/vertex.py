class Vertex :


   def __init__(self,
                node_id):

      self.id = node_id
      self.connectedTo = {}



   def addNeighbor(self,
                   nbr,
                   weight=0):

      self.connectedTo[nbr] = weight



   def __str__(self):

      return str(self.id) + ' connected To ' + \
             str([x.id for x in self.connectedTo]) 


   def getConnections(self):

      return self.connectedTo.keys() 



   def getId(self):

      return self.id


   def getWeight(self,nbr):

      return self.connectedTo[nbr]


   def getNeighborWithMinWeight(self):

      neigh_list = self.getConnections()
      min = self.connectedTo[neigh_list[0]]
      ret_val = neigh_list[0]
      for n in neigh_list :
         if self.connectedTo[n] < min :
            min = self.connectedTo[n]
            ret_val = n
      return ret_val

          



 
