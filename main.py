from enc_dnc_brute import Task
from RSA import create_keys
import sys
if __name__ == "__main__":
    if len(sys.argv) ==  1: 
        print("---- Use help option for more info -----")
        sys.exit(0)
    if sys.argv[1] == "generate_keys":
        create_keys()
        sys.exit(0)
    if sys.argv[1] == "help":
          print("---- Choose the type of operation (generate_keys/ encrypt/ decrypt) ----")
          print("---- generate_keys : no other argument is needed, It will create key files ----")
          print("---- encrypt/decrypt : Enter details as file_location , key_location, output_filename(optional),this creates an encrypted/decrypted file ----")
    type = sys.argv[1].lower()
    if type == "encrypt" or type == "decrypt":
        if len(sys.argv) < 4: 
            print("------ :) Okay, Enter Arguments as file_location , key_location, output_filename(optional) -----")
            sys.exit(0)
        task = Task(file_loc = sys.argv[2],task_name= type,key = sys.argv[3])
        print(type + "ing.....")
        method  = getattr(task,type)
        if len(sys.argv) < 5: method(type+"ed_message.txt")
        else: method(sys.argv[4])
        task.display()
        sys.exit(0)
    print("--- Use help option to understand usage ---")