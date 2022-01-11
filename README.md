# Start

````
#add EP_Data_Extended.csv in Work/Data
cd Work
jupyter notebook exodus_datas_work.ipynb #to start
Work/Trackers.ipynb #work on all trackers
Work/Location-Trackers.ipynb #work on location trackers
````
Project done with @annemkht and @te-mbu


## Anaconda
- permet de créer des environnements de travail
- Anaconda Navigator

````
#si je travaille dans l'environnement "base" y a tous les packages
conda create --name *nom environnement* python=3.6 #créer environnement python 
y #proceeded yes?
source activate *nom environnement* #activer environnement
source deactivate #desactiver environnement
conda install pandas
conda install -c anaconda jupyter
conda list #nous donne tous les package installés
