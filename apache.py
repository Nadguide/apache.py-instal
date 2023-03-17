#!/usr/bin/python3

import os

#Author: Nad
#Date:03-16-23
#Description: apache installation script

print("beginning apache installation")

os.system('yum install httpd -y')
os.system('systemctl start httpd')
os.system('systemctl status httpd')
os.system('systemctl enable httpd')

print ("end of apache installation")