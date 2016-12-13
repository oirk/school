########################################################################
##
## CS 101
## Program #7
## Name: Colby Chandler
## Email: crcn96@mail.umkc.edu
##
## PROBLEM : getting a word and a range of years to compare word relitivity.
##
## ALGORITHM : 
##      1. get both the words that the user want to compare
##      2. get the years that they want the comparison to be between
##      3. print out to the comparisions
##      
##       
## 
## 
##
## 
########################################################################

## checks to see if the word gaven is in the csv file
def check_word(word):
    use_file = open('all_words.csv')
    words =  word
    switch = True
    while switch == True:
        use_file.seek(0)
        for line in use_file:
            frag = line.lower().strip().split(',')
            if frag[0] == words:
                switch = False
                use_file.close()
                return words
        if switch == True:
            print ('',words,'was not found in the file please enter a new word.')
            words = input ('what word do you want to look up?-->')
            continue
        
## make sure the year gaven is in the range of 1900 to 2008
def check_year(year,place):
    years = year
    switch = True
    while switch == True:
        try:
            if years == '' and place == 'start':
                years = 1900
            if years == '' and place == 'end':
                years = 2008
            while int(years) > 2008 or int(years) < 1505:
                print('please enter a number between 1505 and 2008')
                years = int(input('Please enter a number.'))
            return int(years)
        except ValueError:
                print('your year must be a interger.')
                continue


## meau to choose what to do.
def menu():
    switch = True
    while switch == True:
        program = (input('''        do you want to compare two word and view them in a ngram table
        press 1 for ngram table or Q to quit out of the program.

        1. ngram table
        Q. Quit
        -->'''))
        if program == '1' or program == 'Q':
            return program
        else:
            print()
            print('plesae enter 1 or Q')
        
import csv       
run = menu()
## main loop
while run == '1':
    total_dic = {}
    word_dic = {}
    check_list = []
    word_freq = {}
    ngram = '{}  {:.7f}   {:.7f}'
    word_list = [check_word(input ('what word do you want to look up?-->')),check_word(input ('what word do you want to compare to the frist word?-->'))]
    year_range = [check_year(input('what year do you want to start from?-->'),'start'),check_year(input('what year do you want to end in?-->'),'end')]
    usage_file = open('all_words.csv')
    total_file = open('total_counts.csv')

    ## makes a dicanary with the year as the key and the total words used that year under that key.   
    for line in total_file:
        frag = line.strip().split(',')
        if int(frag[0]) in range(year_range[0],year_range[1]+1):
                total_dic[int(frag[0])] = int(frag[1])
        
    total_file.close()
   ## make a dic with the key being the word and under that it make a dic that has the year as keys and they amount the word was use that year.
    for item in word_list:
        usage_file.seek(0)
        for line in usage_file:
            frag = line.strip().split(',')
            if frag[0] == item and  int(frag[1]) in range(year_range[0],year_range[1]+1):
                if item not in check_list:
                    check_list.append(item)
                    word_dic[item] = {}
                if item in check_list:
                    word_dic[item][int(frag[1])] = int(frag[2])
    usage_file.close()               
    cnt = 0
    ## creates a dict for word freq of the words
    for key in word_dic:
        word_freq[key] = []
        for x in range(year_range[0],year_range[1]+1):
            word_freq[key].append((word_dic[key][x])/(total_dic[x])*100)
            
    print()
    print('      {}   '.format('ngram view'))
    print()
    print('{}    {}     {}'.format('year',word_list[0],word_list[1]))
    print('{}'.format('_'*26))
    ## output
    for x in range(year_range[0],year_range[1]+1):
        print(ngram.format(x,float(word_freq[word_list[0]][cnt]),float(word_freq[word_list[1]][cnt])))
        cnt += 1
    print()
    run = menu()
    print()
if run == 'Q':
    print ('GoodBye')
