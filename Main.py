import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sys

import News_Database
import User_Database
import Inform_User


News = News_Database.Database_Post()
Mail = User_Database.Database_User()

#print("""
#Enter '1' to organize user database.
#Enter '2' to start the program.
#Enter 'q' to exit program.
#""")

while True:

	#number = input("Command: ")

	if (sys.argv[1] == "1"):

		print("""
		Enter '1' to see all users.
		Enter '2' to add a new user.
		Enter '3' to delete a user.
		Enter '4' to update a user.
		Enter '5' to see total number of users.
		Enter '6' to go back to main menu.
		Enter 'q' to exit the program.
		""")

		while True:

			command = input("\nCommand for mail: ")

			if (command == "1"):
				Mail.show_mails()

			elif (command == "2"):
				print("Enter a new mail address:")
				new_mail = input().lower()

				if (Mail.check_if_mail_exists(new_mail)):
					print("\n" + new_mail, "already exists on database. Please try again.\n")
					continue

				print("Would you want to receive mails? (Y/N):")
				user_stat = input().upper()

				if (user_stat == "Y"):
					user_stat = True
					text = new_mail + " successfully added to database."

				elif (user_stat == "N"):
					user_stat = False
					text = new_mail + " successfully added to database. Be aware that you wont receive any mails."

				else:
					print("\nInvalid command. Try again.\n")
					continue

				new_user = User_Database.User(new_mail, user_stat)
				Mail.add_mail(new_user)

				print(text)


			elif (command == "3"):

				if (Mail.total_user() == 0):
					print("\nNo user found on database.\n")
					continue

				print("Enter the mail address you want to delete:")
				del_mail = input("Mail: ")

				if (Mail.check_if_mail_exists(del_mail) == 0):
					print("There is not such mail address as " + del_mail + ". Please try again")
					continue

				print("Are you sure you want to delete " + del_mail + "? (Y/N):")
				yes_no = input().upper()

				if (yes_no == "Y"):
					Mail.delete_mail(del_mail)
					print(del_mail, " successfully deleted from database.")

				elif (yes_no == "N"):
					print("Process canceled.")
					continue
				else:
					print("\nInvalid command. Please try again.")


			elif (command == "4"):

				if (Mail.total_user() == 0):
					print("\nNo user found on database.\n")
					continue

				print("Enter the mail address you want to update: ")
				update_mail = input()

				if (Mail.check_if_mail_exists(update_mail) == 0):
					print("There is not such mail address as " + update_mail + ". Please try again")
					continue

				print("What would you want to change? "
					  "To go back, enter 'q' , to change mail, "
					  "enter M, to change status, enter S:")

				change_what = input().upper()

				# Updating User Mail
				if (change_what == "M"):
					new_mail = input("Enter a new mail address: ")
					Mail.update_mail(update_mail, new_mail)
					print(update_mail, "changed to", new_mail + ".")

				# Updating Status (if 0, wont receive mails, else will)
				elif (change_what == "S"):
					print("Would you want to get mails or not? (Y/N)")
					yes_no = input().upper()
					if (yes_no == "Y"):
						Mail.update_stat(update_mail, True)
						print(update_mail, "will now receive mails.")
					elif (yes_no == "N"):
						Mail.update_stat(update_mail, False)
						print(update_mail, "will not receive mails anymore.")
					else:
						print("Wrong command. Please try again.")
						continue

				elif (change_what == "Q"):
					print("You are back to menu.")

				else:
					print("\nInvalid comamnd. Try again.\n")


			elif (command == "5"):

				total = Mail.total_user()

				if (total != 0):
					print("Total number of users: ", total)
				else:
					print("No user found on database.")

			elif (command == "6"):
				# Going Back to Main Menu
				print("\nYou are on main menu right now.\n")
				break

			elif (command == "q"):
				exit()

			else:
				print("Invalid command. Try again.")


	elif (sys.argv[1] == "2"):

		while True:

			new_posts = 0

			right_now = datetime.now()
			day = datetime.today().day
			month = datetime.today().month
			year = datetime.today().year

			month_in_turkish = {'1':'Ocak', '2':'Şubat', '3':'Mart', '4':'Nisan', '5':'Mayıs', '6':'Haziran', '7':'Temmuz', '8':'Ağustos', '9':'Eylül', '10':'Ekim', '11':'Kasım', '12':'Aralık'}

			todays_date = str(day) + " " + str(month_in_turkish[str(month)]) + " " + str(year)

			# Checking if there are any users on database
			if (Mail.total_user() == 0):

				print("No user found on database. You have to add at least one user to continue.")
				user_mail = input("Mail: ").lower()
				print("Would you want to receive mails?")
				print("(If you are running this program for the first time, \nwe recommend "
					  "turning notifications off if you don't\nwant get several mails"
					  " in your first run.\nAfter the first run, the posts will be added to database"
					  " and you can turn notifications on.)")

				stat = input("Y/N: ").upper()

				# Checking Stat
				if (stat == "Y"):
					stat = True
				elif (stat == "N"):
					stat = False
				else:
					print("\nWrong command. Try again.\n")
					continue

				user_info = User_Database.User(user_mail, stat)

				# Adding user to database
				Mail.add_mail(user_info)

				print(user_mail, "successfully added to database.")


			html_content = ""
			try:
				url = "https://seyler.eksisozluk.com/"
				headers = {
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				response = requests.get(url, headers=headers)
				html_content = response.content

			except:
				print("Something unexpected happened. Time: " + str(datetime.strftime(datetime.now(), "%X")))
				time.sleep(180)

			soup = BeautifulSoup(html_content, "html.parser")
			item_html = soup.find_all("div", {"class": "col-flex"})

			html_content = """"""

			for i in item_html:
				html_content += str(i) + "\n"

			soup = BeautifulSoup(html_content, "html.parser")

			link_html = soup.find_all("a")
			text_html = soup.find_all("span", {"class": "hero-headline"})
			images_html = soup.find_all("img", {"class": "hero-img"})

			links = []
			headlines = []
			images = []
			Pos_ID_1 = []

			for i in link_html:
				links.append(i['href'])

			for i in text_html:
				headlines.append(
					str(i.text).replace("\n", "").replace("                  ", "").replace("                ", ""))

			for i in images_html:
				i = str(i['style']).replace("background-image: url('", "").replace("')", "")
				images.append(i)
				ID = i.replace("https://seyler.ekstat.com", "")
				ID = ID.replace("/img/230/", "")
				ID = ID.replace("/img/max/800/", "")
				ID = ID.replace("/img/480/", "")
				ID = ID[19:]
				ID = ID[:-4]
				Pos_ID_1.append(ID)


			for ID, link, headline, image in zip(Pos_ID_1, links, headlines, images):
				url = link
				headers = {
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				response = requests.get(url, headers=headers)
				html_content = response.content
				soup = BeautifulSoup(html_content, "html.parser")

				try:
					cover_img_html = soup.find("div", {"class": "cover-img"})
					cover_img = cover_img_html.img['data-src']
				except:
					cover_img_html = soup.find("div", {"class": "medium-insert-images ui-sortable"})
					cover_img = cover_img_html.img['src']

				cover_img = cover_img.replace("https://seyler.ekstat.com","")
				cover_img = cover_img.replace("/img/max/800/","")
				cover_img = cover_img.replace("/img/230/","")
				cover_img = cover_img.replace("/img/480/","")

				cover_img = cover_img[19:]
				cover_img = cover_img[:-4]

				ID_2 = cover_img

				if (ID_2 == ''):
					ID_2 = 'No Value'

				date_html = soup.find("span", {"class": "meta-date"})
				date = str(date_html.get_text())
				date = date.replace("        ", "").replace("\n", "").replace("\r", "").replace("      ","")
				date_sql = date

				if (todays_date == date and (not News.check_if_post_exists(id_1 = ID) and not News.check_if_post_exists(id_2 = ID_2) and not News.check_if_post_exists(link = link))):
					read_num_html = soup.find("b")
					read_num = read_num_html.get_text()

					genre_html = soup.find("div", {"class": "col-xs-5 meta-category"})

					genre_link = "https://seyler.eksisozluk.com" + str(genre_html.a.get('href'))
					genre = genre_html.a.get_text().replace("\n", "").replace("        ", "")

					size = "big"

					Post = News_Database.News(ID,ID_2,headline,genre,genre_link,date_sql,read_num,link,image,size)
					News.add_post(Post)

					mail_list = Mail.get_mails()

					text_mail = Post.text_of_mail()

					new_posts += 1

					for user in mail_list:
						Inform_User.send_mail(user[0],text_mail)

			try:
				url = "https://seyler.eksisozluk.com/"
				headers = {
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				response = requests.get(url, headers=headers)
				html_content = response.content

			except:
				print("Something unexpected happened. Time: " + str(datetime.strftime(datetime.now(), "%X")))
				time.sleep(180)

			soup = BeautifulSoup(html_content, "html.parser")
			item_html = soup.find_all("div", {"class": "col-md-8"})

			html_content = """"""

			for i in item_html:
				html_content += str(i) + "\n"

			soup = BeautifulSoup(html_content, "html.parser")

			small_items_html = soup.find_all("div",{"class":"col-sm-4"})
			medium_item_html = soup.find("div",{"class":"col-sm-8"})

			small_item_read_num_html = soup.find_all("span",{"class":"meta-stats"})
			small_item_headline_html = soup.find_all("div",{"class":"content-title"})

			small_links = []
			small_headlines = []
			small_genres = []
			small_genre_links = []
			small_read_num = []
			small_images = []
			small_ID = []

			medium_link = ""
			medium_headline = ""
			medium_genre = ""
			medium_genre_link = ""
			medium_read_num = ""
			medium_image = ""
			medium_ID = ""

			for i,j in zip(small_items_html,range(4)):
				small_links.append(i.a['href'])
				small_genre_links.append("https://seyler.eksisozluk.com" + str(i.span.a['href']))
				small_genres.append(str(i.span.text).replace("\n", "").replace("        ", "").replace("  ",""))
				small_images.append(i.img['data-src'])

				img = str(i.img['data-src'])

				ID = img.replace("https://seyler.ekstat.com", "")
				ID = ID.replace("/img/230/","")
				ID = ID.replace("/max/800/","")
				ID = ID.replace("/img/480/","")
				ID = ID[19:]
				ID = ID[:-4]

				small_ID.append(ID)


			for i,j in zip(small_item_read_num_html,range(5)):
				text = (str(i.text).replace("      ","").replace("\r","").replace("\n","").replace("    ",""))
				small_read_num.append(text)

			medium_read_num = small_read_num[1]

			small_read_num.__delitem__(1)

			for i,j in zip(small_item_headline_html,range(5)):
				small_headlines.append(str(i.text).replace("\r","").replace("\n","").replace("      ","").replace("    ",""))

			medium_headline = small_headlines[1]

			small_headlines.__delitem__(1)

			for ID, link, headline, genre, genre_link, read_num, image in zip(small_ID, small_links, small_headlines, small_genres, small_genre_links, small_read_num, small_images):

				url = link
				headers = {
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				response = requests.get(url, headers=headers)
				html_content = response.content
				soup = BeautifulSoup(html_content, "html.parser")

				cover_img = ""

				try:
					cover_img_html = soup.find("div", {"class": "cover-img"})
					cover_img = cover_img_html.img['data-src']
				except:
					try:
						cover_img_html = soup.find("div", {"class": "medium-insert-images ui-sortable"})
						cover_img = cover_img_html.img['src']
					except:
						pass

					




				cover_img = cover_img.replace("https://seyler.ekstat.com", "")
				cover_img = cover_img.replace("/img/max/800/", "")
				cover_img = cover_img.replace("/img/230/", "")
				cover_img = cover_img.replace("/img/480/", "")

				cover_img = cover_img[19:]
				cover_img = cover_img[:-4]


				ID_2 = cover_img

				date_html = soup.find("span", {"class": "meta-date"})
				date = str(date_html.get_text())
				date = date.replace("        ", "").replace("\n", "").replace("\r", "").replace("      ","")
				date_sql = date

				if (ID_2 == ''):
					ID_2 = 'No Value'

				#print("link = " + str(link))
				#print("ID:" + ID + " ID2: " + ID_2 + "Link: " + link + "\n")

				if (todays_date == date and (not News.check_if_post_exists(id_1 = ID) and not News.check_if_post_exists(id_2 = ID_2) and not News.check_if_post_exists(link = link))):

					size = "small"

					Post = News_Database.News(ID, ID_2, headline, genre, genre_link, date_sql, read_num, link, image, size)
					News.add_post(Post)

					mail_list = Mail.get_mails()

					text_mail = Post.text_of_mail()

					new_posts += 1

					for user in mail_list:
						Inform_User.send_mail(user[0], text_mail)



			medium_link = medium_item_html.a['href']
			medium_genre = str(medium_item_html.span.text).replace("\n", "").replace("        ", "").replace("  ","")
			try:
				medium_genre_link = "https://seyler.eksisozluk.com" + str(medium_item_html.span.a['href'])
			except Exception as e:
				medium_genre_link = "#"
			
			medium_image = medium_item_html.img['data-src']

			ID = medium_image.replace("https://seyler.ekstat.com", "")
			ID = ID.replace("/img/max/800/","")
			ID = ID.replace("/img/230/","")
			ID = ID.replace("/img/480/","")
			ID = ID[19:]
			ID = ID[:-4]
			medium_ID = ID


			url = medium_link
			headers = {
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			try:

				response = requests.get(url, headers=headers)
				html_content = response.content
			except:
				print("Something unexpected happened. Time: " + str(datetime.strftime(datetime.now(), "%X")))
				time.sleep(180)


			soup = BeautifulSoup(html_content, "html.parser")

			
			try:
					cover_img_html = soup.find("div", {"class": "cover-img"})
					cover_img = cover_img_html.img['data-src']
			except:
					cover_img_html = soup.find("div", {"class": "medium-insert-images ui-sortable"})
					cover_img = cover_img_html.img['src']

			cover_img = cover_img.replace("https://seyler.ekstat.com", "")
			cover_img = cover_img.replace("/img/max/800/", "")
			cover_img = cover_img.replace("/img/230/", "")
			cover_img = cover_img.replace("/img/480/", "")

			cover_img = cover_img[19:]
			cover_img = cover_img[:-4]

			ID_2 = cover_img

			if (ID_2 == ''):
				ID_2 = 'No Value'

			date_html = soup.find("span", {"class": "meta-date"})
			date = str(date_html.get_text())
			date = date.replace("        ", "").replace("\n", "").replace("\r", "").replace("      ","")
			date_sql = date


			if (todays_date == date and (not News.check_if_post_exists(id_1 = ID) and not News.check_if_post_exists(id_2 = ID_2) and not News.check_if_post_exists(link = medium_link))):

				size = "medium"

				Post = News_Database.News(ID, ID_2, medium_headline, medium_genre, medium_genre_link, date_sql, medium_read_num, medium_link, medium_image, size)
				News.add_post(Post)

				mail_list = Mail.get_mails()

				text_mail = Post.text_of_mail()

				new_posts += 1

				for user in mail_list:
					Inform_User.send_mail(user[0], text_mail)


			output = ""

			if (new_posts == 0):
				output = "No new post released. Waiting for 3 min. Time: " + str(datetime.strftime(datetime.now(), "%X"))
			else:
				output = "0" + str(new_posts) + " new post released. Waiting for 3 min. Time: " + str(datetime.strftime(datetime.now(), "%X"))

			print(output)
			time.sleep(180)


	else:
		print("Invalid command. Try again.")
		exit()
