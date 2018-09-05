if __name__=="__main__":
    import sys

    if (len(sys.argv)!=3):
        print ("Check commandline arguments")
        sys.exit(1)



    def func(fname):
        lines=0
        characters=0
        vowelcount=0
        conscount=0
        vowels='aeiou\u00e9\u00e2\u00ea\u00ee\u00f4\u00fb\u00e0\u00e8\u00f9\u00eb\u00ef\u00fc\u0153'
        consonants='bcdfghjklmnpqrstvwxyz'
        #open the file as f and encoding it to utf-8
        with open(fname, encoding='utf-8') as f:

            for i,line in enumerate(f):
                lines+=1
                characters+=len(line)
                #string function to convert each line to lower case
                low=line.lower()
                for letter in low:
                    if letter in vowels:
                        vowelcount+=1
                    if letter in consonants:
                        conscount+=1

            letters=vowelcount+conscount
            vpercentage=(vowelcount/letters)*100
            vpercentage=round(vpercentage,2)
            #print the required output
            print("Number of lines      = ",lines)
            print("Number of characters = ",characters)
            print("Number of vowels     = ",vowelcount)
            print("Number of consonants = ",conscount)
            print("Number of letters    = ",letters)
            print("% vowels             = ",vpercentage,"%")
            return conscount,vowelcount


    print("Book: ",str(sys.argv[1]))
    x=func(sys.argv[1])
    print("\nBook: ",str(sys.argv[2]))
    y=func(sys.argv[2])

    print("\nActual:")
    print("Book        consonants    vowels")
    print(str(sys.argv[1]),"   ",x[0],"    ",x[1])
    print(str(sys.argv[2]),"   ",y[0],"    ",y[1])

    fr=x[0]+x[1]
    sr=y[0]+y[1]
    fc=x[0]+y[0]
    sc=x[1]+y[1]
    #row total is first row and second row sum
    totalrow=fr+sr
    #column total is first and second column sum
    totalcolumn=fc+sc
    if(totalrow==totalcolumn):
        total=totalrow
        pridecons=(fc*fr/total)
        pridevowel=(sc*fr/total)
        swanncons=(fc*sr/total)
        swannvowel=(sc*sr/total)
print("\nExpected:")
print("Book          consonants     vowels")
print(str(sys.argv[1]),"   ",round(pridecons,2),"   ",round(pridevowel,2))
print(str(sys.argv[2]),"   ",round(swanncons,2),"   ",round(swannvowel,2))

first=((x[0]-pridecons)**2)/pridecons
second=((x[1]-pridevowel)**2)/pridevowel
third=((y[0]-swanncons)**2)/swanncons
fourth=((y[1]-swannvowel)**2)/swannvowel
chisquare=first+second+third+fourth
print("\nchisquare = ",round(chisquare,2))
