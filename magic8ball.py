#a short test of random
import random
messages = ['It is certain', 'It is decidedly so',\
		'Yes definetly', 'Reply hazy try again',\
		'Ask again later', 'Concentrate and ask again',\
		'My reply is no', 'Outlook not so good', \
		'Very doubtfull']
print(messages[random.randint(0, len(messages)-1) ])
