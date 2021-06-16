#Server

import socket as s
import cv2
import pickle as p
import struct as st

soc = s.socket(s.AF_INET,s.SOCK_STREAM)
hn  = s.gethostname()
ip=s.gethostbyname(hn)
port = 1122
soc.bind((ip,port))
print('\n\n\t\t\t\t[>>>   SERVER READY FOR CLIENT CONNECTION   <<<]\n\n')
soc.listen(5)
c,aip = soc.accept()
cap = cv2.VideoCapture(0)
try:
    while True:
        ret,stream = cap.read()
        a = p.dumps(stream)
        size = st.pack("Q",len(a))+a
        c.sendall(size)

        cv2.imshow('TRANSFERING LIVE STREAM',stream)
        #101 is the ASCII value of 'e'
        if cv2.waitKey(1) == 101:
            cv2.destroyAllWindows()
            cap.release()
            break
except:
    cv2.destroyAllWindows()
c.close()
cap.release()