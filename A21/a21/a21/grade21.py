import sys
import os
import shutil
import pandas as pd
import copy
import csv

# =====================================================================================================================================

directory = os.fsencode("./submissions")

cases = [
['Quick zephyrs blow, vexing daft Jim.', 'bird', '<<><!<<>!<<!<!<<><!<<>'],
['Two driven jocks help fax my big quiz.', 'breeze', '<<>>><>>>!<!<<>>>!*!<<>><>'],
['Glib jocks quiz nymph to vex dwarf.', 'wreck', '>>>>!>><!<>>>!>>!>!<>><'],
['Jackdaws love my big sphinx of quartz.', 'trim', '>><<>>!>><<>>>>!>><<>!>><>!<>>>>!<>>!<>>>'],
['Waltz, nymph, for quick jigs vex Bud.', 'bundle', '<>>!<><>!<>!<>>'],
['Glib jocks quiz nymph to vex dwarf.', 'occur', '>>>>!>>>><!><!>!><!>>>><!>>>>><'],
['Glib jocks quiz nymph to vex dwarf.', 'hawk', '>>>!<>>!>>><>!>>>>><<!><!<>!<>>'],
['Two driven jocks help fax my big quiz.', 'room', '<<><!<!<<>>>!><!<<>>!<<>>>!<<><!<<>><'],
['Quick zephyrs blow, vexing daft Jim.', 'tonight', '><>!<<>!<>><><!><>!<<>'],
['Sphinx of black quartz, judge my vow.', 'obvious', '<<<><>>>!<<>>!<<<>!<<>>>!<>>!<<<><>!<<<><>>>'],
["The five boxing wizards jump quickly." ,"speak" ,"<<>!<<<><!*!<!<<!<>>>"],
["Two driven jocks help fax my big quiz." ,"success" ,"<<>>><>>>!<<><<!<<>>>"],
["How vexingly quick daft zebras jump!" ,"moment" ,"<>!<><!>!><><!>!<>>!>>>>"],
["Two driven jocks help fax my big quiz." ,"version" ,">!<<>>!*!<<>>>!<<>><!<>>!<>>"],
["Glib jocks quiz nymph to vex dwarf." ,"cash" ,">>><<!>>><>!<<>!><!>>>!<>>"]]



correct = [
['<<<>!<!><!<<><', 'decide'],
['<<><<>!<>!<<>><!<<>><!>>>>!<<>><','month'],
[">>>>><<><!>>><>!<>>!<>!><>>" ,"unfold"],
[">><><<!>><<>>>>!<>>>>!>><<><" ,"provide"],
["<><<<<!<>>>!<>><!<><<<><!<>!<><<<>" ,"tilt"],
[">>!<>!<>!>>>>!>>><>" ,"utility"],
["><<!<<>!>>>>><<><!><>>" ,"service"],
["<>!<!<!<<>>><>>>" ,"convince"],
["><>>!<>><>!<>><><!<!<<>><!<<>>!><>>" ,"sense"],
["<<>>>!<<<><!><>!<<>!<<>>>!><!*" ,"enforce"],
["<>>>>!<>>><!<<!<<<><!<>><<><" ,"father"],
["<>>!><<!<<><!<<><!<<>><!<>>!<>>" ,"man"],
["><><>!>!><><>!<>!><>!>><<><" ,"ecology"],
["><!<<>><!<>!<>>!<<>>!<!<<>>>" ,"witness"],
["<>!<<>!>>>!><<" ,"praise"]]


debug = True

class Student_Info(object):

		def __init__(self):
				self.name = "No name"
				self.id = "No ID"
				self.score = -1
				self.failures = []
				self.filename = "No File"
		
		def __str__(self):
				return self.name + " " + self.id + " " + str(self.score)

def move_file(source, destination):
		# moves a file from source to destination
		shutil.move(source, destination)

