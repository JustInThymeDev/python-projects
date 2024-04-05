#sentiment creation function
#creates dictionary of all words in file and their respective average sentiment score
def sentiment(inFile):

    #Defining constants and variables

    average = 0
    count = 0
    words_list=[]
    average_list=[]
    sentiment_Dicto = {}

    #Reads file and primes data for parsing

    fileData = open(inFile, 'r')
    TotalData = str.lower(fileData.read())
    reviewsData = TotalData.split('\n')

    #Generates dictionary of all instances of a word and its associated score

    for review in reviewsData:
        words = review.split(' ')
        for word in words:
            if word not in sentiment_Dicto:
                sentiment_Dicto[word] = [1, int(words[0])]
            else:
                sentiment_Dicto[word][0] += 1
                sentiment_Dicto[word][1] += int(words[0])

    #Generates list of all valid wars and averages of those words

    for word in sentiment_Dicto:
        if word in sentiment_Dicto:
            score = (sentiment_Dicto[word][1] / sentiment_Dicto[word][0])
            average += score
            score=round(score, 2)
            count += 1
            words_list.append(word)
            average_list.append(score)

    #Does final conversion of words_list and average_list to for averages_Dicto

    averages_Dicto = {}
    for key in words_list:
        for value in average_list:
            averages_Dicto[key] = value
            average_list.remove(value)
            break
    return(averages_Dicto)
#Function will print the average score of any word in the file, if word does not exist it reprompts the user until a valid word is entered
def get_score(averages_Dicto):
    word_to_search=input("What word are we looking for? ")
    if word_to_search in list(averages_Dicto.keys()):
        print(word_to_search + " has an average rating of " + str(averages_Dicto[word_to_search]))
        if ((averages_Dicto[word_to_search]) >= 2.01):
            print("This is a positive word.")
        elif ((averages_Dicto[word_to_search]) <= 1.99):
            print("This is a negative word.")
        else:
            print("This is a neautral word.")
        #Prompts user for sentiment analysis, rescoring a word based on users manual input, bypassing if sentiment is correct
        correctness=input("Is this sentiment analysis right? ")
        if (correctness == "no"):
            correct_score=input("What is the right score? ")
            correct_score=float(correct_score)
            del averages_Dicto[word_to_search]
            new_entry={word_to_search: correct_score}
            averages_Dicto.update(new_entry)
            print("Thank you for the input.")
        elif (correctness == "yes"):
            print("Thank you for your input.")
        else:
            return
    else:
        print("I dont recognize that word.")
        get_score(inFile)
#Prints the average score of all words in file
def get_total_average(averages_Dicto):
    averages_list=averages_Dicto.values()
    print("The total average of all words is " + str((round(sum(averages_list)/ len(averages_list))), 2))

# After asking instructor and TA no one told me what this function was suppose to do
# In lieu of this I made 2 interpritations of said function
# get_all will print every word attributed to the minimum and maximum occuring score
# get_last will print the last occurance of the minimum and maximum scoring word
#call get last with "3.5" in input, its a hidden function
def get_all_min_and_max(averages_Dicto):
    keys_list=list(averages_Dicto.keys())
    min_or_max_list=list(averages_Dicto.values())
    mini=min(min_or_max_list)
    maxi=max(min_or_max_list)
    for i in range(0, len(keys_list)):
        if (min_or_max_list[i] == mini):
            print(keys_list[i] + " is minimum.")
        if (min_or_max_list[i] == maxi):
            print(keys_list[i]  + " is maximum.")
#See above comment block, input "3.5" to call this function
def get_last_min_and_max(averages_Dicto):
    keys_list=list(averages_Dicto.keys())
    min_or_max_list=list(averages_Dicto.values())
    mini=min(min_or_max_list)
    maxi=max(min_or_max_list)
    for i in range(0, len(keys_list)):
        if (min_or_max_list[i] == mini):
            last_min=keys_list[i]
        if (min_or_max_list[i] == maxi):
            last_max=keys_list[i]
    print("The last lowest scoring word is " + last_min +" with a score of " + str(mini))
    print("The last highest scoring word is " + last_max +" with a score of " + str(maxi))
#Creates Positive and Negative files for high and low sentiment words
def positive_and_negative(averages_Dicto):
    positive=[]
    negative=[]
    words_list=list(averages_Dicto.keys())
    averages_list=list(averages_Dicto.values())
    for i in range(0, len(averages_Dicto)):
        if (averages_list[i]>2):
            positive.append(words_list[i])
        elif (averages_list[i]<2):
            negative.append(words_list[i])
    outFileI=open("positive.txt", 'w')
    for i in range(0, len(positive)):
        outFileI.write(positive[i])
        outFileI.write("\n")
    outFileI.close()
    outFileII=open("negative.txt", 'w')
    for i in range(0, len(negative)):
        outFileII.write(negative[i])
        outFileII.write("\n")
    outFileII.close()
#Prints user options
def print_intro():
    print("1. Get the score of a word")
    print("2: Get the average score of words in a file")
    print("3: Get the highest / lowest scoring words in a file")
    print("4: Sort the words in a file into positive.txt and negative.txt")
    print("5: Exit the program")
#Main function, prompts user input and calls respective functions
def main():
    user_input=''
    inFile=input("Learning data file name? ")
    averages_Dicto=sentiment(inFile)
    while (user_input != "5"):
        print_intro()
        user_input=input("Enter a number: 1 - 5: ")
        if (user_input == "1"):
            get_score(averages_Dicto)
        if (user_input == "2"):
            get_total_average(averages_Dicto)
        if (user_input == "3"):
            get_all_min_and_max(averages_Dicto)
        if (user_input == "3.5"):
            get_last_min_and_max(averages_Dicto)
        if (user_input == "4"):
            positive_and_negative(averages_Dicto)
main()
