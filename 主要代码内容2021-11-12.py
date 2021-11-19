# -*- coding: UTF-8 -*-
"""
@Project    ：版本一（2021-10-23） 
@File       ：主要代码内容2021-11-12.py
@Author     ：Cricy
@Description：-
@Date       ：2021/11/12 20:18 
@URL        ：-
"""
import pymysql
# 使用People学生列表，Class课程列表，Score成绩列表，PerScore品行成绩列表，GenIn综合信息
# tem n
dic_semester = {'第一学期': 0, '第二学期': 1, '第三学期': 2, '第四学期': 3, '第五学期': 4, '第六学期': 5, '第七学期': 6, '第八学期': 7}
dicinfy = {'单项奖学金': 1, '三等奖学金': 2, '二等奖学金': 3, '一等奖学金': 4, '特等讲学金': 5, '校长讲学金': 6, '校级优秀个人': 3, '省级优秀个人': 6,
           '国家优秀个人': 12, '参加奖': 1, '省级三等奖': 4, '省级二等奖': 5, '省级一等奖': 6, '国家级三等奖': 6, '国家级二等奖': 9, '国家级一等奖': 12,
           '校级三等奖': 1, '校级二等奖': 2, '校级一等奖': 3}
dicinfn = {'学校通报批评': 1, '校级警告': 2, '严重警告': 3, '记过': 4, '记大过': 5, '开除学籍留校察看': 6}


def Sort1(elem):
	return elem[3]


# 对学号排序
def Sort2(elem):
	tem1 = 0
	for i in range(1, len(elem)):
		tem1 += elem[i]
	return -tem1


def Sort3(elem):
	tem1 = 0
	for i in range(1, len(elem)):
		tem1 += elem[i]
	return tem1


class People:
	def __init__(self):
		a = []
		num = int(input())
		for i in range(0, num):
			line = input().split()
			a.append(line)
			line = []
		self.list = a
	# 先输入姓名，性别，宿舍号再输入学号，出生年月

	def append_people(self):
		num = int(input())
		for i in range(0, num):
			line = input().split()
			self.list.append(line)
			line = []
	# 先输入姓名，性别，宿舍号再输入学号，出生年月，添加学生
	
	def change_people(self, score, a):
		for i in range(0, len(self.list)):
			if self.list[i][3] == a:
				print(self.list[i])
				tem1 = input().split()
				self.list[i] = tem1
		for i in range(0, len(score.list)):
			if score.list[i][0] == a:
				print(score.list[i])
				score.list[i][0] = tem1[3]
# a是学号的意思
# 以上函数执行后加入数据库，进行数据库的刷新
	
	def people_commit(self):
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("DELETE from student ")
		
		for i in range(len(self.list)):
			c.execute("INSERT INTO student (name,sex,dormitory_id,ID,birth) VALUES ('%s','%s','%s','%s','%s')" % (self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][3], self.list[i][4]))
		conn.commit()
		conn.close()

	def people_print(self):
		conn = pymysql.connect(host='localhost', user='root', password='00000', database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("SELECT *  from student")
		cursor = c.fetchall()
		for row in cursor:
			print('\n')
			print("name = ", row[0])
			print("sex = ", row[1])
			print("dormitory_id = ", row[2])
			print("ID = ", row[3])
			print("birth = ", row[4])
		conn.commit()
		conn.close()

class Classes:
	def __init__(self):
		b = []
		num = int(input())
		for i in range(0, num):
			line = input().split()
			b.append(line)
			line = []
		self.list = b
	
	# 先输入课程号在输入课程类别再输入学期再输入课程名称及学分
	def append_class(self):
		num = int(input())
		for i in range(0, num):
			line = input().split()
			self.list.append(line)
			line = []
	
	# 先输入课程号在输入课程类别再输入学期再输入课程名称及学分，添加课程
	def change_class(self, classnum1, semester):
		for i in range(0, len(self.list)):
			if self.list[i][0] == classnum1 and self.list[i][2] == semester:
				print("请输入新科目")
				self.list[i] = []
				line = input().split()
				self.list[i] = line
	
	# 改变一个课程
	# 以上函数执行后加入数据库，进行数据库的刷新
	def semester_course_list(self):
		temline1 = []
		for i in range(0, 8):
			temline2 = []
			temline2.append(int(0))
			temline1.append(temline2)
		for i in range(0, len(self.list)):
			temline1[dic_semester[self.list[i][2]]].append(int(i))
		self.course_list = temline1
# 统计各个学期的课程情况，输出一个二维数组，8行每一行第一个为0，后来的是第n学期课程的位
	def class_commit(self):
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("DELETE from classes ")
		
		for i in range(len(self.list)):
			c.execute("INSERT INTO classes (course_id,course_must,semester,class_name,credit) VALUES ('%s','%s','%s','%s','%s')" %(self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][3], self.list[i][4]))
		conn.commit()
		conn.close()
	
	def class_print(self):
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("SELECT *  from classes")
		cursor = c.fetchall()
		for row in cursor:
			print('\n')
			print("course_id = ", row[0])
			print("course_must = ", row[1])
			print("semester = ", row[2])
			print("class_name = ", row[3])
			print("credit = ", row[4])
		conn.commit()
		conn.close()


