from lxml import etree
from io import BytesIO

##Gets filepaths
srcPath = input('File path of file with .xml extension: ') ##"C:\\Users\\hagen\\Documents\\Uni\\BSP\\.xml to .py\\test.xml"
destPath = input('File path of .py file: ') ##"C:\\Users\\hagen\\Documents\\Uni\\BSP\\.xml to .py\\test.py"

#----------------------------------------------------------------------
def parseXML(xmlFile, strL):
    """
    Parse the xml file
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()
    
    tree = etree.parse(BytesIO(xml.encode('utf-8')))
    context = etree.iterparse(BytesIO(xml.encode('utf-8')))
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
            
        if elem.tag == 'voice':
            strL.append(text)
        elif elem.tag == 'face':
            strL.append(text)
        elif elem.tag == 'gesture':
            strL.append(text)
        elif elem.tag == 'duration':
            strL.append('sleep(' + text + ')')

##Putting code before 'insert part' into strL and the rest into strL2
dest = open(destPath,'r')

strL = []
strL2 = []
strL = dest.read().splitlines()
for s in strL:
    if s == '##START Commands##':
        strL2 = strL[strL.index(s)+1:]
        strL = strL[:strL.index(s)+1]
dest.close()

##Putting 'insert part' into list
if __name__ == "__main__":
    parseXML(srcPath, strL)

##Concatenates lists
strL = strL + strL2

strL = [s + '\n' for s in strL]

##Writes to file.py              
dest = open(destPath,'w')
dest.writelines(strL)
dest.close()
        
