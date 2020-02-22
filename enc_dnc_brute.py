# Brute Force Encryption / Decryption processing of 3 large files together
import time
import os
import sys
from RSA import *
class Task():
    def __init__(self,file_loc = None,task_name = None,key = None):
        self.task_progress = 0
        self.time_spent = 0
        self.file_loc = file_loc
        self.task_name = task_name.lower()
        self.key = key
        if self.task_name is None or self.key is None : raise NotImplementedError("Are you ^*^ me!!!")

    def reset(self,file_loc = None):
        if file_loc is not None : self.file_loc = file_loc
        self.time_spent+=time.time() - self.st
        self.st = time.time()
    
    def start(self,file_name):
        if self.task_name == "encrypt": self.encrypt(file_name)
        elif self.task_name == "decrypt": self.decrypt(file_name)
        else: print("Are you @ me!!")
    
    def encrypt(self,file_name):
        self.st = time.time()
        content = None
        with open(self.file_loc,"r+") as f:
            content = f.read()
        content = encrypt(content, self.key)
        with open(file_name,"w+") as f: f.write(content)
        self.reset()

    def display(self):
        print("---- 100% complete ---")
        print("Time taken : %s seconds"%(self.time_spent))
    
    def decrypt(self,file_name):
        self.st = time.time()
        content = None
        with open(self.file_loc,"r+") as f:
            content = f.read()
        content = decrypt(content, self.key)
        with open(file_name,"w+") as f: f.write(content)
        self.reset()
   
def exec():
    """
    a prompt for encrypting and decrypting from a file and when key is supplied
    """
    print("-----Brute Force Test Task----")
    if len(sys.argv) < 2 : 
        print("Enter document and key location") 
        exit()
    op = input("Enter operation encrypt/decrypt : ")
    brute_task = Task(task_name = op ,key = sys.argv[-1])
    for name in sys.argv[1:-1]:  
        brute_task.file_loc = name  
        brute_task.start(input("Enter output file name : "))
        brute_task.display()        