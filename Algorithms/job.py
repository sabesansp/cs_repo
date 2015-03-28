class Job:

   def __init__(self,
                weight=None,
                length=None,
                completion=None):

      self.weight = weight
      self.length = length
      self.completion = completion


   def getWeight(self):
      return self.weight


   def getLength(self):
      return self.length


   def getCompletion(self):
      return self.completion


   def setCompletion(self,
                     completion):
      self.completion = completion      
