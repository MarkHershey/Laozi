# This Python file uses the following encoding: utf-8

import json
from pathlib import Path

from matplotlib import pyplot as plt
from wordcloud import WordCloud

CN_punctuations = "，。（）、﹑！：﹕‘’ “” ；﹗？?﹖"


def process_CN1():
    cn1_path = Path("texts/CN1.txt")
    assert cn1_path.is_file()

    with cn1_path.open() as f:
        lines = f.readlines()

    pure_text_string = ""
    for index, line in enumerate(lines):
        if "德" in line:
            print(line)
        line = line.strip()
        first_space_idx = line.find(" ")
        line = line[first_space_idx + 1 :]
        lines[index] = line

        for char in line:
            if char not in CN_punctuations:
                pure_text_string += char

    print(pure_text_string)

    frequency_map = {}
    for token in pure_text_string:
        if token in frequency_map:
            frequency_map[token] += 1
        else:
            frequency_map[token] = 1

    print(f"Total word count: {len(pure_text_string)}")
    print(f"Unique word count: {len(frequency_map.keys())}")

    sorted_keys = sorted(
        frequency_map.keys(), key=lambda x: frequency_map[x], reverse=True
    )
    for i in range(30):
        print(f"{sorted_keys[i]} : {frequency_map[sorted_keys[i]]}")

    ## word cloud
    pure_text_string_space = ""
    for i in pure_text_string:
        pure_text_string_space += i
        pure_text_string_space += " "

    wordcloud = WordCloud(
        font_path="MaShanZheng-Regular.ttf",
        width=800,
        height=600,
        background_color="white",
        min_font_size=10,
        # max_font_size=170,
        prefer_horizontal=1,
        # random_state=9,
        max_words=50,
    ).generate(pure_text_string_space)

    # plot the WordCloud image
    plt.figure(figsize=(8, 6), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    save_file = "wordcloud.png"
    plt.savefig(str(save_file))


if __name__ == "__main__":
    process_CN1()
