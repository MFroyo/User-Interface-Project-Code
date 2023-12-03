import pandas
import matplotlib.pyplot as plt
import numpy as np

sites = np.array(["1", "2", "3", "4"])
#Overall ratings per webpage
ratings = np.array([8 , 36, 43, 33])
#Time to navigate webpages

fig, ax = plt.subplots()

bar_container = ax.bar(sites, ratings)
ax.set_ylabel("Rating Score (Each Person Rating Out of 10)")
ax.set_xlabel("Site Number")
ax.set_title("Different Site Design Overall Ratings")
ax.bar_label(bar_container, fmt='{:,.0f}')
ax.set_xticklabels(('1', '2', '3', '4'))

plt.show()


# Task Time Frames on Test Site
task1_time = np.array([8.44, 12.53, 9.91, 15.27, 19.12])
task2_time = np.array([10.14, 11.07, 8.13, 14.76, 16.41])
task3_time = np.array([9.54, 9.98, 10.13, 12.67, 11.85])
task4_time = np.array([11.31, 12.75, 11.27, 14.61, 13.51])
task5_time = np.array([10.63, 10.12, 9.81, 11.23, 11.90])

user_1_meantimes = (task1_time[0] + task2_time[0] + task3_time[0] + task4_time[0] + task5_time[0])
user_2_meantimes = (task1_time[1] + task2_time[1] + task3_time[1] + task4_time[1] + task5_time[1])
user_3_meantimes = (task1_time[2] + task2_time[2] + task3_time[2] + task4_time[2] + task5_time[2])
user_4_meantimes = (task1_time[3] + task2_time[3] + task3_time[3] + task4_time[3] + task5_time[3])
user_5_meantimes = (task1_time[4] + task2_time[4] + task3_time[4] + task4_time[4] + task5_time[4])

overall_meantime = (user_1_meantimes + user_2_meantimes + user_3_meantimes + user_4_meantimes + user_5_meantimes)/25
overall_tests = ([8.44, 12.53, 9.91, 15.27, 19.12, 10.14, 11.07, 8.13, 14.76, 16.41, 9.54, 9.98, 10.13, 12.67, 11.85, 11.31, 12.75, 11.27, 14.61, 13.51, 10.63, 10.12, 9.81, 11.23, 11.90])
overall_sd = np.std(overall_tests)
print("Overall Meantime: ", overall_meantime, " SD:", overall_sd)

user_1_meantimes = user_1_meantimes/5
user_2_meantimes = user_2_meantimes/5
user_3_meantimes = user_3_meantimes/5
user_4_meantimes = user_4_meantimes/5
user_5_meantimes = user_5_meantimes/5

user1_times = np.array([8.44, 10.14, 9.54, 11.31, 10.63])
user2_times = np.array([12.53, 11.07, 9.98, 12.75, 10.12])
user3_times = np.array([9.91, 8.13, 10.13, 12.75, 10.12])
user4_times = np.array([15.27, 14.76, 12.67, 14.61,11.23])
user5_times = np.array([19.12, 16.41, 11.85, 13.51, 11.90])

user1_sd = np.std(user1_times)
user2_sd = np.std(user2_times)
user3_sd = np.std(user3_times)
user4_sd = np.std(user4_times)
user5_sd = np.std(user5_times)

print("User 1 Mean Time: ",user_1_meantimes, " SD:", user1_sd)
print("User 2 Mean Time: ",user_2_meantimes, " SD:", user2_sd)
print("User 3 Mean Time: ",user_3_meantimes, " SD:", user3_sd)
print("User 4 Mean Time: ",user_4_meantimes, " SD:", user4_sd)
print("User 5 Mean Time: ",user_5_meantimes, " SD:", user5_sd)

tasks = np.array([1, 2, 3, 4, 5])

fig, ax = plt.subplots()
ax.plot(tasks, user1_times)
ax.plot(tasks, user2_times)
ax.plot(tasks, user3_times)
ax.plot(tasks, user4_times)
ax.plot(tasks, user5_times)

ax.set_xlabel("Tasks")
ax.set_ylabel("Time in Seconds")
ax.set_title("Time Per Task Per Person")

plt.show()
#Who is okay with switching to 2 click login

data = [user1_times, user2_times, user3_times, user4_times, user5_times]

fig, ax = plt.subplots()

ax.boxplot(data)

ax.set_xlabel("User")
ax.set_ylabel("Time Variance in Tasks")
ax.set_title("Variance of User's Task Times")

plt.show()

yes_no = [3, 2]
names = 'Yes','No'
explode = (0, 0.1)
fig, ax = plt.subplots()
ax.set_title("Poll of Switching to 2 Click Login")
ax.pie(yes_no, explode=explode, labels = names, autopct='%1.1f%%', shadow=True, startangle=90)