
'''
MANOHAR SAI JASTI   
Z1833049


'''

#importing the modules
import string 
import pickle
from operator import itemgetter
import sys


#generating the every confusion matrix to dicts
del_table = [['a',0,7,58,21,3,5,18,8,61,0,4,43,5,53,0,9,0,98,28,53,62,1,0,0,2,0],
['b',2,2,1,0,22,0,0,0,183,0,0,26,0,0,2,0,0,6,17,0,6,1,0,0,0,0],
['c',37,0,70,0,63,0,0,24,320,0,9,17,0,0,33,0,0,46,6,54,17,0,0,0,1,0],
['d',12,0,7,25,45,0,10,0,62,1,1,8,4,3,3,0,0,11,1,0,3,2,0,0,6,0],
['e',80,1,50,74,89,3,1,1,6,0,0,32,9,76,19,9,1,237,223,34,8,2,1,7,1,0],
['f',4,0,0,0,13,46,0,0,79,0,0,12,0,0,4,0,0,11,0,8,1,0,0,0,1,0],
['g',25,0,0,2,83,1,37,25,39,0,0,3,0,29,4,0,0,52,7,1,22,0,0,0,1,0],
['h',15,12,1,3,20,0,0,25,24,0,0,7,1,9,22,0,0,15,1,26,0,0,1,0,1,0],
['i',26,1,60,26,23,1,9,0,1,0,0,38,14,82,41,7,0,16,71,64,1,1,0,0,1,7],
['j',0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0],
['k',4,0,0,1,15,1,8,1,5,0,1,3,0,17,0,0,0,1,5,0,0,0,1,0,0,0],
['l',24,0,1,6,48,0,0,0,217,0,0,211,2,0,29,0,0,2,12,7,3,2,0,0,11,0],
['m',15,10,0,0,33,0,0,1,42,0,0,0,180,7,7,31,0,0,9,0,4,0,0,0,0,0],
['n',21,0,42,71,68,1,160,0,191,0,0,0,17,144,21,0,0,0,127,87,43,1,1,0,2,0],
['o',11,4,3,6,8,0,5,0,4,1,0,13,9,70,26,20,0,98,20,13,47,2,5,0,1,0],
['p',25,0,0,0,22,0,0,12,15,0,0,28,1,0,30,93,0,58,1,18,2,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,0,0],
['r',63,4,12,19,188,0,11,5,132,0,3,33,7,157,21,2,0,277,103,68,0,10,1,0,27,0],
['s',16,0,27,0,74,1,0,18,231,0,0,2,1,0,30,30,0,4,265,124,21,0,0,0,1,0],
['t',24,1,2,0,76,1,7,49,427,0,0,31,3,3,11,1,0,203,5,137,14,0,4,0,2,0],
['u',26,6,9,10,15,0,1,0,28,0,0,39,2,111,1,0,0,129,31,66,0,0,0,0,1,0],
['v',9,0,0,0,58,0,0,0,31,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,1,0],
['w',40,0,0,1,11,1,0,11,15,0,0,1,0,2,2,0,0,2,24,0,0,0,0,0,0,0],
['x',1,0,17,0,3,0,0,1,0,0,0,0,0,0,0,6,0,0,0,5,0,0,0,0,1,0],
['y',2,1,34,0,2,0,1,0,1,0,0,1,2,1,1,1,0,0,17,1,0,0,1,0,0,0],
['z',1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
['@',20,14,41,31,20,20,7,6,20,3,6,22,16,5,5,17,0,28,26,6,2,1,24,0,0,2]]


d= {d[0]: d[1:] for d in del_table}
alpha = list(string.ascii_lowercase)



deleted = {}

for k in d:
  for  counter, value in enumerate(d[k]):
    newk = k + alpha[counter]
    deleted[newk] = value













# add[X Y] = Insertion of Y after X
# outer subscript = X
# inner subscript = Y (Inserted Letter)


add_table = [['a',15,1,14,7,10,0,1,1,33,1,4,31,2,39,12,4,3,28,134,7,28,0,1,1,4,1],
['b',3,11,0,0,7,0,1,0,50,0,0,15,0,1,1,0,0,5,16,0,0,3,0,0,0,0],
['c',19,0,54,1,13,0,0,18,50,0,3,1,1,1,7,1,0,7,25,7,8,4,0,1,0,0],
['d',18,0,3,17,14,2,0,0,9,0,0,6,1,9,13,0,0,6,119,0,0,0,0,0,5,0],
['e',39,2,8,76,147,2,0,1,4,0,3,4,6,27,5,1,0,83,417,6,4,1,10,2,8,0],
['f',1,0,0,0,2,27,1,0,12,0,0,10,0,0,0,0,0,5,23,0,1,0,0,0,1,0],
['g',8,0,0,0,5,1,5,12,8,0,0,2,0,1,1,0,1,5,69,2,3,0,1,0,0,0],
['h',4,1,0,1,24,0,10,18,17,2,0,1,0,1,4,0,0,16,24,22,1,0,5,0,3,0],
['i',10,3,13,13,25,0,1,1,69,2,1,17,11,33,27,1,0,9,30,29,11,0,0,1,0,1],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['k',2,4,0,1,9,0,0,1,1,0,1,1,0,0,2,1,0,0,95,0,1,0,0,0,4,0],
['l',3,1,0,1,38,0,0,0,79,0,2,128,1,0,7,0,0,0,97,7,3,1,0,0,2,0],
['m',11,1,1,0,17,0,0,1,6,0,1,0,102,44,7,2,0,0,47,1,2,0,1,0,0,0],
['n',15,5,7,13,52,4,17,0,34,0,1,1,26,99,12,0,0,2,156,53,1,1,0,0,1,0],
['o',14,1,1,3,7,2,1,0,28,1,0,6,3,13,64,30,0,16,59,4,19,1,0,0,1,1],
['p',23,0,1,1,10,0,0,20,3,0,0,2,0,0,26,70,0,29,52,9,1,1,1,0,0,0],
['q',0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['r',15,2,1,0,89,1,1,2,64,0,0,5,9,7,10,0,0,132,273,29,7,0,1,0,10,0],
['s',13,1,7,20,41,0,1,50,101,0,2,2,10,7,3,1,0,1,205,49,7,0,1,0,7,0],
['t',39,0,0,3,65,1,10,24,59,1,0,6,3,1,23,1,0,54,264,183,11,0,5,0,6,0],
['u',15,0,3,0,9,0,0,1,24,1,1,3,3,9,1,3,0,49,19,27,26,0,0,2,3,0],
['v',0,2,0,0,36,0,0,0,10,0,0,1,0,1,0,1,0,0,0,0,1,5,1,0,0,0],
['w',0,0,0,1,10,0,0,1,1,0,1,1,0,2,0,0,1,1,8,0,2,0,4,0,0,0],
['x',0,0,18,0,1,0,0,6,1,0,0,0,1,0,3,0,0,0,2,0,0,0,0,1,0,0],
['y',5,1,2,0,3,0,0,0,2,0,0,1,1,6,0,0,0,1,33,1,13,0,1,0,2,0],
['z',2,0,0,0,5,1,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4],
['@',46,8,9,8,26,11,14,3,5,1,17,5,6,2,2,10,0,6,23,2,11,1,2,1,1,2]]


added= {}
a= {a[0]: a[1:] for a in add_table}


for k in a:
  for  counter, value in enumerate(a[k]):
    newk = k + alpha[counter]
    added[newk] = value



# sub[X Y] = Substitution of X (incorrect) for Y (correct)
# outer subscript = X
# inner subscript = Y (correct)



sub_table = [['a',0,0,7,1,342,0,0,2,118,0,1,0,0,3,76,0,0,1,35,9,9,0,1,0,5,0],
['b',0,0,9,9,2,2,3,1,0,0,0,5,11,5,0,10,0,0,2,1,0,0,8,0,0,0],
['c',6,5,0,16,0,9,5,0,0,0,1,0,7,9,1,10,2,5,39,40,1,3,7,1,1,0],
['d',1,10,13,0,12,0,5,5,0,0,2,3,7,3,0,1,0,43,30,22,0,0,4,0,2,0],
['e',388,0,3,11,0,2,2,0,89,0,0,3,0,5,93,0,0,14,12,6,15,0,1,0,18,0],
['f',0,15,0,3,1,0,5,2,0,0,0,3,4,1,0,0,0,6,4,12,0,0,2,0,0,0],
['g',4,1,11,11,9,2,0,0,0,1,1,3,0,0,2,1,3,5,13,21,0,0,1,0,3,0],
['h',1,8,0,3,0,0,0,0,0,0,2,0,12,14,2,3,0,3,1,11,0,0,2,0,0,0],
['i',103,0,0,0,146,0,1,0,0,0,0,6,0,0,49,0,0,0,2,1,47,0,2,1,15,0],
['j',0,1,1,9,0,0,1,0,0,0,0,2,1,0,0,0,0,0,5,0,0,0,0,0,0,0],
['k',1,2,8,4,1,1,2,5,0,0,0,0,5,0,2,0,0,0,6,0,0,0,.4,0,0,3],
['l',2,10,1,4,0,4,5,6,13,0,1,0,0,14,2,5,0,11,10,2,0,0,0,0,0,0],
['m',1,3,7,8,0,2,0,6,0,0,4,4,0,180,0,6,0,0,9,15,13,3,2,2,3,0],
['n',2,7,6,5,3,0,1,19,1,0,4,35,78,0,0,7,0,28,5,7,0,0,1,2,0,2],
['o',91,1,1,3,116,0,0,0,25,0,2,0,0,0,0,14,0,2,4,14,39,0,0,0,18,0],
['p',0,11,1,2,0,6,5,0,2,9,0,2,7,6,15,0,0,1,3,6,0,4,1,0,0,0],
['q',0,0,1,0,0,0,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',0,14,0,30,12,2,2,8,2,0,5,8,4,20,1,14,0,0,12,22,4,0,0,1,0,0],
['s',11,8,27,33,35,4,0,1,0,1,0,27,0,6,1,7,0,14,0,15,0,0,5,3,20,1],
['t',3,4,9,42,7,5,19,5,0,1,0,14,9,5,5,6,0,11,37,0,0,2,19,0,7,6],
['u',20,0,0,0,44,0,0,0,64,0,0,0,0,2,43,0,0,4,0,0,0,0,2,0,8,0],
['v',0,0,7,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,8,3,0,0,0,0,0,0],
['w',2,2,1,0,1,0,0,2,0,0,1,0,0,0,0,7,0,6,3,3,1,0,0,0,0,0],
['x',0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0],
['y',0,0,2,0,15,0,1,7,15,0,0,0,2,0,6,1,0,7,36,8,5,0,0,1,0,0],
['z',0,0,0,7,0,0,0,0,0,0,0,7,5,0,0,0,0,2,21,3,0,0,0,0,3,0]]


subs = {}

s= {a[0]: a[1:] for a in sub_table}


for k in s:
  for  counter, value in enumerate(s[k]):
    newk = k + alpha[counter]
    subs[newk] = value





# transpose[X  Y] = Reversal of XY
# outer subscript = X
# inner subscript = Y


transpose_table =[['a',0,0,2,1,1,0,0,0,19,0,1,14,4,25,10,3,0,27,3,5,31,0,0,0,0,0],
['b',0,0,0,0,2,0,0,0,0,0,0,1,1,0,2,0,0,0,2,0,0,0,0,0,0,0],
['c',0,0,0,0,1,0,0,1,85,0,0,15,0,0,13,0,0,0,3,0,7,0,0,0,0,0],
['d',0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0],
['e',1,0,4,5,0,0,0,0,60,0,0,21,6,16,11,2,0,29,5,0,85,0,0,0,2,0],
['f',0,0,0,0,0,0,0,0,12,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['g',4,0,0,0,2,0,0,0,0,0,0,1,0,15,0,0,0,3,0,0,3,0,0,0,0,0],
['h',12,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0],
['i',15,8,31,3,66,1,3,0,0,0,0,9,0,5,11,0,1,13,42,35,0,6,0,0,0,3],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['k',0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['l',11,0,0,12,20,0,1,0,4,0,0,0,0,0,1,3,0,0,1,1,3,9,0,0,7,0],
['m',9,0,0,0,20,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,0,0,0,0,0],
['n',15,0,6,2,12,0,8,0,1,0,0,0,3,0,0,0,0,0,6,4,0,0,0,0,0,0],
['o',5,0,2,0,4,0,0,0,5,0,0,1,0,5,0,1,0,11,1,1,0,0,7,1,0,0],
['p',17,0,0,0,4,0,0,1,0,0,0,0,0,0,1,0,0,5,3,6,0,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',12,0,0,0,24,0,3,0,14,0,2,2,0,7,30,1,0,0,0,2,10,0,0,0,2,0],
['s',4,0,0,0,9,0,0,5,15,0,0,5,2,0,1,22,0,0,0,1,3,0,0,0,16,0],
['t',4,0,3,0,4,0,0,21,49,0,0,4,0,0,3,0,0,5,0,0,11,0,2,0,0,0],
['u',22,0,5,1,1,0,2,0,2,0,0,2,1,0,20,2,0,11,11,2,0,0,0,0,0,0],
['v',0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['w',0,0,0,0,0,0,0,4,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,8,0],
['x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
['y',0,1,2,0,0,0,1,0,0,0,0,3,0,0,0,2,0,1,10,0,0,0,0,0,0,0],
['z',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

trans={}


t= {a[0]: a[1:] for a in transpose_table}

for k in t:
  for  counter, value in enumerate(t[k]):
    newk = k + alpha[counter]
    trans[newk] = value




pickle_in = open("mydata.dat","rb")
vocab_list_dicts = pickle.load(pickle_in)



N = vocab_list_dicts[3]


words_vocab = vocab_list_dicts[2]


bigrams = vocab_list_dicts[1]

unigrams = vocab_list_dicts[0]


V= len(words_vocab)


#print("Words Vocabulary : ")
#print(words_vocab)

letters = list(string.ascii_lowercase)






#generating the added good strings
def added1(s):

    added_total = []
    for letter in letters:
        for i,c in enumerate(s):
            if i == len(s)-1:
                newstr = s + letter
            else :
                newstr = s[:i]+ letter + s[i:]
            for key in words_vocab.keys():
                if newstr==key:
                    prob = (words_vocab[key] + 0.5)/(N+(0.5*V))
                    prob= '{:.9f}'.format(prob)
                    prob = float(prob)
                    c= newstr[2]
                    e='-'
                    if i ==0:
                        prob_d = deleted['@'+c]/bigrams['<'+c]
                        prob_d = '{:.9f}'.format(prob_d)
                        prob_d = float(prob_d)
                        xw = '@'+c+'|'+'<'+c
                    else :
                        
                        prob_d = deleted[newstr[i-1]+c]/bigrams[newstr[i-1]+c]
              
                        prob_d = '{:.9f}'.format(prob_d) 
                        prob_d = float(prob_d)
              #print(prob_d)
                        xw = s[i-1] + '|' + newstr[i-1]+c
              
                        total_prob =   (10 ** 9) *prob_d * prob
                        total_prob = round(total_prob, 6)
                        total_prob= '{0:.6f}'.format(total_prob)
              #total_prob = 10**9(total_prob)
                        prob= '{:.6f}'.format(prob)
                        #prob = round(prob,6)
                        prob_d = '{:.6f}'.format(prob_d)
                        #prob_d = round(prob_d,6)
          
                        added_t1 = [newstr,c,e,xw,prob_d,prob,total_prob]
          
                        added_total.append(added_t1)
          
                        
    return added_total
    
    




#generating the deleted good strings
    
def deleted1(s):
    
    
    deleted_total =[]
    for i,c in enumerate(s):
          newstr = s[:i] + s[i+1:]
          for key in words_vocab.keys():
              if newstr==key:
                  prob = (words_vocab[key] + 0.5)/(N+(0.5*V))
                  prob= '{:.9f}'.format(prob)
                  prob = float(prob)
                  c='-'
                  e=s[i]
                  if i ==0:
                      prob_d = added['@'+e]/unigrams['<']
                      prob_d = '{:.9f}'.format(prob_d)
                      prob_d = float(prob_d)
                      xw = '@'+e+'|'+'<'
                  else :
                      prob_d = added[s[i-1]+e]/unigrams[s[i-1]]
              
                      prob_d = '{:.9f}'.format(prob_d) 
                      prob_d = float(prob_d)
                      #print(prob_d)
                      xw = s[i-1]+e + '|' + s[i-1]
                      total_prob =   (10 ** 9) *prob_d * prob
                      total_prob = round(total_prob, 6)
                      total_prob= '{0:.6f}'.format(total_prob)
                      #total_prob = 10**9(total_prob)
                      prob= '{:.6f}'.format(prob)
                      #prob = round(prob,6)
                      
                      prob_d = '{:.6f}'.format(prob_d) 
                      #prob_d = round(prob_d,6)
          
                      deleted_t1 = [newstr,c,e,xw,prob_d,prob,total_prob]
          
                      deleted_total.append(deleted_t1)
          
    return deleted_total

        
    
    
    
    
    
    
    
    
    
    

#generating the sub strings

def substitute1(s):
    
    subs_total = [] 
    for letter in letters:
        for i,c in enumerate(s):
            if c== letter:
                continue
            newstr = s[:i]+letter + s[i+1:]
            for key in words_vocab.keys():
                if newstr == key:
                    prob = (words_vocab[key] + 0.5)/(N+(0.5*V))
                    prob= '{:.9f}'.format(prob)
                    prob = float(prob)
                    c= newstr[i]
                    e= s[i]
                    prob_d = subs[e+c]/unigrams[c]
                    xw = e + '|' + c
                    total_prob =   (10 ** 9) *prob_d * prob
                    total_prob = round(total_prob, 6)
                    total_prob= '{0:.6f}'.format(total_prob)
                    prob= '{:.6f}'.format(prob)
                    #prob = round(prob,6)
                    prob_d = '{:.6f}'.format(prob_d)
                    #prob_d = round(prob_d,6)
                    subs_t1 = [newstr,c,e,xw,prob_d,prob,total_prob]
                    subs_total.append(subs_t1)
    return subs_total
            


    
    
    
 #generating the transpose strings    
    
def transpose1(s):
   
    trans_total = [] 
    for i,c in enumerate(s):
        newstr  =  s[:i]+s[i+1:i+2]+s[i:i+1]+s[i+2:]
       
        for key in words_vocab.keys():
            if newstr == key:
                prob = (words_vocab[key] + 0.5)/(N+(0.5*V))
                prob= '{:.9f}'.format(prob)
                prob = float(prob)
        
                if i == len(newstr)-1:
                    continue
                c= newstr[i] + newstr[i+1]
                e = newstr[i+1]+ newstr[i]
                prob_d = trans[c]/bigrams[c]
                xw  = e + '|' + c
                total_prob =   (10 ** 9) *prob_d * prob
                total_prob = round(total_prob, 6)
                total_prob= '{0:.6f}'.format(total_prob)
                prob= '{:.6f}'.format(prob)
                
                #prob = round(prob,6)
                prob_d = '{:.6f}'.format(prob_d)
                #prob_d = round(prob_d,6)
                trans_t1 = [newstr,c,e,xw,prob_d,prob,total_prob]
                trans_total.append(trans_t1)
    return trans_total
                    
    



#suggesting the good words for the mistyped word

def suggested_words(s):
    trans_total = transpose1(s)
    subs_total = substitute1(s)
    added_total = added1(s)
    deleted_total = deleted1(s)
    total_list =[trans_total,subs_total,added_total,deleted_total] 
    nested_list = []
    for l in total_list:
        for l1 in l:
            nested_list.append(l1)
    sorted_list = sorted(nested_list, key=itemgetter(6),reverse=True)
    #print("Candidate","\t","c","\t","e","\t","x|w","\t","P(x|word)","\t","10^9*P(x|w)P(w)")
    headings = ["Candidate","c","e","x|w","P(x|word)","P(word)","10^9*P(x|w)P(w)"]
    '''
    for heading in headings:
        print(heading.ljust(10,' '),end="   ")'''
    print("\n")
    sorted_list.insert(0,headings)
    for l in sorted_list:
        for item in l:
            item = str(item)
            print(item.ljust(10, ' '), end = "  ")
        print("\n")






arguments = sys.argv[1:]

for word in arguments:
    suggested_words(word)
   
    

#sorted_list = suggested_words(s)





            

            
            



        






