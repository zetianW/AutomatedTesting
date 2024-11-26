# 开发人员：泽天

# 开发时间：2024/4/2 14:15

# 项目定义：
import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# 目标 URL
url = "https://www.ultrahuman.com"

# 本地保存图片的路径
save_dir = "/Users/edy/Desktop/photo"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
# 发送 GET 请求获取网页内容
response = requests.get(url)
response.raise_for_status()

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(response.text, "html.parser")

# 查找页面上所有图片
img_tags = soup.find_all("img")

for img_tag in img_tags:
    # 获取图片的完整 URL（处理相对路径）
    img_url = urljoin(url, img_tag["src"])

    # 图片文件名（通常可以从 URL 中提取）
    img_filename = os.path.basename(img_url)

    # 图片保存的完整路径
    save_path = os.path.join(save_dir, img_filename)
    # 下载图片到本地
    with requests.get(img_url, stream=True) as img_response:
        if img_response.status_code == 200:
            with open(save_path, "wb") as img_file:
                img_file.write(img_response.content)
                print(f"Saved image: {img_filename}")
        else:
            print(f"Failed to download image: {img_url} (Status Code: {img_response.status_code})")
