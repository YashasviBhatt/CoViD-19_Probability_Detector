# CoViD-19 Probability Detector

## To run this Project please follow these steps

### A. Pre-Requisites
1. Open _command prompt_ or _powershell window_.
2. Type this command<br>`git clone https://github.com/YashasviBhatt/CoViD-19_Probability_Detector`<br>and press enter.
3. Go inside the _Cloned Repository_ folder and open _command-prompt_ or _powershell window_.

### B. Executing the Project
#### Recommended Method
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install virtualenv`<br>and press enter.
3. Now, type<br>`.\covid_prob\Scripts\activate`<br>and press enter.
    - if you are having Error while _activating virtual environment_ then open _command prompt_ or _powershell window_ as _administrator_.
    - now type<br>`set-executionpolicy remotesigned`<br>press enter and repeat _step 3_.
4. After activating _virtual environment_, the _path_ should look like this ```(covid_prob) .\<your-path>\CoViD-19_Notifier```.
5. Running the Project
    - If you want to use the _trained model_ then simply run the _server_ using this<br>`python srvr.py`<br>And use the link to access.
    - If you want to _retrain_ the _model_ then, firstly, execute<br>`python covid_prob.py`<br>after _training_ the _model_ execute<br>`python srvr.py`<br>And use the link to access.
6. Do not remove any _file_.

#### Alternate Method
In case you don't want to use _virtual environment_ which has all the required _libraries_ installed then follow these steps:<br>
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install -r requirements.txt`<br> and press enter in either _command_prompt_ or _powershell window_ as _administrator_.
3. After Installing all the required _libraries_ execute the _training_ first(**if you want to _retrain_ the _model_, otherwise directly run _part 2_ of this step**)<br>`python covid_prob.py`<br>now execute the server<br>`python srvr.py`<br>And use the link to access.