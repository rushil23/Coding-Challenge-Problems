
count = 0
def permute(prev, word, length):
    if length == 1:
        global count 
        count +=1
        print prev + word
        # return
    else :
        for i in range(length):
            temp = word[i:length] + word[0:i]
            # print temp
            permute(prev+temp[0], temp[1:], length-1)

while True:
    word = raw_input("Word to permute: ")
    permute("", word, len(word))
    print count 
    count = 0
