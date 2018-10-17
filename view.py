from tkinter import*
from tkinter.ttk import Treeview
from tkinter import messagebox
from presenter import present

class view:
	def __init__(self, f):
		self.bgc = "white"
		self.form = f
		self.presenter = present(self)
		self.place_startpage()


##############################################################################
	# 1. Start page

	def init_startpage(self):
		table_headings = ["Название", "Длина", "Дата создания"]

		self.route_table = Treeview(self.form, selectmode="browse", \
			show='headings', height = 25)

		self.route_table["columns"] = table_headings
		self.route_table["displaycolumns"] = table_headings

		for head in table_headings:
			self.route_table.heading(head, text=head, anchor=CENTER)

		colomn_width = 200
		self.route_table.column("Название", anchor=CENTER, width = colomn_width)
		self.route_table.column("Длина", anchor=CENTER, width = colomn_width)
		self.route_table.column("Дата создания", anchor=CENTER, width = colomn_width)

		self.about_route_button = Button(self.form, text="Подробно",\
			width=15,height=3, command=self.about_route)

		self.delete_route_button = Button(self.form, text='Удалить',\
			width=15,height=3, command=self.delete_route)

		self.create_route_button = Button(self.form, text='Создать',\
			width=15,height=3, command=self.create_route)

		self.import_route_button = Button(self.form, text='Импорт',\
			width=15,height=3, command=self.import_route)

		self.presenter.fill_routes_table()

	def about_route(self):
		self.remove_startpage()
		self.place_about_route()

	def delete_route(self):
		pass

	def create_route(self):
		self.remove_startpage()
		self.place_create_route()

	def import_route(self):
		pass

	def place_startpage(self):
		self.init_startpage()
		but_y = 530
		self.route_table.place(x = 100, y = 0)
		self.about_route_button.place(x = 0, y = but_y)
		self.delete_route_button.place(x = 220, y = but_y)
		self.create_route_button.place(x = 430, y = but_y)
		self.import_route_button.place(x = 650, y = but_y)

	def remove_startpage(self):
		self.route_table.destroy()
		self.about_route_button.destroy()
		self.delete_route_button.destroy()
		self.create_route_button.destroy()
		self.import_route_button.destroy()

##############################################################################
	# 2. About route

	def init_about_route(self):
		table_headings = ["№ точки", "Долгота", "Широта", "Высота"]

		self.point_table = Treeview(self.form, selectmode="browse", \
			show='headings', height = 25)

		self.point_table["columns"] = table_headings
		self.point_table["displaycolumns"] = table_headings

		for head in table_headings:
			self.point_table.heading(head, text=head, anchor=CENTER)

		colomn_width = 150
		self.point_table.column("№ точки", anchor=CENTER, width = colomn_width)
		self.point_table.column("Долгота", anchor=CENTER, width = colomn_width)
		self.point_table.column("Широта", anchor=CENTER, width = colomn_width)
		self.point_table.column("Высота", anchor=CENTER, width = colomn_width)

		self.edit_point_button = Button(self.form, text="Редактировать",\
			width=15,height=3, command=self.edit_point)

		self.back_from_point_to_start_button = Button(self.form, text='Назад',\
			width=15,height=3, command=self.back_from_point_to_start)

		self.point_edit_entry = Text(self.form, height=1.2, width=16, font='Arial 12')

		#self.presenter.

	def edit_point(self):
		pass

	def back_from_point_to_start(self):
		self.remove_about_route()
		self.place_startpage()

	def place_about_route(self):
		self.init_about_route()
		self.point_table.place(x = 100, y = 0)
		self.edit_point_button.place(x = 250, y = 530)
		self.back_from_point_to_start_button.place(x = 550, y = 530)
		self.point_edit_entry.place(x = 70, y = 547)

	def remove_about_route(self):
		self.point_table.destroy()
		self.edit_point_button.destroy()
		self.back_from_point_to_start_button.destroy()
		self.point_edit_entry.destroy()

##############################################################################
	# 2. About route

	def init_create_route(self):
		table_headings = ["№ точки", "Долгота", "Широта", "Высота"]

		self.point_table_create = Treeview(self.form, selectmode="browse", \
			show='headings', height = 25)

		self.point_table_create["columns"] = table_headings
		self.point_table_create["displaycolumns"] = table_headings

		for head in table_headings:
			self.point_table_create.heading(head, text=head, anchor=CENTER)

		colomn_width = 150
		self.point_table_create.column("№ точки", anchor=CENTER, width = colomn_width)
		self.point_table_create.column("Долгота", anchor=CENTER, width = colomn_width)
		self.point_table_create.column("Широта", anchor=CENTER, width = colomn_width)
		self.point_table_create.column("Высота", anchor=CENTER, width = colomn_width)

		self.add_point_button = Button(self.form, text="Добавить",\
			width=15,height=3, command=self.add_point)

		self.save_route_button = Button(self.form, text='Сохранить',\
			width=15,height=3, command=self.save_route)

		self.new_route_name_entry = Text(self.form, height=1.2, width=16, font='Arial 12')

		self.new_route_name_label = Label(text='Имя маршрута:',\
		 						 font = 'Arial 16', bg = self.bgc)

		self.new_point_entry = Text(self.form, height=1.2, width=16, font='Arial 12')


	def add_point(self):
		pass

	def save_route(self):
		pass

	def place_create_route(self):
		self.init_create_route()
		self.point_table_create.place(x = 100, y = 50)
		self.add_point_button.place(x = 200, y = 610)
		self.save_route_button.place(x = 450, y = 600)
		self.new_route_name_label.place(x = 225, y = 0)
		self.new_route_name_entry.place(x = 380, y = 4)
		self.new_point_entry.place(x = 200, y = 580)




##############################################################################
	# Interfaces

	def insert_into_route_table(self, routes):
		for i in range(len(routes)):
			self.route_table.insert('', END, values = tuple(routes[i]))

