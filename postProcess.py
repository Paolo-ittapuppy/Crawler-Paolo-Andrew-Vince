import json
def final_sort():
    file = open("data.json", 'r')
    oJson = json.load(file)
    file.close()
    punctuations = [
        ",",
        ".",
        ":",
        "(",
        ")",
        "$",
        "&",
        "|",
        "�",
        "}",
        "{",
        ";",
        "[",
        "?",
        "]",
        "*",
        "''",
        "@",
        "#",
        "’",
        "!",
        ">",
        "%",
        "<",
        "“",
        "”",
        "=",
        "'",
        "`",
        "��",
        "``",
        "�",
        "-",
        "�"

    ]
    newDict = dict(oJson["wCount"])
    delets = []
    for key in newDict.keys():
        if key in punctuations or "�" in key:
            delets.append(key)
    #print(delets)
    for i in delets:
        del newDict[i]

    oJson["wCount"] = newDict
    file = open("output2.txt", 'w')
    json.dump(oJson, file)
    file.close()


    with open('Final_Output.txt', 'w') as f:
        f.write("===== The Results of the Crawler ! =====\n\n")
        f.write(f"Number of Unique Pages: {len(oJson['UPages'])}\n")
        f.write(f"Longest Page in Terms of Words: {oJson['LPage'][0]}\n")
        f.write(f"  # of words: {oJson['LPage'][1]}\n\n")

        # sorting portion
        #sorts words by frequency
        sorted_words = sorted(oJson['wCount'], key = lambda x: oJson['wCount'][x], reverse = True)
        
        #sorts the ics subdomains by name
        sorted_domains = sorted(oJson['sDomains'], key = lambda x: (x,oJson['sDomains'][x]))

        f.write("Top 50 words:\n")
        # still have to do a check to make sure everything is sorted
        for word in sorted_words[:50]:
            f.write(f"{word}, = , {oJson['wCount'][word]}\n")
        f.write("\n")
        f.write(f"ics.uci.edu subdomains:\nCount: {len(oJson['sDomains'])}\n")
        for url in sorted_domains:
            f.write(f"{url}, {oJson['sDomains'][url]}\n")

if __name__ == '__main__':
    final_sort()
