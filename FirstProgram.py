#FirstProgram.py
#Name:AmberArazi
#Date:28Aug
#Assignment:

def main():
  print("First Program")
  #Say hello
  print ("Hello!")
  #Ask for the user's name
  name = input("What is your name? ")
  print (name)
  #Use the user's name in the program.
  print ("Nice to meet you,", name)
  #Ask the user for their age.
  age = input ("How old are you? ")
  print (age)
  #Tell the user what year they were born in.
  age = int(age)
  birth_year = 2024-(age)
  print("You were born in", birth_year)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

