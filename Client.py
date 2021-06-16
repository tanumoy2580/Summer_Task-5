#Client

import socket as s
import cv2
import pickle as p
import struct as st

soc = s.socket(s.AF_INET,s.SOCK_STREAM)
hn = s.gethostname()
ip=s.gethostbyname(hn)
port = 1122
soc.connect((ip,port))
print('\n\n\t\t\t[>>>   CLIENT SUCCESSFULLY ESTABLISHED CONNECTION WITH THE SERVER   <<<]\n\n')
data = b""
size = st.calcsize("Q")

try:
    while True:
        while len(data) < size:
            adata = soc.recv(4096) 
            if not adata: break
            data+=adata
        pmsize = data[:size]
        data = data[size:]
        msize = st.unpack("Q",pmsize)[0]

        while len(data) < msize:
            data += soc.recv(4096)
        fdata = data[:msize]
        data  = data[msize:]
        stream = p.loads(fdata)
        cv2.imshow("LIVE VIDEO STREAMING",stream)
        #101 is the ASCII value of 'e'
        if cv2.waitKey(1) == 101:
            cv2.destroyAllWindows()
            break
except:
    cv2.destroyAllWindows()
soc.close()