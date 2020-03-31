from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("D:\Deep-Learning-Course\lena.jpg")
img_r, img_g, img_b= img.split()
plt.rcParams['font.sans-serif']="SimHei"
plt.figure(figsize=(10, 10))


plt.subplot(221)
plt.axis("off")
img_small = img_r.resize((50, 50))
plt.imshow(img_small)
plt.title("R-缩放", fontsize=14)


plt.subplot(222)
img_flr = img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_r270 = img_flr.transpose(Image.ROTATE_270)
plt.imshow(img_r270)
plt.axis("on")
plt.title("G-镜像+旋转", fontsize=14)


plt.subplot(223)
img_cut = img_b.crop((0, 0, 150, 150))
plt.imshow(img_cut)
plt.axis("off")
plt.title("B-裁剪", fontsize=14)


plt.subplot(224)
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.axis("off")
plt.imshow(img_rgb)
plt.title("RGB", fontsize=14)



img_rgb.save("test.png")

plt.suptitle("图像基本操作", fontsize=20, y=1, color="blue")

plt.show()