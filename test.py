from tldextract import extract

tsd, td, tsu = extract("https://services.runescape.com-un.ru/m=weblogin/loginform356727,955678,44,837,1") # prints abc, hostname, com

url = td + '.' + tsu # will prints as hostname.com

print (url)
