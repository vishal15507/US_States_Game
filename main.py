import turtle
import pandas

data =pandas.read_csv('50_states.csv')
states=data.state
x_cors=data.x
y_cors=data.y

writter=turtle.Turtle()
writter.penup()
writter.hideturtle()

screen=turtle.Screen()
screen.setup(width=700,height=500)
screen.title("US states Game")
img="blank_states_img.gif"
#turtle.register_shape(img)


screen.addshape(img)
turtle.shape(img)

# def get_mouse_location(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_location)
# turtle.mainloop()


guessed_states=[]
missing_states=[]
score=0
answer_state="abc"
while answer_state!="exit":
    answer_state=screen.textinput(title='GUESS THE STATE:',prompt=f"{score}/50 ,what's another state name")
    print(answer_state)

    count=0
    for i in range(len(states)):
        if answer_state.lower()==states[i].lower():
            # print(place)
            count=count+1
            writter.goto(x_cors[i],y_cors[i])            #dfgdffdsjfjshjh
            writter.write(f"{states[i]}", False, align="center", font=("arial", 10, "normal"))
            guessed_states.append(states[i])

    if count!=0:
        print("correct ans")
        score=score+1

    elif count==0:
        print("invalid")


for i in range(len(states)):
        if states[i] not in guessed_states:
            missing_states.append(states[i])

missing={
     "Missing States":missing_states
}

data_base=pandas.DataFrame(missing)
print(missing)
data_base.to_csv('missing states')



screen.exitonclick()