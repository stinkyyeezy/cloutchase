from selenium import webdriver
import os
import datetime as dt
import time
from selenium.webdriver.common.keys import Keys
import random
import re
import csv
import pandas as pd
import matplotlib
from selenium.webdriver import ActionChains
from itertools import chain
z = " "
followers = []
following = []
following_followers_difference = []
past_5_post_likes = []


driver = webdriver.Chrome(r"C:\Users\justi\AppData\Local\Programs\Python\Python38\Lib\site-packages\chromedriver\chromedriver.exe")
driver.get("https://www.instagram.com/")

# fill in your details here 😎:
username = "default_username"
password = "default_password"

#WhiteList:
celebritystatus = []

#un # here 
if username == "default_username" and password == "default_password":
   print("Please fill in your details to proceed:")
   username = input("Type in your username: ")
   password = input("Type in your password: ")

user_url = str("https://www.instagram.com/" + username)
followers_page = str(user_url + '/followers/')

time.sleep(5)

try:
	driver.find_element_by_class_name('f0n8F').send_keys(username)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
	time.sleep(5)
except:
	time.sleep(5)
print("Hello " + str(username) +"!")
print("Finding Followers")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
driver.get(user_url)
time.sleep(2)

follower_count1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').text

try:
	re.search("K", follower_count1)
	follower_count_intermediate = follower_count1.replace('K', '000')
	follower_count2 = follower_count_intermediate[:-9]
	follower_scroll_number_generator = int(following_count2)

except:
	try:
		follower_count_intermediate = follower_count1.replace(',', '')
	except:
		follower_count_intermediate = follower_count1

	follower_count2 = follower_count_intermediate[:-9]

	follower_scroll_number_generator = ((int(follower_count2)-24-12-12)/6)+25

time.sleep(3)
          
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()          

time.sleep(10)
fBody  = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
scroll = 0
while scroll < int(follower_scroll_number_generator): # scroll 5 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(2)
    scroll += 1
time.sleep(2)
link_0 = fBody.find_elements_by_class_name('d7ByH')
pre_followers = [name.text for name in link_0 if name.text != '']
celebritytxt = str("\nVerified")
for pre_follower in pre_followers:
	if re.search(str("\nVerified"), str(pre_follower)):
		celebritystatus.append(pre_follower)
for pre_follower in pre_followers:
	if pre_follower not in celebritystatus:
		followers.append(pre_follower)
#print("Your Followers:")
#print(followers)
#print(z)
print("Number of Followers:")
print(len(followers))
print(z)
print("Finding people you follow!")
driver.get(user_url)
time.sleep(3)
following_page = str(user_url + '/following/')
following_count1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').text
try:
	re.search("K", following_count1)
	following_count_intermediate = following_count1.replace('K', '000')
	following_count2 = following_count_intermediate[:-9]
	following_scroll_number_generator = int(following_count2)

except: 
	try:
		following_count_intermediate = following_count1.replace(',', '')
	except:
		following_count_intermediate = following_count1

	following_count2 = following_count_intermediate[:-10]
	following_scroll_number_generator = ((int(following_count2)-24-12-12)/6)+25
time.sleep(5)


driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(5)
fwBody  = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
scroll = 0
while scroll < int(following_scroll_number_generator): # scroll 5 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fwBody)
    time.sleep(2)
    scroll += 1
celebrities = []
time.sleep(2)
link_1 = fwBody.find_elements_by_class_name('d7ByH')
pre_following = [name.text for name in link_1 if name.text != '']
for pre_followings in pre_following:
	if re.search(str("\nVerified"), str(pre_followings)):
		celebritystatus.append(pre_followings)
for pre_followings in pre_following:
	if pre_followings not in celebritystatus:
		following.append(pre_followings)
for celebrity in celebritystatus:
	celebrities.append(celebrity[:-9])
#print("People you follow:")
#print(following)
#print(z)
print("Number of People you follow:")
print(len(following))
print(z)
print("Verified Accounts you follow:")
print(celebrities)
print(z)
print("Number of Verified Accounts you follow")
print(len(celebrities))
print(z)
print("Calculating Most Recent Likes!")
#un # here 
driver.get(user_url)
#click_storage first 9

video_count = 0
post_count = 0
pre_users_that_liked = []
#for block in post_block[post_count:post_count + 5]:
#href_generator

elems = driver.find_elements_by_class_name("v1Nh3 kIKUG  _bz0w")
links = [elem.get_attribute('href') for elem in elems]

txt = "views"

time.sleep(1)
users_that_liked = []
time.sleep(3)
try:
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div').click()
except:
	driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]').click()
time.sleep(3)
try:
	phrase = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/span').text
	re.search("views", phrase)
	time.sleep(1.5)
	video_count += 1
	driver.get(user_url)
	print("This is a video, like count unavailable")
	print()
	time.sleep(1)
