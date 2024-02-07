list = [1,1]
stop = int(input("How many numbers should I generate? "))
x=0
a=0
b=1
#made sure a and b are 0 and 1, so each time i can add 1 to them, and it will add the two numbers next in the sequence
c=2
#the first "added" number goes into the 3rd slot, so list[2]... the second "added" number goes into the 4th slot.Which is why later i made c*=2 as it goes up in 2s.
z = 3
#n corresponds to the number that is copied. The copied number always ends in an odd spot. (1 ends up in slot 3, 2 ends up in slot 5 e.t.c)
last = list[1]
while x != stop:
    add = list[a] + list[b]
    last=list[b]
    b+=1    
    a+=1
    list.insert(c,add)
    list.insert(z,last)
    c*=2
    x=x+1
    z=z+2
newlist = list[:stop]
print(f"The sequence is {newlist}")
# i had a problem here.. whenever i asked for it to generate for example 4 numbers, it would generate 10.
#so i made it stop at the value you input
a2=0
k=0
b2=1
g = 2
list_two = []
while k!=stop:
    m1 = newlist[a2]
    m2 = newlist[b2-2]
    m=f"{m1}/{m2}"
    list_two.insert(g,m)
    k+=1
    a2+=1
    b2+=1
    g+=1
print(f"The rational numbers are: {list_two}")