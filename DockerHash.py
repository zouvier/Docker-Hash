#!/usr/bin/python3
import os
from datetime import datetime as date
#TODO add comments


def docker_write_hash():
    result = os.popen('docker ps -q').read()
    return result


def docker_archive():
    result = os.popen('docker ps').read()
    return result


def calculate_current_time():
    header = '\n---' + str(date.now()) + '---\n'
    return header


Current_containers = str(docker_write_hash()).strip()

docker_archive_current = str(docker_archive()).strip()

Container_archive = open('Container_archive.txt', 'a+')
#if file does not exist. create it. else
Check_if_exist = open('previous_containers.txt', 'a+')


#hold the current Containers in a text file
temp_container = open('Temp_Container.txt', 'w+')
temp_container.write(Current_containers)
temp_container.close()

if os.path.getsize('previous_containers.txt') == 0 and os.path.getsize('Container_archive.txt') == 0:
    Container_archive.write(docker_archive_current)
    Check_if_exist.write(Current_containers)
    Check_if_exist.close()
    Container_archive.close()

elif os.path.getsize('previous_containers.txt') != 0 and os.path.getsize('Container_archive.txt') != 0:
    Check_if_exist.close()
    Previous_container_file = open('previous_containers.txt', 'r')
    temp_container2 = open('Temp_Container.txt', 'r')
    holder = Previous_container_file.read()
    holder2 = temp_container2.read()
    if holder == holder2:
        print('equal')
        Previous_container_file.close()
        temp_container2.close()
        exit()
    else:
        print('not equal')
        Container_archive = open('Container_archive.txt', 'a+')
        Container_archive.write(calculate_current_time())
        Container_archive.write(docker_archive_current)
        Container_archive.close()

    Previous_container_file.close()
    temp_container2.close()

print("Here is the value for result: " + str(Current_containers))
