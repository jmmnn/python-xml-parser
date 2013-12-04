import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
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


print 'iterate neighbors:'    
for neighbor in root.iter('neighbor'):
    print neighbor.attrib
    
print 'extracting both values and attributes:'    
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank
    
print 'create new xml:'     
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output.xml')