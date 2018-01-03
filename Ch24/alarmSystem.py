

class alarm(object):

	def __init__(self, state):
		self.state = state

	def getStatus(self):
		return self.state

	def changeStatus(self, newStatus):
		self.state = newStatus
		print("New status:", self.state)

class AlarmSystem(object):

	def __init__(self):
		self.curstate = state("SystemInactive")

	def pressButton(self):
		if (self.curStatus.getStatus() == "SystemInactive"):
			self.curStatus.changeStatus("SystemActive")
		else: pass

	def sensorActivated(self):
		if (self.curStatus.getStatus() == "SystemActive"):
			self.curStatus.changeStatus("AlertMode")


	def enterPIN(self):
		if (self.curStatus.getStatus() == "SystemActive") \
			or (self.curStatus.getStatus() == "AlertMode") \
				or (self.curStatus.getStatus() == "AlarmBellRings"):

			self.curStatus.changeStatus("SystemInactive")


	def twoMinutesPass(self):
		if (self.curStatus.getStatus() == "AlertMode"):
			self.curStatus.changeStatus("AlarmBellRings")