class Score:
	def __init__(self, a, b):
		a.list.sort(key=Sort1)
		temline = []
		# 宋安瑞设置了一个变量 self.classes_num 课程个数
		self.classes_num = len(b.list)
		# 宋安瑞设置了一个列表用来复制 课程类里的self.list 列表
		self.classes_list = b.list
		
		self.list = []
		self.mysql_temp_list = []
		for i in range(0, len(a.list)):
			print(a.list[i])
			temline.append(a.list[i][3])
			for j in range(0, len(b.list)):
				print(b.list[j][3])
				tem1 = int(input())
				temline.append(tem1)
				if tem1 < 60:
					temline.append(-1)
				else:
					temline.append(1)
			self.list.append(temline)
			temline = []

	# 输出一个关于成绩的二维数组每一行代表一个人，第2N-1个数代表该生第一个学科的成绩，第2n个数代表该生是否挂科，-1表示挂了,第0个是学号
	def re_in_score(self, a, b):
		for i in range(0, len(self.list)):
			print(a.list[i])
			for j in range(int(len(self.list[i]) / 2), len(b.list)):
				print(b.list[j][3])
				tem1 = int(input())
				
				self.list[i].append(tem1)
				if tem1 < 60:
					self.list[i].append(-1)
				else:
					self.list[i].append(1)
		for i in range(len(self.list), len(a.list)):
			print(a.list[i])
			temline = []
			temline.append(a.list[i][3])
			for j in range(0, len(b.list)):
				print(b.list[j][3])
				tem1 = int(input())
				temline.append(tem1)
				if tem1 < 60:
					temline.append(-1)
				else:
					temline.append(1)
			self.list.append(temline)
	
	# 输出一个关于成绩的二维数组每一行代表一个人，第2N-1个数代表该生第一个学科的成绩，第2n个数代表该生是否挂科，-1表示挂了,对变化的学生起效,第一个数代表学号
	def change_score(self, people, classes, a, b):
		for i in range(0, len(people.list)):
			if people.list[i][3] == a:
				tem1 = i
		for j in range(0, len(classes.list)):
			if classes.list[j][0] == b:
				tem2 = j
		print(people.list[tem1])
		print(classes.list[tem2])
		tem3 = int(input())
		self.list[tem1][tem2 * 2 + 1] = tem3
	
	# 改变学生成绩，输入学生对象和课程对象，在输入对应学号和课程号
	# 以上函数执行后加入数据库，进行数据库的刷新
	def fractional_statistics(self, people, classes, classnum, semester):
		for i in range(0, len(classes.list)):
			if classes.list[i][2] == semester and classes.list[i][0] == classnum:
				tem1 = i
		temline1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in range(0, len(self.list)):
			tem2 = int(self.list[i][2 * tem1 + 1] / 10)
			temline1[tem2] += 1
		print(temline1)
		print("该学科在各个区间成绩如下")
		for i in range(0, 10):
			print(i * 10, end=' ')
			print("~", end=' ')
			print(i * 10 + 10)
			print(temline1[i])
	
	# 统计一个学科在各个区间的分数情况，输入学科号以及所在学期
	def sort_student_grade(self, classes, people, semester):
		semester1 = dic_semester[semester]
		tem_course_list = classes.course_list
		tem_semester_score = []
		for i in range(0, len(self.list)):
			tem_line = []
			tem_line.append(self.list[i][0])
			for j in range(1, len(classes.course_list[semester1])):
				tem_line.append(self.list[i][classes.course_list[semester1][j] * 2 + 1])
			tem_semester_score.append(tem_line)
		tem_semester_score.sort(key=Sort2)
		print(semester, end='')
		print("排名如下")
		for i in range(0, len(tem_semester_score)):
			for j in range(0, len(people.list)):
				if tem_semester_score[i][0] == people.list[j][3]:
					print(people.list[j])
					tem3 = 0
					for k in range(1, len(tem_semester_score[i])):
						tem3 += tem_semester_score[i][k]
					tem3 = tem3 / (len(tem_semester_score[i]) - 1)
					print("平均成绩为", end='')
					print(tem3)
	
	# 输出第n个学期学生专业课排名情况，从高向低
	def sort_student_hang_section(self, classes, people, semester):
		semester1 = dic_semester[semester]
		tem_course_list = classes.course_list
		tem_hang_section = []
		for i in range(0, len(self.list)):
			tem_line = []
			tem_line.append(self.list[i][0])
			tem1 = 0
			for j in range(1, len(classes.course_list[semester1])):
				tem1 += self.list[i][classes.course_list[semester1][j] * 2 + 2]
			tem_line.append(tem1)
			tem_hang_section.append(tem_line)
		tem_hang_section.sort(key=Sort3)
		print(semester, end='')
		print("挂科排名如下")
		for i in range(0, len(tem_hang_section)):
			for j in range(0, len(people.list)):
				if tem_hang_section[i][0] == people.list[j][3]:
					print(people.list[j])
	
	# 输出第n个学期学生挂科情况，从高向低
	def averange_score_for_scores(self, classes, semester):
		semester1 = dic_semester[semester]
		tem_course_list = classes.course_list[semester1]
		averange_score = []
		for i in range(1, len(tem_course_list)):
			tem1 = 0
			for j in range(0, len(self.list)):
				tem1 += self.list[j][tem_course_list[i] * 2 + 1]
			averange_score.append(tem1)
		for i in range(1, len(tem_course_list)):
			print(classes.list[tem_course_list[i]][2], end='')
			print(classes.list[tem_course_list[i]][3], end='')
			print('平均')
			print(averange_score[i - 1] / (len(self.list)))
	
	# 分学期输出各个学科平均成绩，输入一个学期的字符串。
	def ranking(self, classes, people):
		tem_score = []
		for i in range(0, len(self.list)):
			tem_score.append(self.list[i].copy())
		tem_score = tem_score.copy()
		for i in range(0, len(classes.list)):
			tem_score.sort(key=lambda tem: tem[2 * i + 1] * (-1))
			for j in range(0, len(tem_score)):
				tem_score[j][2 * i + 2] = j + 1
		for i in range(0, len(tem_score)):
			for j in range(0, len(people.list)):
				if tem_score[i][0] == people.list[j][3]:
					print(people.list[j][0])
			for k in range(0, len(classes.list)):
				print(classes.list[k][2], end='')
				print(classes.list[k][3], end='')
				print('排名为', end='')
				print(tem_score[i][k * 2 + 2], end=' ')
			print()
	
	# 统计所有学生所有功课的班级排名，tem_score数组是把挂科情况变成该生该科排名的数组。
	def dormitory_ranking(self, people, dormitory):
		tem_score = []
		for i in range(0, len(people.list)):
			if people.list[i][2] == dormitory:
				tem_score.append(self.list[i])
		tem_score.sort(key=Sort2)
		print(dormitory)
		for i in range(0, len(tem_score)):
			for j in range(0, len(people.list)):
				if tem_score[i][0] == people.list[j][3]:
					print(people.list[j], end='')
					print("排名为", end=' ')
					print(i + 1)
	
	# 统计一个寝室学生们的学习情况，不分学期。
	def hang_section_in_semester(self, classes):
		tem_semester_num = [0, 0, 0, 0, 0, 0, 0, 0]
		print(self.list)
		for i in range(0, 8):
			for j in range(1, len(classes.course_list[i])):
				for k in range(0, len(self.list)):
					print(self.list[k][2 * classes.course_list[i][j] + 2], end=' ')
					print(k, end=' ')
					print(2 * classes.course_list[i][j] + 2)
					if self.list[k][2 * classes.course_list[i][j] + 2] == -1:
						tem_semester_num[i] += 1
		print(tem_semester_num)
		for i in range(0, len(tem_semester_num)):
			print("第", end='')
			print(i, end='')
			print("学期,挂了", end='')
			print(tem_semester_num[i], end='')
			print("科")
