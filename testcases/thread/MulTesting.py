# 开发人员：泽天

# 开发时间：2023/11/14 17:02

# 项目定义：
import threading
import Request


# 创建多线程
def mulTesting():
    threads = []
    for i in range(0, 20000):
        threads.append(
            # 将“打印传入的参数”方法传入新创建的线程终，参数以for循环中i为准
            threading.Thread(target=Request.post_glucose()))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# 调用多线程方法
if __name__ == "__main__":
    mulTesting()
