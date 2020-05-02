import re
import requests
import pprint
import json
import pprint
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)+'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari+'
                  '/537.36 Edg/81.0.416.68',

}

def getpage(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:

        return res.text
    else:
        print("请求错误")

def main(i):
    list = []
    url = 'https://www.zhihu.com/api/v4/questions/308457217/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset='+str(i)+'&platform=desktop&sort_by=default'
    data = json.loads(getpage(url))
    name = i
    for item in data['data']:
        s = item['content']
        list.append(re.findall('.*?src="(https://.*?)"', s, re.S))
        print(type(list))

        for link in list:
            link = set(link)
            for url in link:
                print(url)
                response = requests.get(url, headers).content
                name = name + 1
                file_name = str(name) + '.jpg'
                with open(file_name, 'wb') as f:
                    f.write(response)
                    print("第"+str(name)+"张保存完成")
if __name__ == '__main__':
    for i in range(0, 201, 5):
        main(i)
        time.sleep(1)