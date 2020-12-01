# CSE-HUB

Based on [php version](https://github.com/harshraj22/contest) &nbsp; Website under development. Can be accessed [here](https://harshraj22.pythonanywhere.com/)

##### Idea :
To have a website that caters all needs that a CSE UG has.

##### What works ?

* adding problems (login_required)
* adding testcase (for now we can only add one test case at a time, also only author of a problem can add testcase for the problem)
* login/logout
* adding solution (checks if user is logged in or not)
* evaluation of solution
* updation of table for problems upon adding solution by the user(successful/total submissions), ie. each problem stores count of AC/ WA to itself
* adding predefined tags to problems
* We've got a discussion forum with comments functioning !!
* User can now edit profile !! (but currently we don't store anything editable)
* Now user can see/download all submited codes. How cool is that !!
* User Registration, Now user can SignUp, so no need to go to admin section to create user.(will be implementing verification soon).
* We've got a good editor built ! It can do a lot of things (see details [here](https://github.com/harshraj22/CSE_HUB/pull/57))

<details>
<summary> What lacks ? </summary>

* Only mode of submission is through file upload
* No work is done for creating a contest
* frontend for various pages
* Editing of: problem/ added testcase
</details>

<details>
<summary> Mapped urls :</summary>

* ```admin/```
* ```''```
* ```profile/<username>```
* ```profile/<username>/edit```
* ```problems/add```
* ```problems/display/<int:problem_id>```
* ```problems/add/testcase```
* ```problems/submit/<int:problem_id>```
* ```submit/<int:id>/```
* ```submissions/<str:username>/```
* ```submissions/<str:username>/view/<int:id>/```
* ```submissions/download/<int:id>/```
* ```problems```
* ```login```
* ```logout```
* ```forum```
* ```forum/post/<int:post_id>/```
* ```editor/```
</details>

##### Installation :

* create a virtual environment and activate it (google it)
* Install dependencies into it ```pip3 install -r requirements.txt``` or ```python -m pip install -r requirements.txt```.
* Check out to develop branch.
* Make sure if you are using virtual environment, you have all dependencies installed (mentioned in ```requirements.txt```). ```python3 manage.py migrate --run-syncdb ``` [read here](https://stackoverflow.com/a/37799885/10127204) (p.s. all migration files are being ignored, see .gitignore) , ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```. This will update database with tables as we describe in models.py. Then ```python3 manage.py runserver``` and play around testing what all has been developed.
use ```python3 manage.py createsuperuser``` to create admin credentials and then go to ```localhost:8080/admin``` after ```python3 manage.py runserver``` to log-in as admin. Create some user accounts/ profile pages/ question tags etc and play along with them, logging in from ```localhost:8080``` (you may use credentials of user you just created, but make sure you've created his/her profile as well from admin pannel).
###### Make sure you create tags before adding questions.

##### Screenshots :
![Forum](https://user-images.githubusercontent.com/46641953/100749908-55945080-340b-11eb-84f2-68c977b31520.png)

![Forum_post](https://user-images.githubusercontent.com/46641953/100749912-56c57d80-340b-11eb-8b0d-5ab0ac3056cd.png)

![Login_page](https://user-images.githubusercontent.com/46641953/100749917-575e1400-340b-11eb-9893-f0b4da11413f.png)

![problem](https://user-images.githubusercontent.com/46641953/100749920-57f6aa80-340b-11eb-8c17-051d65b5ab8f.png)

![Profile](https://user-images.githubusercontent.com/46641953/100749925-588f4100-340b-11eb-9d76-d6943d726098.png)

![Signup_page](https://user-images.githubusercontent.com/46641953/100749935-5b8a3180-340b-11eb-8807-b3ab749906ba.png)

![submission](https://user-images.githubusercontent.com/46641953/100749937-5c22c800-340b-11eb-976b-1b25b0394935.png)

![Add_Problem](https://user-images.githubusercontent.com/46641953/100749939-5cbb5e80-340b-11eb-9672-db40193372bb.png)

![Add_testcase](https://user-images.githubusercontent.com/46641953/100749941-5d53f500-340b-11eb-8897-c70806c9559d.png)

![All_Problems](https://user-images.githubusercontent.com/46641953/100749944-5dec8b80-340b-11eb-845c-d41141d42b3d.png)

![Create_forum_post](https://user-images.githubusercontent.com/46641953/100749948-5e852200-340b-11eb-8766-9c9575a5fe00.png)

![Editor](https://user-images.githubusercontent.com/46641953/100749955-5f1db880-340b-11eb-9c8e-e2da26eba36e.png)

#### Further Reading :
* [Writing tests](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
