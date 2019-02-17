import urllib2

def Counter():
    search1="<br>"
    csearch1=descr.count(search1) #counts how many time the substring "<br>" is found
    search2="</p>"
    csearch2=descr.count(search2)#counts how many time the substring "</p>" is found
    search3="</a>"
    csearch3=descr.count(search3)#counts how many time the substring "</a>" is found
    changecounter=csearch1+csearch2
    print("Change-line tag (<br> or </p>) Counter:",changecounter)
    linkcounter=csearch3
    print("Links tag(<a>) Counter:",linkcounter)
    open_file.close()
    print("GOODBYE")





print("Hello")
print("DO YOU WANT TO CHECK A FILE OR A SITE ?PRESS F or f for FILE and S or s FOR SITE")
print("press 0 to exit")
choice=raw_input("")
tf= choice=="0" or choice=="f" or choice=="F" or choice=="s" or choice=="S" #boolean
if tf==True:
    if choice=="0":
        print("GOODBYE")
        choice="b"

    elif choice=="s" or choice=="S":
        print("URL of the html page:")
        link=raw_input("")
        open_file= urllib2.urlopen(link)
        descr= open_file.read()
        Counter()
        choice="b"
    else:
        print("Give me the html file:")
        link=raw_input("")
        open_file=open(link,"r")
        descr=open_file.read()
        Counter()
        choice="b"
else:
    print("INVALID.RESTART THE PROGRAMM")
    
