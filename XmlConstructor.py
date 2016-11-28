from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

# xmlRoot = Element('Setup')
# #print('xmlRoot is: ', xmlRoot)
# tree = ElementTree(xmlRoot)
# #print('tree is: ', tree)
# xmlPort = Element('port')
# #print('xmlPort is: ', xmlPort)
# xmlCommand = Element('command')
# #print('xmlCommand is: ', xmlCommand)
# xmlRoot.append(xmlPort)
# xmlRoot.append(xmlCommand)
# #print('xmlRoot append is: ', xmlRoot)
# xmlPort.text = '2323'
# xmlCommand.text = 'vpush'
# listOfElements = eTree.tostring(xmlRoot).decode('utf-8', errors='strict')


# with open('IP_work.txt', 'r') as source:
#     hpL_start = '<HostPortList>'
#     hpL_end = '</HostPortList>'
#     h_start = '<Host>'
#     h_end = '</Host>'
#     ip_start = '<ip>'
#     ip_end = '</ip>'
#     port_start = '<port>'
#     port_end = '</port>'
#     ip = source.read().split()
#     for i in ip:
#         #print(h_start + '\n\t' + ip_start + i + ip_end + '\n\t' + port_start + '2323' + port_end + '\n' + h_end)
#         pass

# with open('config.xml', 'rt') as zx:
#     pars = ElementTree.parse(zx)
#
# for node in pars.iter():
#     print(node.tag, node.attrib)


tree = ET.parse('config.xml')
root = tree.getroot()
ip_items = []
port_items = []

for child_0 in root:
    if child_0.tag == 'HostPortList':
        for child_1 in child_0:
            # print(child_1.tag)
            for child_2 in child_1:
                if child_2.tag == 'ip':
                    ip_items.append(child_2.text)
                elif child_2.tag == 'port':
                    port_items.append(child_2.text)


# for ip_index, ip_value in enumerate(ip_items):
#     print(ip_index, ip_value)
# for port_index, port_value in enumerate(port_items):
#     print(port_index, port_value)

no_ip_items = len(ip_items)
#print(no_ip_items)
no_port_items = len(port_items)
#print(no_port_items)
i = 0
while i < no_ip_items:
    print(ip_items[i] + ':' + port_items[i])
    i += 1
