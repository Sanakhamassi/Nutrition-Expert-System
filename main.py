import tkinter as tk
from PIL import ImageTk, Image
import regime as rules
from experta import Fact
import tkinter.font as tkFont

# Search in the rules which diet was redirected
def detectRegime():
    expertSystem = rules.regimeType()
    expertSystem.reset()
    expertSystem.declare(Fact(vegetarian=str(vegetarian.get())))
    expertSystem.declare(Fact(vegetalian=str(vegetalian.get())))
    expertSystem.declare(Fact(lactose_allergy=str(lactose_allergy.get())))
    expertSystem.declare(Fact(gluten_allergy=str(gluten_allergy.get())))
    expertSystem.declare(Fact(overweight=str(overweight.get())))
    expertSystem.declare(Fact(diabetic=str(diabetic.get())))
    expertSystem.declare(Fact(muscles_gain=str(muscles_gain.get())))
    expertSystem.declare(Fact(physical_activity=str(physical_activity.get())))
    expertSystem.declare(Fact(weight_loss=str(weight_loss.get())))
    #return the suitable diet that matchs the user inputs (chainage avant)
    expertSystem.run()

    return expertSystem.name, expertSystem.description, expertSystem.photo


def openNewWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Régime alimentaire")
    # sets the geometry of toplevel
    newWindow.geometry("1100x800")
    pho = r'.\images\diet.png'
    p1 = ImageTk.PhotoImage(Image.open(pho))
    # Icon set for new window
    newWindow.iconphoto(False, p1)
    name, description, photo = detectRegime()
    exit=True
    #when no diet matches the user inputs
    if name == description == photo == '':
        name = 'Unfortunately, no diet is available for you.'
        photo = r'.\images\no.png'
        exit=False
    #echec image
    img = ImageTk.PhotoImage(Image.open(photo).resize((750, 550)))
    canvas = tk.Canvas(newWindow, width=900, height=700)
    canvas.pack()
    canvas.create_image(400, 360, anchor=tk.CENTER, image=img)
    canvas.img = img

    # label to display name diet
    name_diet = tk.Label(newWindow)
    fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
    name_diet["font"] = fontStyle
    name_diet["fg"] = "#7D8B11"
    name_diet["justify"] = "center"
    name_diet["text"] = str(name)
    name_diet.place(x=300, y=0.5)


    # description displayed in a text field
    if(exit==True):
        ftext = tkFont.Font(family='Helvetica', size=12)
        T = tk.Text(newWindow, height=4, width=80,font=ftext)
        T.insert(tk.END, str(description))
        T.place(x=550,y=710, anchor='center')

#home window
background = "#ffffff"
source = tk.Tk()
source.title("Healthy style ")
source.config(bg=background)
source.resizable(True, True)
source.geometry("900x650")
pho = r'.\images\diet.png'
p1 = ImageTk.PhotoImage(Image.open(pho))
# Icon set for source window
source.iconphoto(False, p1)
# Variables for choosing the selected fields
vegetarian = tk.IntVar()
vegetalian = tk.IntVar()
lactose_allergy = tk.IntVar()
gluten_allergy = tk.IntVar()
overweight = tk.IntVar()
diabetic = tk.IntVar()
muscles_gain = tk.IntVar()
physical_activity = tk.IntVar()
weight_loss = tk.IntVar()


#interface du programme
fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
l1 = tk.Label(source, text="Welcome to The Healthy Style Expert System", width=40,
              fg='#7D8B11', bg=background, font=fontStyle,justify="center",padx=70)
l1.place(x=3,y=3)

fontTipo = tkFont.Font(family="Helvetica", size=12)

# Q1:vegetarian
tk.Label(source, text="Are you a Vegetarian? ",
         width=45, bg=background, font=fontTipo).grid(row=2, column=0,pady=45)

c1 = tk.Checkbutton(source, text="No", variable=vegetarian, onvalue=0, bg=background,)
c1.grid(row=3, column=0)

c2 = tk.Checkbutton(source, text="Yes", variable=vegetarian,
                    onvalue=1,
                    bg=background)
c2.grid(row=4, column=0)

# Q2:Vegetalian
tk.Label(source, text="Are you a Vegetalian (Severe vegetarian)? ",
         width=40, bg=background, font=fontTipo).grid(row=5, column=0)

