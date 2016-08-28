def akram():
 import os
 from datetime import datetime
 net=input("Enter ur Network Adreess :")
 net1=net.split('.')
 a='.'
 net2=net1[0] + a + net1[1] + a + net1[2] + a
 print(net)
 print(net2)
 st1=int(input("Enter the first Numbers : "))
 en1=int(input("Enter The Last Numbers : "))
 en1=en1+1
 t1=datetime.now()
 ping="ping -n 1"
 print("Scanning In Progress ...")

 for ip in range(st1+en1):
               addr=str(net2)+str(ip)
               comm=ping+addr
               response=os.popen(comm)

               for line in response.readlines():
                if(line.count("TTL")):
                  print(addr,"---->LIVE")

 t2=datetime.now()
 total=t2-t1
 print("Scaninng Complete in",total)
 print(" ")
 print("--------------->Any Problems U Should Disable The firewall<------------------")
 akram()
