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

### Build docker image
```
docker build -t trueview-py-api:latest .
```

### Run container for the image
```
docker run -d -p 5000:5000 --name trueview-py-api trueview-py-api
```


### Creare run configuration pe baza Dockerfile
1. Adaugam run configuration de tip Dockerfile
2. selectam fisierul dockerfile in input-ul respectiv
