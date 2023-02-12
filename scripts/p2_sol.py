# Homogeneous Transformation model
# Import important modules
import math
import numpy as np


def trans_x(a):
    """
    Receives an input of translation units along the x-axis
     and returns a translation matrix
    """

    trans = np.array([[1, 0, 0, a],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    return trans


def trans_y(b):
    """
       Receives an input of translation units along the y-axis
        and returns a translation matrix
    """
    trans = np.array([[1, 0, 0, 0],
                      [0, 1, 0, b],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    return trans


def trans_z(c):
    """
         Receives an input of translation units along the z-axis
          and returns a translation matrix
      """
    trans = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, c],
                      [0, 0, 0, 1]])

    return trans


def rot_x(alpha):
    """
    Receives an input in radians and returns a rotation matrix for the x-axis
    """

    rot = np.array([[1, 0, 0, 0],
                    [0, math.cos(alpha), -math.sin(alpha), 0],
                    [0, math.sin(alpha), math.cos(alpha), 0],
                    [0, 0, 0, 1]])

    return rot


def rot_y(beta):
    """
    Receives an input in radians and returns a rotation matrix for the y-axis
    """

    rot = np.array([[math.cos(beta), 0, math.sin(beta), 0],
                    [0, 1, 0, 0],
                    [-math.sin(beta), 0, math.cos(beta), 0],
                    [0, 0, 0, 1]])

    return rot


def rot_z(gamma):
    """
    Receives an input in radians and returns a rotation matrix for the z-axis
    """

    rot = np.array([[math.cos(gamma), -math.sin(gamma), 0, 0],
                    [math.sin(gamma), math.cos(gamma), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    return rot
