import sqlite3

class News():

    def __init__(self,Pos_ID_1,Pos_ID_2,title,section,section_link,date,read_num,link,picture,size):
        self.Pos_ID_1 = Pos_ID_1
        self.Pos_ID_2 = Pos_ID_2
        self.title = title
        self.section = section
        self.section_link = section_link
        self.date = date
        self.read_num = read_num
        self.link = link
        self.picture = picture
        self.size = size


    def text_of_mail(self):

        width_height = ""
        pic_width_height = ""
        headline_font_size = ""
        headline_width = ""

        if (self.size == "big"):
            width_height = "width: 350px; height: 450px;"
            pic_width_height = """width='350' height='300'"""
            headline_font_size = "font-size: 1.2rem;"
            headline_width = "width: 325px;"
        elif (self.size == "medium"):
            width_height = "width: 500px; height: 390px;"
            pic_width_height = """width='500' height='270'"""
            headline_font_size = "font-size: 1.4rem;"
            headline_width = "width: 485px;"
        elif (self.size == "small"):
            width_height = "width: 230px; height: 430px;"
            pic_width_height = """width='230' height='230'"""
            headline_font_size = "font-size: 1.1rem;"
            headline_width = "width: 200px;"

        return """
        <!DOCTYPE html>
		<html>
		<head>
			<title></title>
			<meta charset="utf-8">
			<style type="text/css">
			</style>
		</head>
		<body>

			<div id="main-div" style='""" + width_height + """ background-color: rgb(237, 237, 237); background-color: #fff; border: 3px solid grey;'>
				<div id="content-picture">
					<a href='""" + self.link + """'><img src='""" + self.picture + """' """ + pic_width_height + """ ></a>
					
				</div>

				<div id="content" style="margin-left: 14px;">
					<div id="content-meta" style="margin-top: 10px; color: #c3c1c1;">
						<a href='""" + self.section_link + """' style="text-decoration: none; color: #c3c1c1;">
							<span id="genre">
								""" + self.section + """
							</span>
						</a>
						

						<span id="read-num" style="float: right; margin-right: 14px;">
							""" + self.read_num + " Okuma" + """
						</span>
					</div>

					<div id="headline" style="font-family: 'Open Sans',sans-serif; """ + headline_font_size + " " + headline_width + """ line-height: 1.5; color: #333; margin-top: 12px;">
						<a href='""" + self.link + """' style="text-decoration:none;">
							<span id="title" style="color: black;">
								""" + self.title + """
							</span>
						</a>
					</div>
				</div>

			</div>


		</body>
		</html>
        """


class Database_Post():

    def __init__(self):

        self.connect_database()

    def connect_database(self):

        self.connection = sqlite3.connect("Eksi Seyler.db")
        self.cursor = self.connection.cursor()

        query = "create table if not exists " \
                "Tbl_Posts (" \
                "Pos_ID_1 text," \
                "Pos_ID_2 text," \
                "Title text," \
                "Section text," \
                "Date text," \
                "Read_Num text," \
                "Link text)"
        self.cursor.execute(query)
        self.connection.commit()

    def check_if_post_exists(self,id_1 = "", id_2 = "", link = ""):

        select_ID = ""
        var_value = ""

        if (len(id_1) != 0):
            select_ID = "Pos_ID_1"
            var_value = id_1
        elif (len(id_2) != 0):
            select_ID = "Pos_ID_2"
            var_value = id_2
        elif (len(link) != 0):
            select_ID = "Link"
            var_value = link

        query = "select * from Tbl_Posts where " + select_ID + " = @p1"
        self.cursor.execute(query,(var_value,))
        posts = self.cursor.fetchall()

        if (len(posts) == 0):
            return 0

        else:
            return 1

    def add_post(self,News):

        query = "insert into Tbl_Posts values (@p1,@p2,@p3,@p4,@p5,@p6,@p7)"
        self.cursor.execute(query,(News.Pos_ID_1,News.Pos_ID_2,News.title,News.section,News.date,News.read_num,News.link))
        self.connection.commit()



