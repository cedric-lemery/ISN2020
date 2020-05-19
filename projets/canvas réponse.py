Mon_canvasReponses = Canvas(bg='black')

Mon_canvasReponses.place(x=int(w*0.70),y=int(h*0.10),width=250,height=500)
for loop in range (3):
    y4=80
    Mon_canvasReponses.create_rectangle(x2+i,y2,x2+i+x3,y2+y3,fill='red')
    y2=y4

