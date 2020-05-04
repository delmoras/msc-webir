# msc-webir
Κώδικας για το μάθημα Web Information Retrieval του ΠΜΣ ευφυείς τεχνολογίες διαδικτύου

Παράδειγμα εκτέλεσης : 
python qrels.py -i inputQrels.txt -o outputQrels.txt -s "\t" -n " 0 " -sc 1

ή εαν θελουμε να χρησιμοποιήσουμε τα default arguements

python qrels.py -i inputQrels.txt

Default arguments : 

Output File : qrels-out.txt
Seperator : "\t"
New Seperator : " 0 "
Seperator Count : 1



$ python qrels.py -h
usage: qrels.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-s SEPERATOR]
                [-n NEWSPERATOR] [-sc SEPERATORCOUNT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Input file to read
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output file to store modified data
  -s SEPERATOR, --seperator SEPERATOR
                        Specify the seperator between fields
  -n NEWSPERATOR, --newseperator NEWSPERATOR
                        New seperator between fields
  -sc SEPERATORCOUNT, --seperatorcount SEPERATORCOUNT
                        Seperate nth fields starting from left
         
