import cadquery as cq
from helper_classes import Part

H = 540
W = 420
class Ass(Part):
    def __init__(self):
        super().__init__()

    def selfMate(self):
        pass


def main():
    obj  = Ass()
    show_object(obj)
    debug (obj.top())

main()
