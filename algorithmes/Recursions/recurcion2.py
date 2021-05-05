# recurtion function2
# countdown 


def cd(x):
    
    if x == 0:                  #base  case
        print ('start')
        
    else:                       # recorcion case
        print (x, end = "..........")
        cd(x-1)
#test
print (cd(5))