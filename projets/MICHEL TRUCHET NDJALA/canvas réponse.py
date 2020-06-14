Mon_canvasReponses = Canvas(bg='black')
Mon_canvasReponses.place(x=int(w*0.70),y=int(h*0.10),width=250,height=500)
Rect2 = []
for i in range(3):
    Rect2.append(Mon_canvasReponses.create_rectangle(x2+i*xpas2,y2,x2+i*xpas2+x3,y2+y3,fill='white'))

