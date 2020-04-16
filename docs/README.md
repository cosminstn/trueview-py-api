## Endpoints

### /scores  **GET**
**Provides the scores for all registered products.**  
***WARNING***: *Should not be used in production*  
Example response:  
```json
{
    "mean": {
        "0190198947840": 3.75,
        "6921815605577": 4.4333333333
    },
    "count": {
        "0190198947840": 2,
        "6921815605577": 45
    },
    "bayes": {
        "0190198947840": 3.3611111111,
        "6921815605577": 4.2740384615
    },
    "dirichlet": {
        "0190198947840": 0.0,
        "6921815605577": 0.0
    }
}
```

### /scores/bayes/<ean13>  **GET**
**Provides bayesian mean for a given UPC. 
Usually products are registered by the EAN13 code, so that code should be provided.**  
Example response: **/scores/bayes/6921815605577**
```json
{
  "bayes": 4.274038461538462,
  "confidence": 7,
  "prior": 3.25
}
```

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
3. Setam container name
4. Adaugam bind in Bind Ports