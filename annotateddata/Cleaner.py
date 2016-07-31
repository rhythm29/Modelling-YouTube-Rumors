import sys
import re
def getProcessedData(line,isRumor):
     #idP = re.compile('id=(.*?)')
     #descP = re.compile('description=(.*?)')
     tags = line.split('');
     #print line
     #print tags[0]
     desc = tags[2].split('=',1)[1]
     Id = tags[0].split('=',1)[1]
     #print Id;
     sr= Id+''+desc+''+str(isRumor)+''+tags[6].split('=',1)[1]+''+tags[7].split('=',1)[1]+''+tags[8].split('=',1)[1]+''+tags[9].split('=',1)[1]+''+tags[10].split('=',1)[1]+''+tags[11].split('=',1)[1]+''+tags[12].split('=',1)[1]
     return sr