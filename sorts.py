#how to do custom sorts, including tiebreakers
lst = ["2","5","10","1"]
srt = sorted(lst)

#by key
def numeracize(ch):
        return int(ch)
        
srt = sorted(lst, key=numeracize)
srt

#by comparator
def numcomp(a,b):
    if int(a)==int(b):
        return 0
    elif int(a)>int(b):
        return 1
    elif int(a)<int(b):
        return -1
    else:
        raise Exception("bad input!")
        
srt = sorted(lst, cmp=numcomp)
srt


#make this into a list of tuples
#sorted by value, then by key
d = {
    3: "mouse",
    2: "rat",
    1: "mouse" 
}
# use a list comprehension to change to tuples
tuples = [(key, value) for key,value in d.items()]

#sort using a comparator with nested ifs
def comprodents(a,b):
    if a[1]>b[1]:
        return 1
    elif a[1]<b[1]:
        return -1
    elif a[1]==b[1]:
        if a[0]==b[0]:
            return 0
        elif a[0]>b[0]:
            return 1
        elif a[0]<b[0]:
            return -1
        
srt = sorted(tuples, comprodents)

#sort twice by different keys...tiebreaker first        
def bykey(a):
    return a[0]
    
def byval(a):
    return a[1]

    
srt = cusorted(tuples, key=bykey);
srt2 = sorted(srt, key=byval)
srt2


#sort by a key function that returns a tuple of "tiebreakers" in order
def mysort(a):
    return (a[1],a[0])
    
srt = sorted(tuples, key=mysort)
srt

# you basically just sorted it as if it were this list...
revd = sorted([(a[1],a[0]) for a in tuples])
revd

#...the above works because of how Python sorts tuples
mytups = [
    (1,0),
    (0,1),
    (-1,5),
    (1,-4)
]

srt = sorted(mytups)
srt