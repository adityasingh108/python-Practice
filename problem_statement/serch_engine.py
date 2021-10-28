def serch(sentence1, sentence2):
    """
    This function match the  senteces with the 
    entere query
    """
    word1 = sentence1.strip().split(" ")
    word2 = sentence2.strip().split(" ")
    word_score = 0
    for words1 in word1:
        for words2 in word2:
            if words1.lower() == words2.lower():
                word_score += 1
    return word_score
    


if __name__ == "__main__":
    sentence = ["python is good ", "python is developed by van rossem ", "python is develpoed by 7990",
                "python is not python snake ", "pyton is object oriented language  ", "python is interpreted language "]  # List of sentece

    query = input("Enter the word you want to serch :")

    scores = [serch(query, sentences) for sentences in sentence]


    sorted_sentence = [sent_score for sent_score in sorted(
        zip(scores, sentence), reverse=True) if sent_score[0] != 0]

    print(f"{len(sorted_sentence)} result found in  ")

    for scores, item in sorted_sentence:
        print(f" \"{item}\" : with a score of {scores}")
