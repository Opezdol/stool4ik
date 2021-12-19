import cadquery as cq
class Part():

    """ Standard Part select operators"""

    def __init__(self):
        self.obj = cq.Workplane().box(1,1,1)

    def top(self):
        return self.obj.faces('>Z')

    def bottom(self):
        return self.obj.faces('<Z')

    def mate(self,obj):
        pass