# 统计每个学期总共挂科数
	
	def score_commit(self):
			# 宋安瑞加：另外添加一个二维列表，是二维列表内元素个数达到要求
		self.list_temp = []
		for i in range(len(self.list)):
			self.list_temp.append(self.list[i])
		for i in range(len(self.list_temp)):
			for j in range(50):
				self.list_temp[i].append(0)
				self.list_temp[i].append(-1)
		# print(self.list)
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("DELETE from score ")

		for i in range(len(self.list)):
			c.execute("INSERT INTO score (student_id, subject_score1, student_score_fail1, subject_score2, student_score_fail2, subject_score3, student_score_fail3, subject_score4, student_score_fail4, subject_score5, student_score_fail5, subject_score6, student_score_fail6,  subject_score7, student_score_fail7, subject_score8, student_score_fail8, subject_score9, student_score_fail9, subject_score10, student_score_fail10, subject_score11, student_score_fail11, subject_score12, student_score_fail12, subject_score13, student_score_fail13, subject_score14, student_score_fail14, subject_score15, student_score_fail15, subject_score16, student_score_fail16, subject_score17, student_score_fail17, subject_score18, student_score_fail18, subject_score19, student_score_fail19, subject_score20, student_score_fail20, subject_score21, student_score_fail21, subject_score22, student_score_fail22, subject_score23, student_score_fail23, subject_score24, student_score_fail24, subject_score25, student_score_fail25, subject_score26, student_score_fail26, subject_score27, student_score_fail27, subject_score28, student_score_fail28, subject_score29, student_score_fail29, subject_score30, student_score_fail30, subject_score31, student_score_fail31, subject_score32, student_score_fail32, subject_score33, student_score_fail33, subject_score34, student_score_fail34, subject_score35, student_score_fail35, subject_score36, student_score_fail36, subject_score37, student_score_fail37, subject_score38, student_score_fail38, subject_score39, student_score_fail39, subject_score40, student_score_fail40, subject_score41, student_score_fail41, subject_score42, student_score_fail42, subject_score43, student_score_fail43, subject_score44, student_score_fail44, subject_score45, student_score_fail45, subject_score46, student_score_fail46, subject_score47, student_score_fail47, subject_score48, student_score_fail48, subject_score49, student_score_fail49, subject_score50, student_score_fail50) VALUES ('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')" % (self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][3], self.list[i][4], self.list[i][5], self.list[i][6], self.list[i][7], self.list[i][8], self.list[i][9],self.list[i][10], self.list[i][11], self.list[i][12], self.list[i][13], self.list[i][14],self.list[i][15], self.list[i][16], self.list[i][17], self.list[i][18], self.list[i][19],self.list[i][20], self.list[i][21], self.list[i][22], self.list[i][23], self.list[i][24],self.list[i][25], self.list[i][26], self.list[i][27], self.list[i][28], self.list[i][29],self.list[i][30], self.list[i][31], self.list[i][32], self.list[i][33], self.list[i][34],self.list[i][35], self.list[i][36], self.list[i][37], self.list[i][38], self.list[i][39],self.list[i][40], self.list[i][41], self.list[i][42], self.list[i][43], self.list[i][44],self.list[i][45], self.list[i][46], self.list[i][47], self.list[i][48], self.list[i][49],self.list[i][50], self.list[i][51], self.list[i][52], self.list[i][53], self.list[i][54],self.list[i][55], self.list[i][56], self.list[i][57], self.list[i][58], self.list[i][59],self.list[i][60], self.list[i][61], self.list[i][62], self.list[i][63], self.list[i][64],self.list[i][65], self.list[i][66], self.list[i][67], self.list[i][68], self.list[i][69],self.list[i][70], self.list[i][71], self.list[i][72], self.list[i][73], self.list[i][74],self.list[i][75], self.list[i][76], self.list[i][77], self.list[i][78], self.list[i][79],self.list[i][80], self.list[i][81], self.list[i][82], self.list[i][83], self.list[i][84],self.list[i][85], self.list[i][86], self.list[i][87], self.list[i][88], self.list[i][89],self.list[i][90], self.list[i][91], self.list[i][92], self.list[i][93], self.list[i][94],self.list[i][95], self.list[i][96], self.list[i][97], self.list[i][98], self.list[i][99], self.list[i][100]))
		conn.commit()
		conn.close()
	
	def score_print(self):
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("SELECT *  from score")
		cursor = c.fetchall()
		# print(cursor)
		for row, j in zip(cursor, range(len(cursor))):
			print(f'学号为 {cursor[j][0]} 的学生的成绩如下：')
			for i in range(1, self.classes_num + 1):
				print(f'{self.classes_list[i - 1][3]} 成绩是：{row[2 * i - 1]}')
		conn.commit()
		conn.close()


