"""   Rubix Cube game

Author:  De Fine
================================
"""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

Interval = 10

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

rangle ,sangle = 0, 0 # WHY global variable
c, v, b, ang = 0, 0, 0, 0

terminate = 0
Queue_counter = 0
list1 = []

counteru = 0
counters = 0
counterb = 0
counterR = 0
counterM = 0
counterL = 0

shift_x0 = 0  # Line start .
shift_y0 = 0  #Up
shift_z0 = 0  #right

#0  1   2   3   4   5   6   7   8
UA, UB, UC, UD, UE, UF, UG, UH, UI = [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0]
U = [UA, UB, UC, UD, UE, UF, UG, UH, UI]
SA, SB, SC, SD, SE, SF, SG, SH, SI = [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0]
S = [SA, SB, SC, SD, SE, SF, SG, SH, SI]
BA, BB, BC, BD, BE, BF, BG, BH, BI = [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0], [Stack(),Stack(),Stack(),Stack(),0]
B = [BA, BB, BC, BD, BE, BF, BG, BH, BI]


X = U
Y = S
Z = B


# def init():
#     glClearColor(1.0, 1.0, 1.0, 0)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     # gluPerspective(120,1,0.1,10) # try comment this line ; (note: znear can equal 0)
#     glOrtho(-2, 2, -2, 2, -3, 3)  # try this line ; (note:near can be negative)
#     glMatrixMode(GL_MODELVIEW)  # try this
#     glLoadIdentity()
#     # gluLookAt(0.5,1.1,0, 0,0,0,  -1,0,0) # "glLoadIdentity()" in "display_1()" will remove the effect of "gluLookAt", so we must put "gluLookAt" after "glLoadIdentity()" in "display_1()"
#     glEnable(GL_DEPTH_TEST)  # try this with the colored cube below and notice the "black" (the last drawen color)

