class Point ():
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
        
    def __str__ (self):
        return '< Point %.2f, %.2f >' %(self.x,self.y)
   
    def __eq__ (self,other):
        return self.x == other.x2 and self.y == other.y2
    
    
    def __add__ (self,other):
        x=self.x+other.x
        y=self.y+other.y
        pn= Point(x,y)
        
        return pn