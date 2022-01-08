import random

class SoccerEnv():

	def __init__(self):
		self.agent1 = 8
		self.agent2 = 11
		self.ball = 11

	def reset(self):
		self.__init__()
		return self.agent1, self.agent2

	def step(self, action1, action2):
		firstPlayer = random.randint(0, 1)
		if firstPlayer == 0:
			currentFirst = self.agent1
			currentSecond = self.agent2
			firstAction = action1
			secondAction = action2
		else:
			currentFirst = self.agent2
			currentSecond = self.agent1
			firstAction = action2
			secondAction = action1
		firstReward = 0
		secondReward = 0
		done = False

		firstNew, moved1 = self.actOne(currentFirst, firstAction)
		if not moved1 and currentFirst in [5, 10, 9, 14]:
			if self.checkWin(currentFirst, firstAction):
				firstReward = 1
				done = True
		if currentFirst == self.agent1:
			self.agent1 = firstNew
			reward1 = firstReward
		else:
			self.agent2 = firstNew
			reward2 = firstReward

		secondNew, moved2 = self.actOne(currentSecond, secondAction)
		if not moved2 and currentSecond in [5, 10, 9, 14]:
			if self.checkWin(currentSecond, secondAction):
				secondReward = 1
				done = True

		if currentSecond == self.agent1:
			self.agent1 = secondNew
			reward1 = secondReward
		else:
			self.agent2 = secondNew
			reward2 = secondReward

		return self.agent1, self.agent2, reward1, reward2, done

	def actOne(self, obs, action):
		moved = False
		hasBall = False
		if obs == self.ball:
			hasBall = True
		if obs == self.agent1:
			other = self.agent2
		else:
			other = self.agent1
		if action == 0:  # not move
			pass
		elif action == 1:  # north
			if obs not in [0, 1, 2, 3, 4]:
				if obs - 5 != other:
					obs -= 5
					if hasBall:
						self.ball -= 5
					moved = True
				else:
					if not hasBall:
						self.ball = obs
		elif action == 2:  # south
			if obs not in [15, 16, 17, 18, 19]:
				if obs + 5 != other:
					obs += 5
					if hasBall:
						self.ball += 5
					moved = True
				else:
					if not hasBall:
						self.ball = obs
		elif action == 3:  # east
			if obs not in [4, 9, 14, 19]:
				if obs + 1 != other:
					obs += 1
					if hasBall:
						self.ball += 1
					moved = True
				else:
					if not hasBall:
						self.ball = obs
		elif action == 4:
			if obs not in [0, 5, 10, 15]:
				if obs - 1 != other:
					obs -= 1
					moved = True
					if hasBall:
						self.ball -= 1
				else:
					if not hasBall:
						self.ball = obs
		return obs, moved

	def checkWin(self, obs, act):
		if obs == self.ball:
			if obs == self.agent1:
				goal = [5, 10]
				winAct = 4
			else:
				goal = [9, 14]
				winAct = 3
			return act == winAct and obs in goal
		else:
			return False
