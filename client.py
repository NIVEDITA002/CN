import socket

s = socket.socket()

host = socket.gethostname()

port = 12323

s.connect((host, port))

val = True

while(val):

    message = input("Enter the message : ")
    
    words = message.split()
    
    res = []
    
    for i in words:
        if(i == 'ESC' or i == 'FLAG'):
            res.append("ESC")
            res.append(i)
        else:
            res.append(i)
    
    binForm = []
    for i in res:
        if(i == "ESC"):
            binForm.append("10100011")
        elif(i == "FLAG"):
            binForm.append("01111110")
        else:
            binForm.append(f'{ord(i):08b}')
    
    print(binForm)
    
    bina = ""
    
    for i in binForm:
        bina += i
        bina += " "
        
    pre = '0'
    
    c = 0
    
    bStuff = ""
    
    for i in bina:
        if i == " ":
            bStuff += i
            continue
        if pre == '0':
            if i == '0':
                c = 0
            else:
                c = 1
            pre = i
            bStuff += i
        else:
            if c == 5:
                c = 0
                bStuff += "0"
                if i == '0':
                    c = 0
                else:
                    c += 1
                pre = i
                bStuff += i
            else:
                if i == '0':
                    c = 0
                else:
                    c += 1
                pre = i
                bStuff += i
                
    print(bStuff)
    
    bitStuff = bStuff.split()
    print(bitStuff)
                
    l = len(bitStuff)
    
    j = 0
    
    answer = []
    while(j < l):
        a = ""
        a += "01111110 "
        a += bitStuff[j]
        a += " "
        j += 1
        if(j < l):
            a += bitStuff[j]
            j += 1
        a += " 01111110"
        s.send(a.encode())
        print(a + " is sent")
        
    val = False
    
    s.send("STOP".encode())
    
    """
    s.send(message.encode())
    
    ans = s.recv(1024).decode()

    print("Message from server : " , ans)
    
    ch = input("Do you want to continue : ")
    
    if(ch == 'N' or ch == 'n'):
        val = False"""
        
s.close()