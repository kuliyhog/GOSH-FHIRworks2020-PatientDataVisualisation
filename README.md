# GOSH-FHIRworks2020-PatientDataVisualisation

## 1. Setting up
* **Windows Powershell**

  1. Make sure to have [Python 3.7](https://www.python.org/downloads/) or above installed. 
  2. Run the setup.ps1 with Powershell.
  
  * If setup.ps1 does not work, then do in Powershell
    * ```pip install virtualenv```
    * ```virtualenv env```
    * ```.\env\Scripts\activate.ps1```
    * ```pip install -r .\requirements.txt```    
    
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
  
## 2. Starting the WebApp

Make sure to have the [GOSH-FHIRworks2020 API](https://github.com/greenfrogs/FHIRworks_2020) running.

* **Windows**

  * Run **run.ps1** with Powershell or 
  * In Powershell, do 
      * ```.\env\Scripts\activate.ps1```
      * ```$env:FLASK_ENV = "development"```
      * ```$env:FLASK_APP = "app.py"```
      * ```flask run --port=2000```
  
* **Linux/Mac**
  * In Bash/Terminal, do 
      * ```source env/bin/activate```
      * ```export FLASK_ENV=development```
      * ```export FLASK_APP=app.py```
      * ```flask run --port=2000```


## 3. List of API Endpoints

**General Statistics**
* GET average age of all patients returned as a string: ```/averageage```
* GET observation statistics(total/most common observations and observation components) of all patients returned as a JSON: ```/observationstats```



## 4. Web App Uses

The Web App can be used to get the list of patients, patient information(uuid, fullname, contact, gender, age, address, marital status, languages spoken, multiple birth, identifiers, extensions, etc.), as well as patient observations(uuid, observationtype, observation components, effective datetime, etc.)

Clicking on the Graphs button on the patient information page will open a new tab with a few graphs that are plotted using the patient's observation data. If some of the observation are missing from the patient, the graph will show an empty graph. The graphs that are included are related to Blood Pressure(Diastolic and Systolic), Heart Rate and Respiratory Rate, Height, Weight, BMI and BMI Percentile, as well as Pain Severity.

Routes
* ```/``` -- this is to get the list of patients
* ```/patient/<patient id>``` -- this is to get the patient and observation information
* ```/statistics/<patient id>``` -- this is to get the graphs of a patient



