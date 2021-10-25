from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

# This script makes the end-effector perform pick, pour, and place tasks
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py'

def main():
    bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")
    #bot.arm.go_to_home_pose()
    #bot.gripper.open()
    #bot.arm.set_ee_pose_components(pitch=1.5,x=0.1, z=0.1)
    #bot.arm.set_ee_cartesian_trajectory(x=.04)# Limit for xaxis at pick-up height seems to be 0.1 (changed
    #line 13 to reflect this)
    bot.arm.set_single_joint_position("waist", np.pi/1.33)
    bot.arm.set_single_joint_position("waist", -np.pi/1.33)
    #bot.arm.set_ee_pose_components(x=0.3, z=0.05) #To get to this coordinate, the ggripper must
    #be angled down 90 deg. as shown in line 13 (The process fails at this coordinate)

if __name__=='__main__':
    main()
