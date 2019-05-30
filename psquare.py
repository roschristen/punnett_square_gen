
def simple_table():
        #Title
    print("\nSimple Punnett Square Generator:\nPlease enter parent genotypes below, put a space between each letter\ne.g. H h\n\n")

    #Input functions
    x, y = input("Parent 1 Genotype: ").split()
    z,q = input("Parent 2 Genotype: ").split()
    
    #Margin calculation

    if len(z) > len(q) :
        marginL = len(z)
        qmarginl = len(z)-len(q)
        zmarginl = 0

    else :
        marginL = len(q)
        zmarginl = len(q)-len(z)
        qmarginl = 0

    m = 0
    margin = ""
    while m < marginL:
        margin = margin + " "
        m+= 1

    m1 = 0
    zmargin = ""
    qmargin = ""
    while m1 < zmarginl: 
        zmargin = zmargin + " "
        m1+=1
    m2 = 0
    while m2 < qmarginl:
        qmargin = qmargin + " "
        m2+= 1

    #var declaration
    val1 = x+z
    val2 = y+z
    val3 = x+q
    val4 = y+q

    #length comparison
    varlst = [len(val1)+ len(val2), len(val3) + len(val4)]
    topval = max(varlst) 

    #gap write 
    gap = topval/4
    spaces = ""
    f = 0
    while f < gap:
        spaces = spaces + " "
        f+=1
    totspace = f*4


    # total line length comparison and write

    totalwidth = (zmarginl + len(z) + 3 + totspace + topval -1) *.8974
    totalwidth2 = (qmarginl + len(q) + 3 + totspace + topval - 1) *.8974

    if totalwidth< totalwidth2 :
        totalwidth = totalwidth2

    topline = ""
    s = 0
    while s < totalwidth:
        topline = topline + "-"
        s+=1



    #Inidividual box spacing adjustments
    if (len(val1)< len(val3)):
        diff1 = len(val3)-len(val1)
        e = 0
        while e< diff1:
            val1 = val1 + " "
            e+= 1
    if(len(val3)< len(val1)):
        diff2 = len(val1)- len(val3)
        e = 0
        while e< diff2:
            val3 = val3 + " "
            e+=1
    if(len(val2)< len(val4)):
        diff3 = len(val4)- len(val2)
        e1 = 0
        while e1< diff3:
            val2 = val2 + " "
            e1+=1
    if(len(val4)< len(val2)):
        diff4 = len(val2)- len(val4)
        e1 = 0
        while e1<diff4:
            val4= val4 + " "
            e1 += 1



    #table print
    print("\n" + margin + " " + spaces + x + spaces + spaces + " " + y)
    print(margin + topline)
    print(zmargin + z + "|" + spaces + val1 + spaces + "|" + spaces + val2 + spaces+ "|")
    print(margin + topline)
    print(qmargin + q + "|" + spaces+ val3 +spaces + "|"+ spaces+ val4 + spaces+ "|")
    print(margin + topline)


    #percentage reporting

    #split function definition
    def split(x):
        return list(x)

    varlst1 = [val1, val2, val3, val4]
    varlst2 = [split(val1), split(val2), split(val3), split(val4)]

    #compare function definition
    def compare(lst1, lst2):
        for i in lst1:
            if(i not in lst2 ):
                return False
            else:
                for i in lst2:
                    if(i not in lst1):
                        return False
        
        return True


    #ratio dictionary declaration
    perc = {'box1': 0, 'box2': 0, 'box3': 0, 'box4': 0}

    #main comparison function. This function compares the allele combinations to each other, while incrementally increasing starting values 
    #so values aren't compared to themselves or to each other multiple times. It then adds to the ratio dictionary values if two values are 
    #found to be equivalent
    b = 0
    startval = 1
    for i in varlst1:
        k = varlst2[b]
        for i in range(startval, len(varlst2)):
            j = varlst2[i]
            if len(j) == len(k):
                if (compare(j, k)== True):
                    if(b == 0):
                        perc['box1']+= 1
                        perc['box'+ str(i+1)] += 1
                    else:
                        perc['box'+ str(i+1)] += 1
                        perc['box' + str(b + 1)] += 1
            
        b+=1
        startval +=1

    #ratio list declaration- this takes the definition values of the ratio dictionary and writes them to a list so they can be evaluated.
    ratios = []
    for i in perc:
        ratios.append(perc[i])

    #Percentages print and evaluation: this section then checks to see what ratio is presented by the data, and prints the respective
    #percentages
    print("Percentages: ")
    if(ratios == [1, 0, 0, 1]):
        print(str(varlst1[0]) + ": "+ "50%")
        print(str(varlst1[1])+ ": " + "25%")
        print(str(varlst1[2])+ ": " + "25%")
    if (ratios == [0, 1, 1, 0]):
        print(str(varlst1[1]) + ": "+ "50%")
        print(str(varlst1[0])+ ": " + "25%")
        print(str(varlst1[3])+ ": " + "25%")
    if(ratios == [1, 1, 1, 1]):
        if(varlst1[0] != varlst1[3]):
            print(str(varlst1[0]) + ": "+ "50%")
            print(str(varlst1[3]) + ": "+ "50%")
        else:
            print(str(varlst1[0]) + ": "+ "50%")
            print(str(varlst1[1]) + ": "+ "50%")

    if(ratios == [3, 3, 3, 3]):
        print(str(varlst1[0]) + ": "+ "100%")
    if(ratios == [0, 0, 0, 0]):
        print(str(varlst1[0]) + ": "+ "25%")
        print(str(varlst1[1])+ ": " + "25%")
        print(str(varlst1[2])+ ": " + "25%")
        print(str(varlst1[3])+ ": " + "25%")

