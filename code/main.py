
from flask import Flask, render_template, request
import pymysql.cursors
import sys

app = Flask(__name__)

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       port=8889,
                       db='course_schedule',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods = ('GET', 'POST'))
def hello():
	cursor = conn.cursor()
	query = 'SELECT * FROM course_schedule_sp_2021' 
	cursor.execute(query)
	data = cursor.fetchall()
	cursor.close()
	return render_template('index.html', courses = data)

@app.route('/search', methods = ('GET', 'POST'))
def search_selection():
	if request.method == "POST":
		search_type = request.form.get('search_type')
		if (search_type == "subject"):
			return render_template('course_search.html')
		elif (search_type == "prof"):
			return render_template('course_search_prof.html')
		elif (search_type == "subj_prof"):
			return render_template('course_search_subj_prof.html')
		elif (search_type == "requirement"):
			return render_template('course_search_requirement.html')
		else:
			return render_template('course_search_module.html')


@app.route('/search_course', methods = ('GET', 'POST'))
def search_course_subj():
	subj = request.form.get('subject')
	num = request.form.get('course_num')
	cursor = conn.cursor()
	courses = None
	if num == "":
		query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D where C.crn = D.crn and D.deptid = %s"
		cursor.execute(query, (subj))
		courses = cursor.fetchall()
	else:
		query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D where C.crn = D.crn and D.deptid = %s and D.coursenum = %s"
		cursor.execute(query, (subj, num))
		courses = cursor.fetchall()
	cursor.close()

	return render_template('course_search.html', courses = courses)

@app.route('/search_course_prof', methods = ('GET', 'POST'))
def search_course_prof():
	last = request.form.get('last_name')
	first = request.form.get('first_name')
	cursor = conn.cursor()
	courses = None
	if first == "":
		query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, instructors I where C.crn = I.crn and I.last = %s"
		cursor.execute(query, (last))
		courses = cursor.fetchall()
	else:
		query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, instructors I where C.crn = I.crn and I.last = %s and I.first = %s"
		cursor.execute(query, (last, first))
		courses = cursor.fetchall()
	cursor.close()

	return render_template('course_search_prof.html', courses = courses)

@app.route('/search_course_subj_prof', methods = ('GET', 'POST'))
def search_course_subj_prof():
	subj = request.form.get('subject')
	num = request.form.get('course_num')
	last = request.form.get('last_name')
	first = request.form.get('first_name')
	cursor = conn.cursor()
	courses = None
	if num == "" and first == "":
		query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D, instructors I where C.crn = D.crn and C.crn = I.crn and D.deptid = %s and I.last = %s"
		cursor.execute(query, (subj, last))
		courses = cursor.fetchall()
	else:
		if num == "":
			query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D, instructors I where C.crn = D.crn and C.crn = I.crn and D.deptid = %s and I.last = %s and I.first = %s"
			cursor.execute(query, (subj, last, first))
			courses = cursor.fetchall()
		elif first == "":
			query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D, instructors I where C.crn = D.crn and C.crn = I.crn and D.deptid = %s and I.last = %s and D.coursenum = %s"
			cursor.execute(query, (subj, last, num))
			courses = cursor.fetchall()
		else:
			query = "SELECT distinct C.* FROM course_schedule_sp_2021 C, departments D, instructors I where C.crn = D.crn and C.crn = I.crn and D.deptid = %s and D.coursenum = %s and I.last = %s  and I.first = %s"
			cursor.execute(query, (subj, num, last, first))
			courses = cursor.fetchall()
	cursor.close()

	return render_template('course_search_subj_prof.html', courses = courses)

@app.route('/search_requirement', methods = ('GET', 'POST'))
def search_course_req():
	if request.method == "POST":
		req = request.form.get('search_req')
		courses = None
		cursor = conn.cursor()
		query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.natl = 1"

		if req == "non-western":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.non_western = 1"
		elif req == "lang":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.lang = 1"
		elif req == "soc_sci":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.soc_sci = 1"
		elif req == "nsp":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.nsp = 1"
		elif req == "conn":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.conn = 1"
		elif req == "human":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.human = 1"
		elif req == "arts":
			query = "SELECT C.* FROM course_schedule_sp_2021 C, distributionreqs D where C.crn = D.crn and D.arts = 1"

		cursor.execute(query)
		courses = cursor.fetchall()

		return render_template('course_search_requirement.html', courses = courses)

@app.route('/search_course_module', methods = ('GET', 'POST'))
def search_course_mod():
	if request.method == "POST":
		mod = request.form.get('module')
		print(mod)
		courses = None
		cursor = conn.cursor()
		query = "SELECT * FROM course_schedule_sp_2021 C where C.module = %s"
		cursor.execute(query, (mod))
		courses = cursor.fetchall()
		cursor.close()
		return render_template('course_search_module.html', courses = courses)

if __name__ == "__main__":
	app.run('127.0.0.1', 5004, debug = True)