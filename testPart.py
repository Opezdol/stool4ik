import  cadquery as cq
from math import pi,cos,sin
R = 200
THICK =21
FILLET = 10
seatVerticalScale = 5


sk = (
        cq.Workplane()
        .parametricCurve(
            lambda x:(x,0,
                -seatVerticalScale*cos(x*pi/R)+seatVerticalScale),
            N=400,
            start=0,
            stop=R,
            )
        )

# revolve cosine wave around Z-axis
revolv = sk.revolve(axisStart=(0,0,0), axisEnd=(0,0,1))

# select outer Edge of given circle and offset
res =  revolv.edges('%CIRCLE').workplane(offset= -THICK)
res = res.circle(R).extrude(THICK, combine=False)
# absolute bitchCode
res = res.edges('>Z').fillet(FILLET)
biatch = res.cut(revolv)
res = res.cut(biatch)
show_object(res)
