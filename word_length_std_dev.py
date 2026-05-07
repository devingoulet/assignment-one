# Devin Goulet, 6 May 2026, Github:Devin Goulet Project 6

def word_length_std_dev(text):
    words = text.split()

    lengths = []
    for word in words:
        lengths.append(len(word))

    mean = sum(lengths) / len(lengths)

    squared_diffs = 0
    for length in lengths:
        squared_diffs += (length - mean) ** 2

    variance = squared_diffs / (len(lengths) - 1)
    std_dev = variance ** 0.5

    return std_dev
    # ---TEST---
#text = "There is wisdom in turning as often as possible from the familiar to the unfamiliar"
#answer = word_length_std_dev(text)

#print(answer)