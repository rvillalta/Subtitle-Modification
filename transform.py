#! /home/rv/anaconda3/bin/python
import utils
import json
import pdb
file = 'myjson.json'
with open(file, "r", encoding="latin1") as pa:
    content = json.load(pa)
pdb.set_trace()
duration_factor = 1.0
strech_factor = 1.3
temp = content['1']['start']
temp_index = '1'
for index in content:
    if index == "1":
        ta = content[index]['start']
        tb = content[index]['stop']
        #pdb.set_trace()
        new_persist = utils.modifyInterval(ta, tb, ta, duration_factor)
        content[index].update({'stop': new_persist})
        continue
    #if index == "483":
        #pdb.set_trace()
    ti_a = temp
    #print(index, str(utils.timeToNum(ti_a)))
    #ti_b = content[temp]['stop']
    #new_time = utils.modifyInterval(ti_a, ti_b, ti_a, duration_factor)
    #tt = utils.timeToNum()
    tj_a = content[index]['start']
    tj_b = content[index]['stop']
    #pdb.set_trace()
    new_time = utils.modifyInterval(ti_a, tj_a, content[temp_index]['start'], strech_factor)
    tt = utils.timeToNum(new_time)
    temp = content[index]['start']
    content[index].update({"start": new_time})
    tj_a_new = content[index]['start']
    new_persist = utils.modifyInterval(tj_a, tj_b, tj_a_new, duration_factor)
    content[index].update({"stop": new_persist})
    temp_index = index
pb = open("salida.json", "w")
#for index in content
with open("salida.json", "w") as pb:
    json.dump(content, pb)
print("DONE !!")
#pb.close()
pa.close()

pa = open("result.txt", "w")

for index in content:
    item = content[index]
    pa.write(index + "\n")
    #if index == "483":
        #pdb.set_trace()
    time_string = utils.timeToString(item['start']) 
    pa.write(time_string + " --> ")
    time_string = utils.timeToString(item['stop']) 
    pa.write(time_string + "\n")
    pa.write(str(item['line1']) + "\n")
    if item['line2'] != "":
        pa.write(str(item['line2']) + "\n")
    pa.write("\n")
pa.close()

pa = open("STATISTIC2.txt", "w")

for index in content:
    item = content[index]
    pa.write(index + "\t")
    #if index == "483":
        #pdb.set_trace()
    mili_start = utils.timeToNum(item['start']) 
    pa.write(str(mili_start) + "\t")
    mili_stop = utils.timeToNum(item['stop']) 
    pa.write(str(mili_stop)+ "\n")
pa.close()
    


    

