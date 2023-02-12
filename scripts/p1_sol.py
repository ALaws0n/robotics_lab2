# import math, rigid body motion module, and numpy
import math
import rbm
import numpy as np

if __name__ == '__main__':
    # define rotation values
    psi = math.pi/2
    theta = math.pi/2
    phi = math.pi/2
    # update the output format
    np.set_printoptions(precision=2, suppress=True)
    # define a 3D rotation about the x-axis using psi (1st)
    Rx = rbm.rot_x(psi)
    # define a 3D rotation about the y-axis using theta (2nd)
    Ry = rbm.rot_y(theta)
    # define a 3D rotation about the z-axis using phi (3rd);
    Rz = rbm.rot_z(phi)
    # FIXED FRAME ROLL-PITCH-YAW (pre-multiply)
    RzRy = np.matmul(Rz, Ry)
    Final_Rotation = np.matmul(RzRy, Rx)
    print('The final rotation matrix is:\n',Final_Rotation)


