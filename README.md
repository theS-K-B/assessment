# assessment

##  📌Working Process :
- At first you need to create a MySQL database, then import the given  [```customers.sql```](https://github.com/theS-K-B/assessment/blob/290de2107691cf0fb1a033e6c7b11c1eb063b591/datafiles/customers.sql) table.
- The [```main_connector.py```](https://github.com/theS-K-B/assessment/blob/290de2107691cf0fb1a033e6c7b11c1eb063b591/main_connector.py) is a python script, which perform all the ETL operations.
- It fetches the ```table``` from MySQL  database and convert it into a ```pandas data frame``` for further transformation.
- The transformation process includes, grouping the customers based on their countries, and creating ```separate table``` for each country inside the database e.g. ```table_ind```, ```table_au```.
- The method```get_datafile("IND")``` generates [```ind.csv```](https://github.com/theS-K-B/assessment/blob/290de2107691cf0fb1a033e6c7b11c1eb063b591/datafiles/ind.csv) from the country specific table inside MySQL to the specified local path. 

## 📌Installation Process:
- To install ```sqlalchemy```:
```
pip install sqlalchemy
```
- To install PyMySql:
```
pip install PyMySql
```
- To install pandas:
```
pip install pandas
```

