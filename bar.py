from time import sleep



def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f'\r|{bar}| {int(percent):02}%', end='\r')



if __name__ == '__main__':
    for i in range(100):
        progress_bar(i + 1, 100)
        sleep(0.25)