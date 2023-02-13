# Import necessary modules
import math
import numpy as np
import p2_sol as p2


def H_1():
    """
    Complete the following translation with respect to the current frame
    2.5 units on current x-axis
    0.5 units on current z-axis
    -1.5 units on current y-axis
    """
    # Define a translation along the x-axis
    Tx = p2.trans_x(2.5)
    # Define a translation along the z-axis
    Tz = p2.trans_z(0.5)
    # Define a translation along the y-axis
    Ty = p2.trans_y(-1.5)
    # Calculate the translation with relation to the current frame
    TxTz = np.matmul(Tx, Tz)
    Final_Translation = np.matmul(TxTz, Ty)

    return Final_Translation


def H_2():
    """
    Complete the following translation with the respect to the current frame
    0.5 units on current z-axis
    2.5 units on current x-axis
    -1.5 units on current y-axis
    """
    # Define a translation along the z-axis
    Tz = p2.trans_z(0.5)
    # Define a translation along the x-axis
    Tx = p2.trans_x(2.5)
    # Define a translation along the y-axis
    Ty = p2.trans_y(-1.5)
    # Calculate the translation with relation to the current frame
    TzTx = np.matmul(Tz, Tx)
    Final_Translation = np.matmul(TzTx, Ty)

    return Final_Translation


def H_3():
    """
    Complete the following translation in the fixed frame
    2.5 units on current x-axis
    0.5 units on current z-axis
    -1.5 units on current y-axis
    """

    # Define a translation along the x-axis
    Tx = p2.trans_x(2.5)
    # Define a translation along the z-axis
    Tz = p2.trans_z(0.5)
    # Define a translation along the y-axis
    Ty = p2.trans_y(-1.5)
    # Calculate the translation in the fixed frame
    TyTz = np.matmul(Ty, Tz)
    Final_Translation = np.matmul(TyTz, Tx)

    return Final_Translation


def H_4():
    """
    Complete the following translation in the fixed frame
    0.5 units on current z-axis
    2.5 units on current x-axis
    -1.5 units on current y-axis
    """

    # Define a translation along the z-axis
    Tz = p2.trans_z(0.5)
    # Define a translation along the x-axis
    Tx = p2.trans_x(2.5)
    # Define a translation along the y-axis
    Ty = p2.trans_y(-1.5)
    # Calculate the translation matrix in the fixed frame
    TyTx = np.matmul(Ty, Tx)
    Final_Translation = np.matmul(TyTx, Tz)

    return Final_Translation


def H_5():
    """
    Complete the following transformation
    pi/2 rotation about the current x-axis
    3 units on the current x-axis
    -3 units on the current z-axis
    -pi/2 rotation about the current z-axis
    """

    # Define angles of rotation
    theta = math.pi/2
    phi = -math.pi/2
    # Define a rotation about the x-axis
    Rx = p2.rot_x(theta)
    # Define a translation on the x-axis
    Tx = p2.trans_x(3)
    # Define a translation on the z-axis
    Tz = p2.trans_z(-3)
    # Define a rotation about the z-axis
    Rz = p2.rot_z(phi)
    # Calculate the final transformation matrix with respect to current frame
    RxTx = np.matmul(Rx, Tx)
    RxTxTz = np.matmul(RxTx, Tz)
    Final_Transformation = np.matmul(RxTxTz, Rz)

    return Final_Transformation


if __name__ == '__main__':

    np.set_printoptions(precision=2, suppress=True)

    # Get H_1 Matrix and display it
    Transformation_1 = H_1()
    print("Matrix for transformation 1:\n", Transformation_1)

    # Get H_2 Matrix and display it
    Transformation_2 = H_2()
    print("Matrix for transformation 2:\n", Transformation_2)

    # Get H_3 Matrix and display it
    Transformation_3 = H_3()
    print("Matrix for transformation 3:\n", Transformation_3)

    # Get H_4 Matrix and display it
    Transformation_4 = H_4()
    print("Matrix for transformation 4:\n", Transformation_4)

    # Get H_5 Matrix and display it
    Transformation_5 = H_5()
    print("Matrix for transformation 5:\n", Transformation_5)

