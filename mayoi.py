import sys
import MeCab

def mayoi_convert(text):
    result = ""
    for ch in text:
        if ch == "ラ":
            result += "リャ"
        else:
            result += ch
    return result

def tsubasa_convert(text):
    result = ""
    for ch in text:
        if ch == "ナ":
            result += "ニャ"
        else:
            result += ch
    return result

def say(text, cvt):
    mt = MeCab.Tagger("mecabrc")
    node = mt.parseToNode(text)
    result = ""
    while node:
        arr = node.feature.split(",")
        word_type = arr[1]
        if len(arr) <= 7:
            word = node.surface
        else:
            word = arr[7]
            if word == "*":
                node = node.next
                continue
        result += cvt(word)
        node = node.next
    return result

def mayoi(text):
    return say(text, mayoi_convert)

def tsubasa(text):
    return say(text, tubasa_convert)

