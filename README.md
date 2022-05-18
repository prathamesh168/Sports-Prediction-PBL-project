# Sports Preciction PBL project
 ## Motivation behind Project
   ### Sports like cricket and football are a significant part of people's life. Many use it as a medium to relax or entertain themselves. But most of them are eager to know which team will win and which player will score the most before the match commences. To help with this obstacle, we are planning to build a website that does exactly that. We will collect past data on various teams and players and use Machine Learning to try and predict the outcome of the next match. Not only will this sate the curiosity of the average sports enthusiast, but it will also help those interested in legal betting.
 # Application actual working
  ### Our website currently able to predict scores on current condition and match winner before match in case of  Cricket("Indian Premier League") and match winning team in case of Football("English Premier League").
  ### In case of Cricket prediction, it takes the data from user which enables user to give frredom check any condtion of match to predict score amd match winner. In which match winner predicted is only on venue , toss winner , toss decision  which gives best idea who is gonna win before match. Our other fields are for predicting the final score of batting team in 20 overs based on the given condition by user.
  ### In case of Football, user need not to give any type of input rather it will show the match winner in upcomning matches table. 
  
  # Setup 
  ### If you want to run this site locally then you have to first clone the repository in your system
    $ git clone https://github.com/prathamesh168/Sports-Prediction-PBL-project.git
  ### After clonning the repository go to downloaded folder and open the terminal in `./website_main` folder
    $ cd PredictionWebsite/website_main/
  ### create the virtual environment with `python 2.7` and greater and activate that.
    $ virtualenv --no-site-packages env
    $ source env/bin/activate
  ### Then install dependensies
    $ pip install -r requirements.txt
  ### Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv`.
  ### Once the dependensies get installed correctly then run django local server and you are good to go.
    $ python manage.py runserver
  ### and navigate to  http://127.0.0.1:8000/
  
   # Future Scope
   ### For Cricket prediction, we can live scrape the data we need to predict and make it user friendly and also can give other site to check user inputted score predictions.
   ### For Cricket prediction, score predictor model working with mean squared error of plus or minus 19 runs which can reduce using hyperparameter tunning and applying the more efficent algorithm.
   ### For Football prediction, model other features like weather can be added or current rankings or global rankings in dataset and train the model which will give surely better accuracy. 
 # Contributers
 ### Parag Kulkarni 
 ### Pritish Pore
 ### Aditya Medhe
 ### Prathamesh Mulay

