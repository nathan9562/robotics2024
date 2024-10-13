#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_viqc import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
intake_motor = Motor("IntakeMotor", 1)
intake_bumper = Bumper("IntakeBumper", 2)
front_distance = Distance("FrontDistance", 3)
front_optical = Optical("FrontOptical", 5)
arm_motor = Motor("ArmMotor", 10)

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

def Move_arm_until_hits_floor():
    global myVariable
    arm_motor.spin(FORWARD)
    wait(3, SECONDS)
    arm_motor.stop()

def dispense_purple():
    global myVariable
    intake_motor.spin(FORWARD)
    wait(1.7, SECONDS)
    intake_motor.stop()

def drive_to_purple_dispenser_on_left():
    global myVariable
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 700, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 290, MM)
    drivetrain.turn_for(RIGHT, 25, DEGREES)
    drivetrain.drive_for(FORWARD, 510, MM)
    drivetrain.turn_for(RIGHT, 65, DEGREES)
    drivetrain.drive_for(REVERSE, 80, MM)

def set_to_max_speed():
    global myVariable
    drivetrain.set_turn_velocity(500, PERCENT)
    drivetrain.set_drive_velocity(500, PERCENT)
    intake_motor.set_velocity(500, PERCENT)
    arm_motor.set_velocity(500, PERCENT)

def when_started1():
    drive_to_purple_dispenser_on_left()
    dispense_purple()
    wait(2, SECONDS)
    drivetrain.drive_for(FORWARD, 270, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    Move_arm_until_hits_floor()


# Add project code in "main"
def main():
    drivetrain.drive_for(FORWARD, 200, MM)

# VR threads — Do not delete
vr_thread(when_started1)