import sqlite3

class News():

    def __init__(self,Pos_ID_1,Pos_ID_2,title,section,section_link,date,read_num,link,picture,size):
        self.Pos_ID_1 = Pos_ID_1
        self.Pos_ID_2 = Pos_ID_2
        self.title = title
        self.section = section
        self.section_link = section_link
        self.date = date
        self.read_num = read_num
        self.link = link
        self.picture = picture
        self.size = size


    def text_of_mail(self):

        width_height = ""
        pic_width_height = ""
        headline_font_size = ""
        headline_width = ""

        if (self.size == "big"):
            width_height = "width: 350px; height: 450px;"
            pic_width_height = """width='350' height='300'"""
            headline_font_size = "font-size: 1.2rem;"
            headline_width = "width: 325px;"
        elif (self.size == "medium"):
            width_height = "width: 500px; height: 390px;"
            pic_width_height = """width='500' height='270'"""
            headline_font_size = "font-size: 1.4rem;"
            headline_width = "width: 485px;"
        elif (self.size == "small"):
            width_height = "width: 230px; height: 430px;"
            pic_width_height = """width='230' height='230'"""
            headline_font_size = "font-size: 1.1rem;"
            headline_width = "width: 200px;"

        return """
        <!DOCTYPE html>
		<html>
		<head>
			<title></title>
			<meta charset="utf-8">
			<style type="text/css">
			</style>
		</head>
		<body>

			<div id="main-div" style='""" + width_height + """ background-color: rgb(237, 237, 237); background-color: #fff; border: 3px solid grey;'>
				<div id="content-picture">
					<a href='""" + self.link + """'><img src='""" + self.picture + """' """ + pic_width_height + """ ></a>
					
				</div>

				<div id="content" style="margin-left: 14px;">
					<div id="content-meta" style="margin-top: 10px; color: #c3c1c1;">
						<a href='""" + self.section_link + """' style="text-decoration: none; color: #c3c1c1;">
							<span id="genre">
								""" + self.section + """
							</span>
						</a>
						

						<span id="read-num" style="float: right; margin-right: 14px;">
							""" + self.read_num + " Okuma" + """
						</span>
					</div>

					<div id="headline" style="font-family: 'Open Sans',sans-serif; """ + headline_font_size + " " + headline_width + """ line-height: 1.5; color: #333; margin-top: 12px;">
						<a href='""" + self.link + """' style="text-decoration:none;">
							<span id="title" style="color: black;">
								""" + self.title + """
							</span>
						</a>
					</div>
				</div>

			</div>


		</body>
		</html>
        """


class Database_Post():

    def __init__(self):

        self.connect_database()

    def connect_database(self):

        self.connection = sqlite3.connect("Eksi Seyler.db")
        self.cursor = self.connection.cursor()

        query = "create table if not exists " \
                "Tbl_Posts (" \
                "Pos_ID_1 text," \
                "Pos_ID_2 text," \
                "Title text," \
                "Section text," \
                "Date text," \
                "Read_Num text," \
                "Link text)"
        self.cursor.execute(query)
        self.connection.commit()

    def check_if_post_exists(self,id_1 = "", id_2 = "", link = ""):

        select_ID = ""
        var_value = ""

        if (len(id_1) != 0):
            select_ID = "Pos_ID_1"
            var_value = id_1
        elif (len(id_2) != 0):
            select_ID = "Pos_ID_2"
            var_value = id_2
        elif (len(link) != 0):
            select_ID = "Link"
            var_value = link

        query = "select * from Tbl_Posts where " + select_ID + " = '" + var_value + "'"
        #print(query)
        self.cursor.execute(query)
        posts = self.cursor.fetchall()

        if (len(posts) == 0):
            return 0

        else:
            return 1

    def add_post(self,News):

        query = "insert into Tbl_Posts values (@p1,@p2,@p3,@p4,@p5,@p6,@p7)"
        self.cursor.execute(query,(News.Pos_ID_1,News.Pos_ID_2,News.title,News.section,News.date,News.read_num,News.link))
        self.connection.commit()
