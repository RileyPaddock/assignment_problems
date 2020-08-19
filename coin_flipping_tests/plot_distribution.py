import matplotlib.pyplot as plt
import sys
sys.path.append('coin_flipping_src')
from monte_carlo import monte_carlo
from probability import probability
plt.style.use('bmh')
x_coords = range(10)
probablility_results = [probability(x,10) for x in x_coords]
plt.plot(x_coords,probablility_results,linewidth = 2.5)
# plt.plot([0,1,2,3,4],[0.1, 0.3, 0.5, 0.1, 0.1],linewidth=2.5)
for _ in range(5):
    plt.plot(x_coords,[monte_carlo(x,10,100) for x in x_coords],linewidth = 0.75)
# plt.plot([0,1,2,3,4],[0.3, 0.1, 0.4, 0.2, 0.1],linewidth=0.75)
# plt.plot([0,1,2,3,4],[0.2, 0.2, 0.3, 0.3, 0.2],linewidth=0.75)
plt.legend(['True','MC 1','MC 2','MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 10 Coin Flips')
plt.savefig('plot.png')
plt.show()