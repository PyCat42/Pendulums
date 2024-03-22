from vpython import *
#Web VPython 3.2
g = 1
t = 0
dt = 0.001
theta = 0
theta1 = 0.001
l = 1
m = 1

graph(width=600,height=400,title='<b>Klatno</b>', background=color.white, xtitle = "vreme u s", ytitle = "ugao u rad",align="right")

"""
ldots = gdots(color=color.purple, interval=100)
ldots.plot(t,log(abs(theta1 - theta)))
"""

vdots=gdots(color=color.magenta, interval=1000, size = 1) 
vdots.plot(t,theta)
v1dots=gdots(color=color.blue, interval=1000, size = 1) 
v1dots.plot(t,theta1)

support = box(pos = vector(0,0,0), size = vector(0.5,0.1,0.1), color = color.black)
rod = cylinder(radius = 0.01, pos = support.pos, axis = vector(l*sin(theta),-l*cos(theta), 0), color = color.magenta)
bob = sphere(radius = 0.1, pos = rod.pos + rod.axis, color =color.magenta, make_trail=True, trail_type="points", interval=1000)

support1 = box(pos = vector(3,0,0), size = vector(0.5,0.1,0.1), color = color.black)
rod1 = cylinder(radius = 0.01, pos = support1.pos, axis = vector(l*sin(theta1),-l*cos(theta1), 0), color =color.blue)
bob1 = sphere(radius = 0.1, pos = rod1.pos + rod1.axis, color =color.blue, make_trail=True, trail_type="points", interval=1000)

scene.width = 600
scene.background = vector(0.96, 0.76, 0.76)
scene.center = (support1.pos - support.pos)/2 - vector(0,l/2,0)

def torque(theta, dampConst, omega, driveAmp, drivefreq):
    return -sin(theta) - dampConst * omega + driveAmp * sin(drivefreq*t)
    
dampConst = 0.5 
driveAmp = 1.2
drivefreq = 2/3
omega = 0

dampConst1 = 0.5 
driveAmp1 = 1.2
drivefreq1 = 2/3
omega1 = 0

while t<200:
    
    rate(10/dt)
    
    alpha = torque(theta, dampConst, omega, driveAmp, drivefreq)
    thetamid=theta+omega*0.5*dt
    omegamid=omega+alpha*0.5*dt
    alphamid = torque(thetamid, dampConst, omegamid, driveAmp, drivefreq)
    
    alpha1 = torque(theta1, dampConst1, omega, driveAmp1, drivefreq1)
    thetamid1=theta1+omega1*0.5*dt
    omegamid1=omega1+alpha1*0.5*dt
    alphamid1 = torque(thetamid1, dampConst1, omegamid1, driveAmp1, drivefreq1)

    rod.axis = vector(l*sin(thetamid), -l*cos(thetamid), 0)
    bob.pos = rod.pos + rod.axis
    theta+=omegamid*dt
    omega += alphamid * dt
    
    rod1.axis = vector(l*sin(thetamid1), -l*cos(thetamid1), 0)
    bob1.pos = rod1.pos + rod1.axis
    theta1+=omegamid1*dt
    omega1 += alphamid1 * dt
    
    t+=dt
    
    """
    ldots.plot(t,log(theta - theta1))
    """
    vdots.plot(t,thetamid)
    v1dots.plot(t,thetamid1)
