Expenditure on Research and Development(R&D) by countries with indicators such as source of funds, type of R%&D activity, fields of R&D(medical and health sciences) since 1996.

## Data

Data comes from UNESCO institute for statistics
http://data.uis.unesco.org

It consists of useful information about how much is spent by government/the private sectors, type of activites like Basic research, Applied research, Experimental development for specific countries. Also, we added spendings for Medical and health sciences. 

## Preparation
The main resource is located in `archive/gerd.csv` 
There are several steps have been done to get final data.

* Extracted separately each resource by source of funds "Business enterprise", "Government" and "Higher Education", "Private non-profit", "Rest of the world", "Not specified source"
* Extracted separately each resource by type of activities "Basic research", "Applied research", "Experimental development", "Not specified activities"
* Extracted by field of R&D "Medical and health sciences"
* Merged them into one resource `data/medical.csv` using `pandas` library.


Process is recorded and automated in python script:

```
# to get final merged data which is `data/expenditure.csv`, run the following script
scripts/process.py
```

## License

Public Domain Dedication and License (PDDL)
