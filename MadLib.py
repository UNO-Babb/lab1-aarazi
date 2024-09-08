#MadLib.py
#Name:AmberArazi
#Date:29Aug
#Assignment:MadLib-lab1

def main():
  print("Madlib")
  #Ask user for words
  print ("Let's tell a story together!")
  print ("For this story, we need three nouns.")
  print ("A noun is a person, place, or thing.")
  noun_one = input ("noun one: ")
  print ("Our first noun is",noun_one)
  noun_two = input ("noun two: ")
  print ("Our second noun is",noun_two)
  noun_three = input ("noun three: ")
  print (noun_three)
  print ("Now we need two adjectives.")
  print ("An adjective is a word that describes a noun.")
  adj_one = input ("adjective one: ")
  print ("Our first adjective is", adj_one)
  adj_two = input ("adjective two: ")
  print ("Our second adjective is", adj_two)
  print ("Finally, we need two verbs!")
  print ("A verb is an action word.")
  verb_one = input ("verb one: ")
  verb_two = input ("verb ending in ing: ")
  print ("Here are our verbs:", verb_one,"and", verb_two,)
  print ("Now, let's read our story!")
  #Print the story with the user supplied words.
  print ("Have an idea for the next great American", (noun_one) , "but don't know where to", verb_one+ "?")
  print ("Well, here is some", (adj_one), "advice!")
  print ("First, remember that everyone has to start with their first", (noun_two)+ ".")
  print ("The important thing is to start", (verb_two)+ "!")
  print ("Before you know it, you'll", (verb_one), "into your own", (adj_two), (noun_one) + "!")
  print ("Now, get started and be a", (noun_three) + "!")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