c3 = tk.Checkbutton(source, text="No", variable=vegetalian,
                    onvalue=0,
                    bg=background)
c3.grid(row=6, column=0)

c4 = tk.Checkbutton(source, text="Yes", variable=vegetalian,
                    onvalue=1,
                    bg=background)
c4.grid(row=7, column=0)

# Q3:lactose_allergic
tk.Label(source, text="Are you allergic to lactose? ",
         width=40, bg=background, font=fontTipo).grid(row=8, column=0)

c5 = tk.Checkbutton(source, text="No", variable=lactose_allergy,
                    onvalue=0, bg=background)
c5.grid(row=9, column=0)

c6 = tk.Checkbutton(source, text="Yes", variable=lactose_allergy,
                    onvalue=1, bg=background)
c6.grid(row=10, column=0)

# Q4:gluten_allergic
tk.Label(source, text="Are you allergic to gluten? ",
         width=50, bg=background, font=fontTipo).grid(row=11, column=0)

c7 = tk.Checkbutton(source, text="No", variable=gluten_allergy,
                    onvalue=0,
                    bg=background)
c7.grid(row=12, column=0)

c8 = tk.Checkbutton(source, text="Yes", variable=gluten_allergy,
                    onvalue=1,
                    bg=background)
c8.grid(row=13, column=0)

# Q5:Overweight
tk.Label(source, text="Do you suffer from overweight? ",
         width=50, bg=background, font=fontTipo).grid(row=12, column=1)

c9 = tk.Checkbutton(source, text="No", variable=overweight,
                    onvalue=0,
                    bg=background)
c9.grid(row=13, column=1)

c10 = tk.Checkbutton(source, text="Yes", variable=overweight,
                     onvalue=1,
                     bg=background)
c10.grid(row=14, column=1)

# Q6:diabetic
tk.Label(source, text="Are you diabetic?",
         width=50, bg=background, font=fontTipo).grid(row=17, column=0)

c11 = tk.Checkbutton(source, text="No", variable=diabetic,
                     onvalue=0,
                     bg=background)
c11.grid(row=18, column=0)

c12 = tk.Checkbutton(source, text="Yes", variable=diabetic,
                     onvalue=1,
                     bg=background)
c12.grid(row=19, column=0)

# Q7:muscle_gain
tk.Label(source, text="Do you want to gain muscles?",
         width=50, bg=background, font=fontTipo).grid(row=5, column=1)

c13 = tk.Checkbutton(source, text="No", variable=muscles_gain,
                     onvalue=0,
                     bg=background)
c13.grid(row=6, column=1)

c14 = tk.Checkbutton(source, text="Yes", variable=muscles_gain,
                     onvalue=1,
                     bg=background)
c14.grid(row=7, column=1)

# Q8:physical activity
tk.Label(source, text="Do you practise sports or any physical activity?",
         width=40, bg=background, font=fontTipo).grid(row=2, column=1)

c15 = tk.Checkbutton(source, text="No", variable=physical_activity,
                     onvalue=0,
                     bg=background)
c15.grid(row=3, column=1)

c16 = tk.Checkbutton(source, text="Yes", variable=physical_activity,
                     onvalue=1,
                     bg=background)
c16.grid(row=4, column=1)


# Q9:Weight_lose
tk.Label(source, text="Do you want to lose weight?",
         width=50, bg=background, font=fontTipo).grid(row=9, column=1)

c17 = tk.Checkbutton(source, text="No", variable=weight_loss,
                     onvalue=0, bg=background)
c17.grid(row=10, column=1)

c18 = tk.Checkbutton(source, text="Yes", variable=weight_loss
                     ,
                     onvalue=1, bg=background)
c18.grid(row=11, column=1)
#confirm button
ft = tkFont.Font(family='Times', size=12)
b1 = tk.Button(source, text="Find your diet ", command=openNewWindow, bg="#82b115",borderwidth="0px",font=ft,fg="#ffffff")
b1.place(x=350,y=475,width=200,height=38)
photo = r'.\images\img.png'
img = ImageTk.PhotoImage(Image.open(photo).resize((900, 150)))
canvas = tk.Canvas(source, width=900, height=200)
canvas.place(y=520)
canvas.create_image(1, 0, anchor=tk.NW, image=img)
canvas.img = img
source.mainloop()