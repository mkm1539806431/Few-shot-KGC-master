import requests
import json

rel = open('C:/Users/Dell Optiplex 7050/Desktop/physics/phy_rel.txt', 'w')
attri = open('C:/Users/Dell Optiplex 7050/Desktop/physics/phy_attri.txt', 'w')

f = open('C:/Users/Dell Optiplex 7050/Desktop/physics/ent_physics.txt', 'r')
count = 0
for line in f.readlines():
	count +=1
	print(count)
	head = line.replace('\n', '').replace(' ', '')
	url = 'https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&format=json&languages=en'%(head)

	for attempt in range(10):
		try:
			res=requests.get(url) #返回一个消息实体
			break
		except:
			continue
	r = json.loads(res.text)
	r = r['entities'][head]['claims']

	for key in r.keys():
		for item in r[key]:
			try:
				print(head, "	", key, "	", item['mainsnak']['datavalue']['value']['id'])
				rel.write(head+'	')
				rel.write(key+'	')
				rel.write(item['mainsnak']['datavalue']['value']['id']+'\n')
			except:
				try:
					print(head, "	", key, "	", item['mainsnak']['datavalue']['value'])
					attri.write(head+'	')
					attri.write(key+'	')
					attri.write(item['mainsnak']['datavalue']['value']+'\n')
				except:
					continue

rel.close()
attri.close()