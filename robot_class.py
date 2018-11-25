from math import *
import random

world_size=100
max_steering_angle=pi/4
landmarks=[[0,0],[0,100],[100,0],[100,100]]                                         #landmarks which the robot is going to sense
landmark_name=['landmark 1','landmark 2','landmark 3','landmark 4']                 #the name of each landmark

class robot():

    def __init__(self):
        self.x=random.random()*world_size                                           #initialize the robot's x axis somwhere in the world
        self.y=random.random()*world_size                                           #initialize the robot's y axis somwhere in the world
        self.orientation=random.random()*2*pi                                       #initialize where the robot is heading
         #the forward, turn, sense noise is initialized into 0
        self.forward_noise=0
        self.turn_noise=0
        self.sense_noise=0
        self.d=[]                                                                   #a list that contains the robots distance from each landmark

    def __repr__(self):                                                             #when printing your robot, it shows your x,y,orientation
        return('[x=%.6s y=%.6s orient=%.6s]' % (str(self.x),str(self.y),str(self.orientation)))

    def set(self,new_x,new_y,new_orient):                                           #function that sets the robots position

        pass

    def set_noise(self,new_f_noise,new_t_noise,new_s_noise):                        #function that sets the robots noise(forward, turn sense)
        pass

    def move(self):                 #moves the robot
        pass

    def sense(self):                #senses the distance from each landmark
        pass

    def Gaussian(self, mu, sigma, x):
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

    def measurement_prob(self, distance):

        '''
        :param distance: the actual distance the robot senses
        :return: the probability of how different a particle's sense data is to the actual sense data
        '''
        prob=1

        for i in range(len(landmarks)):
            dist = sqrt( (self.x - landmarks[i][0]) ** 2 + ( self.y - landmarks[i][1] ) ** 2 )
            prob *= self.Gaussian(dist, self.sense_noise, distance[i])
        return prob
