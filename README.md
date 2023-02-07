# Computer Vision RPS
This project involved making a simple rock,paper,scissors game from scratch. First it involved making a manual version and then it involved taking it further, and creating classes and using computer vision to determine the user input.

## Milestone 1
This milestone was simple and involved creating a new github repository for the project.

## Milestone 2
Milestone two involved first creating the model. Instead of doing this from scratch ourselves, we used teachable-machine, which allowed us to insert images of ourselves making the appropriate gestures and then providing a dataset with which the model can be trained. At the end of this, we downloaded the model which had two different files in it. It was important we kept these files in the same folder as our project work as it would be important in the next steps.

## Milestone 3
As this project involved reading models as well as accessing the camera of our device and reading that data, it was important that we installed libraries which allowed us to handle this. As a result we installed things such as:

* numpy
* opencv
* tensor flow

As well as already installed things such as python.

It was also important to do this in a new environment to avoid conflicts of packages. To do this, we used the appropriate conda commands.

We were given a template file which allowed us to test that our model was working. The file showed that for every frame that was being captured, an array was being returned. This numpy array corresponded to our rock, paper and scissors with the largest number in the array being the item with the highest probability.


## Milestone 4
This task involved creating a manual version of rock paper scissors. Although the task did not ask for it, I decided to practice my recent knowledge of classes and create it in OOP instead of how I would have implemented it previously.

The task also required me to code the logic for who would win, as well as defining a user and computer choice.

## Milestone 5
As I had implemented a lot of the logic, class and constraints in the earlier milestone, it made this milestone a lot easier. 
This milestone involved integrating the RPS-Template.py file into my manual rps game. It involved understanding that the RPS-Template file did two things, firstly it allowed us to use the camera on our device and provide information frame by frame, but it also allowed us to make a prediction on the signal being made by the user.
Knowing this, I split the RPS template file into two functions. One to stop the camera after its use as well as one to get the prediction itself.
After this, instead of asking the user for the input, I applied the get_prediction() function and assigned it to user_choice.
I also created a countdown for the terminal, which would ask for a user input every 3 seconds.

## Conclusions
I learnt a lot during this project, and initially it was not easy. To improve this project, I'd like to involve some sort of graphical interface for the user, as well as an option between goes to takes a break.