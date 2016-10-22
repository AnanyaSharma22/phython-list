
def reverse(a,i):
	if(i>=0):
            print "a[" +i+"]"+ a[i]
            i=i-1
            reverse(a,i)
        else:
            return 
a=[1,2,3,4,5]
i=4
reverse(a,i)
