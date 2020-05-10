from lxml import etree
from lxml import etree
import os
import xmltodict
import xml.etree.ElementTree as ET
import collections

data = []

def sorted_by_count(lists):
  counts = collections.defaultdict(int)
  for L in lists:
    for n in L:
      counts[n] += 1

  return [num for num, count in
          sorted(counts.items(),
                 key=lambda k_v: (k_v[1], k_v[0]),
                 reverse=True)]
                 
xmlPath ="E:/TEI/MASTER/IIR/MiniCollection/\MiniCollectionVirtual/all/"

for file in os.listdir(xmlPath):
    try:
        print(file)
        fullPath = xmlPath+file
        xmlTree = ET.parse(fullPath)
        tags = list({elem.tag for elem in xmlTree.iter()})
        data.append(tags)
    except Exception as e:
        print("Exeception occured:{}".format(e))

print(sorted_by_count(data))


