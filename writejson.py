#! /home/rv/anaconda3/bin/python
#import pdb; pdb.set_trace()
import re
import utils
    

filename = "sub.txt"

jsonfile = "myjson.json"

pb = open(jsonfile, "w", encoding="latin1")
pa = open(filename, "r", encoding="latin1")
pattern = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})')
objective = '00:00:15,010 --> 00:00:17,387'
val = [0, 0, 3, 0]
sol = pattern.search(objective)

idPat = re.compile("\d")
timePat = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})')
cont = 0
flag = False
pb.write("{\n")
while True:
    line = pa.readline()
    print(line)
    #print(line)
    if not line:
        pb.write("}\n")
        break 
    if line and flag:
        pb.write("\t\t\t\t\t},\n")
        flag = False
    if cont == 0:
        pb.write("\t\t\"" + line[0:len(line)-1] + "\" : ")
        #pb.write("\t\t" + line[0:len(line)-1] + " : ")
        pb.write("{\n")      
        
    if cont == 1:
        t = timePat.search(line)
        t1 = utils.getTime(t.group(1), False)
        t2 = utils.getTime(t.group(2), False)
        pb.write("\t\t\t\t\t\"start\": " + t1 + ",\n")
        pb.write("\t\t\t\t\t\"stop\": " + t2 + ",\n")
        
    if cont == 2:
        line = line.replace("\"", "'")
        pb.write("\t\t\t\t\t\"line1\": \"" + line[0:len(line)-1] + "\",\n")
        line = pa.readline()
        if line == "\n":
            pb.write("\t\t\t\t\t\"line2\": " + "\"\"" + "\n")
        else:
            line = line.replace("\"", "'")
            pb.write("\t\t\t\t\t\"line2\": \"" + line[0:len(line)-1] + "\"\n")
            line = pa.readline()
        flag = True
        
        cont = -1
    cont = cont + 1
pb.write("\t\t\t\t\t}")
pb.close()
pa.close()
print("DONE !!!!!")