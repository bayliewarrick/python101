emailz = []
with open('emails.txt', 'r') as f:
    #f.write(task)
    #f.write('\r')
    line = f.read()
    line = line.split(',')
for l in range(0,len(line)):
    if(line[l] not in emailz):
        emailz.append(line[l])
for x in range(0,len(emailz)):
    email_file = open('emails-no-duplicates.txt','a')
    email_file.write(emailz[x])
    email_file.close()

