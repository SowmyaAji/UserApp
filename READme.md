## Overview: 

Flask SQL Alchemy app creating, getting and deleting users from a sqlite database


## Installation

git clone repository. Then, 

``` 
$ pip install -r requirements.txt
```

Create database:

```
$ python3
>>> from app import db
>>>  db.create_all()
>>> exit()
```

from terminal run:
```
$ flask run
```

App will run on localhost:5000