def run_submissions_files():

		# emty dictionary to hold students
		students = {}

		# go through each file
		for fi in os.listdir(directory):	
				# give everyone 10 points for submitting
				score = 10
				fails = []
				

				filename = os.fsdecode(fi)
				name = None
				s_id = None
				partner_name = None
				p_id = None
				s_file = filename
				wrong_header = False


				# get all of the student info
				with open("./submissions/" + filename, "r", encoding="utf-8") as student_file: 
						print('Grading ' + filename)
						for line in student_file:
								line = line.lower()

								try: 
										# extract info from header
										if "Student's Name".lower() in line: 
												name = line.strip().split(':')[1].strip()
										elif "Student Name".lower() in line:
												name = line.strip().split(':')[1].strip()

										elif "Student UT EID".lower() in line:
												s_id = line.strip().split(':')[1].strip()
										elif "Student's UT EID".lower() in line:
												s_id = line.strip().split(':')[1].strip()

										elif "Partner UT EID".lower() in line:
												p_id = line.strip().split(':')[1].strip()
										elif "Partner Name".lower() in line: 
												partner_name = line.strip().split(':')[1].strip()
								except:
										input("Something wrong with student's header for filename: " + filename)
										wrong_header = True

				# missing either the student name or eid
				if not name or not s_id: 
					wrong_header = True

				if wrong_header:
					fails.append('wrong header, -5')
					print('wrong header, -5')
					name = input('enter student name:')
					s_id = input('enter student eid:')

					score -= 5

				
				# create student and partner objects
				student = Student_Info()
				student.name = name
				student.id = s_id
				student.filename = s_file
				student.score = score

				partner = None

				if(partner_name):
						partner = Student_Info()
						partner.name = partner_name
						partner.id = p_id
						partner.filename = s_file
						partner.score = score


				# write student and setup file to temp_file
				with open("setup.py", "r", encoding="utf-8") as setup_file:
						start_lines = [line for line in setup_file.readlines() if line.strip()]

				with open("./submissions/" + filename, "r", encoding="utf-8") as student_file:
						all_lines = [line for line in student_file.readlines() if line.strip()]

				with open("temp_file.py", "w+", encoding="utf-8") as t_file:
						t_file.writelines(start_lines)
						t_file.writelines(all_lines)


				try:
					import temp_file
				except Exception as e:
					input("problem reloading file for " + filename)
					print(e)
					move_file("./submissions/" + filename, "./manual_grade")
					continue

				# do the actual grading here
				func = getattr(temp_file, 'grade')
				for i in range(len(cases)):
					try:

						if(debug):
							print('Case ' + str(i))

						case = cases[i]
						answer = correct[i]

						a1, a2, consistent = func(case[0], case[1], case[2])
						this_score = 0
						try:
							if(a1 == answer[0]):
								this_score += 3
								if(debug):
									print('passed')
									print()

							else:
								if(debug):
									print('FAIL')
									print('Actual: ' + a1)
									print('Correct: ' + answer[0])

								fails.append('failed encode for case ' + str(i))
								if(debug):
									print('failed encode for case ' + str(i))
									print()

						except:
							fails.append('error in encode for case ' + str(i))
							if(debug):
								print('error in encode for case ' + str(i))
								print()

						try:
							if(a2 == answer[1]):
								this_score += 3
								if(debug):
									print('passed')
									print()
							else:
								if(debug):
									print('FAIL')
									print('Actual: ' + a2)
									print('Correct: ' + answer[1])

								fails.append('failed decode for case ' + str(i))
								if(debug):
									print('failed decode for case ' + str(i))
									print()

						except:
							fails.append('error in decode for case ' + str(i))
							if(debug):
								print('error in decode for case ' + str(i))
								print()

						if(consistent):
							if(debug):
								print('consistent!')
								print()
							if(this_score == 0):
								this_score += 3
							elif(this_score == 3):
								this_score += 1.5
						score += this_score

					except Exception as e:
						print(e)
						continue

				if(debug):
					print(student.name)
					print(score)

					if(partner):
						print(partner.name)
						print(score)
					
				
				student.score = score
				student.failures = fails

				if(partner):
						partner.score = score
						partner.failures = fails

				students[s_id] = student

				if partner and (not p_id in students):
						students[p_id] = partner

				if(score <= 10):
					move_file("./submissions/"+filename, "./fails")
				else:
					move_file("./submissions/"+filename, "./graded")

				# delete temp file
				del sys.modules[temp_file.__name__]


		# loop through the gradebook, add students who have been graded

		grades = []
		failures = []

		with open("gradebook.csv", "rt") as f:
				reader = csv.DictReader(f, delimiter=',')
				with open("newfile.csv", "wt") as f_out:
						writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames, delimiter=",")
						writer.writeheader()
						for row in reader:
								if row['SIS Login ID'] in students.keys():
									if(students[row['SIS Login ID']].score > 9):
										writer.writerow(row)
										grades.append(students[row['SIS Login ID']].score)
										failures.append(students[row['SIS Login ID']].failures)
									del students[row['SIS Login ID']]

		gradebook = pd.read_csv('newfile.csv')
		gradebook['A21 (5264763)'] = grades
		gradebook['Comments'] = failures
		gradebook.to_csv(r'graded.csv')

		print('something went wrong for the following students')
		for st in students.keys():
			print(students[st].name + ' ' + students[st].id + ' ' + str(students[st].score))


run_submissions_files()