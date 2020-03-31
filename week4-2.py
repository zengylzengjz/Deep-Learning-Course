import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()
plt.rcParams['font.sans-serif']="SimHei"
plt.figure(figsize=(10, 10))


for i in range(1, 17):
    num = np.random.randint(1,50000)
    plt.subplot(5, 4, i+4)
    plt.axis("off")
    plt.imshow(train_x[num], cmap='gray')
    plt.title("标签值："+str(train_y[num]))

plt.suptitle("MNIST测试集样本", y=0.9, fontsize=20, color='red')
plt.show()
