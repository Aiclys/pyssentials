#!/usr/bin/env python3
import os



def readfile(file_to_open):
    file_to_read = open(file_to_open, "rt")
    return file_to_read.read()

def delfile(file_to_delete):
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    else:
        return "The file does not exist"

def writetofile(content, file_to_write, writing_type):
    if writing_type == "a":
        file_writing = open(file_to_write, "a")
        write = file_writing.write(content)
        file_writing.close()
        file_written = open(file_to_write, "rt")
        read_file = file_written.read()
        return read_file
    elif writing_type == "w":
        file_writing = open(file_to_write, "w")
        write = file_writing.write(content)
        file_writing.close()
        file_written = open(file_to_write, "rt")
        read_file = file_written.read()
        return read_file

def createfile(file_name, content):
    if content == False:
        new_file = open(file_name, "x")
    else:
        new_file = open(file_name, "a")
        new_file.write(content)
        new_file = open(file_name, "rt")
        return new_file.read()

def delfold(folder_to_delete):
    os.rmdir(folder_to_delete)


