from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
line=''
for i in range(1,73):
    url='./pages/page{}.html'.format(i)
    soup = BeautifulSoup(open(url).read(), "html.parser")
    tbl = soup.find_all('div',{'class':'style-scope ytd-expander'})
    for i in tbl:
        line+=str(i.text)+'\n'

    f=open('data.text','a')
    f.write(line)
    f.close()