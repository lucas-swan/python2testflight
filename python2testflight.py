# python把这个网页"https://github.com/pluwen/awesome-testflight-link" 里Available状态位Full和yes的类似/join/QN934ULR后面的8位邀请码输出

import requests
from bs4 import BeautifulSoup

# 获取网页响应
response = requests.get('https://github.com/pluwen/awesome-testflight-link') 

# 创建soup对象
soup = BeautifulSoup(response.text, 'html.parser') 

# 查找所有包含href属性的a标签
links = soup.find_all('a', href=True) 
# 查找所有包含href属性的a标签
codes = [] 
# 遍历所有链接
for link in links: 
    # 获取链接的href值
    href = link['href'] 
    # 如果链接包含/join/
    if '/join/' in href: 
        # 获取链接所在的表格单元格
        cell = link.parent 
        # 获取单元格旁边的Available状态值,并去除空白字符
        status = cell.next_sibling.next_sibling.text.strip() 
        # 如果状态为F或Y或D,则获取邀请码
        if status == 'F' or status == 'Y' or status == 'D' :
            # 获取链接最后8位作为邀请码
            code = href[-8:] 
            # 将邀请码添加到列表中
            codes.append(code) 
# 打印列表中的所有邀请码,输出以逗号分隔的邀请码
print(','.join(codes))