def init_my_scene(Width, Height):
    glClearColor(0.5, 0.5, 0.5, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix.
    gluPerspective(90, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # not necessary
    glEnable(GL_DEPTH_TEST)  # try this

def Rotate_Upper(an):
    global X
    funcUA(an, 0, 1, 0)
    funcUB(an, 0, 1, 0)
    funcUC(an, 0, 1, 0)
    funcUD(an, 0, 1, 0)
    funcUE(an, 0, 1, 0)
    funcUF(an, 0, 1, 0)
    funcUG(an, 0, 1, 0)
    funcUH(an, 0, 1, 0)
    funcUI(an, 0, 1, 0)

    temp1 = X[0]
    temp2 = X[1]
    X[0] = X[2]
    X[1] = X[5]
    X[2] = X[8]
    X[5] = X[7]
    X[8] = X[6]
    X[7] = X[3]
    X[6] = temp1
    X[3] = temp2

def Rotate_middle_row(an):
    global Y
    funcSA(an, 0, 1, 0)
    funcSB(an, 0, 1, 0)
    funcSC(an, 0, 1, 0)
    funcSD(an, 0, 1, 0)
    funcSE(an, 0, 1, 0)
    funcSF(an, 0, 1, 0)
    funcSG(an, 0, 1, 0)
    funcSH(an, 0, 1, 0)
    funcSI(an, 0, 1, 0)

    temp1 = Y[0]
    temp2 = Y[1]
    Y[0] = Y[2]
    Y[1] = Y[5]
    Y[2] = Y[8]
    Y[5] = Y[7]
    Y[8] = Y[6]
    Y[7] = Y[3]
    Y[6] = temp1
    Y[3] = temp2

def Rotate_lower(an):
    global Z
    funcBA(an, 0, 1, 0)
    funcBB(an, 0, 1, 0)
    funcBC(an, 0, 1, 0)
    funcBD(an, 0, 1, 0)
    funcBE(an, 0, 1, 0)
    funcBF(an, 0, 1, 0)
    funcBG(an, 0, 1, 0)
    funcBH(an, 0, 1, 0)
    funcBI(an, 0, 1, 0)

    temp1 = Z[0]
    temp2 = Z[1]
    Z[0] = Z[2]
    Z[1] = Z[5]
    Z[2] = Z[8]
    Z[5] = Z[7]
    Z[8] = Z[6]
    Z[7] = Z[3]
    Z[6] = temp1
    Z[3] = temp2

def Rotate_Right(an):
    global X, Y, Z
    funcUI(an, 1, 0, 0)
    funcUF(an, 1, 0, 0)
    funcUC(an, 1, 0, 0)

    funcSI(an, 1, 0, 0)
    funcSF(an, 1, 0, 0)
    funcSC(an, 1, 0, 0)

    funcBI(an, 1, 0, 0)
    funcBF(an, 1, 0, 0)
    funcBC(an, 1, 0, 0)

    temp1 = X[8]
    temp2 = X[5]
    X[8] = X[2]
    X[5] = Y[2]
    X[2] = Z[2]
    Y[2] = Z[5]
    Z[2] = Z[8]
    Z[5] = Y[8]
    Z[8] = temp1
    Y[8] = temp2

def Rotate_Middle_column(an):
    global X, Y, Z
    funcUH(an, 1, 0, 0)
    funcUE(an, 1, 0, 0)
    funcUB(an, 1, 0, 0)

    funcSH(an, 1, 0, 0)
    funcSE(an, 1, 0, 0)
    funcSB(an, 1, 0, 0)

    funcBH(an, 1, 0, 0)
    funcBE(an, 1, 0, 0)
    funcBB(an, 1, 0, 0)

    temp1 = X[7]
    temp2 = X[4]
    X[7] = X[1]
    X[4] = Y[1]
    X[1] = Z[1]
    Y[1] = Z[4]
    Z[1] = Z[7]
    Z[4] = Y[7]
    Z[7] = temp1
    Y[7] = temp2

def Rotate_Lift(an):
    global X, Y, Z
    funcUG(an, 1, 0, 0)
    funcUD(an, 1, 0, 0)
    funcUA(an, 1, 0, 0)

    funcSG(an, 1, 0, 0)
    funcSD(an, 1, 0, 0)
    funcSA(an, 1, 0, 0)

    funcBG(an, 1, 0, 0)
    funcBD(an, 1, 0, 0)
    funcBA(an, 1, 0, 0)

    temp1 = X[6]
    temp2 = X[3]
    X[6] = X[0]
    X[3] = Y[0]
    X[0] = Z[0]
    Y[0] = Z[3]
    Z[0] = Z[6]
    Z[3] = Y[6]
    Z[6] = temp1
    Y[6] = temp2

def Rotate_Face_One(an):
    global X, Y, Z
    funcUG(an, 0, 0, 1)
    funcUH(an, 0, 0, 1)
    funcUI(an, 0, 0, 1)

    funcSG(an, 0, 0, 1)
    funcSH(an, 0, 0, 1)
    funcSI(an, 0, 0, 1)

    funcBG(an, 0, 0, 1)
    funcBH(an, 0, 0, 1)
    funcBI(an, 0, 0, 1)

    temp1 = X[6]
    temp2 = X[7]
    X[6] = X[8]
    X[7] = Y[8]
    X[8] = Z[8]
    Y[8] = Z[7]
    Z[8] = Z[6]
    Z[7] = Y[6]
    Z[6] = temp1
    Y[6] = temp2

def Rotate_Face_Two(an):
    global X, Y, Z
    funcUD(an, 0, 0, 1)
    funcUE(an, 0, 0, 1)
    funcUF(an, 0, 0, 1)

    funcSD(an, 0, 0, 1)
    funcSE(an, 0, 0, 1)
    funcSF(an, 0, 0, 1)

    funcBD(an, 0, 0, 1)
    funcBE(an, 0, 0, 1)
    funcBF(an, 0, 0, 1)

    temp1 = X[3]
    temp2 = X[4]
    X[3] = X[5]
    X[4] = Y[5]
    X[5] = Z[5]
    Y[5] = Z[4]
    Z[5] = Z[3]
    Z[4] = Y[3]
    Z[3] = temp1
    Y[3] = temp2

def Rotate_Face_Three(an):
    global X, Y, Z
    funcUA(an, 0, 0, 1)
    funcUB(an, 0, 0, 1)
    funcUC(an, 0, 0, 1)

    funcSA(an, 0, 0, 1)
    funcSB(an, 0, 0, 1)
    funcSC(an, 0, 0, 1)

    funcBA(an, 0, 0, 1)
    funcBB(an, 0, 0, 1)
    funcBC(an, 0, 0, 1)

    temp1 = X[0]
    temp2 = X[1]
    X[0] = X[2]
    X[1] = Y[2]
    X[2] = Z[2]
    Y[2] = Z[1]
    Z[2] = Z[0]
    Z[1] = Y[0]
    Z[0] = temp1
    Y[0] = temp2


def display_1():
    global X, Y, Z, U, S, B, UA, UB, UC, UD, UE, UF, UG, UH, UI, SA, SB, SC, SD, SE, SF, SG, SH, SI, BA, BB, BC, BD, BE, BF, BG, BH, BI
    global rangle, sangle, Queue_counter, terminate
    global list1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # necessary to remove the previous frame
    glColor(1.0, 0.0, 0.0)

    glLoadIdentity()  # necessary to remove the previous transformations

    gluLookAt(0, 4, 8, 0, 2, 0, 0, 2, 0)
    glTranslate(0, 0, 0) #z,zoom in,x
    # glRotate(rangle, 0, 1, 0)

    # try to swap between translation and rotation
    # glRotate(rangle,0,1,0)
    # glTranslate(0.0,0.0,-2)

    # Rotate_Right(rangle)
    # Rotate_Middle_column(90)

    # Rotate_Upper(90)
    # Rotate_middle_row(90)
    # Rotate_Right(90)
    #
    # Rotate_Upper(90)
    # Rotate_Face_One(90)
    # Rotate_middle_row(90)
    for j in range(Queue_counter):

        if j == (Queue_counter-1):

            if list1[j] == "1":
                Rotate_Upper(rangle)
            elif list1[j] == "2":
                Rotate_middle_row(rangle)
            elif list1[j] == "3":
                Rotate_lower(rangle)
            elif list1[j] == "4":
                Rotate_Lift(rangle)
            elif list1[j] == "5":
                Rotate_Middle_column(rangle)
            elif list1[j] == "6":
                Rotate_Right(rangle)
            elif list1[j] == "7":
                Rotate_Face_One(rangle)
            elif list1[j] == "8":
                Rotate_Face_Two(rangle)
            elif list1[j] == "9":
                Rotate_Face_Three(rangle)
            elif list1[j] == "rotate_R":
                Rotate_Upper(rangle)
                Rotate_middle_row(rangle)
                Rotate_lower(rangle)
            elif list1[j] == "rotate_L":
                Rotate_Upper(-rangle)
                Rotate_middle_row(-rangle)
                Rotate_lower(-rangle)
        else:
            if list1[j] == "1":
                Rotate_Upper(90)
            elif list1[j] == "2":
                Rotate_middle_row(90)
            elif list1[j] == "3":
                Rotate_lower(90)
            elif list1[j] == "4":
                Rotate_Lift(90)
            elif list1[j] == "5":
                Rotate_Middle_column(90)
            elif list1[j] == "6":
                Rotate_Right(90)
            elif list1[j] == "7":
                Rotate_Face_One(90)
            elif list1[j] == "8":
                Rotate_Face_Two(90)
            elif list1[j] == "9":
                Rotate_Face_Three(90)
            elif list1[j] == "rotate_R":
                Rotate_Upper(90)
                Rotate_middle_row(90)
                Rotate_lower(90)
            elif list1[j] == "rotate_L":
                Rotate_Upper(-90)
                Rotate_middle_row(-90)
                Rotate_lower(-90)

    Reverse()
    # Rotate_Right(90)
    # Rotate_lower(rangle)
    # Rotate_middle_row(rangle)
    # Rotate_Upper(rangle)
    # Rotate_lower(rangle)
    # Rotate_Middle_column(90)
    #

    Rubix()
    rangle += 2   #speed of rotating
    if terminate == 1:
        sangle -= 2   #speed of rotating

    UA, UB, UC, UD, UE, UF, UG, UH, UI = [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0]
    U = [UA, UB, UC, UD, UE, UF, UG, UH, UI]
    SA, SB, SC, SD, SE, SF, SG, SH, SI = [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [ Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0]
    S = [SA, SB, SC, SD, SE, SF, SG, SH, SI]
    BA, BB, BC, BD, BE, BF, BG, BH, BI = [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [ Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0], [Stack(), Stack(), Stack(), Stack(), 0]
    B = [BA, BB, BC, BD, BE, BF, BG, BH, BI]
    X = U
    Y = S
    Z = B
    if (rangle >= 90):
        rangle = 90
    if (sangle <= -90):
        sangle = 0
        Queue_counter -= 1
    glutSwapBuffers()

def Reverse():
    global terminate, Queue_counter, list1
    if (terminate == 1):

        if list1[(Queue_counter - 1)] == "1":
            Rotate_Upper(sangle)
        elif list1[(Queue_counter - 1)] == "2":
            Rotate_middle_row(sangle)
        elif list1[(Queue_counter - 1)] == "3":
            Rotate_lower(sangle)
        elif list1[(Queue_counter - 1)] == "4":
            Rotate_Lift(sangle)
        elif list1[(Queue_counter - 1)] == "5":
            Rotate_Middle_column(sangle)
        elif list1[(Queue_counter - 1)] == "6":
            Rotate_Right(sangle)
        elif list1[(Queue_counter - 1)] == "7":
            Rotate_Face_One(sangle)
        elif list1[(Queue_counter - 1)] == "8":
            Rotate_Face_Two(sangle)
        elif list1[(Queue_counter - 1)] == "9":
            Rotate_Face_Three(sangle)
        elif list1[(Queue_counter - 1)] == "rotate_R":
            Rotate_Upper(sangle)
            Rotate_middle_row(sangle)
            Rotate_lower(sangle)
        elif list1[(Queue_counter - 1)] == "rotate_L":
            Rotate_Upper(-sangle)
            Rotate_middle_row(-sangle)
            Rotate_lower(-sangle)

        if Queue_counter == 0:
            terminate = 0
            list1.clear()


def funcUA(a, x, y, z):
    X[0][4] += 1
    X[0][0].push(a)
    X[0][1].push(x)
    X[0][2].push(y)
    X[0][3].push(z)
def funcUB(a, x, y, z):
    X[1][4] += 1
    X[1][0].push(a)
    X[1][1].push(x)
    X[1][2].push(y)
    X[1][3].push(z)
def funcUC(a, x, y, z):
    X[2][4] += 1
    X[2][0].push(a)
    X[2][1].push(x)
    X[2][2].push(y)
    X[2][3].push(z)
def funcUD(a, x, y, z):
    X[3][4] += 1
    X[3][0].push(a)
    X[3][1].push(x)
    X[3][2].push(y)
    X[3][3].push(z)
def funcUE(a, x, y, z):
    X[4][4] += 1
    X[4][0].push(a)
    X[4][1].push(x)
    X[4][2].push(y)
    X[4][3].push(z)
def funcUF(a, x, y, z):
    X[5][4] += 1
    X[5][0].push(a)
    X[5][1].push(x)
    X[5][2].push(y)
    X[5][3].push(z)
def funcUG(a, x, y, z):
    X[6][4] += 1
    X[6][0].push(a)
    X[6][1].push(x)
    X[6][2].push(y)
    X[6][3].push(z)
def funcUH(a, x, y, z):
    X[7][4] += 1
    X[7][0].push(a)
    X[7][1].push(x)
    X[7][2].push(y)
    X[7][3].push(z)
def funcUI(a, x, y, z):
    X[8][4] += 1
    X[8][0].push(a)
    X[8][1].push(x)
    X[8][2].push(y)
    X[8][3].push(z)


def funcSA(a, x, y, z):
    Y[0][4] += 1
    Y[0][0].push(a)
    Y[0][1].push(x)
    Y[0][2].push(y)
    Y[0][3].push(z)
def funcSB(a, x, y, z):
    Y[1][4] += 1
    Y[1][0].push(a)
    Y[1][1].push(x)
    Y[1][2].push(y)
    Y[1][3].push(z)
def funcSC(a, x, y, z):
    Y[2][4] += 1
    Y[2][0].push(a)
    Y[2][1].push(x)
    Y[2][2].push(y)
    Y[2][3].push(z)
def funcSD(a, x, y, z):
    Y[3][4] += 1
    Y[3][0].push(a)
    Y[3][1].push(x)
    Y[3][2].push(y)
    Y[3][3].push(z)
def funcSE(a, x, y, z):
    Y[4][4] += 1
    Y[4][0].push(a)
    Y[4][1].push(x)
    Y[4][2].push(y)
    Y[4][3].push(z)
def funcSF(a, x, y, z):
    Y[5][4] += 1
    Y[5][0].push(a)
    Y[5][1].push(x)
    Y[5][2].push(y)
    Y[5][3].push(z)
def funcSG(a, x, y, z):
    Y[6][4] += 1
    Y[6][0].push(a)
    Y[6][1].push(x)
    Y[6][2].push(y)
    Y[6][3].push(z)
def funcSH(a, x, y, z):
    Y[7][4] += 1
    Y[7][0].push(a)
    Y[7][1].push(x)
    Y[7][2].push(y)
    Y[7][3].push(z)
def funcSI(a, x, y, z):
    Y[8][4] += 1
    Y[8][0].push(a)
    Y[8][1].push(x)
    Y[8][2].push(y)
    Y[8][3].push(z)


def funcBA(a, x, y, z):
    Z[0][4] += 1
    Z[0][0].push(a)
    Z[0][1].push(x)
    Z[0][2].push(y)
    Z[0][3].push(z)
def funcBB(a, x, y, z):
    Z[1][4] += 1
    Z[1][0].push(a)
    Z[1][1].push(x)
    Z[1][2].push(y)
    Z[1][3].push(z)
def funcBC(a, x, y, z):
    Z[2][4] += 1
    Z[2][0].push(a)
    Z[2][1].push(x)
    Z[2][2].push(y)
    Z[2][3].push(z)
def funcBD(a, x, y, z):
    Z[3][4] += 1
    Z[3][0].push(a)
    Z[3][1].push(x)
    Z[3][2].push(y)
    Z[3][3].push(z)
def funcBE(a, x, y, z):
    Z[4][4] += 1
    Z[4][0].push(a)
    Z[4][1].push(x)
    Z[4][2].push(y)
    Z[4][3].push(z)
def funcBF(a, x, y, z):
    Z[5][4] += 1
    Z[5][0].push(a)
    Z[5][1].push(x)
    Z[5][2].push(y)
    Z[5][3].push(z)
def funcBG(a, x, y, z):
    Z[6][4] += 1
    Z[6][0].push(a)
    Z[6][1].push(x)
    Z[6][2].push(y)
    Z[6][3].push(z)
def funcBH(a, x, y, z):
    Z[7][4] += 1
    Z[7][0].push(a)
    Z[7][1].push(x)
    Z[7][2].push(y)
    Z[7][3].push(z)
def funcBI(a, x, y, z):
    Z[8][4] += 1
    Z[8][0].push(a)
    Z[8][1].push(x)
    Z[8][2].push(y)
    Z[8][3].push(z)




def Rubix():
    # Upper floor
    glPushMatrix()
    for j in range(UE[4]):
        glRotate(UE[0].pop(), UE[1].pop(), UE[2].pop(), UE[3].pop())
    draw_cube(shift_x0, 2, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UF[4]):
        glRotate(UF[0].pop(), UF[1].pop(), UF[2].pop(), UF[3].pop())
    draw_cube(2, 2, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UD[4]):
        glRotate(UD[0].pop(), UD[1].pop(), UD[2].pop(), UD[3].pop())
    draw_cube(-2, 2, shift_z0, 0)  # Largest cube.
    glPopMatrix()


    glPushMatrix()
    for j in range(UH[4]):
        glRotate(UH[0].pop(), UH[1].pop(), UH[2].pop(), UH[3].pop())
    draw_cube(shift_x0, 2, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UI[4]):
        glRotate(UI[0].pop(), UI[1].pop(), UI[2].pop(), UI[3].pop())
    draw_cube(2, 2, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UG[4]):
        glRotate(UG[0].pop(), UG[1].pop(), UG[2].pop(), UG[3].pop())
    draw_cube(-2, 2, 2, 0)  # Largest cube.
    glPopMatrix()


    glPushMatrix()
    for j in range(UB[4]):
        glRotate(UB[0].pop(), UB[1].pop(), UB[2].pop(), UB[3].pop())
    draw_cube(shift_x0, 2, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UC[4]):
        glRotate(UC[0].pop(), UC[1].pop(), UC[2].pop(), UC[3].pop())
    draw_cube(2, 2, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(UA[4]):
        glRotate(UA[0].pop(), UA[1].pop(), UA[2].pop(), UA[3].pop())
    draw_cube(-2, 2, -2, 0)  # Largest cube.
    glPopMatrix()


    # 2nd floor

    glPushMatrix()
    for j in range(SE[4]):
        glRotate(SE[0].pop(), SE[1].pop(), SE[2].pop(), SE[3].pop())
    draw_cube(shift_x0, shift_y0, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SF[4]):
        glRotate(SF[0].pop(), SF[1].pop(), SF[2].pop(), SF[3].pop())
    draw_cube(2, shift_y0, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SD[4]):
        glRotate(SD[0].pop(), SD[1].pop(), SD[2].pop(), SD[3].pop())
    draw_cube(-2, shift_y0, shift_z0, 0)  # Largest cube.
    glPopMatrix()


    glPushMatrix()
    for j in range(SH[4]):
        glRotate(SH[0].pop(), SH[1].pop(), SH[2].pop(), SH[3].pop())
    draw_cube(shift_x0, shift_y0, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SI[4]):
        glRotate(SI[0].pop(), SI[1].pop(), SI[2].pop(), SI[3].pop())
    draw_cube(2, shift_y0, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SG[4]):
        glRotate(SG[0].pop(), SG[1].pop(), SG[2].pop(), SG[3].pop())
    draw_cube(-2, shift_y0, 2, 0)  # Largest cube.
    glPopMatrix()


    glPushMatrix()
    for j in range(SB[4]):
        glRotate(SB[0].pop(), SB[1].pop(), SB[2].pop(), SB[3].pop())
    draw_cube(shift_x0, shift_y0, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SC[4]):
        glRotate(SC[0].pop(), SC[1].pop(), SC[2].pop(), SC[3].pop())
    draw_cube(2, shift_y0, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(SA[4]):
        glRotate(SA[0].pop(), SA[1].pop(), SA[2].pop(), SA[3].pop())
    draw_cube(-2, shift_y0, -2, 0)  # Largest cube.
    glPopMatrix()


    # base floor
    glPushMatrix()
    for j in range(BE[4]):
        glRotate(BE[0].pop(), BE[1].pop(), BE[2].pop(), BE[3].pop())
    draw_cube(shift_x0, -2, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BF[4]):
        glRotate(BF[0].pop(), BF[1].pop(), BF[2].pop(), BF[3].pop())
    draw_cube(2, -2, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BD[4]):
        glRotate(BD[0].pop(), BD[1].pop(), BD[2].pop(), BD[3].pop())
    draw_cube(-2, -2, shift_z0, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BH[4]):
        glRotate(BH[0].pop(), BH[1].pop(), BH[2].pop(), BH[3].pop())
    draw_cube(shift_x0, -2, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BI[4]):
        glRotate(BI[0].pop(), BI[1].pop(), BI[2].pop(), BI[3].pop())
    draw_cube(2, -2, 2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BG[4]):
        glRotate(BG[0].pop(), BG[1].pop(), BG[2].pop(), BG[3].pop())
    draw_cube(-2, -2, 2, 0)  # Largest cube.
    glPopMatrix()


    glPushMatrix()
    for j in range(BB[4]):
        glRotate(BB[0].pop(), BB[1].pop(), BB[2].pop(), BB[3].pop())
    draw_cube(0, -2, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BC[4]):
        glRotate(BC[0].pop(), BC[1].pop(), BC[2].pop(), BC[3].pop())
    draw_cube(2, -2, -2, 0)  # Largest cube.
    glPopMatrix()

    glPushMatrix()
    for j in range(BA[4]):
        glRotate(BA[0].pop(), BA[1].pop(), BA[2].pop(), BA[3].pop())
    draw_cube(-2, -2, -2, 0)  # Largest cube.
    glPopMatrix()



def draw_cube(shift_x0, shift_y0, shift_z0, edge_length):

    glBegin(GL_QUADS)  # use glTranslate(0.0,0.0,-2), so that the cube will be in the front of camera

    glColor(0, 0, 0)  # black
    glVertex(1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glVertex(1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glColor(0.0, 0.270, 0.678)  # blue
    glVertex(0.95+shift_x0, 1.001+shift_y0, -0.95+shift_z0)
    glVertex(-0.95+shift_x0, 1.001+shift_y0, -0.95+shift_z0)
    glVertex(-0.95+shift_x0, 1.001+shift_y0, 0.95+shift_z0)
    glVertex(0.95+shift_x0, 1.001+shift_y0, 0.95+shift_z0)

    glColor(0, 0, 0)  # black
    glVertex(1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glVertex(1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glColor(0.0, 0.608, 0.282)  # green
    glVertex(0.95+shift_x0, -1.001+shift_y0, 0.95+shift_z0)
    glVertex(-0.95+shift_x0, -1.001+shift_y0, 0.95+shift_z0)
    glVertex(-0.95+shift_x0, -1.001+shift_y0, -0.95+shift_z0)
    glVertex(0.95+shift_x0, -1.001+shift_y0, -0.95+shift_z0)

    glColor(0, 0, 0)  # black
    glVertex(1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glVertex(-1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glVertex(1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glColor(1, 0.349, 0.0)  # orange
    glVertex(0.95+shift_x0, 0.95+shift_y0, 1.001+shift_z0)
    glVertex(-0.95+shift_x0, 0.95+shift_y0, 1.001+shift_z0)
    glVertex(-0.95+shift_x0, -0.95+shift_y0, 1.001+shift_z0)
    glVertex(0.95+shift_x0, -0.95+shift_y0, 1.001+shift_z0)

    glColor(0, 0, 0)  # black
    glVertex(1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glVertex(1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glColor(0.725, 0.0, 0.0)  # red
    glVertex(0.95+shift_x0, -0.95+shift_y0, -1.001+shift_z0)
    glVertex(-0.95+shift_x0, -0.95+shift_y0, -1.001+shift_z0)
    glVertex(-0.95+shift_x0, 0.95+shift_y0, -1.001+shift_z0)
    glVertex(0.95+shift_x0, 0.95+shift_y0, -1.001+shift_z0)

    glColor(0, 0, 0)  # black
    glVertex(-1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glVertex(-1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glVertex(-1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glColor(1, 1, 1)  # white
    glVertex(-1.001+shift_x0, 0.95+shift_y0, 0.95+shift_z0)
    glVertex(-1.001+shift_x0, 0.95+shift_y0, -0.95+shift_z0)
    glVertex(-1.001+shift_x0, -0.95+shift_y0, -0.95+shift_z0)
    glVertex(-1.001+shift_x0, -0.95+shift_y0, 0.95+shift_z0)

    glColor(0, 0, 0)  # black (the last drawn color)
    glVertex(1.0+shift_x0, 1.0+shift_y0, -1.0+shift_z0)
    glVertex(1.0+shift_x0, 1.0+shift_y0, 1.0+shift_z0)
    glVertex(1.0+shift_x0, -1.0+shift_y0, 1.0+shift_z0)
    glVertex(1.0+shift_x0, -1.0+shift_y0, -1.0+shift_z0)
    glColor(1, 0.835, 0.0)  # yellow (the last drawn color)
    glVertex(1.001+shift_x0, 0.95+shift_y0, -0.95+shift_z0)
    glVertex(1.001+shift_x0, 0.95+shift_y0, 0.95+shift_z0)
    glVertex(1.001+shift_x0, -0.95+shift_y0, 0.95+shift_z0)
    glVertex(1.001+shift_x0, -0.95+shift_y0, -0.95+shift_z0)

    glEnd()

def Keyboard_callback(key, x, y):
    global Queue_counter, list1, rangle, terminate
    if (key == b"1") and (terminate != 1):
        list1.append("1")
        Queue_counter += 1
        rangle = 0
    elif (key == b"3") and (terminate != 1):
        list1.append("3")
        Queue_counter += 1
        rangle = 0
    elif (key == b"6") and (terminate != 1):
        list1.append("6")
        Queue_counter += 1
        rangle = 0
    elif (key == b"5") and (terminate != 1):
        list1.append("5")
        Queue_counter += 1
        rangle = 0
    elif (key == b"4") and (terminate != 1):
        list1.append("4")
        Queue_counter += 1
        rangle = 0
    elif (key == b"7") and (terminate != 1):
        list1.append("7")
        Queue_counter += 1
        rangle = 0
    elif (key == b"8") and (terminate != 1):
        list1.append("8")
        Queue_counter += 1
        rangle = 0
    elif (key == b"9") and (terminate != 1):
        list1.append("9")
        Queue_counter += 1
        rangle = 0
    elif (key == b"+") and (terminate != 1):
        list1 = []
        Queue_counter = 0
    elif (key == b"-") and (terminate != 1):
        list1.append("rotate_R")
        Queue_counter += 1
        rangle = 0
    elif (key == b"*") and (terminate != 1):
        list1.append("rotate_L")
        Queue_counter += 1
        rangle = 0
    elif (key == b"0"):
        terminate = 1


def game_timer(v):
    display_1()
    glutTimerFunc(Interval, game_timer, 1)

glutInit()
glutInitWindowSize(800, 600)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutCreateWindow(b'Rubix Cube')
glutDisplayFunc(display_1)
glutTimerFunc(Interval, game_timer, 1)
# glutIdleFunc(display_1)
glutKeyboardFunc(Keyboard_callback)
init_my_scene(800, 600)
glutMainLoop()