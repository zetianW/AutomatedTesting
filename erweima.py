# 开发人员：泽天

# 开发时间：2024/7/15 15:33

# 项目定义：
import qrcode
from PIL import Image

# 输入链接
link = "https://www.bokhealth.com/download.html"

# 创建二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 使用高纠错率
    box_size=5,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# 生成二维码图像
img = qr.make_image(fill='black', back_color='white').convert('RGB')

# 打开中心图标
icon = Image.open('/Users/edy/Desktop/WechatIMG544.jpg')

# 计算图标大小
img_w, img_h = img.size
factor = 4  # 图标相对于二维码的比例因子
size_w = img_w // factor
size_h = img_h // factor
icon = icon.resize((size_w, size_h), Image.LANCZOS)

# 计算图标位置
w = (img_w - size_w) // 2
h = (img_h - size_h) // 2
img.paste(icon, (w, h), icon)

# 保存最终图像
img.save("BOK-Health.png")

print("二维码已生成并保存为 'BOK-health.png'")
