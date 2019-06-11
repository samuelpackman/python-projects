import numpy as np
import random as ra
import cmath as cm
import math as m

class robot:
    def __init__(self,space,space_object):
        self.sensors #figure out later

    def __str__(self):
        return "space: " + str(self.space) + "coords: " + str(self.coords) + "vel: " + str(self.vel) + "dims: " + str(self.dims) + "sensors: " + str(self.sensors)

    def plotmotion(self,vels,time):
        self.vel += vels
        space.progress(time)
        self.vel -= vels




class space:
    def __init__(self,dims,plank_length):
        self.dims = dims
        self.objects = []
        self.time = 0
        self.plank_length = plank_length

    def __str__(self):
        return str(self.dims)

    def addobject(self,object1):
        self.robots.append(object1)

    def collision_detect(self):

    def progress(self,timedif):
        timeinc = 1
        while collsion_detect > plank_length:
            for i in range(timeinc):
                for object1 in self.objects:
                    object1.move(1/timeinc)




class space_object:
    def __init__(self,space,coords, vel = 0):
        self.space = space #the space the object is in
        self.coords  = np.array(coords)  # the coordinates in that space
        self.vel = vel  #  the velocity of the object
        self.dims =space_object
        if self.vel == 0:
            self.vel = np.zeros(self.coords.shape)
        self.space.addobject(self)

    def move(self,timeinc):
        self.coords += timeinc * self.vel
