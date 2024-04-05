#takes list of all valid words and creates set of valud book names
def text_list(doc):
    books = set()
    for i in range(1, len(doc), 3):
        books.add(doc[i].strip())
    return list(books)
#finds valid user names and assigns a rating slot for each valid book
def user_dict(doc, books):
    users = {}
    for i in range(0, len(doc), 3):
        if doc[i].strip() not in users.keys():
            users[doc[i].strip()] = [0] * len(books)
    return users
#updates valid ratings slot per book review
def update_ratings(doc, books, users):
    for i in range(0, len(doc), 3):
        elem = doc[i].strip()
        users[elem][books.index(doc[i + 1].strip())] = int(doc[i + 2])
#generates initial ratings of all books in valid books list
def compute_average_for_book(book, books, users):
    total = 0
    count = 0
    #searches for user name (elem) in user.keys (user side of dictionary)
    for elem in users.keys():
        if users[elem][books.index(book)] != 0:
            #takes sum of user ratings and computes marching average
            total += users[elem][books.index(book)]
            count += 1
    return round(float(total / count), 2)

def averages(books, users):
    average = []
    for elem in books:
        tupple = (elem, compute_average_for_book(elem, books, users))
        average.append(tupple)
        #generates tupple of book name and average score
    average.sort()
    average.reverse()
    return average
#does dot product for certain matrix multiplication applications
def dot_product(a_vec, b_vec):
    total = 0
    for i in range(len(a_vec)):
        total += a_vec[i] * b_vec[i]
    return total
#generates list of users whos opinions were most similar to given user
def get_most_similar(username, users):
    similar = []
    for elem in users.keys():
        if elem != username:
            similar.append((dot_product(users[username], users[elem]), elem))
    most_similar = []
    for _ in range(3):
        elem = similar.pop()
        most_similar.append(elem[1])
    print(most_similar)
    return most_similar
#finds average book ratings from the averages functions
def average_ratings(most_similar, users, books):
    ratings = [0] * len(books)
    for i in range(len(ratings)):
        count = 0
        total = 0
        for user in most_similar:
            if users[user][i] != 0:
                total += users[user][i]
                count += 1
        if count != 0:
            ratings[i] = total / count
    return ratings
#cross referances similar book ratings with users to display list of book recommendations
def print_recomendations_list(ratings, books):
    recommendations = []
    for i in range(len(books)):
        if ratings[i] > 0:
            recommendations.append((ratings[i], books[i]))
    recommendations.sort()
    for _ in range(len(recommendations)):
        elem = recommendations.pop()
        print(elem[1], elem[0])

#main function
def main():
    #opens file, breaks down by line and creates initial variables
    f = open("ratings_small.txt")
    doc = f.readlines()
    f.close()
    books = text_list(doc)
    users = user_dict(doc, books)
    update_ratings(doc, books, users)
    average = averages(books, users)
    average.sort()
    #prints intro statement and displays user options
    print("Welcome to the CSC110 Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages : output the average ratings of all books in the system")
    print("quit : exit the program")
    print()
    sentinal = False
    while not sentinal:
        #takes user input and acts accordingly
        response = input("next task? ")
        response = response.lower()
        #prints average book rating based on averages list "elem"
        if response == "averages":
            for elem in average:
                print(elem[0], elem[1])
        #gets user name and begins recommendation process
        elif response == "recommend":
            username = input("user? ")
            if username not in users.keys():
                for elem in average:
                    print(elem[0], elem[1])
            else:
                #as outlined above, gets similar user input
                #generates list based on said input
                #prints list of most viable books for inputted user
                most_similar = get_most_similar(username, users)
                ratings = average_ratings(most_similar, users, books)
                print_recomendations_list(ratings, books)
        #sentinal condition, exits program
        elif response == "quit":
            sentinal = True
main()
