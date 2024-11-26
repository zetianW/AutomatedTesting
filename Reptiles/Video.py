# 开发人员：泽天

# 开发时间：2024/4/2 14:31

# 项目定义：
import requests
from bs4 import BeautifulSoup
import os


def download_video(video_url, save_path):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            print(f'Successfully downloaded video to {save_path}')
    else:
        print(f'Failed to download video: {video_url} (Status Code: {response.status_code})')


def crawl_videos(url, save_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <video> tags and then find <source> tags within them
    videos = soup.find_all('video')
    sources = [source['src'] for video in videos for source in video.find_all('source')]


    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for video_url in sources:
        # Handle relative URLs if necessary
        if not video_url.startswith('http'):
            video_url = url + video_url
            print(video_url)

        save_path = os.path.join(save_dir, os.path.basename(video_url))
        download_video(video_url, save_path)


url_demo = 'https://www.ultrahuman.com'
save_dir_demo = '/Users/edy/Desktop/photo'
crawl_videos(url_demo, save_dir_demo)
