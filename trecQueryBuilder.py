import os
import sys
from bs4 import BeautifulSoup
import argparse
import threading
import queue 
import time

#οριζω αριθμό threads ανάλογα με τα cores του υπολογιστή. μπορείτε να το αλλάξετε με το χερι εαν θέλετε παραπάνω 
# δεν σημαίνει όμως ότι θα πηγαίνει γρηγορότερα
num_worker_threads = os.cpu_count()
timeStart = time.time()

xml_path ="E:/TEI/MASTER/IIR/MiniCollection/PAC_topics/files"
sgml_path="E:/TEI/MASTER/IIR/MiniCollection/PAC_topics/sgml_threads"

def do_work(filename):
    print(filename)
    content = open(xml_path+"/"+filename,'r',encoding='utf8').read()
    soup = BeautifulSoup(content,'lxml')
    inv_title=soup.findAll("invention-title")  # Όνομα του xml tag
    abstract=soup.findAll("abstract")
    f=open(sgml_path+"/"+"SGML_Topics.txt",'a+',encoding='utf8')
    f.write("<TOP>\n<NUM>"+os.path.splitext(filename)[0]+"</NUM>\n<TITLE>\n") 
    for text in inv_title:
        invt=text.getText()
        f.write(invt+" ") 
    for text in abstract:
        abstr=text.getText()
        f.write(abstr+" ")  
    f.write("\n</TITLE>\n</TOP>\n")


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


q = queue.Queue()

threads = []

for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)


for item in os.listdir(xml_path):
    q.put(item)

# block until all tasks are done
q.join()

print('Stopping workers!')

# stop workers
for i in range(num_worker_threads):
    q.put(None)

for t in threads:
    t.join()

print("all done")
timeEnd = time.time()
totalTime = timeEnd-timeStart
#Τυπώνουμε πόσα δευτερόλεπτα πήρε η εκτέλεση του προγράμματος
print("Συνολικός Χρόνος Εκτέλεσης σε δευτερόλεπτα : "+str(totalTime))  