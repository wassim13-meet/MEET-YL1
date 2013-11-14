def Check(x):
    for i in range(0,len(x)/2):
        if x[i]!= x[len(x)-i-1]:
            print "FALSE"
            return
    print "TRUE"

if __name__=="__main__":
    x=raw_input()
    Check(x) 
