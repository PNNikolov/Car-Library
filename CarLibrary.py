from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql


class ConnectorDB:
    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Cars Library GUI")
        self.root.geometry("")
        self.root.resizable(width=True, height=True)

        main_frame = Frame(root, bd=10, width="800", height="500", padx=0, pady=0, relief=GROOVE, bg='black')
        main_frame.pack()

        title_frame = Frame(main_frame, bd=10,  width="600",  height="500", relief=GROOVE, bg="black")
        title_frame.grid(row=0, column=0)

        top_frame = Frame(main_frame, bd=10, width="800", height="500", relief=GROOVE, bg="black")
        top_frame.grid(row=1, column=0)

        left_frame = Frame(top_frame, bd=5, width="400", height="200", padx=2, relief=GROOVE, bg="black")
        left_frame.pack(side=LEFT)
        left_frame2 = Frame(left_frame, bd=5, width="400", height="200", padx=2, pady=4, relief=GROOVE, bg="black")
        left_frame2.pack(side=TOP, padx=2, pady=2)

        right_frame = Frame(top_frame, bd=5, width="100", height="200", padx=2, relief=GROOVE, bg="black")
        right_frame.pack(side=RIGHT)
        right_frame2 = Frame(right_frame, bd=5, width="100", height="200", padx=0, pady=0, relief=GROOVE, bg="black")
        right_frame2.pack(side=TOP)



        # ===============================================Variables==========================================
        ID = StringVar()
        Make = StringVar()
        Model = StringVar()
        BHP = StringVar()
        Torque = StringVar()
        Specs = StringVar()
        EngineNumber = StringVar()
        EngineType = StringVar()
        Country = StringVar()

        # ===============================================Functions==========================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("GUIdb", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entID.delete(0, END)
            self.entMake.delete(0, END)
            self.entModel.delete(0, END)
            self.entBHP.delete(0, END)
            self.entTorque.delete(0, END)
            self.entSpecs.delete(0, END)
            self.entEngineNumber.delete(0, END)
            self.entEngineType.delete(0, END)
            self.entCountry.delete(0, END)

        def addData():
            if ID.get() == "" or Make.get == "" or Model.get == "" or BHP.get == "" or Torque.get == "" or Specs.get == "" \
                    or EngineNumber.get == "" or EngineType.get == "" or Country.get == "":
                tkinter.messagebox.showerror("GUIdb", "Enter correct Details")
            else:
                sqlString = "insert into Cars values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                    .format(ID.get(), Make.get(), Model.get(), BHP.get(), Torque.get(), Specs.get(), EngineNumber.get,
                            EngineType.get(), Country.get())
                self.executeSql(sqlString)
                tkinter.messagebox.showinfo("GUIdb", "Record Added Successfully")

        def DisplayData():
            sqlCon = pymysql.connect(host="localhost", user="root", password="12345678", database="sys")
            cur = sqlCon.cursor()
            cur.execute("select * from Cars")
            result = cur.fetchall()
            if len(result) != 0:
                self.Cars.delete(*self.Cars.get_children())
                for row in result:
                    self.Cars.insert('', END, values=row)

            sqlCon.commit()
            sqlCon.close()


        def CarsInfo(ev):
            viewInfo = self.Cars.focus()
            learnerData = self.Cars.item(viewInfo)
            row = learnerData['values']
            ID.set(row[0])
            Make.set(row[1])
            Model.set(row[2])
            BHP.set(row[3])
            Torque.set(row[4])
            Specs.set(row[5])
            EngineNumber.set(row[6])
            EngineType.set(row[7])
            Country.set(row[8])

        def update():
            if Make.get() and Model.get() and BHP.get() and Torque.get() and Specs.get() and EngineNumber.get() and \
                    EngineType.get() and Country.get() and ID.get():
                sqlString = "update Cars set Make='{}', Model='{}', BHP='{}', Specs='{}', EngineNumber='{}' " \
                            "where ID={}".format(Make.get(), Model.get(), BHP.get(), Torque.get(), Specs.get(),
                                                 EngineNumber.get(), EngineType.get(), Country.get(), ID.get())
                self.executeSql(sqlString)
                DisplayData()
                tkinter.messagebox.showinfo("GUIdb", "Record Updated Successfully")
            else:
                tkinter.messagebox.showinfo("GUIdb", "Select a Car")

        def delete():
            sqlString = "delete from Cars where ID=%s".format(ID.get)
            self.executeSql(sqlString)
            DisplayData()
            tkinter.messagebox.showinfo("GUIdb", "Record Deleted Successfully")
            Reset()

        def searchButton():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="12345678", database="sys")
                cur = sqlCon.cursor()
                cur.execute("select * from Cars where ID=%s", ID.get())

                row = cur.fetchone()

                ID.set(row[0])
                Make.set(row[1])
                Model.set(row[2])
                BHP.set(row[3])
                Torque.set(row[3])
                Specs.set(row[4])
                EngineNumber.set(row[5])
                EngineType.set(row[3])
                Country.set(row[3])

                sqlCon.commit()

            except:
                tkinter.messagebox.showinfo("Data Entry Form", "Record NOT Found")
                Reset()
            finally:
                sqlCon.close()

        # ===============================================TextBoxes==========================================
        self.lbltitle = Label(title_frame, font=('arial', 40, 'bold'), text="Car library", bd=7, fg="blue", bg="black")
        self.lbltitle.grid(row=0, column=0, padx=430)

        # ===================================================================================================
        self.lblID = Label(left_frame2, font=('arial', 12, 'bold'), text="ID", bd=7, fg="red", bg="black")
        self.lblID.grid(row=0, column=0, sticky=W, padx=5)
        self.entID = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left', textvariable=ID, bg="grey")
        self.entID.grid(row=0, column=1, sticky=W, padx=5)

        self.lblMake = Label(left_frame2, font=('arial', 12, 'bold'), text="Make", bd=7, fg="red", bg="black")
        self.lblMake.grid(row=1, column=0, sticky=W, padx=5)
        self.entMake = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left', textvariable=Make, bg="grey")
        self.entMake.grid(row=1, column=1, sticky=W, padx=5)

        self.lblModel = Label(left_frame2, font=('arial', 12, 'bold'), text="Model", bd=7, fg="red", bg="black")
        self.lblModel.grid(row=2, column=0, sticky=W, padx=5)
        self.entModel = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left',
                              textvariable=Model, bg="grey")
        self.entModel.grid(row=2, column=1, sticky=W, padx=5)

        self.lblBHP = Label(left_frame2, font=('arial', 12, 'bold'), text="BHP", bd=7, fg="green", bg="black")
        self.lblBHP.grid(row=3, column=0, sticky=W, padx=5)
        self.entBHP = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left', textvariable=BHP, bg="grey")
        self.entBHP.grid(row=3, column=1, sticky=W, padx=5)

        self.lblTorque = Label(left_frame2, font=('arial', 12, 'bold'), text="Torque", bd=7, fg="green", bg="black")
        self.lblTorque.grid(row=4, column=0, sticky=W, padx=5)
        self.entTorque = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left', textvariable=Torque, bg="grey")
        self.entTorque.grid(row=4, column=1, sticky=W, padx=5)

        self.lblSpecs = Label(left_frame2, font=('arial', 12, 'bold'), text="Specs", bd=7, fg="green", bg="black")
        self.lblSpecs.grid(row=5, column=0, sticky=W, padx=5)
        self.entSpecs = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left', textvariable=Specs, bg="grey")
        self.entSpecs.grid(row=5, column=1, sticky=W, padx=5)

        self.lblEngineNumber = Label(left_frame2, font=('arial', 12, 'bold'), text="EngineNumber", bd=7, fg="Blue", bg="black")
        self.lblEngineNumber.grid(row=6, column=0, sticky=W, padx=5)
        self.entEngineNumber = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left',
                                     textvariable=EngineNumber, bg="grey")
        self.entEngineNumber.grid(row=6, column=1, sticky=W, padx=5)

        self.lblEngineType = Label(left_frame2, font=('arial', 12, 'bold'), text="EngineType", bd=7, fg="blue", bg="black")
        self.lblEngineType.grid(row=7, column=0, sticky=W, padx=5)
        self.entEngineType = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left',
                                   textvariable=EngineType, bg="grey")
        self.entEngineType.grid(row=7, column=1, sticky=W, padx=5)

        self.lblCountry = Label(left_frame2, font=('arial', 12, 'bold'), text="Country", bd=7, fg="blue", bg="black")
        self.lblCountry.grid(row=8, column=0, sticky=W, padx=5)
        self.entCountry = Entry(left_frame2, font=('arial', 12, 'bold'), bd=5, width=105, justify='left',
                                textvariable=Country, bg="grey")
        self.entCountry.grid(row=8, column=1, sticky=W, padx=5)

        # ==========================================Table Treeview==========================================
        scroll_y = Scrollbar(left_frame, orient=VERTICAL)

        self.Cars = ttk.Treeview(left_frame, height=12, columns=("ID", "Make", "Model", "BHP", "Torque", "Specs",
                                                                 "EngineNumber", "EngineType", "Country"),
                                 yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Cars.heading("ID", text="ID")
        self.Cars.heading("Make", text="Make")
        self.Cars.heading("Model", text="Model")
        self.Cars.heading("BHP", text="BHP")
        self.Cars.heading("Torque", text="Torque")
        self.Cars.heading("Specs", text="Specs")
        self.Cars.heading("EngineNumber", text="EngineNumber")
        self.Cars.heading("EngineType", text="EngineType")
        self.Cars.heading("Country", text="Country")

        self.Cars['show'] = 'headings'

        self.Cars.column("ID", width="10")
        self.Cars.column("Make", width="20")
        self.Cars.column("Model", width="20")
        self.Cars.column("BHP", width="30")
        self.Cars.column("Torque", width="10")
        self.Cars.column("Specs", width="100")
        self.Cars.column("EngineNumber", width="10")
        self.Cars.column("EngineType", width="10")
        self.Cars.column("Country", width="10")

        self.Cars.pack(fill=BOTH, expand=1)
        self.Cars.bind("<ButtonRelease-1>", CarsInfo)
        DisplayData()

        # ==========================================Buttons==================================================
        self.btnAddNew = Button(right_frame2, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=10, height=4, command=addData, fg="blue")\
            .grid(row=0, column=0, padx=1)

        self.btnDisplay = Button(right_frame2, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=10, height=4, command=DisplayData, fg="blue")\
            .grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(right_frame2, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=10, height=4, command=update, fg="blue")\
            .grid(row=2, column=0, padx=1)

        self.btnDelete = Button(right_frame2, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=10, height=4, command=delete, fg="blue")\
            .grid(row=3, column=0, padx=1)

        self.btnSearch = Button(right_frame2, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=10, height=4, command=searchButton, fg="blue")\
            .grid(row=4, column=0, padx=1)

        self.btnReset = Button(right_frame2, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=10, height=4, command=Reset, fg="blue")\
            .grid(row=5, column=0, padx=1)

        self.btnExit = Button(right_frame2, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=10, height=4, command=iExit, fg="blue")\
            .grid(row=6, column=0, padx=1)

    def executeSql(self, sqlString):
        print(sqlString)
        sqlCon = pymysql.connect(host="localhost", user="root", password="12345678", database="sys")
        cur = sqlCon.cursor()
        cur.execute(sqlString)


        sqlCon.commit()
        sqlCon.close()


tk = Tk()
application = ConnectorDB(tk)
tk.mainloop()
