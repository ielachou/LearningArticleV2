import numpy as np
import matplotlib.pyplot as plt

from agents.wolf_agent import WoLFAgent
from agents.Q_learner_agent import QLearnerAgent
from environments.gridWorld import GridWorldEnv



if __name__ == "__main__":
    nb_episode = 100000
    evaluate_every = 2000
    nb_runs = 1
    probsNorth1 = []
    probsNorth2 = []
    probsWest2 = []
    probsEast1 = []

    game = GridWorldEnv()
    for i in range(nb_runs):
        actions = np.arange(4)
        agent1 =  WoLFAgent(alpha=0.1, actions=actions,nb_states=9, high_delta=0.004, low_delta=0.001)
        agent2 =  WoLFAgent(alpha=0.1, actions=actions,nb_states=9, high_delta=0.004, low_delta=0.001)
        for episode in range(nb_episode):
            done=False
            obs1, obs2 = game.reset()
            t=0
            while not done:
                action1 = agent1.act(obs1)
                action2 = agent2.act(obs2)
                new_obs1, new_obs2, rew1, rew2, done = game.step(action1, action2)

                agent1.observe(rew1, obs1, new_obs1)
                agent2.observe(rew2, obs2, new_obs2)
                obs1 = new_obs1
                obs2 = new_obs2
                t+=1

            if episode % (evaluate_every) == 0:
                print(episode)
                index = int(episode / evaluate_every)
                if i ==0:
                    probsNorth1.append(agent1.pi[6][0])
                    probsNorth2.append(agent2.pi[8][0])
                    probsEast1.append(agent1.pi[6][2])
                    probsWest2.append(agent2.pi[8][3])
                else:
                    probsNorth1[episode//evaluate_every]+=agent1.pi[6][0]
                    probsNorth2[episode//evaluate_every]+=agent2.pi[8][0]
                    probsEast1[episode//evaluate_every]+=agent1.pi[6][2]
                    probsWest2[episode//evaluate_every]+=agent2.pi[8][3]


    fig, ax = plt.subplots()
    print(probsNorth2)
    print(probsWest2)

    print(probsNorth1)
    print(probsEast1)

    plt.plot(probsNorth1, probsEast1, label="Player1 : Wolf-PHC", linewidth=0.7)

    plt.plot(probsNorth2,probsWest2, label="Player2 : Wolf-PHC", linewidth=0.7)

    plt.xlabel("Pr(North)")
    plt.ylabel("Pr(East||West)")
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.legend()
    plt.savefig("resultsGrid.png")
    plt.show()