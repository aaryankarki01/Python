import cmath
a,b,c=map(int,input("enter the coeffficient of equation").split())
discriminant = b**2 - 4*a*c

root1=(-b-cmath.sqrt(discriminant))/2*a
root2=(-b+cmath.sqrt(discriminant))/2*a

if discriminant>0:
        print("Types of Roots: Two Distinct real roots")
elif discriminant==0:
    print("Types of Roots: Two Equal real roots")
elif discriminant<0:
    print("Types of Roots: Two Complex real roots")

print("Root1",root1,"Root2",root2);


