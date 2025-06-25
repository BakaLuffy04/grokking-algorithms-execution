import numpy as np
import matplotlib.pyplot as plt

#Built a NumPy-Only Project that ask user for:
#List of weights and hours slept over 10 days and show:
#Mean, max, min, standard deviation
#Days with above-average sleep but below-average weight
#Bar chart of both lists using matplotlib

bw= input ("enter bodyweight(in kg) for 10 days seperated by space")
sleep= input("enter sleep (in hrs) for 10 days seperated by space")

bwlist = list(map(int, bw.split()))
sllist = list(map(int, sleep.split()))

bwmean= np.mean(bwlist)
slmean= np.mean(sllist)

bwmax= np.max(bwlist)
slmax= np.max(sllist)

bwmin= np.min(bwlist)
slmin= np.min(sllist)

bwstd= np.std(bwlist)
slstd= np.std(sllist)

qual= []

for i, (s, w) in enumerate(zip(sllist, bwlist)):
    if s > slmean and w < bwmean:
        qual.append(i+1)

print("Mean bodyweight was at", bwmean, "kgs")
print("Maximum bodyweight was", bwmax, "kgs")
print("Minimum bodyweight was", bwmin, "kgs")
print("Standard deviation bodyweight is", bwstd, "kgs")

print("Mean sleep was at", slmean, "hrs")
print("Maximum sleep was", slmax, "hrs")
print("Minimum sleep was", slmin, "hrs")
print("Standard deviation sleep is", slstd, "hrs")

print("quality day(s) were", qual)


#chart
days = list(range(1, 11))

bar_width = 0.4
x = np.arange(len(days))

plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, bwlist, width=bar_width, label='Weight (kg)', color='skyblue')
plt.bar(x + bar_width/2, sllist, width=bar_width, label='Sleep (hrs)', color='salmon')

plt.xlabel("Day")
plt.ylabel("Value")
plt.title("Body Weight and Sleep Over 10 Days")
plt.xticks(x, [f"Day {d}" for d in days])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
