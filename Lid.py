import cadquery as cq
from math import pi, cos, sin


def makeLid(
        R: float = 200,
        THICK: float = 21,
        FILLET: float = 10,
        seatVerticalScale: float = 5
    ) -> cq.Workplane:
    """
    Makes the lid of stool4ik
    """

    sk = (
        cq.Workplane()
        .parametricCurve(
            lambda x: (x, 0,
                       -seatVerticalScale*cos(x*pi/R)+seatVerticalScale),
            N=400,
            start=0,
            stop=R,
        )
    )

    # revolve cosine wave around Z-axis
    revolv = sk.revolve(axisStart=(0, 0, 0), axisEnd=(0, 0, 1))

    # select outer Edge of given circle and offset
    res = revolv.edges('%CIRCLE').workplane(offset=-THICK)
    res = res.circle(R).extrude(THICK, combine=False)
    # cut off Solid
    res = res.edges('>Z').fillet(FILLET)
    # WTF!!!
    biatch = res.cut(revolv)
    res = res.cut(biatch)
    return res

def makeLid_theSecond(
        R: float = 200,
        THICK: float = 21,
        FILLET: float = 10,
        seatVerticalScale: float = 5
    ) -> cq.Workplane:
    """ Second version of lid.
    """
    def _wave(plane: cq.Workplane)->cq.Solid:
        """
        generates solid wave to cut the base perpendicular to given plane"""

        wave =(
                plane
                .parametricCurve(
                    lambda x: (x,0,
                        seatVerticalScale*cos(1.69*x*pi/R)-seatVerticalScale
                        ),
                    start = 0,
                    stop = R
                    )
                )
        debug(wave)
        res = wave.revolve(axisEnd=plane.val().normalized(),combine=False)
        return res
    base = (
            cq.Workplane()
            .circle(R)
            .extrude(THICK)
            )
    return _wave(base.faces('>Z').workplane())
res = makeLid_theSecond()
show_object(res)
