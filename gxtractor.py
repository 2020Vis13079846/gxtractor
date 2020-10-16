# Based on ShellcodeReports

import sys
import re

def help_usage():
    print("Usage: objdump -d <input_file> | gxtractor")

def main():
    if not sys.stdin.isatty():
        try:
            shellcode = ""
            lenght = 0
            while 1:
                item = sys.stdin.readline()
                if item:
                    if re.match("^[ ]*[0-9a-f]*:.*$",item):
                        item = item.split(":")[1].lstrip()
                        x = item.split("\t")
                        opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                        for i in opcode:
                            shellcode += "\\x" + i
                            lenght += 1
                else: 
                    break
                print(shellcode)
                print("Shellcode Lenght: " + str(lenght))
        except:
            help_usage()
    else:
        help_usage()
        
main()
