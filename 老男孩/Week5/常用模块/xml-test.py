import xml.etree.ElementTree as ET
tree=ET.parse("scratch_1.xml")
# 获取根节点
root=tree.getroot()
print(root)

# 遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

for node in root.iter('year'):
    print(node.tag,node.text)

for node in root.iter('year'):
    new_year=int(node.text)+1
    node.text=str(new_year)
    node.set("updated","yes")

tree.write("scratch_1.xml")