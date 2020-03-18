# GOSH-FHIRworks2020-PatientWebApp

## 1. Setting up
* **Windows**

  1. Make sure to have [Python 3.7](https://www.python.org/downloads/) or above installed. 
  2. Run the setup.ps1 with Powershell.

* **Linux/Mac**
    
  1. Install Python 3.7 or above
      * ```sudo apt-get update```
      * ```sudo apt-get install python3.8```
      
  2. Install Virtualenv
      * ```pip install virtualenv```
      
  3. Setup Virtual Environment
      * ```virtualenv env```
      * ```source env/bin/activate```
      
  4. Install Packages
      * ```pip install flask```
      * ```pip install FHIR-Parser```
      
  5. Setup Flask Environment
      * ```source env/bin/activate```
      * ```$env:FLASK_ENV = "development"```
      * ```$env:FLASK_APP = "app.py"```
  
## 2. Starting the WebApp

Make sure to have the [GOSH-FHIRworks2020 API](https://github.com/greenfrogs/FHIRworks_2020) running.

* **Windows**

  * Run **run.ps1** with Powershell or 
  * In Powershell, do ```.\env\Scripts\activate.ps1``` then ```flask run --port=2000```
  
* **Linux/Mac**
  * In Bash/Terminal, do ```source env/bin/activate```
  * then do ```flask run --port=2000```


## 3. List of API Endpoints

**General Statistics**
* GET average age of all patients returned as a string: /averageage
* GET observation statistics(total/most common observations and observation components) of all patients returned as a JSON: /observationstats



## 4. Web App Uses



