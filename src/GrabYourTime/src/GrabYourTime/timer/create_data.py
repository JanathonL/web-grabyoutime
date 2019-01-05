from timer.models import *
from django.contrib.auth.models import User
from random import randint
import datetime

# for i in range(5):
# 	g = Group.objects.create(groupName="Group" + str(i))
# 	g.save()
# 	uid = i % 2
# 	user = User.objects.all()[uid]
# 	user1 = User.objects.all()[uid ^ 1]
# 	ownership = Own.objects.create(manager= user, groupID=g)
# 	membership = Belong.objects.create(member= user1, groupID=g)
# 	ownership.save()
# 	membership.save()

# # generate 20 projects
# for i in range(20):
# 	projectName = "Project" + str(i)
# 	description = "Our Demo Project" + str(i)
# 	now = datetime.datetime.now()
# 	estimateTime = now + datetime.timedelta(days=randint(5, 10)) # hours
# 	startTime = now - datetime.timedelta(days=randint(5, 10))
# 	finishTime = None if i % 5 != 0 else now
# 	priority = randint(1, 5)
# 	p = Project.objects.create(
# 		projectName =projectName,
# 		description = description,
# 		estimateTime=estimateTime,
# 		startTime=startTime,
# 		finishTime=finishTime,
# 		priority=priority)
# 	p.save()

# generate progress for each project 
# for i in range(-9, 0):
# 	for j in range(20):
# 		p = Project.objects.filter(projectName= "Project" + str(j))[0]
# 		user = User.objects.all()[0]  # uid ??
# 		user1 = User.objects.all()[1]
# 		now = datetime.datetime.now()
# 		time = now + datetime.timedelta(days=i)
# 		time = time.date
# 		progress1 = randint(0,10) / 10. 
# 		progress2 = randint(0,10) / 10.
# 		p1 = Progress.objects.create(
# 			user=user,
# 			project=p,
# 			time=time,
# 			progress=progress1)
# 		p2 = Progress.objects.create(
# 			user=user1,
# 			project=p,
# 			time=time,
# 			progress=progress2)
# 		p1.save()
# 		p2.save()

	# generate TODO Project 
# for i in range(10):
# 	projectName = "ProjectTODO" + str(i)
# 	description = "Our Demo Project" + str(i)
# 	now = datetime.datetime.now()
# 	estimateTime = now + datetime.timedelta(days=randint(20, 30)) # hours
# 	startTime = now + datetime.timedelta(days=randint(5, 15))
# 	finishTime = None
# 	priority = randint(1, 5)
# 	p = Project.objects.create(
# 		projectName =projectName,
# 		description = description,
# 		estimateTime=estimateTime,
# 		startTime=startTime,
# 		finishTime=finishTime,
# 		priority=priority)
# 	p.save()

for j in range(10):
	p = Project.objects.get(projectName= "ProjectTODO" + str(j))
	user = User.objects.all()[0]  # uid ??
	user1 = User.objects.all()[1]
	now = datetime.datetime.now()
	time = now.date
	progress1 = 0. 
	progress2 = 0.
	p1 = Progress.objects.create(
		user=user,
		project=p,
		time=time,
		progress=progress1)
	p2 = Progress.objects.create(
		user=user1,
		project=p,
		time=time,
		progress=progress2)
	p1.save()
	p2.save()