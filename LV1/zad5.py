def average_word_count(sms_list):
    total_words_count = 0
    for sms in sms_list:
        total_words_count += len(sms.split(" "))
    return total_words_count / len(sms_list)

def ends_with_ex(sms):
    return sms[-1] == '!'

spam = []
ham = []

sms = open("SMSSpamCollection.txt")
for line in sms:
    line = line.rstrip()
    parts = line.split("\t")
    if (parts[0] == "ham"):
        ham.append(parts[1])
    elif (parts[0] == "spam"):
        spam.append(parts[1])

print(f"Average word count in spam {average_word_count(spam)}")
print(f"Average word count in ham {average_word_count(ham)}")
print(f"Number of spam ending with !: {len(list(filter(ends_with_ex, spam)))}")

sms.close()