import os
import re

#set path to the election_data.csv which is in the resources folder
paragraph_path = os.path.join("raw_data","paragraph_2.txt")

#open the file to read the paragraph
with open(paragraph_path) as paragraph_file:   

    paragraph = paragraph_file.read()

    #replace new pargraph notation with space
    paragraph = paragraph.replace("\n\n"," ")

    #split the paragragh into a list of words
    words = paragraph.split(" ")
 
    #find the number of words
    word_count = len(words)

    #split the paragraph into sentences
    sentences = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len(sentences)

    #find the lengths of all words and add them
    letter_length = [len(word) for word in words]
    sum_letters = sum(letter_length)
  
    #find average number of letters per word
    avg_letter = round(sum_letters/word_count,1)
    
    #find average number of words in a sentence
    avg_sentence = round(word_count/sentence_count,1)

    print("Pargraph Analysis")
    print("-----------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {avg_letter}")
    print(f"Average Sentence Length: {avg_sentence}")
            