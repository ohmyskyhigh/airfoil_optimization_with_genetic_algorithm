#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Composite Quadratic Bezier Curve Example (Airfoil)
#   2015-08-12
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import numpy as np

#--- MAIN ---------------------------------------------------------------------+

class Bezier(object):
    def __init__(self):
        pass

    def airfoil(ctlPts,numPts, location):

        def quadraticBezier(t, points):
            #recreated the bezier curve formula
            B_x=(1-t)*((1-t)*points[0][0]+t*points[1][0])+t*((1-t)*points[1][0]+t*points[2][0])
            B_y=(1-t)*((1-t)*points[0][1]+t*points[1][1])+t*((1-t)*points[1][1]+t*points[2][1])
            return B_x,B_y

        curve=[]
        #construct the independent variable
        t=np.array([i*1/numPts for i in range(0,numPts)])

        # calculate first Bezier curve
        midX=(ctlPts[1][0]+ctlPts[2][0])/2
        midY=(ctlPts[1][1]+ctlPts[2][1])/2
        B_x0,B_y0=quadraticBezier(t,[ctlPts[0],ctlPts[1],[midX,midY]])
        curve=curve+list(zip(B_x0,B_y0))

        # calculate middle Bezier Curves
        for i in range(1,len(ctlPts)-3):
            p0=ctlPts[i]
            p1=ctlPts[i+1]
            p2=ctlPts[i+2]
            midX_1=(ctlPts[i][0]+ctlPts[i+1][0])/2
            midY_1=(ctlPts[i][1]+ctlPts[i+1][1])/2
            midX_2=(ctlPts[i+1][0]+ctlPts[i+2][0])/2
            midY_2=(ctlPts[i+1][1]+ctlPts[i+2][1])/2

            B_xi,B_yi=quadraticBezier(t,[[midX_1,midY_1],ctlPts[i+1],[midX_2,midY_2]])
            curve=curve+list(zip(B_xi,B_yi))

        # calculate last Bezier curve
        midX=(ctlPts[-3][0]+ctlPts[-2][0])/2
        midY=(ctlPts[-3][1]+ctlPts[-2][1])/2

        B_x1,B_y1=quadraticBezier(t,[[midX,midY],ctlPts[-2],ctlPts[-1]])
        curve=curve+list(zip(B_x1,B_y1))
        curve.append(ctlPts[-1])

        # write airfoil coordinates to text file
        if True:
            xPts,yPts=zip(*curve)
            f=open(location,'w+')
            for i in range(len(xPts)):
                f.write(str(xPts[i])+','+str(yPts[i])+'\n')
            f.close()

        return curve
