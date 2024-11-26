# 开发人员：泽天

# 开发时间：2024/7/9 16:43

# 项目定义：
import os
import requests

# 创建一个文件夹来存储下载的图片
save_dir = '/Users/edy/Desktop/photo/intro-air-h5'
os.makedirs(save_dir, exist_ok=True)

# 图片 URL 模板
url_template = 'https://cdn.speedsize.com/3f711f28-1488-44dc-b013-5e43284ac4b0/https://public-web-assets.ultrahuman.com/web_v2/sequence/intro-air/sm/{:04d}.png/w_600'
# 要下载的图片数量
num_images = 357  # 你可以根据需要修改这个数量
for i in range(1, num_images + 1):
    url = url_template.format(i)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(save_dir, f'{i:04d}.png'), 'wb') as f:
            f.write(response.content)
        print(f'Image {i:04d}.png downloaded successfully.')
    else:
        print(f'Failed to download image {i:04d}.png. Status code: {response.status_code}')
