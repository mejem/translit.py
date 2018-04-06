#!/usr/bin/env python3

import sys, os
# https://stackoverflow.com/questions/4374455/how-to-set-sys-stdout-encoding-in-python-3
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
sys.stdin = open(sys.stdin.fileno(), mode='r', encoding='utf8', buffering=1)

def main():
    input = sys.stdin.read()
    lang = os.environ['QUERY_STRING']

    output = transliterate(input, lang)

    print("Content-type: text/html; charset=utf-8\n")
    print(output, end = '')

def transliterate(input, lang):
    if lang == "ru":
        return tr_russian(input)
    elif lang == "uk":
        return tr_ukrainian(input)
    else:
        raise ValueError

def tr_ukrainian(input):
    cyrilic =      "АаБбВвГгҐґДдЕеЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфЦцЧчШшЬь"  + "ЄєХхЩщЮюЯя"
    czech   = list("AaBbVvHhGgDdEeŽžZzYyÌìÏïJjKkLlMmNnOoPpRrSsTtUuFfCcČčŠš’’") + ['Je', 'je', 'Ch', 'ch', 'Šč', 'šč', 'Ju', 'ju', 'Ja', 'ja']

    rules = dict(zip(cyrilic, czech))

    output = []
    for i in range(len(input)):
        if input[i] in rules:
            #                            po nebo pred je velke pismeno----------------------------------------------------
            if input[i] in "ЄХЩЮЯ" and ((i < len(input) - 1 and input[i + 1].isupper()) or (i > 0 and input[i - 1].isupper())):
                output.append(rules[input[i]].upper())
            else:
                output.append(rules[input[i]])
        else:
            output.append(input[i])

    return ''.join(output)

def tr_russian(input):
    cyrilic =      "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфЦцЧчШшЪъЫыЬьЭэ"  + "ХхЩщЮюЯя"
    czech   = list("AaBbVvGgDdEeEeŽžZzIiJjKkLlMmNnOoPpRrSsTtUuFfCcČčŠš””Yy’’Èè") + ['Ch', 'ch', 'Šč', 'šč', 'Ju', 'ju', 'Ja', 'ja']

    rules = dict(zip(cyrilic, czech))
    vocals = list("АаЕеЁёИиОоУуЪъЫыЬьЭэЮюЯя")

    output = []
    for i in range(len(input)):
        if input[i] in rules:
            #                                              na zacatku slova a po apostrofu-----      po vokalech a jerech--
            if   (input[i] == 'Е' or input[i] == 'Ё') and (i == 0 or (not input[i - 1].isalnum()) or input[i - 1] in vocals):
                output.append('J')
                #   po nebo pred je velke pismeno----------------------------------------------------
                if (i < len(input) - 1 and input[i + 1].isupper()) or (i > 0 and input[i - 1].isupper()):
                    output.append('E')
                else:
                    output.append('e')
            #                                              na zacatku slova a po apostrofu-----      po vokalech a jerech--
            elif (input[i] == 'е' or input[i] == 'ё') and (i == 0 or (not input[i - 1].isalnum()) or input[i - 1] in vocals):
                output.append('je')
            elif input[i] == 'И' and (i > 0 and input[i - 1] == 'Ь'):
                output.append('JI')
            elif input[i] == 'и' and (i > 0 and input[i - 1] == 'Ь'):
                output.append('Ji')
            elif input[i] == 'и' and (i > 0 and input[i - 1] == 'ь'):
                output.append('ji')
            #                             po nebo pred je velke pismeno----------------------------------------------------
            elif input[i] in "ХЩЮЯ" and ((i < len(input) - 1 and input[i + 1].isupper()) or (i > 0 and input[i - 1].isupper())):
                output.append(rules[input[i]].upper())
            else:
                output.append(rules[input[i]])
        else:
            output.append(input[i])

    return ''.join(output)


main()
