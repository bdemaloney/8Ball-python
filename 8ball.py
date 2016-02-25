Python 3.4.0 (default, Jun 19 2015, 14:18:46) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import random
question = input("Welcome to the\nMAGIC EIGHT BALL!\nPress enter for answer")
x = random.randint(1,20)
answers_dict = {
    1:"Yes",
    2:"No",
    3:"Maybe",
    4:"All Signs Point to Yes",
    5:"All Signs Point to No",
    6:"Future Hazey, Ask Again",
    7:"Definitely",
    8:"Decidedly Not",
    9:"Unclear",
    10:"It is Certain",
    11:"Nope",
    12:"Please Ask Again",
    13:"The Universe Says Yes",
    14:"The Universe Says No",
    15:"It Is Yet To Be Seen",
    16:"Affirmitive",
    17:"Negative",
    18:"You Betcha!",
    19:"No Way Jose",
    20:"Please Focus and Ask Again"
}
print (answers_dict[x])
again = input("Shake Again? y/n")
if again == 'y':
    x = random.randint(1,20)
    print (answers_dict[x])


if again == 'n':
    print ("Goodbye!")

else:
    again != 'y' or again != 'n'
    print ("I did not understand. Please enter y or n")
