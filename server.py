import socket

s = socket.socket()

host = socket.gethostname()

port = 12323

s.bind((host, port))

s.listen(5)

while True:

    c, addr = s.accept()
    
    val = True
    
    unBit = ""
    
    while val:
        msg = c.recv(1024).decode()
        print(msg)
        
        #print(msg , " h")
        
        if(msg == "STOP"):
            val = False
            
        if val:
            stuffed = msg.split()
            
            '''print(stuffed)
            
            print(msg)
            
            print(val)'''
        
            stuffed.pop()
        
            stuffed.pop(0)
        
            print(stuffed)
        
            for i in stuffed:
                unBit += i
                unBit += " "
            
    print(unBit)
    
    c = 0
    
    byteStuff = ""
    
    pre = '0'
    
    for i in unBit:
        if i == " ":
            byteStuff += i
            continue
        if pre == '0':
            if i == '0':
                c = 0
            else:
                c += 1
            pre = i
            byteStuff += i
        else:
            if c == 5:
                c = 0
                if i == '0':
                    c = 0
                else:
                    c += 1
            else:
                if i == '0':
                    c = 0
                else:
                    c += 1
                pre = i
                byteStuff += i
                
    print(byteStuff)
    
    byte = byteStuff.split()
    
    abcd = []
    
    for i in byte:
        if i == "10100011":
            abcd.append("ESC")
        elif i == "01111110":
            abcd.append("FLAG")
        else:
            b = int(i , 2)
            alph = chr(b)
            abcd.append(alph)
    print(abcd)
        
    """rep = ""
        
    for i in msg:
            
        rep += "0"
            
        b = bin(ord(i))
            
        rep += b[2:]
        
        rep += " "
        
    c.send(rep.encode())"""

c.close()