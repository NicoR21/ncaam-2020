# National Collegiate Athletic Aassociation Men - 2020 
Google Cloud & NCAA® ML Competition 2020-NCAAM  

## Installation instructions
 Download Kaggle data, in  `ncaam/resources/data` directory with the following command, executed within the data directory:  

```bash
kaggle competitions download -c google-cloud-ncaa-march-madness-2020-division-1-mens-tournament
```

*N.B.* : Be sure to accept the rules for this competition, and to have a *kaggle.json* with your API token in the *~/.kaggle* folder, or to use the environment method correctly.  

Run the following command from the project root, to organize *.csv* samples: 

```bash
./ncaam/src/local_data_organizer.sh
```
