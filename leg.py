import cadquery as cq
from math import sin, cos, pi

def makeLeg(
        r_up: float = 80,
        r_down: float = 120,
        h: float = 350,
        k: float = 3, # k-parabola form
        ) -> cq.Workplane:
    sweep = (
            cq.Workplane()
            .parametricCurve(
                #lambda x: (x,0,-h*sin(0.5*pi*x/r_down)),
                lambda x: (x,0, -h*((x)/r_down)**2),
                N = 100,
                start = 0,
                stop = r_down,
                )
            )
    debug (sweep)
    res_sine = (
            cq.Workplane()
            .rect(-40,21,centered = (False,True,False))
            .sweep(sweep,multisection=True)
            )
    res_parabola = (
            cq.Workplane("YZ")
            .rect(21,-40)
            .sweep(sweep)
            )
    # dimentions on zaxis
    top = res_parabola.val().BoundingBox().zmax
    zmin = res_parabola.val().BoundingBox().zmin
    cut_plane = (
            cq.Workplane(origin=(0,0,-(h-top)))
            .rect(r_down+50,50,centered=(False,True,True))
            .extrude((h-top+zmin))
            )
    #debug(cut_plane)
    # Cutoff extra
    res_parabola = res_parabola.cut(cut_plane)


    print(f'Zlen -> {res_parabola.val().BoundingBox().zlen} mm')
    return res_parabola

show_object(makeLeg())
