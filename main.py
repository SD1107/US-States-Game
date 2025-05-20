import pandas
import turtle
# global c
# global answer_state
def continue_game():
    answer_state=my_screen.textinput(title=f"{len(correct)}/50 correct guesses!",prompt="What is the Name of the US State?")
    answer_state=answer_state.title()
    data=pandas.read_csv("50_states.csv")
    names=data.state
    
    if answer_state=="Exit":
        return 0
    
    for i in names:
        if answer_state==i:
            correct.append(answer_state)
            tim=turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            # tim.speed("fastest")
            xcor=int(data[data.state==answer_state].x.item())
            ycor=int(data[data.state==answer_state].y.item())
            tim.goto(xcor,ycor)
            #tim.write(answer_state,font=("courier",8,"normal"))
            tim.write(answer_state)
            return 1
            



my_screen=turtle.Screen()
correct=[]
missing=[]
my_screen.title("U.S. States Game")
#my_screen.bgcolor("black")
image="blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)
c=0
game_on=True


while game_on:
    if c==50:
        print("Congratulations!You have successfully named all the states! You are a pro!")
        game_on=False
    else:
        if continue_game()==0:
            data=pandas.read_csv("50_states.csv")
            # for states in data.state:         ABSOLUTELY CORRECT BUT BETTER METHOD AVAILABLE!!
            #     if states not in correct:     ABSOLUTELY CORRECT BUT BETTER METHOD AVAILABLE!!      
            #         missing.append(states)    ABSOLUTELY CORRECT BUT BETTER METHOD AVAILABLE!!
            missing=[x for x in data.state if x not in correct]#only single line required!!
            print("These are the states that you forgot to label! Better luch next time!!\n\n")
            print(missing)
            game_on=False
            break

            
        else:
            
            continue_game()



my_screen.exitonclick()