def complex_table():
    print("\nTwo-gene Punnett Square Generator:\nPlease enter parent genotypes below, put a space between each letter\ne.g. H h J j\n\n")

    #Input functions
    x, y, x1, y1 = input("Parent 1 Genotype: ").split()
    z,q, z1, q1 = input("Parent 2 Genotype: ").split()
     
    #Basic table formula
    print("\n      " + x +x1 + "       "+ x+ y1 + "       "+ y + x1+ "       "+ y+y1)
    print("  -------------------------------------")
    print(z+z1 + "|"+"  "+ x+z+x1+z1+ "  "+"|"+"  "+x+z+y1+z1 + "  "+ "|"+ "  " + y+z+x1+z1 + "  " + "|" + "  "+ y+z+y1+z1 + "  " + "|")
    print("  -------------------------------------")
    print(z+ q1 + "|"+ "  "+ x+z+x1+q1 + "  "+ "|"+ "  "+x+z+y1+q1+ "  "+ "|"+ "  "+ y+z+x1+q1+ "  "+ "|"+ "  "+ y+z+y1+q1+ "  "+ "|")
    print("  -------------------------------------")
    print(q+z1 + "|"+ "  "+ x+q+x1+z1 + "  "+ "|"+ "  "+x+q+y1+z1+ "  "+ "|"+ "  "+y+q+x1+z1+ "  "+ "|"+ "  "+ y+q+y1+z1+ "  "+ "|")
    print("  -------------------------------------")
    print(q+q1 + "|"+ "  "+ x+q+x1+q1 + "  "+ "|"+ "  "+x+q+y1+q1+ "  "+ "|"+ "  "+ y+q+x1+q1+ "  "+ "|"+ "  "+ y+q+y1+q1+ "  "+ "|")
    print("  -------------------------------------")

 #Title
print("\nPunnett Square Generator:\nTo select a simple punnett square, please type '1' below.\nTo select a two-gene punnett square, please type'2' below.")
select = input("Selection: ")
if select == '1':
    simple_table()
elif select == '2':
    complex_table()



            






        
