########################################################################
##
## CS 101
## Program #5
## Name: Colby Chandler
## Email: crcn96@mail.umkc.edu
##
## PROBLEM : getting word commonailty and word relitivty.
##
## ALGORITHM : 
##      1. 
##      2. 
##      3. 
##      4. 
##      5. 
## 
## 
##
## 
########################################################################
import string
import math

## reads though a file an turns it into a list.
def file_to_list(file):
    puntlist = string.punctuation
    filestring = ''
    file1 = open(file)
    for line in file1:
        filestring += line.lower()
    file1.close()
    
    for char in filestring:
        
        if char in puntlist:
            filestring = filestring.replace(char,'')
            
    filelist = filestring.split()
    return filelist

##turns a dicitnary keys into a list.
def key_to_list(dic):
    key_list = []
    for key in dic:
        key_list.insert(0,key)
    return key_list

## turns a list into a dictinary and adds how many times a word apperse.
def list_to_dict(lists):
    dicta = {}
    for char in lists:
        if char not in dicta:
            dicta[char] = 0
        if char in dicta:
            dicta[char] += 1
    return dicta

## removes stop words from a dictinary.
def word_removal(dictr,file):
    x = 0
    dic = dictr
    key_list = key_to_list(dictr)
    stop_words = file_to_list(file)
    while x < len(key_list):
        
            try:
                key = key_list[x]
                if key in stop_words:
                    
                    dic.pop(key)
                    x -=1
                x +=1
            except IndexError:
                continue
            except KeyError:
                x += 1
                continue
    return dic

## counts the number of common words between two dictinaries
def count_common(dic1,dic2):
    cnt = 0
    
    for key in dic1:
        if key in dic2:
            cnt += 1
    return cnt

## get a dictiary of a file with stop words removed
def file_get(file):
    file1 = word_removal((list_to_dict(file_to_list(file))),'stopWords.txt')        
    return file1

## get a total of all values in a dictniaries
def total_dic(dic):
    cnt = 0
    dic1 = dic
    for key in dic:
        cnt += (dic1[key])
    return cnt

## gets the relitivy between two files
def relitive_common(file,next_file):
    file1 = file_get(file)
    file2 = file_get(next_file)
    sqr_sums = 0
    
    common_words = {}
    total_dic1 = total_dic(file1)
    total_dic2 = total_dic(file2)
    
    for key in file1:
        if key in file2:
            common_words[key]= [file1[key]]
    for key in file2:
        if key in file1:
            common_words[key].append((file2[key]))
    
    for key in common_words:
        sqr_sums += ((int(common_words[key][0])/total_dic1)-(int(common_words[key][1])/total_dic2))**2
    if sqr_sums < 0 :
        sqr_sums = sqr_sums*-1
    total = math.sqrt((sqr_sums/len(common_words)))
    return '{:.4f}'.format(total)

## gets the word commonality between two files   
def word_common(file,next_file):
    file1 = file_get(file)
    file2 = file_get(next_file)
    common_words = count_common(file1,file2)
    common_value = len(file1) + len(file2) - common_words
    common_prt = (common_words / common_value)*100
    return '{:.2f}'.format(common_prt)

## varibles
default_files = ['mystery1','mystery2','mystery3','mystery4']
known_files = ['romney','obama','trump','clinton']
best_common = ''
best_relitive = ''
new_common = ''
new_relitive = ''
name_cit = ''
name_rit = ''
cnt = 0

## iterates over Mystery list
for item in default_files:
    print(item)
    ## get reid of veribles that might of stayed
    best_common = ''
    best_relitive = ''
    new_common = ''
    new_relitive = ''
    name_cit = ''
    name_rit = ''
    
    ## iterates over known file list
    for it in known_files:
        cnt += 1
        
        ## gets the itnitale values
        if cnt == 1 or cnt==5 or cnt == 9 or cnt == 13:
            best_common = float(word_common(item + '.txt',it + '.txt'))
            name_iit = item
            name_cit = it
            name_rit = it
            best_relitive = float(relitive_common(item + '.txt',it + '.txt'))

        ## gets values that to compare
        new_common = float(word_common(item + '.txt',it + '.txt'))
        new_relitive = float(relitive_common(item + '.txt',it + '.txt'))

        ## check if best values is the best
        if (new_common) >= (best_common):
            best_common = new_common
            name_cit = it
            name_iit = item
        
        if (new_relitive) < (best_relitive):
            
            best_relitive = new_relitive
            name_rit = it

        ## for print out to user
        if cnt == 4 or  cnt == 8 or cnt == 12 or cnt == 16:
            string_printout = '''The text {0} has the highest word commonality with {1} ({2}%).
The text {0} has the highest frequency similarity with {3} ({4}).'''
            print(string_printout.format(name_iit,name_cit,best_common,name_rit,best_relitive))
            print()
