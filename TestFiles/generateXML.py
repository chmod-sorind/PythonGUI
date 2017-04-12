from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as eTree

xmlRoot = Element('Setup')
tree = ElementTree(xmlRoot)
xmlPort = Element('port')
xmlCommand = Element('command')
xmlRoot.append(xmlPort)
xmlRoot.append(xmlCommand)
xmlPort.text = '2323'
xmlCommand.text = 'vpush'
print(eTree.tostring(xmlRoot))
