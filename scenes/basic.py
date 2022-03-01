
import multiprocessing as mp
import time

from project.simulation.robot import Robot
from project.simulation.scene import *
from project.simulation.state_machine import SimpleStateMachine
from project.simulation.controller import Control
from project.simulation.utilities import *
from project.simulation.mjremote import mjremote


def run(with_unity=False):
    unity_src = "./unity_builds/Basic.x86_64 &"
    unity = None
    if with_unity:
        # os.system(unity_src)
        # time.sleep(5)
        unity = mjremote()
        while not unity._s:  
            unity.connect() 
            print("conecting...")
        print("SUCCESS")
    
    xml_path = "./project/models/vx300s/vx300s_face_down.xml"
    scene = Mujocoation(xml_path, unity)
    robot = Robot(scene.model, scene.simulation)
    control = Control(robot, scene.simulation)
    moore = SimpleStateMachine(robot, scene, control, orientation=1)
    while True:
        moore.eval()
        control.PID()
        scene.show_step()
    
if __name__ == '__main__':
    
    run(with_unity=True)
