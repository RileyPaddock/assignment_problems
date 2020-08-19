import matplotlib.pyplot as plt
from probability import probability
plt.style.use('bmh')
coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH', 'TTH', 'TTH', 'TTH', 'THT', 'TTH', 'HTH', 'HTH', 'TTT', 'HTH', 'HTH', 'TTH', 'HTH', 'TTT', 'TTT', 'TTT', 'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH', 'THH', 'HHH', 'HHH', 'HTT', 'TTH', 'TTH', 'HHT', 'TTH', 'HTH', 'HHT', 'THT', 'THH', 'THT', 'TTH', 'TTT', 'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH', 'HHT', 'HHT', 'HHH', 'TTT', 'THH', 'HHH', 'HHH', 'TTH', 'THH', 'THH', 'TTH', 'HTT', 'TTH', 'HTT', 'HHT', 'TTH', 'HTH', 'THT', 'THT', 'HTH']
coinsets = [coin_1, coin_2, coin_3]

def analyze_coinset(num_heads,coinset):
    num_succesful_results = 0
    for coindata in coinset:
        heads = 0
        for outcome in coindata:
            if outcome == 'H':
                heads+=1
        if heads == num_heads:
            num_succesful_results+=1
    return num_succesful_results/len(coinset)


x_coords = range(4)
probablility_results = [probability(x,3) for x in x_coords]
plt.plot(x_coords,probablility_results,linewidth = 2.5)
# plt.plot([0,1,2,3,4],[0.1, 0.3, 0.5, 0.1, 0.1],linewidth=2.5)
for coinset in coinsets:
    plt.plot(x_coords,[analyze_coinset(x,coinset) for x in x_coords],linewidth = 0.75)
# plt.plot([0,1,2,3,4],[0.3, 0.1, 0.4, 0.2, 0.1],linewidth=0.75)
# plt.plot([0,1,2,3,4],[0.2, 0.2, 0.3, 0.3, 0.2],linewidth=0.75)
plt.legend(['True','Coinset 1','Coinset 2','Coinset 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Coinsets')
plt.savefig('plot.png')
plt.show()

#Coin 2 is a fair coinset as it has an even likely hood of 1 and 2 heads which is the same as having th same likeliehood of having 2 heads and 2 tails.
#Coin 1 is more likely to land tails because it is above the regular distribution before the halfway point
#Coin 3 is more likely to land on heads because it is above the regular distribution after the midway point