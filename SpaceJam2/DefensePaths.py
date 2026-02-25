import random, math
from panda3d.core import Vec3

def Cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1
    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec * radius

def BaseballSeams(step, numSeams, B, F=1):
    time = step / float(numSeams) * 2 * math.pi

    F4 = 0
    R = 1

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)

    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    return Vec3(x, y, z)

def CircleX(radius, t):
    x = 0
    y = radius * math.cos(t)
    z = radius * math.sin(t)

    return (x, y, z)

def CircleY(radius, t):
    x = radius * math.cos(t)
    y = 0
    z = radius * math.sin(t)

    return (x, y, z)

def CircleZ(radius, t):
    x = radius * math.cos(t)
    y = radius * math.sin(t)
    z = 0

    return (x, y, z)