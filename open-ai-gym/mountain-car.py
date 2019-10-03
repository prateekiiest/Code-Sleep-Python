'''The mountain car problem, although fairly simple, is commonly applied because it requires a reinforcement learning agent to learn
on two continuous variables: position and velocity. For any given state (position and velocity) of the car, the agent is given the
possibility of driving left, driving right, or not using the engine at all'''
# https://en.wikipedia.org/wiki/Mountain_car_problem
# environment: https://github.com/openai/gym/wiki/MountainCar-v0
# 3 actions: 0:push_left, 1:no_push, 2:push_right
# 2 observations: 0:position ; 1:volecity
# inspired by https://github.com/llSourcell/Q_Learning_Explained

import numpy as np

import gym
from gym import wrappers

# initializations
number_states = 40 # number_of_states
max_iteration = 5000 # max_iteration
initial_learning_rate = 1.0 # initial learning rate
min_learning_rate = 0.005   # minimum learning rate
max_step = 10000 # max_step

# parameters for q learning
epsilon = 0.05
gamma = 1.0




def observation_to_state(environment, observation):
    # map an observation to state
    environment_low = environment.observation_space.low
    environment_high = environment.observation_space.high
    environment_dx = (environment_high - environment_low) / number_states

    # observation[0]:position ;  observation[1]: volecity
    p = int((observation[0] - environment_low[0])/environment_dx[0])
    v = int((observation[1] - environment_low[1])/environment_dx[1])
    # p:position, v:volecity
    return p, v


def episode_simulation(environment, policy=None, render=False):
    observation= environment.reset()
    total_reward = 0
    step_count = 0
    for _ in range(max_step):
        if policy is None:
            action = environment.action_space.sample()
        else:
            p,v = observation_to_state(environment, observation)
            action = policy[p][v]
        if render:
            environment.render()
        # proceed environment for each step
        # get observation, reward and done after each step
        observation, reward, done, _ = environment.step(action)
        total_reward += gamma ** step_count * reward
        step_count += 1
        if done:
            break
    return total_reward


if __name__ == '__main__':
    # use gym environment: MountainCar-v0
    # https://github.com/openai/gym/wiki/MountainCar-v0
    environment_name = 'MountainCar-v0'
    environment = gym.make(environment_name)
    environment.seed(0)
    np.random.seed(0)
    
    # create qTable with zeros
    # 3 actions: 0:push_left, 1:no_push, 2:push_right
    q_table = np.zeros((number_states, number_states, 3))

    # training for maximum iteration episodes
    for i in range(max_iteration):
        observation = environment.reset()
        total_reward = 0
        # eta: learning rate is decreased at each step
        eta = max(min_learning_rate, initial_learning_rate * (0.85 ** (i//100)))
        # each episode is max_step long
        for j in range(max_step):
            p, v = observation_to_state(environment, observation)
            # select an action
            if np.random.uniform(0, 1) < epsilon:
                # get random action
                action = np.random.choice(environment.action_space.n)
            else:
                logits = q_table[p][v]
                # calculate the exponential of all elements in the input array.
                logits_exp = np.exp(logits)
                # calculate the probabilities
                probabilities = logits_exp / np.sum(logits_exp)
                # get random action
                action = np.random.choice(environment.action_space.n, p=probabilities)
                # get observation, reward and done after each step
                observation, reward, done, _ = environment.step(action)

            total_reward += reward
            # update q table
            # p:position, v:volecity
            p_, v_ = observation_to_state(environment, observation)
            # gamma: discount factor
            # Bellmann eq: Q(s,a)=reward + gamma* max(Q(s_,a_))  ::: Q_target = reward+gamma*max(Qs_prime)
            q_table[p][v][action] = q_table[p][v][action] + eta * (reward + gamma *  np.max(q_table[p_][v_]) - q_table[p][v][action])
            if done:
                break
        if i % 50 == 0:
            print('Iteration No: %d -- Total Reward : %d.' %(i+1, total_reward))

    solution_policy = np.argmax(q_table, axis=2)
    solution_policy_scores = [episode_simulation(environment, solution_policy, False) for _ in range(100)]
    print("Mean score : ", np.mean(solution_policy_scores))
# run with render=True for visualization
episode_simulation(environment, solution_policy, True)

