# Qlearning
Implementing reinforcement learning through Q-learning method on a maze
Q-learning is a model free learning algorithm.
The belief here is that there is no access to the details of the environment and everything should be learned.
There is also an epsilon greedy action being done here.
Input/output to the program were:
1. <maze input>: path to the environment input .txt described previously
2. <value file>: path to output the values V (s)
3. <q value file>: path to output the q-values Q(s, a)
4. <policy file>: path to output the optimal actions π(s)
5. <num episodes>: the number of episodes your program should train the agent for. One episode is a sequence of states, actions and rewards, which ends with terminal state or ends when the maximum
episode length has been reached.
6. <max episode length>: the maximum of the length of an episode. When this is reached, we terminate the current episode.
7. <learning rate>: the learning rate α of the q learning algorithm
8. <discount factor>: the discount factor γ.
9. <epsilon>: the value  for the epsilon-greedy strategy
