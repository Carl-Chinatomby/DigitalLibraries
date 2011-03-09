"""
"""

class BinaryImageProc():
    """
    """
    def __init__(self):
        """
        """
        pass
    
    def read_img(self, filename):
        """
        """
        try:
            data = open(filename, 'rb').read()
        except IOError:
            print filename + "Not Found!"
            raise SystemExit
        
        hexlist = []
        for ch in data:
            byte = "%02X" % ord(ch)
            hexlist.append(byte)
        
        k=0
        for byte in hexlist:
            if k % 8 == 0:
                print " ",
            if k% 16 == 0:
                print
            print byte,
            k += 1
        
        print
        print "-"*50
        
        for k in range(len(hexlist)-1):
            if hexlist[k] == 'FF' and hexlist[k+1]=='C4':
                print "end of header at index %d (%s)" % (k, hex(k))
                break
        
        for k in range (len(hexlist)-1):
            if hexlist[k] == 'FF' and (hexlist[k+1] == 'C0' or hexlist[k+1] == 'C2'):
                height = int(hexlist[k+5],16)*256 + int(hexlist[k+6],16)
                width  = int(hexlist[k+7],16)*256 + int(hexlist[k+8],16)
                print "width = %d height = %d pixels" % (width, height)
                
        comment = ""
        for k in range(len(hexlist)-1):
            if hexlist[k] == 'FF' and hexlist[k+1] == 'FE':
                length = int(hexlist[k+2],16)*256 + int(hexlist[k+3],16)
                for m in range(length-3):
                    comment = comment + chr(int(hexlist[k+m+4],16))
        
        if len(comment) > 0:
            print commment
        else:
            print "No Comments Found"
            
        return hexlist
    

if __name__=="__main__":
    proc = BinaryImageProc()
    proc.read_img("cowboy_sil.jpeg")