template = ['<!DOCTYPE html><html><head><title>",
'</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="../styles.css"></head><body class="contentWrapper"><div class="pageTitle"><p>',
'</p><a href="../index.html" class="headerLink">Home</a><a href="bibliography.html" class="headerLink">Bibliography</a></div><div class="paragraph"><p>',
'</p></div><div class="sidebar"><table class="sideTable"><tr><td class="hoverable"><a style="font-size: 25px;"ref="bibliography.html%23',
'">Sources</a></td><td class="hoverable"><a style="font-size: 25px;"ref="imageBib.html%23',
'">Image</a></td></tr></table><img src="../images/',
'"></img><p style="margin-left: 5%;font-weight: normal;"><i>-',
'</i></p></div></body></html>']

class page:
    def __init__(this,raw):
        this.title=raw[0];
        this.url=strip(raw[0],' ')
        this.imgurl=raw[1]
        this.caption=raw[2]
        this.cite=raw[3]
        this.text=replace(raw[4],,'\t','....')
    def writeFile(this):
        f = open("pages/" + this.title + ".html","w")
        str = template[0]
        fields = [this.title,this.title,this.text,this.url,this.url,this.imgurl,this.caption]
        html = template[0]
        for i in range(len(fields)):
            
        
        f.close()
        

TITLE
IMGURL
IMGCAPTION
citation
passage

def main():
    with open("data.txt","r") as f:
        lines = [line.rstrip('\n') for line in file]
    psgs = 

if __name__=="__main__":
    main()
