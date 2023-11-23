import time


def sleep(seconds):
    for i in range(seconds):
        print(f"等待{seconds - i} 秒...")
        time.sleep(1)



