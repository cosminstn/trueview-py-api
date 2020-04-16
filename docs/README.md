### Profanity checking
```bash
pip3 install profanity-check
```
Pentru ca libraria sa functioneze corect avem nevoie de scikit-learn 0.20.2. Putem face din pip, sau din Pycharm Preferences.

### MongoDB
For MongoDB we are going to use PyMongo, which is the recommended way to work with Mongo in Python.  
[PyMongo Docs](https://docs.mongodb.com/ecosystem/drivers/pymongo/#introduction)
```bash
pip3 install pymongo
```
Pentru a folosi conexiune de MongoAtlas avem nevoie de **dnspython**
```bash
pip3 install dnspython
```


### Customize Flask Server startup
```bash
pip3 install Flask-Script
```

### Generare requirements.txt
```
pip freeze > requirements.txt
```