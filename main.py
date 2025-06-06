import random
import sys
import os


def resource_path(relative_path) :
    try : 
        base_path = sys._MEIPASS ## Temp path
    except :
        base_path = os.path.abspath(".") ## Absolute path
        
    return os.path.join(base_path, relative_path)

def answer_check(answer_en, list_sentence_en , random_index) :
    if (list_sentence_en[random_index] == answer_en) :
        return "Correct!"
    else :
        return list_sentence_en[random_index]
    

def main() :
    while (True) :
        unit = "Unit " + input("Please enter the Unit Number: ")
        
        try :
            sentences_en_path = resource_path("Resource/" + unit + "/Sentences_EN.txt")
            sentences_kor_path = resource_path("Resource/" + unit + "/Sentences_KOR.txt")
            
            with open(sentences_kor_path, encoding="utf-8") as kor_file :
                sentences_kor = kor_file.readlines()
            with open(sentences_en_path, encoding="utf-8") as en_file :
                sentences_en = en_file.readlines()
            
            break
        except FileNotFoundError :
            print("This unit isn't ready yet.")
        
    list_sentences_en = [i.strip() for i in sentences_en]
    list_sentences_kor = [i.strip() for i in sentences_kor]
    
    while (True) :
        random_index = random.randrange(0, len(list_sentences_en))
        
        question_kor = list_sentences_kor[random_index]
        
        print("- Please answer the question.")
        print("Q: " + question_kor)
        
        answer_en = input("A: ")
        
        if (answer_en == "/exit") :
            break
        elif (answer_en == "/pass") :
            print(list_sentences_en[random_index])
            print()
        
            continue
        
        print(answer_check(answer_en, list_sentences_en , random_index))
        print()
    


if (__name__ == "__main__") :
    main()