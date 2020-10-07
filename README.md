# CoViD-19 Probability Detector

This Project use **Logistic Regression** to calculate **Probability** of a person having **CoViD-19** so as to prioritize the testing such that those who have _high probability_ of getting _infected_ could be _tested_ before those who have _relatively less probability_ of getting infected. User will be asked for conditions like **Travel Status**, **Fever Level**, **Body Pain**, **Runny Nose** etc and according to that data the model will predict the probability of having _infected_.

## To run this Project please follow these steps

1. Open _command prompt_ or _powershell window_.
2. Type this command<br>`git clone https://github.com/YashasviBhatt/CoViD-19_Probability_Detector`<br>and press enter.
3. Go inside the _Cloned Repository_ folder and open _command-prompt_ or _powershell window_.

4. Type<br>`pip install -r requirements.txt`<br> and press enter in either _command_prompt_ or _powershell window_ as _administrator_.
5. After Installing all the required _libraries_ create the server using<br>`python srvr.py`.<br>Open the _IP Address_ in a browser and use this _Project_.
6. `srvr.py` uses the _saved model_ which was pre-trained and kept saved, if you want to _retrain_ the model then execute<br>`python covid_prob.py`<br>now repeat step 5.

## Working

1. Firstly, _data_ is imported using `pandas library`.
2. Secondly, we divide the _features_ and _label_ into to seperate _dataframes_.
3. Now, after creating the separate dataframes for features and label, we split them into _training_ and _testing_ sets.
4. The _training set_ is used to train the _model_ using **Logistic Regression** (since, we are talking about probability and Tabular Datasets, thus _Logistic Regression_ best fit the approach).
5. The _trained model_ is saved into a file using `pickle` module in _python_.
6. `srvr.py` file is used to create a _localhost server_ using `flask` module in _python_ which will reflect the _HTML_ pages.
7. The data after submitting the _form_ from **HTML** pages is passed to _trained model_ which will later calculate _Probability_.
<br><br><br>
**This Model is completely trained on random data, thus accuracy should not be taken in concern, however if real stats is used for training, this Model can perform much-much better**.