class Programmer:
	work_time: int = 0
	salary: int = 0
	role_salary = {
		"Junior" : 10,
		"Middle" : 15,
		"Senior" : 20,
	}

	def __init__(self, name: str=None, role: str=None) -> None:
		self.name = name
		self.role = role
		self.salary_hour = self.role_salary[role]

	def work(self, time: int=0) -> None:
		self.work_time += time
		self.salary += time * self.salary_hour

	def rise(self) -> None:
		if self.role == "Junior":
			self.role = "Middle"
			self.salary_hour = self.role_salary[self.role]
			self.work()

		elif self.role == "Middle":
			self.role = "Senior"
			self.salary_hour = self.role_salary[self.role]
			self.work()

		elif self.role == "Senior":
			self.salary_hour += 1
			self.work()

	def info(self) -> str:
		return f"{self.name} {self.work_time} {self.salary}"
	
programmer = Programmer('Васильев Иван', 'Junior')  
programmer.work(750)  
print(programmer.info())  
programmer.rise()  
programmer.work(500)  
print(programmer.info())  
programmer.rise()  
programmer.work(250)  
print(programmer.info())  
programmer.rise()  
programmer.work(250)  
print(programmer.info())  