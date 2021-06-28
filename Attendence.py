fileptr=open('MYFILES/attendance.csv','r')
lines=fileptr.readlines()
outptr=open('MYFILES/Output.csv','a')
notptr=open('MYFILES/notConsidered.csv','w')
for eachline in lines:
    slist=eachline.split(',')
    if '-' in slist[0]:
        regdno=slist[0].split('-')[0]
        time=slist[4]
        outptr.write(regdno+','+time)
    else:
        name=slist[0].split('-')[0]
        time=slist[4]
        notptr.write(name+','+time)

finalptr=open('MYFILES/final.csv','a')
outptr=open('MYFILES/Output.csv','r')
slist=outptr.readlines()

for student in slist:
    studentDetails=student.split(',')
    studentDetails[1]=studentDetails[1].replace('\n','')
    if(int(studentDetails[1])>=70):
        finalptr.write(studentDetails[0]+','+"Present"+'\n')
    else:
        finalptr.write(studentDetails[0]+','+"ABSENT"+'\n')
