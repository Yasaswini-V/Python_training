from Assignment1_Day2 import f
def plot_histogram(f):
    for key,value in f.items():
        print(key,"|","="*(value*3),value)

plot_histogram(f)