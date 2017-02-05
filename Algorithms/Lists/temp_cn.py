__author__ = 'Meghna'
from matplotlib import pyplot as plt
start_cwnd = 64
end_cwnd = 70
def plot(segment_sizes,title):
    RTTs = range(1,len(segment_sizes)+1)
    print RTTs
    plt.figure(1,figsize=(10,20))
    plt.plot(RTTs,segment_sizes,c="g")
    plt.title(title)
    plt.ylabel("Congestion window (in segments)")
    plt.xlabel('RTTs')
    plt.show()
plot(range(start_cwnd,end_cwnd),'TCP RENO')