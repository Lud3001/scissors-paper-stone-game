import tkinter
from random import choice
ssp = ('ножницы' , 'камень' , 'бумага')
def click(button):
    global w , l , n 
    opponent = choice(ssp)
    print(opponent)
    print(button)
    if button == opponent:
        visual.configure(text= 'ничья')
        n += 1
    elif button == 'камень' and opponent == 'бумага':
        visual.configure(text='вы проиграли')
        l += 1
    elif button == 'камень' and opponent == 'ножницы':
        visual.configure(text='вы выиграли')
        w += 1
    elif button == 'ножницы' and opponent == 'бумага':
        visual.configure(text='вы выиграли')
        w += 1
    elif button == 'ножницы' and opponent == 'камень':
        visual.configure(text='вы проиграли')
        l += 1
    elif button == 'бумага' and opponent == 'камень':
        visual.configure(text='вы выиграли')
        w += 1
    elif button == 'бумага' and opponent == 'ножницы':
        visual.configure(text='вы проиграли')
        l += 1
    del opponent 
def total():
    global w, l , n
    stone.destroy()
    paper.destroy()
    scissors.destroy()
    visual.destroy()
    intotal.destroy()
    totalvisual = tkinter.Label(root, text= f'Число побед: {w} \n Число проигрышей: {l} \n Ничья: {n} ',  font=('SimSun'), bg='pink', fg='black', justify='center')
    totalvisual.place(width= 550 , x= 80, y=150)
root = tkinter.Tk()
root.geometry('700x400')
root.title('Камень-ножницы-бумага')
root['bg'] = 'pink'
visual = tkinter.Label(root, text= 'Привет:) \n Нажми на кнопку, \n чтобы начать играть', font=('SimSun'), bg= 'pink', fg= 'black', justify='center')
visual.place(width=550, x=100, y=50)
stone = tkinter.Button(root, text='камень', font=('SimSun'), command=lambda button='камень': click(button))
stone.place(width=200 , height=50 , x = 30, y=200)
scissors = tkinter.Button(root, text='ножницы', font=('SimSun') , command=lambda button='ножницы': click(button))
scissors.place(width=200 , height=50 , x = 250, y=200)
paper = tkinter.Button(root, text='бумага', font=('SimSun'), command=lambda button='бумага': click(button))
paper.place(width=200, height=50 , x =  470, y=200)

intotal = tkinter.Button(root, text='Завершить игру' , font=('Simsun'), command= total )
intotal.place(width=300, height= 60, x=200 , y=300)


w = 0
l = 0
n = 0



root.mainloop()