except:
	time.sleep(2)
	total_likes_1 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]').text
	try:
		total_likes_intermediate = total_likes_1.replace(',', '')
	except:
		total_likes_intermediate = following_count1
	total_likes_2 = total_likes_intermediate.split()

	like_counter = int(total_likes_2[4]) + 1
	like_scroll_number_generator = ((like_counter - 24 - 12 -12)/6) + 10
	post_count += 1
	driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button').click() 
	time.sleep(2)
	likeBody = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div")
	scroll_like = 0
	time.sleep(1)


	height = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div").value_of_css_property("padding-top")
	match = False
	while match==False:
		lastHeight = height
		elements = driver.find_elements_by_xpath("//*[@id]/div/a")
		for element in elements:
			if element.get_attribute('title') not in users_that_liked:
				users_that_liked.append(element.get_attribute('title'))
		driver.execute_script("return arguments[0].scrollIntoView();", elements[-1])
		time.sleep(1)
		height = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div").value_of_css_property("padding-top")
		if lastHeight==height:
			match = True
	print("People who liked your most recent post:")			
	print(users_that_liked)
	print(z)
	print("Your most recent likes:")
	print(len(users_that_liked))
	print(z)

	
#link_users = likeBody.find_elements_by_tag_name('a')
#pre_users_that_liked = [link_user.text for link_user in link_users if link_user.text != '']	

snakes1 = []
print("loop complete")
driver.get(user_url)
print("Calculating Snakes!")
users_whom_you_follow_but_do_not_follow_back = []
for following_ in following:
	if following_ not in followers:
		snakes1.append(following_)
for snakes_ in snakes1:
	if snakes_ not in celebritystatus:
		users_whom_you_follow_but_do_not_follow_back.append(snakes_)

#print("Snakes:")
#print(users_whom_you_follow_but_do_not_follow_back)
print("Number of Snakes:")
print(len(users_whom_you_follow_but_do_not_follow_back))
you_a_snake_to_these_people = []
for peeps in followers:
	if peeps not in following:
		you_a_snake_to_these_people.append(peeps)
peeps_urls = []
for peep in you_a_snake_to_these_people:
	peeps_urls.append("https://www.instagram.com/" + str(peep) +"/")
peep_dict = {"Peeps": peeps_urls}
peep_df = pd.DataFrame.from_dict(peep_dict, orient="index")
final_peep_df = peep_df.transpose()
snake_urls = []
for snake in users_whom_you_follow_but_do_not_follow_back:
	snake_urls.append("https://www.instagram.com/" + str(snake) +"/")
snake_dict = {"Snakes": snake_urls}
snake_df = pd.DataFrame.from_dict(snake_dict, orient="index")
final_snake_df = snake_df.transpose()

print(z)
print("Your Summary:")
print("followers: " + str(len(followers)))
print("following: " + str(len(following)))
print("snakes: " + str(len(users_whom_you_follow_but_do_not_follow_back)))
print("You are a snake to:" + str(len(you_a_snake_to_these_people)))
print("Fs/Fw Ratio: " + str(len(followers)/len(following)))
follower_counter = [str(len(followers))]
following_counter = [str(len(followers))]
snake_count = [str(len(users_whom_you_follow_but_do_not_follow_back))]
Lastpost = []
R_E_Ratio  = []
Fs_Fw_Ratio = [str(len(followers)/len(following))]
try:
	R_E_Ratio.append(int(len(users_that_liked))/int(len(followers)))
except:
	R_E_Ratio.append("NULL")

if video_count > 1:
	Lastpost.append("Video")
else:
	Lastpost.append("Photo")
dataframe = [followers, following, users_whom_you_follow_but_do_not_follow_back, follower_counter, following_counter, snake_count, Lastpost, Fs_Fw_Ratio]
dict_dataframe = {"Followers": followers, "Following": following, "Snakes": users_whom_you_follow_but_do_not_follow_back, "You a snake to these people": you_a_snake_to_these_people, "Flwer Count": follower_counter, "Flwing Count": following_counter, "Snake Count": snake_count, "Lastpost": Lastpost, "Fs/Fw Ratio": Fs_Fw_Ratio, "R/E": R_E_Ratio}
filename = "cloutchase" + str(dt.datetime) + str(".csv")
df = pd.DataFrame.from_dict(dict_dataframe, orient="index")
finaldf = df.transpose()
finaldf.to_csv("CloutChase", header=True, index = True)
final_snake_df.to_csv("Snakes", header=True, index = True)
final_peep_df.to_csv("Follow these", header=True, index = True)
print(finaldf)
print(final_snake_df)
print(final_peep_df)
print("Data Saved to CSV files!!!")
print("Process Complete")