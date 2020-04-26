import re
# use codebeautify.org to beautify before
string = '''


'''
url = re.findall(r'(?P<url>https?://[^\s]+)', string)
urls = []
for i in url:
	if i.endswith('.jpeg",') or i.endswith('.jpeg'):
		urls.append(i)
	else:
		next
urls2 = list(set(urls))
for i in urls2:
	print(i)
