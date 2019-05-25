import re

#template tags
"""
~TITLE~
~BODY~
~TITLEURL~
~IMGURL~
~IMGNAME~
~IMGPAGE~
~CAPTION~
"""

#input:       
'''
~
TITLE
IMGURL
IMGPAGEURL
IMGCAPTION
IMGNAME
passage
'''

class Page:
    def __init__(this,raw):
        this.title=raw[0];
        this.url = raw[0].replace(' ','')
        this.imgurl=raw[1]
        this.imgpage=raw[2]
        this.caption=raw[3]
        this.imgname=raw[4]
        this.paragraph=raw[5:]
        this.text = '\n<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(this.paragraph)

        
    def writeFile(this):
        with open("pages/template.html","r") as template:
            data = template.readlines()

        i = 0
        for i in range(len(data)):
            line = data[i]
            line=line.replace('~TITLE~',this.title)
            line=line.replace('~BODY~',this.text)
            line=line.replace('~TITLEURL~',this.url)
            line=line.replace('~IMGNAME~',this.imgname)
            line=line.replace('~IMGURL~',this.imgurl)
            line=line.replace('~IMGPAGE~',this.imgpage)
            line=line.replace('~CAPTION~',this.caption)
            data[i] = line
        print(this.title)
        with open("pages/" + this.url + ".html","w") as f:
            f.write(''.join(data))


def main():
    with open("data.txt","r") as f:
        lines = [line.rstrip('\n') for line in f]
    temp = []
    for s in lines:
        if s == '~':
            if(len(temp)>=4):
                Page(temp).writeFile()
                temp = []
        else:
            temp.append(s)
    if(len(temp)>=5):
        Page(temp).writeFile()
        temp = []

if __name__=="__main__":
    main()
