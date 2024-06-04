from PIL import Image

# 打开深度图像
depth_image = Image.open("target_image_depth1.jpg")

# 将图像转换为灰度图像
gray_image = depth_image.convert("L")

# 调整像素值范围为0-255
gray_image = gray_image.point(lambda x: x * (255/gray_image.getextrema()[1]))

# 显示灰度图像
gray_image.show()

# 保存灰度图像
gray_image.save("gray_image_depth1.jpg")