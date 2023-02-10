from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class stud :
	def __init__(self,x):
		self.x = x
		self.x.geometry('1350x690')
		self.x.config(bg='silver')
		self.x.title("students management system")
		self.x.resizable(False,False)
		title = Label(self.x,text='students management system',bg='#00897B',font=('monospace',14,'bold'),fg='white')
		title.pack(fill=X)
		#variables of the entries
		self.id_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.phone_var=StringVar()
		self.moahel_var=StringVar()
		self.gender_var=StringVar()
		self.address_var=StringVar()
		self.se_var=StringVar()
		self.se_by = StringVar()
		self.delevar = StringVar()
		#management frame
		Manage_Frame = Frame (self.x, bg='white')
		Manage_Frame.place (x=1137, y=30,width=210,height=400)
		lbl_ID = Label (Manage_Frame, text='ID', bg='white')
		lbl_ID.pack()
		ID_Entry = Entry (Manage_Frame,textvariable=self.id_var,bd='2', justify='center')
		ID_Entry.pack()
		lbl_name = Label (Manage_Frame, bg='white', text='name')
		lbl_name.pack()
		Name_Entry = Entry (Manage_Frame, textvariable=self.name_var,bd='2', justify='center')
		Name_Entry.pack()
		email_label = Label(Manage_Frame,text='email',bg='white')
		email_label.pack()
		email_Entry = Entry (Manage_Frame,textvariable=self.email_var ,bd='2', justify='center')
		email_Entry.pack()
		phone_label = Label(Manage_Frame,text='phone',bg='white')
		phone_label.pack()
		phone_Entry= Entry (Manage_Frame,textvariable=self.phone_var ,bd='2', justify='center')
		phone_Entry.pack()
		lbl_certi = Label (Manage_Frame, bg='white',text='grade')
		lbl_certi.pack ()
		certi_Entry= Entry (Manage_Frame,textvariable=self.moahel_var, bd='2', justify='center')
		certi_Entry.pack()
		lbl_gender = Label (Manage_Frame, text='choose gender', bg='white')
		lbl_gender.pack()
		gender_box = ttk.Combobox(Manage_Frame,textvariable=self.gender_var)
		gender_box['value']=('male','female')
		gender_box.pack()
		address = Label(Manage_Frame,text='address',bg='white')
		address.pack()
		address_entry = Entry(Manage_Frame,bd=2,justify='center',textvariable=self.address_var)
		address_entry.pack()
		deletel = Label(Manage_Frame,text='delete student by his name',fg='red',bg='white',font=('Courier',10,'bold'))
		deletel.pack()
		delet = Entry(Manage_Frame,textvariable=self.delevar,bd=2,justify="center")
		delet.pack()
		#control panel
		btn_Frame = Frame (self.x, bg='white')
		btn_Frame.place (x=1137, y=435, width=210, height=253)
		titlel= Label (btn_Frame, text="Control panel", font=('Deco', 14), bg='black',fg='white')
		titlel.pack (fill=X)
		add_btn= Button (btn_Frame, text='add',bg='#009688',width=40,activebackground='black',activeforeground='white',command=self.add_student)
		add_btn.pack()
		del_btn= Button (btn_Frame, text='delete',bg='#009688',width=40,activebackground='black',activeforeground='white',command=self.delet)
		del_btn.pack()
		update = Button (btn_Frame, text='update',bg='#009688',width=40,activebackground='black',activeforeground='white',command=self.edit)
		update.pack()
		clear = Button (btn_Frame, text='clear',bg='#009688',width=40,activebackground='black',activeforeground='white',command = self.clear)
		clear.pack()
		about = Button (btn_Frame, text='about',bg='#009688',width=40,activebackground='black',activeforeground='white',command=self.message)
		about.pack()
		exit = Button (btn_Frame, text='exit',bg='#009688',width=40,command=x.quit,activebackground='black',activeforeground='white')
		exit.pack()
		#search frame in the up
		search_Frame = Frame (self.x, bg='#004D40')
		search_Frame.place (x=1, y=30,width=1134, height=50)
		lbl_search=Label (search_Frame, text='search', bg='#004D40',fg='white',font=('Courier',10,'bold'))
		lbl_search.place (x=1, y=12)
		combo_search= ttk.Combobox (search_Frame, justify='right',textvariable=self.se_by)
		combo_search['value']=('id', 'name', 'email', 'phone')
		combo_search.place (x=55, y=12)
		search_Entry = Entry (search_Frame, textvariable=self.se_var, justify='right' , bd='2')
		search_Entry.place(x=200, y=12)
		se_but = Button(search_Frame,text='Search',bg='#009688',command=self.search)
		se_but.place(x=331,y=12)
		#frame of treeview and database
		Dietals_Frame = Frame (self.x, bg='#F2F4F4')
		Dietals_Frame.place(x=1, y=82, width=1134, height=605 )
		scroll_x = Scrollbar (Dietals_Frame, orient=HORIZONTAL)
		scroll_y= Scrollbar (Dietals_Frame, orient=VERTICAL)
		self.student_table=ttk.Treeview (Dietals_Frame,columns=('id', 'name', 'email', 'phone', 'certi', 'gender','address')
		,xscrollcommand=scroll_x.set,
		yscrollcommand=scroll_y.set)
		self.student_table.place (x=18, y=1,width=1130,height=587)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=LEFT, fill=Y)
		scroll_x.config(command=self.student_table.xview)
		scroll_y.config(command=self.student_table.yview)
		self.student_table ['show']='headings'
		self.student_table.heading ('address', text='address')
		self.student_table.heading ('gender', text='gender')
		self.student_table.heading('certi', text='grade')
		self.student_table.heading ('phone', text='phone')
		self.student_table.heading ('email', text='email')
		self.student_table.heading('name',text='name')
		self.student_table.heading('id',text='id')
		self.student_table.column ('address',width=130)
		self.student_table.column ('gender',width=30)
		self.student_table.column('certi',width=65)
		self.student_table.column ('phone', width=65)
		self.student_table.column ('email', width=70)
		self.student_table.column ('name', width=100)
		self.student_table.column('id',width=12)
		self.student_table.bind('<ButtonRelease-1>',self.curs)
		 #--------- connect with database + adding data---------
		self.fetch_all()
		#functions of buttons

	def add_student(self):
		con = pymysql.connect(host = 'localhost',user = 'root',password='',database= 'student')
		cur = con.cursor()
		cur.execute('insert into studen values(%s,%s,%s,%s,%s,%s,%s)',(
			                                                   self.id_var.get(),
			                                                   self.name_var.get(),
			                                                   self.email_var.get(),
			                                                   self.phone_var.get(),
			                                                   self.moahel_var.get(),
			                                                   self.gender_var.get(),
			                                                   self.address_var.get()
		                                                         ))
		con.commit()
		self.fetch_all()
		self.clear()
		con.close()
	def fetch_all(self):
		con = pymysql.connect(host='localhost', user='root', password='', database='student')
		cur = con.cursor()
		cur.execute('select * from studen')
		rows = cur.fetchall()
		if (rows) != 0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,value=row)
			con.commit()
		con.close()
	def delet(self):
		con = pymysql.connect(host='localhost', user='root', password='', database='student')
		cur = con.cursor()
		cur.execute('delete from studen where name=%s',self.delevar.get())
		con.commit()
		self.fetch_all()
		self.clear()
		con.close()
	def clear(self):
		self.id_var.set('')
		self.name_var.set('')
		self.email_var.set('')
		self.phone_var.set('')
		self.moahel_var.set('')
		self.gender_var.set('')
		self.address_var.set('')
		self.delevar.set('')
	def curs (self,le):
		curl = self.student_table.focus()
		contents = self.student_table.item(curl)
		row = contents['values']
		self.id_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.phone_var.set(row[3])
		self.moahel_var.set(row[4])
		self.gender_var.set(row[5])
		self.address_var.set(row[6])
	def edit(self):
		con = pymysql.connect(host='localhost', user='root', password='', database='student')
		cur = con.cursor()
		cur.execute('update studen set address=%s,name=%s,email=%s,phone=%s,certi=%s,gender=%s where id=%s', (
			self.address_var.get(),
			self.name_var.get(),
			self.email_var.get(),
			self.phone_var.get(),
			self.moahel_var.get(),
			self.gender_var.get(),
			self.id_var.get()
		))
		con.commit()
		self.fetch_all()
		self.clear()
		con.close()
	def search(self):
		con = pymysql.connect(host='localhost', user='root', password='', database='student')
		cur = con.cursor()
		cur.execute('select * from studen where ' +
					str(self.se_by.get())+" LIKE'%"+str(self.se_var.get())+"%'")
		rows = cur.fetchall()
		if (rows) != 0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('', END, value=row)
			con.commit()
		con.close()
	def message(self):
		messagebox.showinfo('about','programmer : mohamed elemary all praise for GOD else thanks for all people that helped me in this project')





















x = Tk()
ob = stud(x)
x.mainloop()