import xml.etree.ElementTree as ET
tree = ET.parse('ODS-28-01-2013.xml')
root = tree.getroot()
print root
attrib = root.attrib
tag = root.tag

print 'root attributes:'
print attrib

print 'root tag:'
print tag

# looping over childs

print 'childs:'
for child in root:
    print child.tag, child.attrib

# End result: works !!! to create a new HTML file with just the links to the URLS of each doc
f = open('workfile.html', 'w')
f.write('<html>')
#iterate meta tags   
for meta in root.iter('meta'):
    if meta.get('name')=='URL':
        content = meta.get('content')
        f.write('<A href="' + content + '">' + content + '</A>' + '<br>')
f.write('</html>')
  
 

  
  
###works !!!!!  to display just the content of the URL meta tag
#print 'iterate meta:'    
#for meta in root.iter('meta'):
    #if meta.get('name')=='URL':
        #content = meta.get('content')
        #print content
    
###works to display just the meta URL tag
#print 'iterate meta:'    
#for meta in root.iter('meta'):
    ##if 'URL'=='URL':
    #if meta.get('name')=='URL':
        #print meta.attrib
     
##this works to list the content of meta tags   
#print 'iterate meta:'    
#for meta in root.iter('meta'):
    #print meta.attrib

#this works
#print 'iterate records:'    
#for record in root.iter('record'):
    #print record.attrib
    
#print 'create new xml:'     
#for rank in root.iter('rank'):
    #new_rank = int(rank.text) + 1
    #rank.text = str(new_rank)
    #rank.set('updated', 'yes')
#tree.write('output.xml')

##works!!!! Create a new text file with just the URLS
#f = open('workfile', 'w')
##iterate meta tags   
#for meta in root.iter('meta'):
    #if meta.get('name')=='URL':
        #content = meta.get('content')
        #f.write(content + '\n')

  


