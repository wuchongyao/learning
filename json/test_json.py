import json
from tkinter import W

# data = open(u'F:\\code\\python\\json\\test-01.json', encoding="UTF-8")
# print(json.load(data))
# print(json.loads(data.read()))

data = {'sites': 
            {'site': 
                [
                    {'id': '1', 
                    'name': '菜鸟教程', 
                    'url': 'www.runoob.com'
                    }, 
                    {'id': '3',
                    'name': 'Google', 
                    'url': 'www.google.com'
                    }
                ]
            }
        }      

f = open(u'F:\\code\\python\\json\\test-03.json', 'w', encoding="UTF-8") 
# json.dump(data, f, ensure_ascii=False)
f.write(json.dumps(data, ensure_ascii=False))