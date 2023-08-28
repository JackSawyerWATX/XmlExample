import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Jonathan Fausset</name>
    <phone type="intl">+1 (206) 713-3756</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone Number', tree.find('phone').text)
print('Attribute:', tree.find('email').get('hide'))