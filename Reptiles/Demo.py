# 开发人员：泽天
import time

import form as form
# 开发时间：2024/4/10 09:59

# 项目定义：

import requests
from bs4 import BeautifulSoup

# # url = 'https://www.iqiyi.com/playlist/2505665296161402?'
# url = 'https://mesh.if.iqiyi.com/tvg/lw/play_list_detail?device_id=813b2102c0b74b23d1389622c4251409&timestamp=1712723261&app_version=12.3.13276&src=pcw&auth_cookie=&page_size=20&page_num=1&collection_id=2505665296161402&sign=31712CBE493811DAE896B1219073BD33'
# headers = {
#     'Referer': 'https://www.iqiyi.com/',
#     'Sec-Ch-Ua': 'Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123',
#     'Sec-ch-Ua-mobile': '?0',
#     'Sec-Ch-Ua-Platform': "macOS",
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# if 'content-type' in response.headers and 'charset' in response.headers['content-type']:
#     encoding = response.headers['content-type'].split('charset=')[-1].strip()
# else:
#     encoding = 'utf-8'
# response_text = response.content.decode(encoding)
# soup = BeautifulSoup(response_text, 'html.parser')
# title = soup.find_all('title')
# print(title)

# lists = ["1", "2", "3", "4", "5"]
# new_lists = []
# for i in lists:
#     lists.remove(i)
#     new_lists.append(i)
# print(new_lists)

# t_0 = ([0],)
# try:
#     t_0[0] += [1]
# except:
#     t_0[0].append(2)
# else:
#     t_0[0].append(3)
# finally:
#     print(t_0)

# class A:
#     __x = 10
#
#     def get_x(self):
#         return self.__x
#
# A.__x = 100
# a = A()
# print(a.__x, a.get_x())

#
# import random
# import smtplib
# import dns.resolver
# import logging
#
# # 配置日志级别和格式
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#
# logger = logging.getLogger(__name__)
#
#
# def fetch_mx(host):
#     """
#     解析给定域名的MX记录
#     """
#     logger.info(f'正在查找域名 {host} 的邮箱服务器')
#     try:
#         answers = dns.resolver.query(host, 'MX')
#         mx_servers = [str(rdata.exchange)[:-1] for rdata in answers]
#         logger.info(f'查找结果为：{mx_servers}')
#         return mx_servers
#     except Exception as e:
#         logger.error(f'解析MX记录时发生错误: {e}')
#         return []
#
#
# def verify_istrue(email):
#     """
#     验证邮箱地址的有效性
#     """
#     email_list = [email] if isinstance(email, (str, bytes)) else email
#     email_obj = {}
#     final_res = {}
#
#     for em in email_list:
#         name, host = em.split('@')
#         email_obj.setdefault(host, []).append(em)
#
#     for key in email_obj:
#         logger.info(f'开始验证 {key} 域名下的邮箱')
#         mx_servers = fetch_mx(key)
#         if not mx_servers:
#             logger.warning(f'无法获取 {key} 的MX记录，跳过验证')
#             continue
#
#         host = random.choice(mx_servers)
#         logger.info(f'选择MX服务器 {host} 进行验证')
#
#         try:
#             with smtplib.SMTP(host, timeout=10) as smtp:
#                 helo_response = smtp.helo('localhost')
#                 logger.debug(f'HELO 响应: {helo_response}')
#
#                 mail_from_response = smtp.mail('you@example.com')  # 使用有效的发件邮箱
#                 logger.debug(f'MAIL FROM 响应: {mail_from_response}')
#
#                 for need_verify in email_obj[key]:
#                     rcpt_to_response = smtp.rcpt(need_verify)
#                     logger.debug(f'RCPT TO {need_verify} 响应: {rcpt_to_response}')
#
#                     response_code = rcpt_to_response[0]
#                     if response_code == 250 or response_code == 451:
#                         final_res[need_verify] = True
#                         logger.info(f'{need_verify} 存在')
#                     elif response_code == 550:
#                         final_res[need_verify] = False
#                         logger.info(f'{need_verify} 不存在')
#                     else:
#                         final_res[need_verify] = None
#                         logger.info(f'{need_verify} 验证结果未知')
#
#         except Exception as e:
#             logger.error(f'验证邮箱 {need_verify} 时出现错误: {e}')
#
#     return final_res
#
#
# if __name__ == '__main__':
#     test_emails = ['shgajdjagdg@qq.com', 'test@163.com']
#     results = verify_istrue(test_emails)
#     print(results)
a = [10, 20, 30, 40]
b = 11
if b in a:
    print("b包含在a内")
else:
    assert False, "b不包含在a内"
