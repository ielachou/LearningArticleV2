import matplotlib.pyplot as plt
import numpy as np

from agents.wolf_agent import WoLFAgent
from environments.soccerEnv import SoccerEnv

if __name__ == "__main__":
	nb_episode = 10000
	nb_runs = 1
	probsNorth1 = []
	probsNorth2 = []
	probsWest2 = []
	probsEast1 = []

	game = SoccerEnv()
	for i in range(nb_runs):
		actions = np.arange(5)
		agent1 = WoLFAgent(alpha=0.1, actions=actions, nb_states=20, high_delta=0.004, low_delta=0.001)
		agent2 = WoLFAgent(alpha=0.1, actions=actions, nb_states=20, high_delta=0.004, low_delta=0.001)
		for episode in range(nb_episode):
			done = False
			obs1, obs2 = game.reset()
			t = 0
			while not done:
				action1 = agent1.act(obs1)
				action2 = agent2.act(obs2)
				new_obs1, new_obs2, rew1, rew2, done = game.step(action1, action2)

				agent1.observe(rew1, obs1, new_obs1)
				agent2.observe(rew2, obs2, new_obs2)
				obs1 = new_obs1
				obs2 = new_obs2
				t += 1

	fig, ax = plt.subplots()

for i in range(len(agent1.pi)):
	print(i, agent1.pi[i])

print("---------------")
for i in range(len(agent2.pi)):
	print(i, agent2.pi[i])
""" plt.plot(probsNorth1, probsEast1, label="Player1 : Wolf-PHC")

    plt.plot(probsNorth2,probsWest2, label="Player2 : PHC")

    plt.xlabel("Pr(North)")
    plt.ylabel("Pr(East||West)")
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.legend()
    plt.savefig("resultsGrid")
    plt.show()"""
