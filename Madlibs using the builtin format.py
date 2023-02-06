def madlib() -> str:
    """
    We're going to play Madlibs! All you have to do is type in a word that
    that follows the constraint about the type of word it must be.
    """
    print("We're going to play MadLibs!")
    print("Put in the correct form of the word for the following:")
    adj = input("An adjective - ")
    adj2 = input("Another adjective - ")
    bird = input("A type of bird - ")
    room = input("A room in a house - ")
    verbed = input("A verb in past tense - ")
    verb = input("A verb - ")
    name = input("A name - ")
    noun = input("A noun - ")
    liquid = input("A liquid - ")
    verbing = input("A verb in continuous - ")
    body = input("A body part that is more than 1 (eg. ears)- ")
    noun2 = input("A plural noun - ")
    verbing2 = input("Another verb in continuous - ")
    noun3 = input("Last noun! - ")

    print("\nHere is the result!\n")

    print( "It was a " + adj + ", cold November day. I woke up to the \n"
           + adj2 + " smell of " + bird + " roasting in the " + room + "\n"
           "downstairs. I " + verbed + " down the stairs to see if I could \n"
           "help " + verb + " the dinner. My mom said, \"See if \n"
           + name + " needs a fresh " + noun + ".\" So I carried a tray of \n"
           + liquid + " into the " + verbing + " room. When I got there, I \n" 
           "couldn't believe my " + body + "! There were " + noun2 + "\n"
           + verbing2 + " on the " + noun3 + "!"
           )


def madlib2() -> str:
    """
    We're going to play Madlibs! All you have to do is type in a word that
    that follows the constraint about the type of word it must be.
    """
    print("We're going to play MadLibs!")
    print("Put in the correct form of the word for the following:")
    holiday = input("A holiday - ")
    noun = input("An object noun - ")
    place = input("A location - ")
    costume = input("A person/job - ")
    adj = input("An adjective - ")
    body = input("A body part that is more than 1 (eg. ears) - ")
    verb = input("A verb - ")
    adj2 = input("Another adjective - ")
    noun2 = input("Another noun - ")
    food = input("A food, plural - ")
    noun3 = input("The last noun, also plural - ")

    print("\nHere is the result!\n")

    print("I can't believe it's already {0}! I can't wait to put on my \n"
          "{1} and visit every {2} in my neighbourhood. This year, I am \n"
          "going to dress up as a {3} with {4} {5}. Before I {6}, I \n"
          "made sure to grab my {7} {8} to hold all my {9}. Finally, \n"
          "all of my {10} are ready to go!".format(holiday, noun, place,
                                               costume, adj, body, verb,
                                               adj2, noun2, food, noun3)
          )

### The above is the cool string method called `format`! I think it helps make
### the return line far more compact.
