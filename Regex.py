import re
ha=re.compile(r'(Ha){3}')


greed=re.compile(r'(a){3,5}')
c=greed.search("aaaaa")
print(c.group())
code=re.compile(r'(\d\d)-(\d\d)-(\d\d)')
new=code.findall("hello the code is 25-80-00 and 00-00-00")
print(new)
bat=re.compile(r'Bat( Shit|Woman|copter|ever)')
s=bat.search("Batcopter is god")
print(s.group())
print(s.group())
phone=re.compile(r'(\d\d)?\d\d\d\d')
nu=phone.search("4321 is num??")
print(nu.group())
string=re.compile(r'\D\D\D\D')
print(string.search("shit is bacon  and  a ansi").group())
xmas=re.compile(r'\d+\s+\w+')
print(xmas.findall("16 bacon,3 choc"))
n=re.compile('\s\s\s')
print(n.search("beacon    ").group())
at=re.compile(r'.at')
print(at.findall('the cat in the hat and found bat mat'))
endswith=re.compile(r'\D+$')
print(endswith.search("string is"))
