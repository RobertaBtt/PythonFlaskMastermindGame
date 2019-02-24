# MastermindAPI
Rest API that simulates the role of Masterminds codemaker.

It's a small webserver done with Flesk.



![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mastermind.jpg/150px-Mastermind.jpg)



Instructions:

```
mkdir MastermindAPI
```
 
 
``` 
cd MastermindAPI

``` 

```
virtualenv -p /usr/bin/python2.7 MASTERMIND_ENV

```

Create the virtual env ONCE

```
source MASTERMIND_ENV/bin/activate
```


And you will find yourself in the virtual environment, ready to get the corret dependencies
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
FLASK_APP=FLASK_APP=mastermind_api/mastermind.py flask run
```

And then visit http://127.0.0.1:5000/  (depending on your local config file, that you are free to change)

With /new/game the codeBreaker tells to the CodeBreaker that he wants to play.

