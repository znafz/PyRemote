#Copyright 2017 Zachary Nafziger
#PyRemote - Python library for controlling a tv through HDMI
#Note that this was only tested on one Roku-powered tv, I am unsure if the commands are universal
import os
import requests
ipaddr = ""

with open('tvip', 'r') as f:
    ipaddr=f.read().replace('\n', '')

def send_rest_command(cmd):
    """Send a rest command to the tv"""
    url = "http://" + ipaddr + ":8060/" + cmd
    print url
    requests.post(url=url)


def play_pause():
    '''Play or pause the tv via REST'''
    send_rest_command('keypress/play')


def power_on():
    """Turn the tv on."""
    os.system('echo on 0 | cec-client -s -d 1')

def power_off():
    """Turn the tv off."""
    #switching to current device as active source so that standby command is read
    os.system('echo "as" | cec-client -s -d 1')
    os.system('echo "standby 0" | cec-client -s -d 1')

def hdmi_1():
    """Switch to the HDMI 1 source"""
    os.system('echo "tx 4F:82:10:00" | cec-client -s -d 1')

def hdmi_2():
    """Switch to the HDMI 2 source"""
    os.system('echo "tx 4F:82:20:00" | cec-client -s -d 1')

def hdmi_3():
    """Switch to the HDMI 3 source"""
    os.system('echo "tx 4F:82:30:00" | cec-client -s -d 1')

def hdmi_4():
    """Switch to the HDMI 4 source"""
    os.system('echo "tx 4F:82:40:00" | cec-client -s -d 1')

def hdmi_5():
    """Switch to the HDMI 4 source"""
    os.system('echo "tx 4F:82:50:00" | cec-client -s -d 1')

def volume_up():
    """Turn up the volume"""
    os.system('echo "volup" | cec-client -s -d 1')

def volume_down():
    """Turn down the volume"""
    os.system('echo "voldown" | cec-client -s -d 1')

def mute():
    """Mute/unmute"""
    os.system('echo "mute" | cec-client -s -d 1')
