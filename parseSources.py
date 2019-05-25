body=""

def writeFile(title,sources):
    global body
    page=title.replace(' ','')
    html=['  <div id="' + page + '" class="pageBib paragraph">',
          '    <a class="bibLink" href="pages/' + page + '.html">' + title + '</a><br>']
    for i in range(len(sources)):
        sources[i]=sources[i].replace("https:","\n<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https:")
        if(sources[i].find('https:')!=-1):
            url = sources[i][max(sources[i].find("https:"),0):-1]
        else:
            url ="https://isbnsearch.org/isbn/0465024963"

        html.append('    <br><a href="' + url + '" style="font-weight:normal">&middot;&nbsp;&nbsp;')
        html.append('      ' + sources[i] + '</a><br>')
    html[-1]+="</div>\n\n"
    return '\n'.join(html)


def main():
    global body
    with open("bibTemplate.html","r") as f:
        body = [i[:-1] for i in f.readlines() if i.find("<!-- -->")!=0]
    with open("biblio.txt","r") as f:
        lines = [i[:-1] for i in f.readlines()]
    print('\n'.join(lines))
    temp = []
    for s in lines:
        if s == '~':
            if(len(temp)>=2):
                print('\n'.join(temp))
                body.append(writeFile(temp[0],temp[1:]));
                temp = []
        else:
            temp.append(s)
    if(len(temp)>=2):
        print('\n'.join(temp))
        body.append(writeFile(temp[0],temp[1:]));
        temp = []
    body.append("</body></html>")
    with open("bibliography.html","w") as f:
        f.write('\n'.join(body))

if __name__=="__main__":
    main()
        
