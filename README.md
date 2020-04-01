# MastermindAPI
Rest API that simulates the role of Masterminds codemaker.

It's a small webserver done with Flesk.



![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mastermind.jpg/150px-Mastermind.jpg)



Instructions:

```
mkdir MastermindAPI

cd MastermindAPI

virtualenv -p /usr/bin/python2.7 MASTERMIND_ENV

```

Create the virtual env ONCE and use it more.

```
source MASTERMIND_ENV/bin/activate
```


And you will find yourself in the virtual environment, 
ready to get the corret dependencies
without influencing other python installation and environments.



**Install the requirements for this virtual env for this project:**

```
pip install -r requirements.txt
```

---

To deactivate the virtual env:

```
deactivate
```

To run the Application server:

From the directory *MastermindAPI*
run:

```
FLASK_APP=mastermind_api/FlaskApp.py flask run
```

And then visit http://127.0.0.1:5000/  
(depending on your local config file, that you are free to change)

# Create the game 
by visiting the page http://127.0.0.1:5000/new/game

You will have in returns the code of the game, for example 

```{
id: 140349232018880
}
```
#Then
Visit the page

http://127.0.0.1:5000/play/140349232018880/

And the game will respond with: << please give me the numbers you want to play


First
With /new/game the codeBreaker tells 
to the CodeBreaker that he wants to play.

