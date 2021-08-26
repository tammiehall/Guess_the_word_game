# # choose_cities = ['barcelona','london', 'Washington','Bristol','Paris','Shanghai','Bangladesh','Dresden','Casablanca', 'Liverpool']

# import random

# countries = ['Nepal', 'Peru', 'India', 'Spain', 'Germany', 'Argentina', 'Morocco', 'Colombia', 'Kazakhstan', 'Cambodia']
# print("GUESS THE WORD!")
# print("YOU HAVE 7 CHANCES")

# guess_a_letter = input("Guess a letter: ").lower

# country = random.choice(countries)

# guesses = ""

# print(f"The word has {len(country)} letters ")

# for guess_a_letter in country:
#     # for i in range(len(country)):
#     #     if country == guess_a_letter:
#     #         print("Correct")
#             # guessed_word=country
#     if guess_a_letter in guesses:
#         print(guess_a_letter)
#     else:
#         print("_")

# guess_a_letter

# # for letter in country:
# #     if letter == guess_a_letter:
# #         print("correct")
# #     else:
# #         print('There is no such a letter in this world')

# print(input('WELCOME TO THE WORD GUESSING GAME! PRESS ANY KEY'))
# y = True
# n = False
# def lets_begin():
#     start_a_game = input('Would you like play a game? y/n ').lower()
#     if start_a_game == 'y':
#         print("Let's begin!")
#     elif start_a_game =='n':
#         print("Sorry to see you go :(")
#         pass
# lets_begin()
# countries =['nepal', 'peru', 'india', 'spain', 'germany', 'argentina', 'morocco', 'colombia', 'kazakhstan', 'cambodia']

# import random

# chosen_word = random.choice(countries)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 7


# display = []
# for _ in range(word_length):
#     display += "_"

# while len(chosen_word) > 0 and lives > 0:
#     while not end_of_game:
#         guess = input("Guess a letter: ").lower()

#     for position in range(word_length):
#         letter = chosen_word[position]

#         if letter == guess:
#             display[position] = letter

#     if guess not in chosen_word:

#         lives -= 1
#         if lives==0:
#              end_of_game==True
#              print("You lost. Please try again")
#              print("The word was", word , "!")
#         else:
#              end_of_game==True
#              print('Congratulations!You won!')

#     print(f"{' '.join(display)}")