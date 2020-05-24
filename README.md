## VideoLib 
![Image](https://2.bp.blogspot.com/-lHldOTZaVDY/VwgyVX433zI/AAAAAAAAAFo/LU64Kzxc9yITH2AnmNsydFm7WPug5TitA/s1600/flaskMySql.jpeg)
![Image](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRgb3aQO8jjXhwH1vs0l0kOWv-ZawfM3awKsUV6t7-Oi7tABkOf&usqp=CAU)

This is example of Flask web-application which use Flask_Admin Panel for work with mysql using ORM SqlAlchemy.

### Installing

Before running the server, you must install Flask and pybadges. You can install both with:

```sh
pip install -r requirements.txt
```

* And you need to run command in run.sql file to create data base and tables with Data.
* Also need to write you database pass in config.py to connect it"
### Running

To run the server, you must set the FLASK_APP environment variable before running the server using Flask:

```sh
export FLASK_APP=main.py
flask run
```

If it not work try this

```sh
source venv/bin/activate
flask run
```


After this step, you can view your badge on http://127.0.0.1:5000/