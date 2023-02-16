import requests
import datetime
from time import sleep
import json

class CookieError(Exception):
    def __init__(self,ErrorInfo):
        self.ErrorInfo = ErrorInfo
    def __str__(self):
        return self.ErrorInfo

def RequestClass(Cookies,Buildings=['主楼A', '主楼B', '主楼C', '主楼D'],dateStr=datetime.date.today().isoformat()):
	url='http://ehall.xjtu.edu.cn/jwapp/sys/kxjas/modules/kxjscx/cxkxjs.do'
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie':Cookies,
		'Host':'ehall.xjtu.edu.cn',
		'Origin':'http://ehall.xjtu.edu.cn',
		'Refer':'http://ehall.xjtu.edu.cn/jwapp/sys/kxjas/*default/index.do?amp_sec_version_=1&gid_=TWNwdmdmcW1PRThTODBBRVZzMGpNQ25HUk9tait3UkRPTEJNYWZMSFVlc1pNTFl1TGNkSkhLcnprS01ubEoxK0lmZnpJQVNYS01yenJRcTBoZUdhZFE9PQ&EMAP_LANG=zh&THEME=cherry',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	BuildingDict={
		'主楼A':'1001',
		'主楼B':'1002',
		'主楼C':'1003',
		'主楼D':'1004',
	}
	Dict={key:BuildingDict[key] for key in Buildings}
	classKey=','.join(Dict.keys())
	classVal=','.join(Dict.values())
	sections=[('1','2'),('3','4'),('5','6'),('7','8'),('9','10')]
	class_data={'update_date':dateStr,'data':[]}
	for KSJC,JSJC in sections:
		query=[{"name":"XXXQDM","caption":"学校校区","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":"1","value_display":"兴庆校区"},{"name":"JXLDM","caption":"教学楼","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":classVal,"value_display":classKey},{"name":"JASLXDM","caption":"教室类型","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":"4296667874","value_display":"多媒体教室"},{"name":"KXRQ","caption":"空闲日期","linkOpt":"AND","builderList":"cbl_Other","builder":"equal","value":dateStr},{"name":"KXJC","caption":"空闲节次","builder":"lessEqual","linkOpt":"AND","builderList":"cbl_Other","value":JSJC},{"name":"KXJC","caption":"空闲节次","linkOpt":"AND","builderList":"cbl_String","builder":"moreEqual","value":KSJC},{"name":"XXXQDM","value":"1","linkOpt":"and","builder":"equal"},{"name":"JXLDM","value":classVal,"linkOpt":"and","builder":"equal"},{"name":"JASLXDM","value":"4296667874","linkOpt":"and","builder":"equal"},{"name":"KXRQ","value":dateStr,"linkOpt":"and","builder":"equal"},{"name":"JSJC","value":JSJC,"linkOpt":"and","builder":"equal"},{"name":"KSJC","value":KSJC,"linkOpt":"and","builder":"equal"}]
		data={
			"XXXQDM": "1",
			"JXLDM": classVal,
			"JASLXDM": "4296667874",
			"KXRQ": dateStr,
			"JSJC": JSJC,
			"KSJC": KSJC,
			"querySetting":str(query),
			"pageSize": "50",
			"pageNumber": "1"
		}
		r=requests.post(url,data=data,headers=headers)
		if r.headers.get('content-type') != 'application/json; charset=UTF-8':
			raise CookieError('Cookie is invalid.')
		temps=r.json()['datas']['cxkxjs']['rows']
		for temp in temps:
			class_data['data'].append({'JASMC':temp['JASMC'],'KSJC':KSJC,'JSJC':JSJC})
		sleep(1)
	with open('empty_class.json','w',encoding='utf-8') as f:
		json.dump(class_data,f,ensure_ascii=False)
	