class Perform_score:
	def __init__(self, a):
		PerScore = []
		for i in range(0, len(a.list)):
			line = []
			print(a.list[i])
			for j in range(0, 3):
				print("第 ", j + 1, "个为")
				temnum1 = int(input())
				line.append(temnum1)
			PerScore.append(line)
			PerScore[i].append(a.list[i][3])
		self.list = PerScore
	
	# 输出一个关于品行的二维数组，第n-1个数代表辅导员，班主任，班级评议的成绩，第四个表示学号
	def re_in_perform(self, a):
		for i in range(len(self.list), len(a.list)):
			line = []
			print(a.list[i])
			for j in range(0, 3):
				print("第 ", j + 1, "个为")
				temnum1 = int(input())
				line.append(temnum1)
			self.list.append(line)
			self.list[i].append(a.list[i][3])
# 输出一个关于品行的二维数组，第n-1个数代表辅导员，班主任，班级评议的成绩，第四个表示学号，实现添加
# 以上函数执行后加入数据库，进行数据库的刷新
	
	def perform_score_commit(self):
		conn = pymysql.connect(host='localhost',user='root',password='00000',database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("DELETE from classes ")
		
		for i in range(len(self.list)):
			c.execute(
				"INSERT INTO perform_score (counselor_comment,teacher_comment,class_comment,student_id) VALUES ('%s','%s','%s','%s')" % (
				self.list[i][0], self.list[i][1], self.list[i][2], self.list[i][3]))
		conn.commit()
		conn.close()
	
	def perform_score_print(self):
		conn = pymysql.connect(host='localhost',user='root', password='00000', database='winprogramhomework_v1')
		c = conn.cursor()
		c.execute("SELECT *  from perform_score")
		cursor = c.fetchall()
		for row in cursor:
			print('\n')
			print("student_id = ", row[3])
			print("counselor_comment = ", row[0])
			print("teacher_comment = ", row[1])
			print("class_comment = ", row[2])
		conn.commit()
		conn.close()


class General_info:
    def __init__(self, people):
        self.listi = []
        self.listd = []
        for i in range(0, len(people.list)):
            print(people.list[i][0], people.list[i][3])
            tem1=[]
            tem2=[]
            tem1.append(people.list[i][3])
            tem1.append(int(0))
            tem2.append(people.list[i][3])
            tem2.append(int(0))
            while 1:
                tem3=[]
                tem3=input().split()
                if tem3[0]=='end':
                    break
                for i in range(0,2):
                    tem1.append(tem3[i])
            while 1:
                tem3=[]
                tem3=input().split()
                if tem3[0]=='end':
                    break
                for i in range(0,2):
                    tem2.append(tem3[i])
            self.listi.append(tem1)
            self.listd.append(tem2)
    # 输入现存学生的奖惩情况，每一行有获奖种类和学期，得到两个列表分别是listi和listd，分别表示学生正面奖励情况和负面奖励情况。
    def re_in_general_info(self,people):
        for i in range(len(self.listi),len(people.list)):
            print(people.list[i][0], people.list[i][3])
            tem1 = []
            tem2 = []
            tem1.append(people.list[i][3])
            tem1.append(int(0))
            tem2.append(people.list[i][3])
            tem2.append(int(0))
            while 1:
                tem3 = []
                tem3 = input().split()
                if tem3[0] == 'end':
                    break
                for i in range(0, 2):
                    tem1.append(tem3[i])
            while 1:
                tem3 = []
                tem3 = input().split()
                if tem3[0] == 'end':
                    break
                for i in range(0, 2):
                    tem2.append(tem3[i])
            self.listi.append(tem1)
            self.listd.append(tem2)
    # 输入现存学生的奖惩情况，每一行有获奖种类和学期，得到两个列表分别是listi和listd，分别表示学生正面奖励情况和负面奖励情况。
    def change_general_info(self,studentnum):
        for i in range(0,len(self.listi)):
            if self.listi[i][0]==studentnum:
                while len(self.listi[i])>=3:
                    del self.listi[i][2]
                while len(self.listi[i]) >= 3:
                    del self.listi[i][2]
                while 1:
                    tem3 = []
                    tem3 = input().split()
                    if tem3[0] == 'end':
                        break
                    for j in range(0, 2):
                       self.listi[i].append(tem3[j])
                while 1:
                    tem3 = []
                    tem3 = input().split()
                    if tem3[0] == 'end':
                        break
                    for j in range(0, 2):
                       self.listd[i].append(tem3[j])
    #改变学生奖惩情况，函数获得学生学号，以以上方法再次输入该学生奖惩信息。
    def count_general_info_score(self):
        for i in range(0,len(self.listi)):
            tem1=0
            tem2=0
            for j in range(1,int(len(self.listi[i])/2)):
                tem1+=dicinfy[self.listi[i][j*2]]
            for j in range(1,int(len(self.listd[i])/2)):
                tem2+=dicinfn[self.listd[i][j*2]]
            self.listi[i][1]=tem1
            self.listd[i][1]=tem2
    #计算学生总共得奖情况(总共得分与扣分)。




# 改变学生的品行成绩，输入学生对象和对应学生学号


# # 宋安瑞的测试：
# # 导入mysql驱动
#
#
# # 连接mysql
# conn = sqlite3.connect('test.db')
#
# # 连接cursor
# cursor = conn.cursor()
#
# # 创建usr表
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE "classes" (
# 	"courseid"	TEXT,
# 	"coursecotegory"	TEXT,
# 	"semester"	TEXT,
# 	"classname"	TEXT,
# 	"credit"	TEXT
# )''')
# c.execute('''CREATE TABLE "people" (
# 	"name"	TEXT NOT NULL,
# 	"sex"	TEXT,
# 	"dormitorynum"	TEXT,
# 	"ID"	TEXT,
# 	"age"	TEXT
# )''')
# c.execute('''CREATE TABLE "performscore" (
# 	"counselorcomment"	INTEGER,
# 	"teachercomment"	INTEGER,
# 	"classreview"	INTEGER,
# 	"studentid"	TEXT
# )''')
#
# # # 提交事务
# # conn.commit()
# # conn.close()
#
# # 插入操作
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# print('插入操作')
#
# c.execute("INSERT INTO people (name,sex,dormitorynum,ID,age) \
#       VALUES tuple(line)")
#
# c.execute("INSERT INTO classes (courseid,coursecotegory,semester,classname,credit) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
# c.execute("INSERT INTO performscore (counselorcomment,teachercomment,classreview,studentid) \
#       VALUES ()")
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
#
# conn.commit()
# conn.close()
#
# # 运行查询
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# print('查询操作')
#
# cursor = c.execute("SELECT name,sex,dormitorynum,ID,age  from people")
# for row in cursor:
# 	print("name = ", row[0])
# 	print("sex = ", row[1])
# 	print("dormitorynum = ", row[2])
# 	print("ID = ", row[3])
# 	print("age = ", row[4])
#
# conn.close()
#
# # 更新操作
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# print('更新操作')
#
# c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)
#
# cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
# for row in cursor:
# 	print("ID = ", row[0])
# 	print("NAME = ", row[1])
# 	print("ADDRESS = ", row[2])
# 	print("SALARY = ", row[3], "\n")
#
# conn.close()
#
# # 删除操作
# print('删除操作')
#
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# c.execute("DELETE from COMPANY where ID=2;")
# conn.commit()
# print("Total number of rows deleted :", conn.total_changes)
#
# cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
# for row in cursor:
# 	print("ID = ", row[0])
# 	print("NAME = ", row[1])
# 	print("ADDRESS = ", row[2])
# 	print("SALARY = ", row[3], "\n")
#
# conn.close()    # 宋安瑞的代码模板


'''
#测试代码
# while 1:
#     print("请输入密码")
#     line=int(input())
#     if line==int(00000):
#         break
People1=People()
print(People1.list)
Class1=Classes()
print(Class1.list)
Score1=Score(People1,Class1)
print(Score1.list)
Class1.semester_course_list()
print(Class1.course_list)
Score1.fractional_statistics(People1,Class1,'1','第一学期')
Score1.sort_student_grade(Class1,People1,'第一学期')
Score1.sort_student_hang_section(Class1,People1,'第一学期')
Score1.averange_score_for_scores(Class1,'第一学期')
Score1.ranking(Class1,People1)
Score1.dormitory_ranking(People1,'B519')
Score1.hang_section_in_semester(Class1)
# while Ture:
#     print("学生管理系统")
#     print("1--录入部分")
#     print("2--修改部分")
#     print("3--统计部分")
#     swit1=int(input())
#     if swit1==1:
#         print("1--学生信息输入")
#         print("2--课程信息输入")
#         print("3--品行表现信息输入")
#         print("4--课程成绩信息输入")
#         print("5--奖惩信息输入")
#         swit2 = int(input())
#         if swit2==1:
#             People1.append_people()
#         elif swit2==2:
#             Class1.append_class()
#         elif swit2 == 3:
#             Perform_score1.re_in_perform(People1)
#         elif swit2 == 4:
#             Score1.re_in_score(People1,Class1)
#         elif swit2 == 5:
#             General_info1.re_in_general_info(People1)
#         else:
#             break
#     elif swit1 == 2:
#         print("1--修改课程信息")
#         print("2--修改个人信息")
#         print("3--修改课程信息")
#         print("4--修改奖惩信息")
#         swit2 = int(input())
#         if swit2==1:
#             print("请输入课程号")
#             classnum1=input()
#             print("请输入课程所在学期")
#             semester1=input()
#             Class1.change_class(classnum1,semester1)
#         if swit2==2:
#             print("请输入学生学号")
#
#             People1.change_people(Score1,)

# General_info1=General_info(People1)
# General_info1.count_general_info()
# print(General_info1.list)
# Perform_score1=Perform_score(People1)
# print(Perform_score1.list)
# Class1=Classes()
# print(Class1.list)
# Score1=Score(People1,Class1)
# print(Score1.list)
# People1.change_people(Score1,'2008040105')
# print(People1.list)
# print(Score1.list)
# General_info1=General_info(People1)
# General_info1.count_general_info()
# print(General_info1.list)
# People1.append_people()
# General_info1.re_in_general_info(People1)
# General_info1.count_general_info()
# print(General_info1.list)

# Class1.append_class()
# Score1.re_in_score(People1,Class1)
# print(Score1.list)
# Perform_score1.re_in_perform(People1)
# print(Perform_score1.list)
'''


# 宋安瑞代码测试 ：

# 测试people类
people_test = People()
people_test.people_commit()
people_test.people_print()

# 测试class类
class_test = Classes()
class_test.class_commit()
class_test.class_print()

# 测试Perform_score类
# perform_score_test = Perform_score()
# perform_score_test.perform_score_commit()
# perform_score_test.perform_score_print()


# 测试score类：
score_test = Score(people_test, class_test)
score_test.score_commit()
score_test.score_print()
