def add1(a,b):
    return (a[0]+b[0],a[1]+b[1])     # Addition of two elements of ring of integers in the quadratic field

def sub1(a,b):
    return(a[0]-b[0],a[1]-b[1])      # Subraction of two elements of ring of integers in the quadratic field

def mul1(a,b):
    real= (a[0]*b[0]) + ((d)*(a[1]*b[1]))      # Product of two elements of ring of integers in the quadratic field when d = -1,-2
    imag= (a[0]*b[1]) + (a[1]*b[0])
    return (real,imag)

def norm1(a):
    return (a[0]**2) + ((-d)*(a[1]**2))         # Norm of an Element in ring of integers in the quadratic field when d = -1,-2

def div1(a,b):
    den=norm1(b)
    if den==0:
        return ZeroDivisionError("Cannot Divide by zero")         # Quotient of two elements of ring of integers in the quadratic field after Division when d = -1,-2
   
    real = ((a[0]*b[0]) + ((-d)*(a[1]*b[1])))/den                # Real and Imaginary Part of Quotient
    imag = ((a[1]*b[0]) - (a[0]*b[1]))/den

    r_real = int(round(real))                               # Rounding off the real and imaginary parts of Quotient
    r_imag = int(round(imag))

    return (r_real,r_imag)

def mod1(a,b):                      # Reminder of two elements of ring of integers in the quadratic field after division when d = -1,-2
    quo = div1(a,b)                
    prod = mul1(quo,b)              
    c = sub1(a,prod)
    return c
def gcd_Z1 (a,b) :                    # G.C.D and Co-efficients of a and b when expressing G.C.D as linear combination of a and b when d = -1,-2
    if b == (0,0) :
        return a,(1,0),(0,0)        
   
    gcd,x1,y1 = gcd_Z1(b,mod1(a,b))    # Recurrence relations for calculating G.C.D

    q = div1(a,b)
    x = y1                               # Recurrence relations for equation for calculating Co-efficients when d = -1,-2
    y = sub1(x1,mul1(q,y1))

    return gcd,x,y

def mul2(a,b):                          
    real = a[0] * b[0] + d1 * a[1] * b[1]               # Product of two elements of ring of integers in the quadratic field when d = -3,-7,-11        
    imag = a[0] * b[1] + a[1] * b[0] + a[1] * b[1]
    return (real,imag)

def norm2(a):
    return (a[0]**2) + a[0] * a[1] + (-d1) * a[1]**2         # Norm of an Element in ring of integers in the quadratic field when d = -3,-7,-11


def div2(a,b):
    den = norm2(b)
    if den==0:
        raise ZeroDivisionError("Cannot Divide by zero")               # Quotient of two elements of ring of integers in the quadratic field after Division when d = -3,-7,-11
   
    real1 = (a[0] * b[0] + a[0] * b[1] + (-d1) * a[1] * b[1]) / den      # Real and Imaginary Part of Quotient    
    imag1= (-a[0] * b[1] + a[1] * b[0]) / den
    rounded_real = int(round(real1))
    rounded_imag = int(round(imag1))

    return (rounded_real, rounded_imag)
def mod2(a,b):          
    q = div2(a,b)                              # Reminder of two elements of ring of integers in the quadratic field after division when d = -3,-7,-11
    p = mul2(q,b)
    c = sub1(a,p)
    return c

def gcd_Z2(a,b):
    if b==(0,0):
        return a,(1,0),(0,0)                   # G.C.D and Co-efficients of a and b when expressing G.C.D as linear combination of a and b when d = -3,-7,-11
   
    gcd,x1, y1 = gcd_Z2(b,mod2(a,b))          # Recurrence relations for calculating G.C.D when d = -3,-7,-11

    q=div2(a,b)
    x=y1
    y=sub1(x1,mul2(q,y1))                    # Recurrence relations for calculating Co-efficients of a and b when d = -3,-7,-11

    return gcd, x, y


d = int(input("Value of D (put any negative integer) = "))      # Defining the input to the user
d1 = int((d-1)/4)
                        # Making two cases when d = -1,-2 and -3,-7,-11
if d == -1 or d == -2:                  
    print("Check")
    a1 = int(input("Enter the value for a1: "))  # Taking inputs for real and imaginary parts of a
    a2 = int(input("Enter the value for a2: "))              

        #Similary Enter the next element of the ring as b = b1+b2*w, where w depends on the value of d
    b1 = int(input("Enter the value for b1: "))
    b2 = int(input("Enter the value for b2: "))

    a = (a1, a2)
    b = (b1, b2)
    gcd, x, y = gcd_Z1(a, b)

    print(f"a = {a}")                 # Printing the outputs
    print(f"b = {b}")
    print(f"gcd(a, b) = {gcd}")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Check: a*x + b*y = {add1(mul1(a, x), mul1(b, y))}")    # Checking the coefficients of a and b
       
elif d == -3 or d==-7 or d==-11:
    a1 = int(input("Enter the value for a1: "))  # Taking inputs for real and imaginary parts of a
    a2 = int(input("Enter the value for a2: "))

        #Similary Enter the next element of the ring as b = b1+b2*w, where w depends on the value of d
    b1 = int(input("Enter the value for b1: "))
    b2 = int(input("Enter the value for b2: "))

    a = (a1, a2)
    b = (b1, b2)
    gcd, x, y = gcd_Z2(a, b)

    print(f"a = {a}")            # Printing the outputs
    print(f"b = {b}")
    print(f"gcd(a, b) = {gcd}")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Check: a*x + b*y = {add1(mul2(a, x), mul2(b, y))}")       #  Checking the coefficients of a and b
       

else:
    print("THIS IS AN INVALID INPUT(For this value of D, the ring will not be a Euclidean Domain)")
    print("From theory we know only valid input are -1,-2,-3,-7,-11") 