# -*- coding: utf-8 -*-
from turtle import *

def rectangle(points):
    [[x0, y0], [xl, yl], [x2, y2], [x3, y3]]= points
    up() 
    setpos(x0, y0) 
    down() 
    setpos(xl, yl) 
    setpos(x2, y2) 
    setpos(x3, y3) 
    setpos(x0, y0)
    
    
def deviding_point(p0, pl, ratio): 
    [x0, y0] = p0 
    [xl, yl] = pl 
    
    xr = deviding(x0, xl, ratio)
    yr = deviding(y0, yl, ratio) 
    return [xr, yr]

def deviding_points(points, ratio): 
    [p0, pl, p2, p3] = points 
    pr0 = deviding_point(p0, pl, ratio) 
    prl = deviding_point(pl, p2, ratio) 
    pr2 = deviding_point(p2, p3, ratio) 
    pr3 = deviding_point(p3, p0, ratio) 
    return [pr0, prl, pr2, pr3] 

def rose_window_recursion(points, ratio, depth):
    rectangle(points) 
    new_points = deviding_points(points, ratio)
    if depth== 0:
        up()
        setpos(-200, -200)
    else:
        rose_window_recursion(new_points, ratio, depth - 1) 

def deviding(p0, pl, r): 
    return p0 * (1 - r) +pl*r

