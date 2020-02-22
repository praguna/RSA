from enc_dnc_brute import *

# Still should be developed, it's giving a lot of bugs
class Task_Breaker(Task):
    def __init__(self, file_loc=None, task_name=None, key=None, out_file = None):
        super().__init__(file_loc=file_loc, task_name=task_name, key=key)
        if file_loc is None: raise RuntimeError("Howdy,input don't @ me!")
        self.file_name = file_loc
        self.task_name = task_name.lower()
        self.fobj = open(self.file_name,"r+")
        self.file_size = os.stat(self.file_name).st_size
        self.out = open(out_file,"a+")
    
    def encrypt(self,cv=None):
        self.st = time.time()
        content = ""
        if self.task_progress == 100:
            print("Encryption is Complete!!")
            self.fobj.close()
            return True
        elif self.file_size > 10 : 
            content = self.fobj.read(self.file_size//10)
            self.file_size-= self.file_size//10
            self.task_progress+=10
        else : 
            content = self.fobj.read(self.file_size)
            self.task_progress=100
        content = encrypt(content,self.key)
        self.out.write(content)
        self.reset()
        self.display()
        

    def display(self):
        print("Task accomplished : %s percent"%(self.task_progress))
        print("Time taken : %s"%(self.time_spent))

    def start(self, file_name=None):
        if self.task_name == "encrypt" : return self.encrypt()
        elif self.task_name == "decrypt": return self.decrypt()


    def decrypt(self):
        self.st = time.time()
        content = ""
        if self.task_progress == 100:
            print("Decryption is Complete!!")
            self.fobj.close()
            return True
        elif self.file_size > 10 : 
            content = self.fobj.read(self.file_size//10)
            self.file_size-= self.file_size//10
            self.task_progress+=10
        else : 
            content = self.fobj.read(self.file_size)
            self.task_progress=100
        content = decrypt(content,self.key)
        self.out.write(content)
        self.reset()
        self.display()

if __name__ == "__main__":
    print("-----Enc-Dnc Test----")
    task1 = Task_Breaker(sys.argv[1],sys.argv[-2],sys.argv[-1],sys.argv[2])
    while task1.start() is None:
        pass