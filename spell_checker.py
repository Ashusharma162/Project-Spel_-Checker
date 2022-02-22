from textblob import TextBlob
import time

word = str(input("Enter the word you want to get corrected : "))

# used to create a delay of 1 ( provided in the parameter ) second
time.sleep(1)

print("\n\nTHE CORRECTED WORD WILL THE CLOSETS WORD WHICH WILL BE MATCHING TO THE WORD YOU WROTE.....\n THE WORD "
      "MAY NOT BE THE BEST SUITED FOR THE WORD YOU WERE EXPECTING......... ")

# used to create a delay of 1 ( provided in the parameter ) second
time.sleep(1)

# this line will change the word you wrote to the corrected closets matching word....
b = TextBlob(word)

# this line will try to print the corrected word
print("The text you might be looking for : " + str(b.correct()))
