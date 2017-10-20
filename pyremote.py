#Copyright 2017 Zachary Nafziger
#PyRemote - Python library for controlling a tv through HDMI
#Note that this was only tested on one tv, I am unsure if the commands are universal
import os

def power_on():
    """Turn the tv on."""
    os.system('echo on 0 | cec-client -s -d 1')

def hdmi_1():
    """Switch to the HDMI 1 source"""
    os.system('echo "tx 4F:82:10:00" | cec-client -s -d 1')
