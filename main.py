f = open("message-history.txt", "r")
lines = f.readlines()

out = open("twitter-handles.txt", "w")

for line in lines:
    if "twitter.com" in line:
        words = line.split(" ")
        for word in words:
            if "https://twitter.com" in word:
                out.write(word.replace("https://twitter.com/", "@"))